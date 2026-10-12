def Print(n:int):
    for i in range(1, n + 1):
    # Print leading spaces, then print the stars
         print(" " * (n- i) + "* " * i)
Print(5)