import matplotlib.pyplot as plt

# Function to calculate the quadratic solution
def calculate_quadratic(a, b, c, x_values):
    y_values = [a * x**2 + b * x + c for x in x_values]
    return y_values

# Function to plot the graph
def plot_graph(x_values, y_values, title="Weather Parameter Visualization"):
    plt.figure(figsize=(8, 5))
    plt.plot(x_values, y_values, label="y = ax² + bx + c", color="blue", marker="o")
    plt.axhline(0, color="black", linewidth=0.5, linestyle="--")
    plt.axvline(0, color="black", linewidth=0.5, linestyle="--")
    plt.title(title)
    plt.xlabel("Time (x)")
    plt.ylabel("Weather Parameter (y)")
    plt.grid(alpha=0.3)
    plt.legend()
    plt.show()

# Stage 1: Hard-coded example
def hard_coded_example():
    a, b, c = 0.5, -3, 10
    x_values = list(range(-10, 11))  # Time values from -10 to 10
    y_values = calculate_quadratic(a, b, c, x_values)
    plot_graph(x_values, y_values, title="Hard-Coded Variables Example")

# Stage 2: Keyboard Input
def keyboard_input_example():
    a = float(input("Enter the coefficient a: "))
    b = float(input("Enter the coefficient b: "))
    c = float(input("Enter the coefficient c: "))
    x_start = int(input("Enter the start of time range (x): "))
    x_end = int(input("Enter the end of time range (x): "))
    x_values = list(range(x_start, x_end + 1))
    y_values = calculate_quadratic(a, b, c, x_values)
    plot_graph(x_values, y_values, title="Keyboard Input Example")

# Stage 3 & 4: Read from File
def file_input_example(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
    
    for idx, line in enumerate(lines):
        a, b, c, x_start, x_end = map(float, line.split())
        x_values = list(range(int(x_start), int(x_end) + 1))
        y_values = calculate_quadratic(a, b, c, x_values)
        plot_graph(x_values, y_values, title=f"File Input Example Set {idx + 1}")

# Choose a stage to run
print("Choose a stage to visualize:")
print("1. Hard-coded variables")
print("2. Keyboard input")
print("3. File input (multiple sets)")
choice = int(input("Enter your choice (1/2/3): "))

if choice == 1:
    hard_coded_example()
elif choice == 2:
    keyboard_input_example()
elif choice == 3:
    file_name = input("Enter the file name (e.g., input_multiple.txt): ")
    file_input_example(file_name)
else:
    print("Invalid choice!")