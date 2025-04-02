"""
Souleyman Mahamat
CIS-131
4/1/2025

This program calculates the result of raising a base to an exponent using recursion.
It prompts the user to input a base and an exponent (integer >= 1), then recursively
computes base^exponent. The calculation is done via a custom recursive function
without using built-in exponentiation.
"""


def power(base, exponent):
    """Recursively computes base raised to exponent."""
    
    # Base case: if exponent is 1, return the base
    if exponent == 1:
        return base
    else:
        # Recursive step: base * base^(exponent - 1)
        return base * power(base, exponent - 1)


def main():
    """Handles user input and displays the result."""

    try:
        # Prompt user to enter base and exponent
        base = int(input("Enter the base (integer): "))
        exponent = int(input("Enter the exponent (integer >= 1): "))

        # Check for valid exponent input
        if exponent < 1:
            print("Exponent must be greater than or equal to 1.")

        # Call the recursive power function
        result = power(base, exponent)

        # Display the result
        print(f"{base}^{exponent} = {result}")

    except ValueError:
        # Handle non-integer input
        print("Please enter valid integers for base and exponent.")

# Run the program only if this file is executed directly
if __name__ == "__main__":
    main()