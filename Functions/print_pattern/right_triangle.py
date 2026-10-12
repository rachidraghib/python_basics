def print_pattern(row:int):
    for i in range(1, row + 1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()
#////////////////////////////////////////////////        
def print_inverted(n:int):
    for i in range(n, 0, -1):
        for j in range(0, i):
            print("*", end=" ")
        print()
#////////////////////////////////////////////////
print_inverted(5)   
print_pattern(5)