# Author: Barini Simhadri
# Date: 16-01-2024
# Honor Statement: "I have not given or received any unauthorized assistance on this assignment."
# link: https://youtu.be/M6fhc1ke7v0

# This function asks the user whether the file is submitted as uncompressed.py file(yes/no) and returns the user input
def correctFile():
    """
    Asks the user whether the assignment is submitted as a single uncompressed .py file.
    Returns:True if the user input is 'yes', False otherwise.
    """
    file_type = input("Is the assignment submitted as a single uncompressed .py file? (yes/no): ")
    return file_type.lower() == 'yes'

# This function asks the user whether the name and date is included(yes/no) and returns the user input
def includesName():
    """
    Asks the user whether the assignment includes the author's name and date.
    Returns:True if the user input is 'yes', False otherwise.
    """
    name = input("Does the assignment include the author's name and date? (yes/no): ")
    return name.lower() == 'yes'

# This functions asks the user whether the honor statement is included(yes/no) and returns the user input
def includesHonorStatement():
    """
    Asks the user whether the assignment includes the honor statement.
    Returns:True if the user input is 'yes', False otherwise.
    """
    honor_statement = input("Does the assignment include the honor statement? (yes/no): ")
    return honor_statement.lower() == 'yes'

# This function asks the user whether the link is included whichi not more than 3-minute video(yes/no) and returns the user input
def includesYouTubeLink():
    """
    Asks the user whether the assignment includes a link to an unlisted 3-minute YouTube video.
    Returns:True if the user input is 'yes', False otherwise.
    """
    youtube_link = input("Does the assignment include a link to an unlisted 3-minute YouTube video? (yes/no): ")
    return youtube_link.lower() == 'yes'

# This function asks the user to rate on a scale of 0-10 that evaluates the correctness of the code and returns the user input
def correctnessPoints():
    """
    Asks the user to rate the correctness of the code on a scale of 0-10.
    Returns:The user's input as an integer.
    """
    points = int(input("Out of ten points, how would you evaluate the correctness of the code? (0-10): "))
    return points

# This function asks the user to rate on a scale of 0-10 that evaluates the elegance of the code and returns the user input
def elegancePoints():
    """
    Asks the user to rate the elegance of the code on a scale of 0-10.
    Returns:The user's input as an integer.
    """
    points = int(input("Out of ten points, how would you evaluate the elegance of the code? (0-10): "))
    return points

# This function asks the user to rate on a scale of 0-10 that evaluates the code hygiene and returns the user input
def hygienePoints():
    """
    Asks the user to rate the code hygiene on a scale of 0-10.
    Returns:The user's input as an integer.
    """
    points = int(input("Out of ten points, how would you evaluate the code hygiene? (0-10): "))
    return points

# This function asks the aser to rate on a scale of 0-10 that evaluates the quality of the discussion in the YouTube video and returns the user input
def videoQualityPoints():
    """
    Asks the user to rate the quality of the discussion in the YouTube video on a scale of 0-10.
    Returns:The user's input as an integer.
    """
    points = int(input("Out of ten points, how would you evaluate the quality of the discussion in the YouTube video? (0-10): "))
    return points

# This computeGrade function returns 0 if any of the conditions specified in the if statements are not met and it computes the total points 
def computeGrade():
    """
    Computes the final grade based on aformentioned conditions and user inputs.
    Returns:The total points if all conditions are met, otherwise 0.
    """
    if not correctFile():
        return 0
    
    if not includesName():
        return 0
    
    if not includesHonorStatement():
        return 0
    
    if not includesYouTubeLink():
        return 0

    total_points = correctnessPoints() + elegancePoints() + hygienePoints() + videoQualityPoints()

    return total_points

# Run the computeGrade function
final_grade = computeGrade()

# Prints the student's final grade
print(f"The student's total score is: {final_grade}")
