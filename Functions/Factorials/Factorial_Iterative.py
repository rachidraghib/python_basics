def pause():
    print("\nPress enter to continue...")
    input()

################################################################

def factorial_iterative(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print("Factorial of 5 using iterative method:\n")
print(factorial_iterative(5))  # Output: 120
################################################################
pause()
