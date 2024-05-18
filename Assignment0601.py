# Author: Barini Simhadri
# Date: 20-02-2024
# Honor Statement: "I have not given or received any unauthorized assistance on this assignment."
# link: https://youtu.be/HEf0CyJr3VE

def is_palindrome(s):
    """
    Check if a string is a palindrome.
    Args:
        s (str): The string to check.
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    return s == s[::-1]

def generate_palindrome_dates():
    """
    Generate and save all palindrome dates in the 21st century to a text file.
    """
    palindrome_dates = []  # Initialize an empty list to store palindrome dates
    for year in range(2000, 2100):
        for month in range(1, 13):
            for day in range(1, 32):
                date_str = f"{day:02d}/{month:02d}/{year}"
                if is_palindrome(date_str):
                    palindrome_dates.append(date_str)  # Append palindrome date to list

    # Write palindrome dates to file only if there are any
    if palindrome_dates:
        with open("palindrome_dates.txt", "w") as file:
            for date_str in palindrome_dates:
                file.write(date_str + "\n")

if __name__ == "__main__":
    generate_palindrome_dates()
