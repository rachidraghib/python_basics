def pause():
    print("\nPress enter to continue...")
    input()
########################################################################################
def is_super(my_list:list,marker:int,target:int):
    inside_one:bool
    inside_two:bool
    inside_one=False
    inside_two=False
    for i in my_list:
        if my_list[i]==target:
            for j in my_list[:i]:
                if my_list[i]==marker:
                    inside_one=True
                  
            for j in my_list[i+1:]:
                if my_list[i]==marker:
                    inside_two=True
    print()        
                
    if inside_one==True and inside_two==True:
        print("Is Nop Super returns\n")
        return 0
        
    else:
         print("Is Super returns\n")
         return 1
        

########################################################################################

my_list:list
my_list={1,2,3,4,5}
size=len(my_list)
print("\n")
(my_list,3,1)

print("\n")