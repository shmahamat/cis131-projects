"""
Souleyman Mahamat cis-131
3/11/2025
This script demonstrates the capabilities of the Fraction class and the built-in complex type in Python:

Performing arithmetic operations (addition, subtraction, multiplication, and division) on Fraction objects.
Displaying Fraction objects in the form a/b.
Converting Fraction objects to floating-point numbers.
Performing arithmetic operations on complex numbers.
Extracting and displaying the real and imaginary parts of complex numbers.
"""

from fractions import Fraction

# Demonstrating Fraction operations
frac1 = Fraction(3, 4)
frac2 = Fraction(2, 5)

# Addition
sum_result = frac1 + frac2
print(f"Addition: {frac1} + {frac2} = {sum_result}")

# Subtraction
diff_result = frac1 - frac2
print(f"Subtraction: {frac1} - {frac2} = {diff_result}")

# Multiplication
prod_result = frac1 * frac2
print(f"Multiplication: {frac1} * {frac2} = {prod_result}")

# Division
div_result = frac1 / frac2
print(f"Division: {frac1} / {frac2} = {div_result}")

# Printing fractions explicitly as a/b
print(f"Fraction 1: {frac1.numerator}/{frac1.denominator}")
print(f"Fraction 2: {frac2.numerator}/{frac2.denominator}")

# Converting to float
print(f"Float representation of {frac1}: {float(frac1)}")
print(f"Float representation of {frac2}: {float(frac2)}")

# Demonstrating complex number operations
complex1 = complex(3, 4)
complex2 = complex(1, -2)

# Printing complex numbers
print(f"Complex Number 1: {complex1}")
print(f"Complex Number 2: {complex2}")

# Addition
complex_sum = complex1 + complex2
print(f"Addition: {complex1} + {complex2} = {complex_sum}")

# Subtraction
complex_diff = complex1 - complex2
print(f"Subtraction: {complex1} - {complex2} = {complex_diff}")



# Getting real and imaginary parts
print(f"Real part of {complex1}: {complex1.real}")
print(f"Imaginary part of {complex1}: {complex1.imag}")
print(f"Real part of {complex2}: {complex2.real}")
print(f"Imaginary part of {complex2}: {complex2.imag}")
