def reverse_int(x):
    list_x = [y for y in x]
    list_y = list_x[::-1]

    if list_y == list_x:
        return True
    else:
        return False


x = input("Podaj liczbe: ")

if reverse_int(x):
    print("true")
else:
    print("false")


for x in range(0, len(list_x)):
    while z < m:
        if x+1 > len(list_x)-1:
            if list_y[0][-z] != list_y[-1][-z]:
                list_y[x].pop()
                z += 1
        else:
            if list_y[0][-z] != list_y[x+1][-z]:
                list_y[x].pop()
                z += 1
        z+=1