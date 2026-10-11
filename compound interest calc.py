# Python Compound Interest Calculator

# 1. Get principal, rate, and time with validation
principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principal amount: "))
    if principle <= 0:
        print("Principal must be greater than zero.")

while rate <= 0:
    rate = float(input("Enter the interest rate (%): "))
    if rate <= 0:
        print("Interest rate must be greater than zero.")

while time <= 0:
    time = int(input("Enter the time in years: "))
    if time <= 0:
        print("Time must be greater than zero.")

# 2. Calculate compound amount
# Formula: A = P * (1 + r/100)^t
total = principle * pow((1 + rate / 100), time)

# 3. Output formatted results
print(f"\n--- Summary ---")
print(f"Principal Amount : ${principle:,.2f}")
print(f"Interest Rate    : {rate}%")
print(f"Time Period      : {time} years")
print(f"Total Balance    : ${total:,.2f}")
print(f"Interest Earned  : ${total - principle:,.2f}")