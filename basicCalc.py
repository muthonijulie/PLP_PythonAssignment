a=float(input("Enter the first value:"))#converts the string into float
b=float(input("Enter the second value:"))
op=input("Enter the operator(+,-,*,/):")
#function
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    if b!=0:

      return a/b
    else:
        return "Impossible"
#condition to perform the operation
if op=="+":
    res=add(a,b)
elif op=="-":
    res=subtract(a,b)
elif op=="*":
    res=multiply(a,b)
elif op=="/":
    res=division(a,b)
else:
    print(f"Invalid")


print(f"The result is:{res}")
