def Print(row:int,col:int):
    if row==0 and col==0: return
    for i in range(1,row+1):
        for j in range(1,col+1):   
               print("&",end=" ")
        print()
    
print("\n")   
Print(5,5)        
print("\n")