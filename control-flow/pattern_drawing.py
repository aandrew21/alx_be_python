# pattern_drawing.py

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Use a while loop to iterate through each row
row = 0
while row < size:
    # Use a for loop to print the asterisks in each row
    for col in range(size):
        print("*", end="")  # Print '*' without moving to the next line
    print()  # Move to the next line after printing a row
    row += 1  # Increment the row count
