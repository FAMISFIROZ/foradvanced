print("**********8")
print("enter the number1:")
num=int(input())
print("enter the number2:")
num=int(input())
print("these are the operators you can use: ")
print("1. Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Modulus")
result=0
operator=input("please choose an option from these(1,2,3,4,5):")
def add(num1,num2):
    return num1+num2
if operator==1:
   result=add(num1,num2)
   print(result)
def sub(num1,num2):
    return num1-num2
if operator==1:
   result=sub(num1,num2)
   print(result)
if operator == "3":
    if num1==0 or num2==0:
        print("cannot multiply by zero")
    else:
        result=num1*num2
        print("The result of multiplication of ",num1,"and",num2,"is",result)
if operator == "4":
    if num2==0:
        print("cannot divide by zero")
    else:
          result=num1//num2
          print("The result of division of",num1,"and",num2,"is",result)
if operator=="5":
    if num2==0:
        print("cannot modulus by zero")
    else:
         result=num1%num2
    print("The result of modulus of",num1,"and",num2,"is",result)




