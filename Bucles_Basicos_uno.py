for i  in range(151):
    print(i)
print("-----")

for i in range(5, 1000, 5):
    print(i)
print("-----")

for i in range(1, 100):
    if i % 10 == 0:
        print("Coding Cojo")
    if i % 5 == 0:
        print("coding")
    print(i)
    
print("-----")

suma_numeros = 0
for i in range(0, 500000):
    if i % 2 != 0:
        suma_numeros += i
print("La suma de los numeros impares es", suma_numeros)

print("-----")

for i in range(2018, 0 ,- 4):
    print (i)

print("-----")

low_num = 2
high_num = 60
mult = 4
for i in range(low_num, high_num, + 1):
    if i % mult == 0:
        print(i)
