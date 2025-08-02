print("Welcome to the tip calculator!")
total_bill = int(input("What was the total bill? $ "))
tip_percent = int(input("How much tip would you like to give? 10, 12, or 15? "))
tip_calculate = total_bill * (tip_percent / 100)
total_bill+=tip_calculate
bill_split = int(input("How many people to split the bill? "))
individual_bill = round(total_bill / bill_split,2)
print(f"Each person should pay: ${individual_bill}")