Terms = int(input("How many terms:"))
print("Fibonacci sequence:")
a,b = 0,1
for i in range(Terms):
    print(a)
    a,b = b,a+b