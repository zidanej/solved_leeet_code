def plusone(x):
    s = " " #creating empty string to add the entered list
    for i in x:
        s = s+str(i) #additing list in string form
    n = int(s)+1 #converting string to int for adding 1
    s = str(n) # converting int to string to add in list
    fr = [] # storing the final result
    for i in s:
        fr.append(int(i)) #adding the result
    return (fr)

#TAKING INPUT
l = []
num = int(input("Enter the number of elements: "))
for i in range(0, num):
    ele = int(input())
    l.append(ele)
print(plusone(l))
