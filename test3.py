def max_of_three(a,b,c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
num1 = int(input("Enter a Number1:"))
num2 = int(input("Enter a Number2:"))
num3 = int(input("Enter a Number3:"))
sum=max_of_three(num1,num2,num3)
print(sum)