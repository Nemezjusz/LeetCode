x = int(input("Podaj numer: "))
y = 0

while x != 0:
    if x % 2 == 0:
        x = x / 2
        y += 1
    if x % 2 != 0:
        x = x - 1
        y += 1

print(y)