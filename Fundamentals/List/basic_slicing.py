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
    print("\nN=M[2:6]\n#extracts range[2,6["\
           " and copies it to list N\nprint(N) returns") 
def show_code2():
        print("\nM=",M)
        print("\nA=M[:4]\nprint(A) returns") 
            
def show_code3():
    print("\nM=",M)
    print("\nB=M[:]\nprint(B) returns")    
def show_code4():
    print("\nM=",M)
    print("\nC=M[:]\n#extracts range[7,default=last item] "\
              "and copies it to list C\nprint(C) returns") 
        
########################################################################################
def pause():
    print("\nPress enter to continue...")
    input()
########################################################################################
def program1():
    show_code1()
    N=M[2:6] #extracts range[2,6[ and copies it to list list2
    print(N,str)
    pause()
########################################################################################
def program2():
    show_code2()
    A=M[:4] #extracts range[default=0,4[ and copies it to list A
    print(A,str)
    pause()
########################################################################################
def program3():
    show_code3()
    B=M[:] #copies the entire list creating a shallow copy
    print(B,str)
    pause()

########################################################################################
def program4():
    show_code4()
    C=M[7:] ##extracts range[7 default=last item] and copies it to list C
    print(C,str)
    pause()


############################## Calling Program Functios ################################
program1()
program2()
program3()
program4()
#######################################################################################

