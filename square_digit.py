def square_digits(number):
    return int(''.join(str(int(d)**2) for d in str(number)))
print(square_digits(9765))
print(square_digits(234))
print(square_digits(56789))