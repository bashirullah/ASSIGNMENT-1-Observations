x = 123
x=str(x)
for i in x:
    print(i)

i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
    else:
        print("error")

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

'''

output of the program
1
2
3
0
error
1
error
2
0
1
2
3
4
'''