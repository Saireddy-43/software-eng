import math

# Read values from file
with open('/Users/hemanthroyal/Desktop/exp1/input2.txt', 'r') as file:
    a = float(file.readline().strip())
    b = float(file.readline().strip())
    c = float(file.readline().strip())

# Calculate discriminant
discriminant = b**2 - 4*a*c

if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(f"Two roots: {root1}, {root2}")
elif discriminant == 0:
    root = -b / (2 * a)
    print(f"One root: {root}")
else:
    print("No real roots")