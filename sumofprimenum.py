print("prime numbers betweem 1 to 10 are:")
for number in range(2,11):
    for i in range (2,number):
        if number % i == 0:
            break
        else:
            print(number)
