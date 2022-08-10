num1=int(input("famis Enter a Number1: "))
print(num1)

num2=int(input("famis Enter another Number2: "))
print(num2)

print("these are the operators you can use: ")
print("1. Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Modulus")
sum=input("please choose an option from these(1,2,3,4,5): ")
if sum=="1":
    print("1.Addition")
    print("the sum of two numbers:",num1 + num2)
if sum=="2":
    print("2.substraction")
    print("the sum of two numbers:", num1 - num2)
if sum=="3":
    print("3.Multiplication")
    print("the sum of two numbers:", num1 * num2)
if sum=="4":
    print("4.Division")
    print("the sum of two numbers:", num1 / num2)
if sum=="5":
    print("5.Modulus")
    print("the sum of two numbers:", num1 % num2)


