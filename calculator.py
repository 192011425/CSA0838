def add (x,y):
    return x+y
def sub (x, y):
    return x-y
def mult (x, y):
    return x*y
def div (x, y):
    return x/y
print ("select operation")
print ("1.add")
print ("2.sub")
print ("3.mult")
print ("4.div")
choice=input("enter choice (1/2/3/4):")
if choice in ("1","2","3","4"):
    a=int(input ("enter the number 1:"))
    b=int(input ("enter the number 2:"))
    c=int(input ("enter the number 3:"))
if choice=="1":
    print (a, "+",b, "=", add (a, b,c))
elif choice=="2":
    print (a, "-",b, "=", sub (a,b,c))
elif choice=="3":
    print (a, "*",b,"=",mult (a, b,c))
elif choice=="4":
    print (a,"/",b,"=", div(a,b,c))
else:    
    print ("3+2*2")
