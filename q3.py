


num1 = 10
num2 = 20

print("Value of num1 before swapping: ", num1)
print("Value of num2 before swapping: ", num2)

# swapping two numbers using temporary variable
temp = num1
num1 = num2
num2 = temp

print("Value of num1 after swapping: ", num1)
print("Value of num2 after swapping: ", num2)


# Python code to swap two numbers
# without using another variable


x = 10
y = 20

print ("Before swapping: ")
print("Value of x : ", x, " and y : ", y)

# code to swap 'x' and 'y'
x, y = y, x

print ("After swapping: ")
print("Value of x : ", x, " and y : ", y)
