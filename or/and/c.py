# input() = A function that prompts the user for input in the console.
# It reads input as a string and returns it.

name = input("What is your name?: ")
print(f"Hello {name}, I am Godwin Unomah.")

age = int(input("What is your age?: "))
print(f"Wow! You are {age} years old. I am 21 years old.")

print("I heard today is your birthday, HAPPY BIRTHDAY TO YOU!")
next_age = age + 1

age_check = input(f"So, are you {next_age} years old now? (yes/no): ").strip().lower()

if age_check in ["yes", "y"]:
    print("Wow, that's great!")
elif age_check in ["no", "n"]:
    print("Sorry for mistaking it!")
else:
    print("I'll take that as a maybe! Either way, I am happy for you.")