# Author: Barini Simhadri
# Date: 29-01-2024
# Honor Statement: "I have not given or received any unauthorized assistance on this assignment."
# link: https://youtu.be/k1EUQf2ZhLU

def is_happy_sad_number(num):
    """
    Checks if a number is a happy number or sad number
    Returns:A tuple containing a string indicating whether the number is happy or sad,
    and a list of all numbers visited during the process.
    """
    visited = set()
    
    while num != 1 and num not in visited:#The function enters a while loop that continues until either num becomes 1 or it enters a cycle (sad).
        visited.add(num) #it adds the current number to the set of visited numbers.
        num = sum(int(digit) ** 2 for digit in str(num)) #its then sum of the squares of the digits of the current number.
    
    if num == 1:#if the num is equal to 1,then it returns happy with inlcusion of list of visited numbers.
        return "happy", list(visited) + [1]
    else:
        return "sad", list(visited) #If num is not 1, it returns a tuple with the string "sad" and the list of visited numbers.

def main():
    """
    This function serves as the main interaction loop with the user and processes happy or sad number
    """
    results = {} #a dictionary to store the results for each input number

    while True:#it enters the loop, and prompts the user, until user wants toexit the program.
        try:
            user_input = input("please,Enter a positive number (or type 'end' to finish): ")#prompts the user with this message.

            # Check if the user wants to end the program
            if user_input.lower() == 'end': #if the user input is end,
                break#then breaks the loop
            
            # it Converts input to integer and check if it's positive, then continue to the next step
            num = int(user_input)
            if num <= 0: #if the number is less than 0(user input),it displays the following message
                print("Please enter a positive number.")
                continue#continue to the next step

            # Check if the number is happy or sad
            result, visited_numbers = is_happy_sad_number(num) #It calls the is_happy_sad_number function to check if the number is happy or sad.

            # Display the result to the user
            print(f"{num} is a {result} number: {visited_numbers}") #The result is displayed to the user along with the list of visited numbers.

            # Update results dictionary
            results[num] = (result, visited_numbers)

        except ValueError:
            print("Please enter a valid positive integer.")

    print("\nSumming up the results:")
    print(results)


if __name__ == "__main__":
    main()