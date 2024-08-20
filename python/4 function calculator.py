def add():
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))
    print(num1+num2)
#add()
def subtract():
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))
    print(num1 - num2)
#subtract()
def multiply():
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))
    print(num1 * num2)
#multiply()
def divide():
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))
    print(num1 / num2)
#divide()
choice = input( "what you want to perform; +,-,x,/ : ")
if choice == '+':
    add()
elif choice == '-':
    subtract()
elif choice == 'x':
    multiply()
elif choice == '/':
    divide()
else:
    print("enter correct choice!!!")
