def pause():
    print("\nPress enter to continue...")
    input()

################################################################
def factorial_recursive(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    # Base case: 0! and 1! are both 1
    if n <= 1:
        return 1
    # Recursive case
    return n * factorial_recursive(n - 1)

print(factorial_recursive(5))  # Output: 120

################################################################
pause()
