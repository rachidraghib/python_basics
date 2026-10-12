def show_menu():
    print("\n\t\t\t\tMAIN MENU")
    print("\t\t\t0. QuitT")
    print("\t\t\t1. append(item) List")
    print("\t\t\t2. insert(index,item) List")
    print("\t\t\t3. extend() List")
    print("\t\t\t4. pop() List")
    print("\t\t\t5. sort() List")
    print("\t\t\t6. reverse() List")
    print("\t\t\t7. remove() List")
def remove():
     list1=[9,-6,900,0,22]
     list2=["a","X","P","O","M","N"]
     list3=[]
     nl="\n"
     print("*"*78)
     print(nl,"List 2 ",list2)
     list2.remove("a") 
     list2.remove("N")
     print(nl,"'a'and 'N' removed from List 2 ",list2)
def pop():
    list1=[9,-6,900,0,22]
    list2=["a","X","P","O","M","N"]
    list3=[]
    nl="\n"
    print(nl,"List 1 ",list1)
    list1.pop(900)
    print(nl,"Popped List 1 (item '900' popped)",list1)

    print(nl,"List 2 ",list2)
    list2.pop("O")
    print(nl,"Popped List 2 (item 'O')",list2)

    print(nl,"List 1 ",list1)
    list1.pop(-6)
    print(nl,"Popped List 1 (item '-6' popped)",list1)

def reverse():
    list1=[9,-6,900,0,22]
    list2=["a","X","P","O","M","N"]
    list3=[]
    nl="\n"
    print(nl,"List 1 ",list1)
    list1.reverse()
    print(nl,"Reversed List 1 is  ",list1)

          
     
                   
def insert():
    list1=[9,-6,900,0,22]
    list2=["X","P","O","M","N"]
    list3=[]
    nl="\n"
    print("*"*78)
    print(nl,"List 1",list1)
    list1.insert(0,-2000)
    print(nl,"Inserteded List 1 ",list1,nl)
    print("*"*78)
    print(nl,"List 2",list2)
    list2.insert(1,"R")
    print(nl,"Inserteded List 2",list2,nl)
    print("*"*78)
    print(nl,"List 3",list3)
    list3.insert(1,"Rachid")
    print(nl,"Inserteded List 3",list3,nl)
def extend():
        list1=[9,-6,900,0,22]
        list2=["X","P","O","M","N"]
        list3=[]
        nl="\n"
        print("*"*78)
        print(nl,"List 3",list3)  
        list3.extend(list1+list2)
        print(nl,"Inserteded List 3",list3,nl)
        print("*"*78)
def append():
        
  list1=[9,-6,900,0,22]
  list2=["X","P","O","M","N"]
  list3=[]
  nl="\n"

  print(nl,"List 1",list1)
  list1.append(78)
  print(nl,"Appended List 1",list1,nl)
  print("*"*78)

  print(nl,"List 2",list2)
  list2.append("Y")
  print(nl,"Appended List 2",list2,nl)
  print("*"*78)

  print(nl,"List 3",list3)
  list3.append(0.0001)
  print(nl,"Appended List 3",list3,nl)
  print("*"*78)

  print(nl,"List 3",list3)
  list3.append(list2)
  print(nl,"Appended List 3",list3,nl)
  print("*"*78)

def switch(choice):
    if choice==0:
        return print()
    elif choice==1:
        return append()
    elif choice==2:
        return insert()
    elif choice==3:
        return extend()
    elif choice==4:
        return remove()
    elif choice==5:
        return pop()
    elif choice==6:
            return reverse()
    elif choice==7:
                return remove()
        
    
nl="\n"
show_menu()
choice=int(input("\nEnter your choice: "))
print(switch(choice))






