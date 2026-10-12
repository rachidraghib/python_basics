def show_menu():
    print("\t\tMAIN MENU")
    print("\t\t0. QUIT")
    print("\t\t1. Java Script")
    print("\t\t2. PHP")
    print("\t\t3. Python")
    print("\t\t4. Solidity ")
    print("\t\t4. Java")

def switch(choice):
    if choice==0:
        return print()
    elif choice==1:
        return "You become a web developer"
    elif choice==2:
        return "You become a web developer"
    elif choice==3:
        return "You become a data scientst"
    elif choice==4:
        return "You become a blockchain developer"
    elif choice==5:
        return "You become a mobile app developer"
nl="\n"
show_menu()
choice=int(input("\nEnter your choice: "))
print(nl,switch(choice),nl)