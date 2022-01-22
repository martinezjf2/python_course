

# Create a Tuple initialized with 15 to 25 related values such as automobile types, states, names, etc. Complete the following steps using the Tuple you have just created. Steps:

# Initialize with values.

cars = ("Acura", "Audi", "Buick", "Cadillac", "Dodge", "GMC", "Honda", "Hyundai", "Infiniti", "Kia", "Jeep", "Lexus", "Mercedes-Benz", "Nissan", "Ram", "Porsche", "Saturn", "Tesla", "Toyota", "Volkswagon", "Volvo", "Mazda", "Genesis", "BMW")

# Display the contents in a single statement.

print(cars)

# Iterate through the collection displaying the output as a single complete sentence for each value.

for i in cars:
    print(i)

# Use the f-string format to control the output.

for index, car in enumerate(cars):
    print(f"The {car} is at index of {index} of the cars list")
    
    # resource used for this: https://stackoverflow.com/questions/522563/accessing-the-index-in-for-loops


# Repeat the output in reverse order using a different context string.

for index, car in enumerate(reversed(cars), -1):
    print(f"The {car} is number {index} of your cars list")

# Test your program until it works and the output looks nice.