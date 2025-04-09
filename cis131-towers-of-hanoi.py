'''
Souleyman Mahamat
CIS131
04/08/25
'''

# Recursive solution to the Towers of Hanoi problem

def towers_of_hanoi(n, source, target, auxiliary):
    """
    Recursive function to solve the Towers of Hanoi puzzle.

    Parameters:
    n (int): Number of disks to move.
    source (int): The peg from which to move the disks.
    target (int): The peg to which the disks should be moved.
    auxiliary (int): The peg used for temporary storage.
    """
    # Base case: Only one disk to move
    if n == 1:
        print(f"{source} → {target}")
        return

    # Step 1: Move n-1 disks from source to auxiliary peg
    towers_of_hanoi(n - 1, source, auxiliary, target)

    # Step 2: Move the nth (largest) disk directly from source to target
    print(f"{source} → {target}")

    # Step 3: Move the n-1 disks from auxiliary to target peg
    towers_of_hanoi(n - 1, auxiliary, target, source)

# Main block to run the program
if __name__ == "__main__":
    # Prompt the user for number of disks
    num_disks = int(input("Enter the number of disks: "))

    # Print the move instructions
    print(f"Moves to solve Towers of Hanoi with {num_disks} disks:")
    towers_of_hanoi(num_disks, 1, 3, 2)