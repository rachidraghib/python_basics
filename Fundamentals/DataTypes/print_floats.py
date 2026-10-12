def pause():
    print("\nPress enter to continue...")
    input()
########################################################################################

x=123.123
print("\nx=1234.1234\n")
# Method roun(float,decimal) 
print(round(x,1),"    /1 decimal")
print(round(x,2),"   /2 decimals")
print(round(x,3),"  /3 decimals")
pause()
print(f"{x:.1f}","    /1 decimal")
print(f"{x:.2f}","   /2 decimal")
print(f"{x:.3f}","  /3 decimal")
pause()
print("{:.1f}".format(x),"    /1 decimal")
print("{:.2f}".format(x),"   /2 decimal")
print("{:.3f}".format(x),"  /3 decimal")