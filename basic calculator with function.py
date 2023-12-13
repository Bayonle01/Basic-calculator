def add(a,b):
    answer=a+b
    print(f"{a}+{b} = {answer}")
def sub(a,b):
    answer=a-b
    print(f"{a}-{b} = {answer}")
def mul(a,b):
    answer=a*b
    print(f"{a}*{b} = {answer}")
def div(a,b):
    answer=a/b
    print(f"{a}/{b} = {answer}")


print("A. Addition")
print("B. Subtraction")
print("C. Multiplication")
print("D. Division")
print("E. Exit")


while True:
    choice=input("enter the choice")
    if choice=="e" or choice=="E":
        print("program ended")
    
    
    a=int(input('input a'))
    b=int(input('input b'))
    
    if choice=="a" or choice== "A":
        print("Addition")
        add(a,b)
    elif choice== "b" or  choice=="B":
        print("Subtraction")
        sub(a,b)
    elif choice=="c" or choice=="C":
        print("Multiplication")
        mul(a,b)
    elif choice=="d" or choice=="D":
        print("Division")
        div(a,b)
    
    
   


    




























