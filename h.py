# format specifiers = {:flags} format a value based on what flags are inserted

price = 3.14159
num = 5
text = "code"
pos = 20
neg = -20
balance = 1000000

# 1. Round to decimal places (fixed point)
print(f"1. Precision: {price:.2f}")

# 2. Field width and zero padding
print(f"2. Width (10 spaces): '{num:10}'")
print(f"   Zero pad (3 digits): {num:03}")

# 3. Text alignment
print(f"3. Left justify:   '{text:<10}'")
print(f"   Right justify:  '{text:>10}'")
print(f"   Center align:   '{text:^10}'")

# 4. Sign indicators
print(f"4. Plus sign: {pos:+}")
print(f"   Leftmost sign: {neg:=10}")
print(f"   Space before positive: '{pos: }'")

# 5. Comma separator
print(f"5. Comma separator: ${balance:,}")

# 6. Combined specifiers
big_price = 1234.5678
print(f"6. Combined flags: {big_price:+15,.2f}")