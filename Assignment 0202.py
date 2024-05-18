# Author: Barini Simhadri
# Date: 22-01-2024
# Honor Statement: "I have not given or received any unauthorized assistance on this assignment."
# link: https://youtu.be/MGhz2fOczSY

def greet_user():
    """
    This function greets the user by welcome messasgeg
    """
    print("Hey,Welcome to the Stem and Leaf Plot!")

def read_data_file(file_path):
    """
    This function just reads the file path which consists of three text files.
    """
    with open(file_path, 'r') as file: # to close the file once it reaeds, we use with statement
        data = [int(line.strip()) for line in file.readlines()] # this data stores the all the integers present in the specified files.
    return data #returns the data

def display_stem_and_leaf_plot(data):
    """
    This function displays the stemleaf chart based on the file provided by the user.
    """
    stem_and_leaf_dict = {}
    for number in data:
        stem, leaf = divmod(number, 10)
        if stem not in stem_and_leaf_dict:
            stem_and_leaf_dict[stem] = [leaf]
        else:
            stem_and_leaf_dict[stem].append(leaf)

    print("This is the Stem and Leaf Plot for the given datafile:")
    for stem, leaves in sorted(stem_and_leaf_dict.items()): #we use for clause, in order to sort the numbers in the chart
        print(f"{stem} | {' '.join(map(str, sorted(leaves)))}")

def main():
    greet_user() #greets the user is the first step in this function.

    file_paths = ["C:/Users/bunty/Desktop/week_2/StemAndLeaf1.txt",#file1 which is consists of stemandleaf1 text file
                  "C:/Users/bunty/Desktop/week_2/StemAndLeaf2.txt",#file1 which is consists of stemandleaf2 text file
                  "C:/Users/bunty/Desktop/week_2/StemAndLeaf3.txt"]#file1 which is consists of stemandleaf3 text file

    while True:
        user_input = input("Enter 1, 2, or 3 to display a stem and leaf plot,otherwise Enter 0 to exit: ")#enters the loop to promts the user to enter 1-3 or 0 numbers,until he answers
        
        if user_input == '0':# if user enters 0,it prints 'bye'
            print("Bye")
            break

        try:
            user_input = int(user_input) #it saves the user input in to user_input variablel
            if 1 <= user_input <= 3: # now it takes the user input(1-3)
                data = read_data_file(file_paths[user_input - 1]) # it reads the file based on the user inmput
                display_stem_and_leaf_plot(data) # display the plot,where it takes the arguments from the stem and leeaf function.
            else:
                print("Please enter 1, 2, or 3.") # if user enter other than 0-3,like any characters,strings,floats
        except (ValueError, IndexError):
            print("Please enter a valid number between 1 and 3, or enter 0 to exit the porgram.") # its prints this message

if __name__ == "__main__":
    main() 
