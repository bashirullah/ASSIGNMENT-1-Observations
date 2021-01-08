num1=int(input("Enter num1:-"))
num2=int(input("Enter num2:-"))

Input=int(input("Enter your option:"))

if Input==1:
    num3=num1+num2
     
    print("Addation of two numbers is",num3)
    if num3 < 0:
        print(" And it is a Negative value")

if Input==2:
    num3=num1-num2
    print("subtraction of two number is",num3)
    if num3 < 0:
        print(" And it is a Negative value")
    
if Input==3:
    num3=num1/num2
    print("Division of two number is",num3)
    if num3 < 0:
        print(" And it is a Negative value")
    

if Input==4:
    num3=num1*num2
    print("Multiplication of two number is",num3)
    if num3 < 0:
        print(" And it is a Negative value")
    
if Input==5:
    print("Enter numbers to calculate average: ")
    num_first=int(input("Enter first number: "))
    num_second=int(input("Enter second number: "))
    

    avg=(num_first+num_second)/2
    print("average",avg)
    if avg < 0:
        print(" And it is a Negative value")
 