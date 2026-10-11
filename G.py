credit_card = "1234-5678-9012-3456"

# Get the first 4 characters
print(credit_card[0:4])    # Output: "1234"

# Get characters starting from index 5 to the end
print(credit_card[5:])     # Output: "5678-9012-3456"

# Get every second character
print(credit_card[::2])    # Output: "13-680235"

# Reverse a sequence using a negative step
print(credit_card[::-1])   # Output: "6543-2109-8765-4321"

last_digits = credit_card[-4:]
print(f"Last digits: {last_digits}")