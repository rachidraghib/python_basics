def print_elements(list: list, size: int):
    # Optional safety check to verify the list length matches the argument
    if len(list) != size:
        raise ValueError(f"Error: List length {len(list)} does not match expected {size}.")
    
    print(f"Processing list of verified length {size}:")
    for i in list:
        print(f"{i}")

# --- How to call the function ---
fruits = ["apple", "banana", "cherry"]
numbers = [1,2,3,4,5,6,7,8,9,10]
# This works perfectly
print_elements(fruits,3) 

print_elements(numbers,len(numbers)) 
