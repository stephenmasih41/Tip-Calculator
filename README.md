# 🧮 Tip Calculator 💸  
### 📅 Day 2 of My Python Bootcamp Journey 🚀  

Welcome to my second Python project — a **Tip Calculator**! 🎉  
This program helps you easily calculate how much each person should pay when splitting a bill, including the tip. No more awkward math at the restaurant! 🍽️💰

---

## 💡 What This Does

This program:
1. Greets the user with a warm welcome! 👋  
2. Asks for the **total bill** amount 💵  
3. Lets the user choose a **tip percentage** (10%, 12%, or 15%) 💯  
4. Calculates the **total with tip** included 🧾  
5. Asks how many people are **splitting the bill** 👥  
6. Outputs **how much each person should pay**, rounded to 2 decimal places 💳

---

## 🧠 Code Used

```python
print("Welcome to the tip calculator!") 
total_bill = int(input("What was the total bill? $ "))
tip_percent = int(input("How much tip would you like to give? 10, 12, or 15? "))
tip_calculate = total_bill * (tip_percent / 100)
total_bill += tip_calculate
bill_split = int(input("How many people to split the bill? "))
individual_bill = round(total_bill / bill_split, 2)
print(f"Each person should pay: ${individual_bill}")
