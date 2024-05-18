# Author: Barini Simhadri
# Date: 13-03-2024
# Honor Statement: "I have not given or received any unauthorized assistance on this assignment."
# link: https://youtu.be/wy83a1A_zWs

#importing required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def read_data(file_path):
    """
    this function Reads data from a CSV file using Pandas.
    """
    data = pd.read_csv(file_path)  # Read data from CSV file
    return data

def divide_groups(data):
    """
    this function divides the data into male and female groups.
    """
    male_data = data[data['Sex'] == 'Male']  # Extract male data
    female_data = data[data['Sex'] == 'Female']  # Extract female data
    return male_data, female_data

def plot_histograms(male_data, female_data):
    """
    this function Plots histograms of male and female heights on the same figure.
    """
    # Plot histogram for male heights
    plt.hist(male_data['Height'], bins=30, alpha=0.5, label='Male', color='blue')
    # Plot histogram for female heights
    plt.hist(female_data['Height'], bins=30, alpha=0.5, label='Female', color='pink')
    plt.xlabel('Height (cm)')  # Set x-axis label
    plt.ylabel('Frequency')  # Set y-axis label
    plt.title('Distribution of Heights for Male and Female Subjects')  # Set plot title
    plt.legend()  # Show legend
    plt.show()  # Display the plot

def compute_means(male_data, female_data):
    """
    This function Computes the mean of male and female heights.
    """
    male_mean = np.mean(male_data['Height'])  # Compute mean of male heights
    female_mean = np.mean(female_data['Height'])  # Compute mean of female heights
    return male_mean, female_mean

def plot_mean_lines(male_mean, female_mean):
    """
    This function Plots vertical lines at the location of mean values for male and female heights.
    """
    # Plot vertical line at male mean height
    plt.axvline(x=male_mean, color='blue', linestyle='--', label='Male Mean')
    # Plot vertical line at female mean height
    plt.axvline(x=female_mean, color='pink', linestyle='--', label='Female Mean')

def main():
    # Reads data
    file_path = "C:/Users/bunty/Desktop/DSC430/week_9/hw/Heights_and_Weights.csv"  # File path
    data = read_data(file_path)  # Read data from file

    # Divides data into male and female groups
    male_data, female_data = divide_groups(data)

    # Plots histograms
    plot_histograms(male_data, female_data)

    # Computing means
    male_mean, female_mean = compute_means(male_data, female_data)
    print("Male Mean Height:", male_mean)  # Print male mean height
    print("Female Mean Height:", female_mean)  # Print female mean height

    # Plotting mean lines
    plot_mean_lines(male_mean, female_mean)

    # Show plot
    plt.legend()  # Show legend
    plt.show()  # Display the plot

    # Compute area under histograms
    male_hist, _ = np.histogram(male_data['Height'], bins=30, density=True)  # Compute histogram for male heights
    female_hist, _ = np.histogram(female_data['Height'], bins=30, density=True)  # Compute histogram for female heights
    male_area = np.sum(male_hist * np.diff(_))  # Compute area under male histogram
    female_area = np.sum(female_hist * np.diff(_))  # Compute area under female histogram
    print("Area under Male Histogram:", male_area)  # Print area under male histogram
    print("Area under Female Histogram:", female_area)  # Print area under female histogram

if __name__ == "__main__":
    main()