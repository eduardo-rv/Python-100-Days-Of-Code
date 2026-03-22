# Day 2: Tip calculator
# This program asks for the total bill, the percentage of tip, and the number of people.
# It calculates how much each person should pay and prints the result.

print(f"Welcome to the split calculator")

bill = float(input("What was the total bill?: "))
tip_percent = float(input("How much tip would you like to give?: "))

total_bill =  bill + ((tip_percent / 100) * bill)

peoples = int(input("How many people to split the bill?: "))
each_pay = round(total_bill / peoples, 2)

print(f"Each person should pay: {each_pay}")

