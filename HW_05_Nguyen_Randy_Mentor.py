import pandas as pd
import sys
import numpy as np

# quantize num - function that rounds the number to the nearest bin
    # num - number to be quantized
    # bin - nearest multiple to be rounded to ie. 2,4,6... etc if bin is 2
    # returns - number rounded to nearest bin of size bin
def quantize_num(num, bin):
    return bin * round(num/bin)


# calculate_gini_index - function to calculate the gini index
    # occurrences
    # total - total number of events at node
    # returns the gini coefficient computed using the probability of the occurrences squared
def calculate_gini_index(occurrences, total):
    return 1 - (occurrences/total)**2 - ((total-occurrences)/total)**2

# find_num_of_occurrences - counts the number of occurrences where a value is less than threshold in the column
    # threshold - threshold to separate the numbers
    # df - column of values to check threshold against and class
    # returns number of occurrences where num < threshold
def find_num_of_occurrences(threshold, df):
    occurrences = 0
    for index, row in df.iteritems():
        if row <= threshold:
            occurrences += 1
    return occurrences

# find_best_threshold - finds best threshold for the given column based on minimum gini index
    # df - column to find the best threshold with class
    # column_name - name of column to separate by threshold
    # returns the best threshold as calculated by the minimum gini index
def find_best_threshold(df, column_name):
    if column_name == "Age":
        increment = 2
    if column_name == ""
    best_threshold = 0
    best_weighted_gini = 100
    minimum = int(df[column_name].min(axis = 0))
    maximum = int(df[column_name].max(axis = 0))
    for threshold in range(minimum, maximum):
        df_lower = df[df[column_name] <= threshold]
        df_upper = df[df[column_name] > threshold]
        df_lower_assam = df_lower[df_lower['Class'] == "Assam"]
        df_lower_bhuttan = df_lower[df_lower['Class'] == "Bhuttan"]
        df_upper_assam = df_upper[df_upper['Class'] == "Assam"]
        df_upper_bhuttan = df_upper[df_upper['Class'] == "Bhuttan"]
        count_lower_assam_upper_bhuttan = len(df_lower_assam) + len(df_upper_bhuttan)
        count_upper_assam_lower_bhuttan = len(df_upper_assam) + len(df_lower_bhuttan)
        if count_lower_assam_upper_bhuttan >= count_upper_assam_lower_bhuttan:
            upper = "Bhuttan"
            lower = "Assam"
            gini_lower = (1 - ((len(df_lower_assam)/len(df_lower))**2)) - (len(df_lower_bhuttan)/len(df_lower))**2
            gini_upper = (1 - ((len(df_upper_bhuttan) / len(df_upper))**2)) - len(df_upper_assam)/len(df_upper)**2
            weighted_gini = len(df_lower)/len(df) * gini_lower + len(df_upper)/len(df) * gini_upper
            if weighted_gini < best_weighted_gini:
                best_weighted_gini = weighted_gini
                best_threshold = threshold
        if count_upper_assam_lower_bhuttan > count_lower_assam_upper_bhuttan:
            upper = "Assam"
            lower = "Bhuttan"
            gini_lower = (1 - ((len(df_lower_bhuttan)/len(df_lower))**2)) - (len(df_lower_assam)/len(df_lower))**2
            gini_upper = (1 - ((len(df_upper_assam)/len(df_upper))**2)) - (len(df_upper_bhuttan)/len(df_upper))**2
            weighted_gini = len(df_lower) / len(df) * gini_lower + len(df_upper) / len(df) * gini_upper
            if weighted_gini < best_weighted_gini:
                best_weighted_gini = weighted_gini
                best_threshold = threshold
    print(best_weighted_gini)
    print("Upper:",upper)
    print("Lower:",lower)
    return best_threshold

def main():
    testing_file = sys.argv[1]

    data = pd.read_csv(testing_file)
    print(data.head())
    # the following quantizes the correct columns to the appropriate bins, ignores class column
        # Age - bins of 2
        # Ht - bins of 5
        # Everything else - bins of 1
    data.update(data['Age'].apply((lambda x: quantize_num(x, 2))))
    data.update(data['Ht'].apply((lambda x: quantize_num(x, 5))))
    data.update(data.apply((lambda x: quantize_num(x, 1) if x.name != 'Age' and x.name != 'Ht' and x.name != 'Class' else x)))
    print(data.head())
    for column_name, content in data.iteritems():
        if column_name != 'Class':
            print(column_name)
            best_column_threshold = find_best_threshold(data[[column_name, 'Class']], column_name)
            print(best_column_threshold)


if __name__ == "__main__" :
    main()
