def pause():
    print("\nPress enter to continue...")
    input()
########################################################################################
def print_list(list: list):
    s=print(list)
    return s
#########################################################################################      

#########################################################################################
def copy_list(source:list,length:int):
     # Using list slicing to safely copy elements up to the specified length
     destination=source[:length]
     
     print("\nOriginal List\n")
     print_list(source)
     print("\nCopied List\n")
     print_list(destination)

     return destination
#########################################################################################  
# --- Calling Functions ---
original=["Rachid","Fatima","Julie","Adam","Leah"]


copy_list(original,len(original))
                              
pause()
##################################
