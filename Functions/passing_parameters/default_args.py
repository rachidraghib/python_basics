def greet(name, age=50):
    print(f"Hello {name}, you are {age} years old ")
print("By Default\n")
greet("Rachid")  # Uses default age of 50 
print("\n")
greet("Rachid",36),print(" By Call",end="") # Overrides default age with 36. Priority is given to the argument passed during the function call.
print("\n")