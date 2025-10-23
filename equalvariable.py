def equal(a,b,c):
    if a == b == c:
        return 3
    elif a == b or b == c or a == c :
        return 2
    else:
        return 0
print(equal(2,2,4))
print(equal(1,1,1))    
print(equal(1,2,3))