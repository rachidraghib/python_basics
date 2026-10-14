nl='\n'
################################################################
def pause():
    print("\nPress enter to continue...")
    input()

################################################################

def Print_Sum(x,y):
    print(int(x+y))
#############################################################

print("The sum is")
Print_Sum(1,2)

a=[1,2,3,4,5,6,7,8,9,10]
b=a
c=b[:]
d=a[:]
a.append(11)
b.append(4)
c.append(5)
print(nl,a,nl,b,nl,c,nl,d)
pause()
################################################################
print("\n")
x=[1,2,3,4,5,6,7,8,9,10]
print("x=[1,2,3,4,5,6,7,8,9,10]")
print("print(x[::-1])\n")
print(x[::-1])
print("\n")
pause()
################################################################
print("print(x[::-2])\n")
print(x[::-2])

print("print(x[::-3])\n")
print(x[::-3])

print("print(x[::1])\n")
print(x[::1])
print("print(x[::2])\n")
print(x[::2])
print("print(x[::3])\n")
print(x[::3])

s="rachidraghib"
length=len(s)

print(s.upper())
print(nl) 
print("The lenth of "+s+" is ") 
print(length)
s="First Name: "+s[:6]+nl+"Last Name: "+s[6:]
print(s)
