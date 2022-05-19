usr = [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]

for x in range(0, (len(usr)-1)):
    for y in range(0, len(usr[0])):
        usr[x].reverse()
        if usr[x][y] == 1:
            usr[x][y] = 0
        elif usr[x][y] == 0:
            usr[x][y] = 1

print(usr)