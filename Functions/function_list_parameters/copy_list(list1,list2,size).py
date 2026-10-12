def pause():
    print("\nPress enter to continue...")
    input()
########################################################################################
def print_list(list: list):
    s=print(list)
    return s
#########################################################################################      
def copy_items(list1: list,list2: list, size: int):
  
    #Appends a specific number of items from the source list to an existing list.
         
    list2.extend(list1[:size])
        
#########################################################################################


##################################
list1 = [1,2,3,4,5]
list2=[6,7]
size1=len(list1)
size2=len(list2)

#########################################################################################
copy_items(list1,list2,size1)
print("\nOriginal\n",list1)

print("\nModified\n",list2)

print(f"\nNow Check above for updated list2")
pause()
#########################################################################################




