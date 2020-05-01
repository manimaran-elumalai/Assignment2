"""
File: moon_weight.py
--------------------
Add your comments here.
"""


def main():
    """
    You should write your code for this program in this function.
    Make sure to delete the 'pass' line before starting to write
    your own code. You should also delete this comment and replace
    it with a better, more descriptive one.
    """
    weight_on_earth = int(input("Pls enter your weight in KG's: "))
    earth_to_moon_conversion = 0.165
    weight_on_moon = weight_on_earth * earth_to_moon_conversion
    print("Your weight on moon will be: " + str(weight_on_moon))


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
