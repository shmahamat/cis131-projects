import datetime
import time

# Get the current date and time and store it in variable x
x = datetime.datetime.now()

# Waste some time to get an interesting output
time.sleep(1)

# Get the current date and time again and store it in variable y
y = datetime.datetime.now()

# Display each datetime object
print(f"x: {x}")
print(f"y: {y}")

# Display each datetime object's data attributes individually
print("\nAttributes of x:")
print(f"Year: {x.year}, Month: {x.month}, Day: {x.day}, Hour: {x.hour}, Minute: {x.minute}, Second: {x.second}, Microsecond: {x.microsecond}")

print("\nAttributes of y:")
print(f"Year: {y.year}, Month: {y.month}, Day: {y.day}, Hour: {y.hour}, Minute: {y.minute}, Second: {y.second}, Microsecond: {y.microsecond}")

# Use the comparison operators to compare the two datetime objects
print("\nComparison Results:")
print(f"x == y: {x == y}")
print(f"x < y: {x < y}")
print(f"x > y: {x > y}")
print(f"x <= y: {x <= y}")
print(f"x >= y: {x >= y}")

# Calculate the difference between y and x
time_difference = y - x
print(f"\nTime difference (y - x): {time_difference}")
