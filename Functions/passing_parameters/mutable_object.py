def add_item(my_list):
    my_list.append("new_item")  # Modifies the object in place

fruits = ["apple", "banana"]
add_item(fruits)
print("\n")

print(fruits)  # Output: ['apple', 'banana', 'new_item']
print("\n")