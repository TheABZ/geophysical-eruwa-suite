import math

radius = float(input('Enter the radius of a circle: '))

circumference = 2 * math.pi * radius

print(f"The circumference is: {round(circumference, 2)}cm")
area = math.pi * radius ** 2
print(f"The area is: {round(area, 2)}")
