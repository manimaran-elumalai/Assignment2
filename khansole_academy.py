"""
This program takes the comparison_count as the argument for parameter count and prints the result when the user enters
the sum of num1 and num2 correctly 3 times consecutively else will prompt the user to try again till they get it right.
"""

import random


def main():
    comparison_count = 1
    while comparison_count < 4:
        if random_addition(comparison_count):
            comparison_count += 1
        else:
            comparison_count = 1
    print("Congratulations! You mastered the addition.")


""" 
    # Defining a function with parameter COUNT
    # Creating 2 variable and storing the random number generated between 0 - 99
    # Print the sum of the 2 variable and stores the value under variable result
    # Checks if the input value from the user is equal to result
    
"""


def random_addition(count):
    num1 = random.randint(0, 99)
    num2 = random.randint(0, 99)
    result = num1 + num2
    print("What is " + str(num1) + " + " + str(num2))
    answer = int(input("Your answer: "))
    comparison_result = (answer == result)
    if comparison_result:
        print("Correct! You've gotten " + str(count) + " correct in a row")
    else:
        print("Incorrect... The expected answer is: " + str(result))
    return comparison_result


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
