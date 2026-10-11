# logical operators = evaluate multiple conditions (or, and, not)
#                     or  = at least one condition must be True
#                     and = both conditions must be True
#                     not = inverts the condition (not False, not True)

temp = 32
is_raining = True

if temp >= 30 and is_raining:
    print("It is HOT outside")
    print("It is SUNNY")
elif temp <= 0 and is_raining:
    print("It is COLD outside")
    print("It is SUNNY")
elif 30 >temp > 0 and is_raining:
    print("It is WARM outside")

