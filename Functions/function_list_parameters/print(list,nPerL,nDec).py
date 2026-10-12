################################# VARIABLES INITIALIZATION ###############################
str:str
str="\n################## DONE ##################"
nl="\n"
M = [0,1,2,3,4,5,6,7,8,9]
N=[]
size1=len(M)
size2=len(N)
########################################################################################
def pause():
    print("\nPress enter to continue...")
    input()
########################################################################################
def print_list(data:list,n_l:int,decimals:float):
    # Formats the decimal formatting rule (e.g., {:.2f})
    fmt = f"{{:.{decimals}f}}"
    
    # Loop through the list in chunks
    for i in range(0, len(data), n_l):
        chunk = data[i:i + n_l]
        # Format each float and join them with spaces
        line1 = "     ".join(fmt.format(num) for num in chunk)
        
        
        print(line1)
        
        

########################################################################################
scores=[99.23456,97.3456,99.23456,97.3456,99.23456,97.3456,99.23456,97.3456,99.23456,97.3456]
print_list(scores,5,2)