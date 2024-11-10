print ('Введите первое число')
a = float(input())
print ('Введите второе число')
b = float(input())

sum = a + b
dif = a - b
com = a * b

print(str(a) + " + " + str(b) + " = " + str(sum))
print(str(a) + " - " + str(b) + " = " + str(dif))
print(str(a) + " * " + str(b) + " = " + str(com))
if b != 0:
    pri = a / b
    print(str(a) + " / " + str(b) + " = " + str(pri))

