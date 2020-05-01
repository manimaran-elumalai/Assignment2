SHEET = 160
USAGE = 6


def main():
    rolls = float(input("Enter amount of rolls you have: "))
    toilet_visit_per_day = float(input("Enter the number of times of you visit toiler per day: "))
    how_long = int(SHEET * rolls / (USAGE * toilet_visit_per_day))
    print("How long = 160 sheets per roll * number of rolls / (6 sheets per toilet visit * toilet visit per day)...")
    print("Number of rolls = " + str(rolls) + " rolls")
    print("Toilet visit = " + str(toilet_visit_per_day) + " per day")
    print("You will last " + str(how_long) + " days!")
    print("")


if __name__ == '__main__':
	main()