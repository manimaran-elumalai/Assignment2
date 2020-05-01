"""
File: nimm.py
-------------------------
Add your comments here.
"""


def main():
    stones = 20
    print("There are " + str(stones) + " stones")
    while stones > 0:
        stones_to_remove = int(input("enter the stones to remove: "))
        stones -= stones_to_remove
        print("there are " + str(stones) + " stones remaining.")
    print("Game over!")




"""
This provided line is required at the end of a Python file to call the main() function
"""

if __name__ == '__main__':
    main()
