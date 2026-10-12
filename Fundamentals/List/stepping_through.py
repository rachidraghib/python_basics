################################# VARIABLES INITIALIZATION ###############################
str:str
str="\n################## DONE ##################"
nl="\n"
M = [0,1,2,3,4,5,6,7,8,9]
N=[]
size1=len(M)
size2=len(N)
################################ CODE DISPLAY FUNCTIONS #################################
def show_code1():
    print("\n\nM=",M)
    print("\nN=M[::2]\n#Gets every second item"\
           "Skips items based on the step value") 
def show_code2():
        print("\nM=",M)
        print("\nA=M[1:7:3]\nprint(A) returns") 
            
        
########################################################################################
def pause():
    print("\nPress enter to continue...")
    input()
########################################################################################
def program1():
    show_code1()
    N=M[::2] #Gets every second item.Skips items based on the step value
    print(N,str)
    pause()
########################################################################################
def program2():
    show_code2()
    A=M[1:7:3] #starts at 1 included. stops at 7 excluded but incrementing by 3 
    print(A,str)
    pause()
########################################################################################


############################## Calling Program Functios ################################
program1()
program2()
#######################################################################################

