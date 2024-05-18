# Author: Barini Simhadri
# Date: 16-01-2024
# Honor Statement: "I have not given or received any unauthorized assistance on this assignment."
# link: https://youtu.be/crB-7Yil21k

def calculate_gcd(a, b):
    """
    Calculate the Greatest Common Divisor (GCD) of two integers using the Euclidean algorithm and it Returns The GCD of the two input integers.
    """
    while b:
        a, b = b, a % b
    return a

def coprime(a, b):
    """
    Check if two integers are coprime and Returns True,otherwise false
    """
    return calculate_gcd(a, b) == 1

def coprime_test_loop():
    """
    Continuously asks the user for pairs of integers and check if they are coprime.
    If the user enters 'exit', the loop will break, and the program will end.
    """
    while True:
        num1 = int(input("Enter the first number: "))
        if num1 == 0:
            break
        num2 = int(input("Enter the second number: "))
        
        result = coprime(num1, num2)
        
        if result:
            print(f"{num1} and {num2} are coprime.")
        else:
            print(f"{num1} and {num2} are not coprime.")
        
        next_question = input("Do you want to enter another pair? (Type 'exit' to end): ")
        if next_question.lower() == 'exit':
            break
if __name__ == "__main__":
    coprime_test_loop()