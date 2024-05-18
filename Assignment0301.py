# Author: Barini Simhadri
# Date: 29-01-2024
# Honor Statement: "I have not given or received any unauthorized assistance on this assignment."
# link: https://youtu.be/34IB6Q6UuzY

def Check_prime(n):
    """
    this function Checks if a given number is a prime.and it prints the sum of two primes that equals the even number. 
    """
    if n < 2:#if the n-number is less than 2,its not a prime
        #Because 1 is not a prime number.
        return False#so,it returns false
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:#if the n is divisible by any number within this range, its not a prime number
            return False#return false
    return True#if there are no divisors,its a prime and returns true

def goldbach_conjecture(limit):
    """
    This function looks for all possible integers less than the given limit-100
    """
    if limit < 4: #if the limit(100) is less than 4, then it prints the following message.
        print("Conjecture in number theory is not applicable for integers less than 4.")
        return
    
    for num in range(4, limit + 1, 2): #it iterates from 4 to the limit+1(including the 100) with a step size of 2,(only even numbers)
        found = False #for every even number, it intializes the found to false,then goes to the next step
        for i in range(2, num // 2 + 1):#it iterates from 2 to the current even number
            if Check_prime(i) and Check_prime(num - i):#if both i and num-i are prime, it sums up
                print(f"{num} = {i} + {num - i}")#it prints the sum of two prime that equals the even number
                found = True#and set to found true
                break#breaks the loop
        if not found:#if there's no prime sum,it prints the following mesasage.
            print(f"Not found{num}")

if __name__ == "__main__":
    goldbach_conjecture(100)