"""
Souleyman Mahamat
CIS-131
4/1/2025

This script calculates Fibonacci numbers using recursive approach.
It also tracks and displays the total number of function calls made during 
the computation for a given input.
"""

# Global variable to count function calls
call_count = 0

def fibonacci(n):
    """
    Recursively computes the nth Fibonacci number.
    Increments the global call counter with each function call.
    """
    
    global call_count
    call_count += 1

    # Base cases: return n if it's 0 or 1
    if n in (0, 1):
        return n
    else:
        # Recursive calls to compute previous two Fibonacci numbers
        return fibonacci(n - 1) + fibonacci(n - 2)

# Test fibonacci function and display results for specific values
for num in [10, 20, 30]:
    call_count = 0  # Reset the call count before each test
    result = fibonacci(num)
    print(f"fibonacci({num}) = {result}, function calls = {call_count}")