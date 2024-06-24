def pal(x):
    res = False
    a = str(x)

    if a == a[::-1]:
        res = True
    return res
print(pal(121))