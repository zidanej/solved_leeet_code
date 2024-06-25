def h_n(x):
    x1 = x
    sum = 0
    while(x1!=0):
        ext = x1%10
        sum = sum+ext
        x1 = x1//10
    if (x%sum==0):
     return sum
    return -1

print(h_n(14))


