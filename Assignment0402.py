# Author: Barini Simhadri
# Date: 06-02-2024
# Honor Statement: "I have not given or received any unauthorized assistance on this assignment."
# link: https://youtu.be/FHYLoU4ajkI

def humanPyramid(row, column):
    # Base case: If the person is at the top of the pyramid (row 0), they have no weight on their back.
    if row == 0:
        return 0
    # Base case: If the person is at the edges of the pyramid (column 0 or the same as the row), they support their own weight.
    if column == 0 or column == row:
        return 128 + humanPyramid(row - 1, 0) / 2
    # Recursive case: Calculate the weight on the person's back by splitting the weight of the two people above them.
    return 128 + (humanPyramid(row - 1, column - 1) + humanPyramid(row - 1, column)) / 2

# Example usage:
row = 5
column = 5
total_weight = humanPyramid(row, column)
print(f"Total weight on the person at row {row}, column {column}: {total_weight} pounds")