x = input("Podaj słowa oddzielone spacją: ")

list_x = x.split(" ")
n = ""
b = 144
for x in list_x:
    if len(x) <= b:
        b = len(x)
        n = x

print(n)
list_y = [list(x) for x in list_x]

for y in range(0, len(list_x)):
    while len(list_y[y]) > b:
        list_y[y].pop()

print(list_y)
output = []
x = 0
y = 1
for y in range(1, len(list_y)):
    for x in range(0, b):
        if list_y[0][x] == list_y[y][x]:
            output.append(list_y[y][x])
        elif list_y[0][x] != list_y[y][x]:
            break


for x in range(1, len(output)):
    if output.count(output[x]) > output.count(output[0]):
        output.remove(output[x])


print(output)
