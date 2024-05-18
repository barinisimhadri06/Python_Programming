# Author: Barini Simhadri
# Date: 07-03-2024
# Honor Statement: "I have not given or received any unauthorized assistance on this assignment."
# link: https://youtu.be/dk0si3FvP7k

import numpy as np

def load_interaction_matrix(file_path):
    """
    Load interaction matrix from file.
    """
    # Load the interaction matrix from file using np.loadtxt
    interaction_matrix = np.loadtxt(file_path)
    return interaction_matrix

def verify_symmetry(interaction_matrix):
    """
    Verify symmetry of the interaction matrix.
    """
    # Check if the matrix is symmetric by comparing it with its transpose
    return np.array_equal(interaction_matrix, interaction_matrix.T)

def analyze_interaction_matrix(interaction_matrix):
    """
    Analyze interaction matrix and print out information.
    """
    # Verify symmetry of the interaction matrix
    if verify_symmetry(interaction_matrix):
        print("The interaction matrix is symmetric.")
    else:
        print("The interaction matrix is not symmetric.")

    # Calculate the number of members in the Karate club
    num_members = interaction_matrix.shape[0]
    print(f"The Karate club has {num_members} members.")

    # Calculate the number of interactions each member had
    interactions_per_member = np.sum(interaction_matrix, axis=1)
    print("Interactions per member:", interactions_per_member)

    # Find indices of least and most active members
    least_active_member_index = np.argmin(interactions_per_member)
    most_active_member_index = np.argmax(interactions_per_member)
    print(f"Index of least active member: {least_active_member_index}")
    print(f"Index of most active member: {most_active_member_index}")

    # Determine if the least and most active members had any interaction
    least_active_member_interaction = np.any(interaction_matrix[least_active_member_index])
    most_active_member_interaction = np.any(interaction_matrix[most_active_member_index])
    print(f"Did the least active member have any interaction? {least_active_member_interaction}")
    print(f"Did the most active member have any interaction? {most_active_member_interaction}")

    # Calculate the average and standard deviation of interactions across all members
    average_interactions = np.mean(interactions_per_member)
    std_interactions = np.std(interactions_per_member)
    print(f"Average interactions across all members: {average_interactions}")
    print(f"Standard deviation of interactions across all members: {std_interactions}")

# Path to the file containing the interaction matrix
file_path = "C:/Users/bunty/Desktop/DSC430/week_8/hw/karate_club_interactions.txt"

# Load the interaction matrix
interaction_matrix = load_interaction_matrix(file_path)

# Analyze the interaction matrix and print out information
analyze_interaction_matrix(interaction_matrix)
