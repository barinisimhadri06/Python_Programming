# Author: Barini Simhadri
# Date: 13-03-2024
# Honor Statement: "I have not given or received any unauthorized assistance on this assignment."
# link: https://youtu.be/xiVI5sd3GEE

#Importing required libraries
import pandas as pd
import matplotlib.pyplot as plt

#this is the File path
file_path = "C:/Users/bunty/Desktop/DSC430/week_9/hw/Heights_and_Weights.csv"

# Reads the data
data = pd.read_csv(file_path)

# Checks the column names
print(data.columns)

# Identify the column names for height, weight, and sex
height_col = None
weight_col = None
sex_col = None

for col in data.columns:
    if 'height' in col.lower():
        height_col = col
    elif 'weight' in col.lower():
        weight_col = col
    elif 'sex' in col.lower():
        sex_col = col

# Separates data for male and female if the column names are found
if height_col and weight_col and sex_col:
    male_data = data[data[sex_col] == 'Male']
    female_data = data[data[sex_col] == 'Female']
else:
    print("Column names for height, weight, or sex not found.")

# Scatter plot for male and female data if data separation is successful
if male_data is not None and female_data is not None:
    plt.scatter(male_data[height_col], male_data[weight_col], color='blue', label='Male')
    plt.scatter(female_data[height_col], female_data[weight_col], color='red', label='Female')

    # Fit line parameters
    slope = 0.28
    intercept = 23.2

    # Compute endpoints of the regression line
    x_values = [data[height_col].min(), data[height_col].max()]
    y_values = [slope * x + intercept for x in x_values]

    # Plot the regression line
    plt.plot(x_values, y_values, color='green', label='Regression Line')

    # Compute outliers for height
    height_mean = data[height_col].mean()
    height_std = data[height_col].std()
    height_lower_bound = height_mean - 2.5 * height_std
    height_upper_bound = height_mean + 2.5 * height_std

    # Compute outliers for weight
    weight_mean = data[weight_col].mean()
    weight_std = data[weight_col].std()
    weight_lower_bound = weight_mean - 2.5 * weight_std
    weight_upper_bound = weight_mean + 2.5 * weight_std

    # Plot the bounds for height
    plt.axvline(x=height_lower_bound, color='gray', linestyle='--', label='Height Lower Bound')
    plt.axvline(x=height_upper_bound, color='gray', linestyle='--', label='Height Upper Bound')

    # Plot the bounds for weight
    plt.axhline(y=weight_lower_bound, color='orange', linestyle='--', label='Weight Lower Bound')
    plt.axhline(y=weight_upper_bound, color='orange', linestyle='--', label='Weight Upper Bound')

    # Detect and annotate outliers
    outliers = data[(data[height_col] < height_lower_bound) | (data[height_col] > height_upper_bound) | 
                    (data[weight_col] < weight_lower_bound) | (data[weight_col] > weight_upper_bound)]

    for index, row in outliers.iterrows():
        plt.text(row[height_col], row[weight_col], 'Outlier', fontsize=8, color='purple')

    # Add labels and legend
    plt.xlabel('Height')
    plt.ylabel('Weight')
    plt.legend()

    # Show the plot
    plt.show()
