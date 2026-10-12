def Print(list:list):
    for num in list:
        print(" ",num,end=" ")
    print()
#///////////////////////////////////
def largest(list:list,len:int):
    largest=list[0]
    for num in range(0,len+1):
        if list[num]>largest:
            largest=list[num]
            continue
    print(largest)

#//////////////////////////////////    
numbers = [55, 35, 1, 10, 34, 1, 99]
print("\n")
print("The numbers in the list are:\n")
Print(numbers)
print("The largest number in the list is:\n")
largest(numbers,len(numbers))
print("\n")

