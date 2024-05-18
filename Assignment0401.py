# Author: Barini Simhadri
# Date: 06-02-2024
# Honor Statement: "I have not given or received any unauthorized assistance on this assignment."
# link: https://youtu.be/hsqMz-0I-O4

import random  #Importing the random module for generating random numbers.

# Taking user input for the number of elements in the list.
num = int(input("Enter a number: "))

myList = []  #Creating an empty list to store the random numbers.

# Generating 'num' random numbers and appending them to the list.
for i in range(0, num):
    x = random.randint(0, 100)
    myList.append(x)

myList.sort()  # Sorting the list in ascending order.
print("Random list: {}".format(myList))  # Printing the sorted list.

# Taking user input for the desired sum.
sum = int(input("Enter a sum: "))

i = 0  # Initializing variable i for the first index of the list.
j = len(myList) - 1  # Initializing variable j for the last index of the list.
flag = False  # Flag variable to indicate whether a pair is found or not.

# Loop to find pairs whose sum equals the given sum.
while i < j:
    if sum == myList[i] + myList[j]:  # Checking if the sum of elements at indices i and j equals the desired sum.
        print("Pair found with values {} and {}".format(myList[i], myList[j]))  # Printing the pair.
        flag = True  # Setting flag to True since a pair is found.
        break  # Exiting the loop since a pair is found.
    elif myList[i] + myList[j] > sum:  # If the sum of elements is greater than the desired sum.
        j = j - 1  # Decrementing j to move towards smaller numbers.
    else:  # If the sum of elements is less than the desired sum.
        i = i + 1  # Incrementing i to move towards larger numbers.

# Checking if a pair is not found and printing a message accordingly.
if flag == False:
    print("Pair not found with sum: {}".format(sum))
