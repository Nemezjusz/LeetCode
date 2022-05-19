def roman_to_int(usr):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    list_a = [x for x in usr]
    list_b = []

    for a in list_a:
        list_b.append(roman[a])

    list_c = []
    x = 0

    while x < len(list_b):
        if x+1 > len(list_b)-1:
            list_c.append(list_b[x])
        else:
            if list_b[x] < list_b[x+1]:
                o = list_b[x+1] - list_b[x]
                list_c.append(o)
                x += 1
            else:
                list_c.append(list_b[x])
        x += 1

    list_c = [int(x) for x in list_c]
    output = 0
    for x in list_c:
        output += x

    return output


print(roman_to_int("XLII"))