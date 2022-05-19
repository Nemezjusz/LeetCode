x = input("Podaj liczbe: ")


def reverse_int(x):
    if x[0] == "-":
        list_x = [y for y in x]
        list_y = list_x[::-1]

        list_y.remove("-")
        list_y.insert(0, "-")
        output = "".join(list_y)
    else:
        list_x = [y for y in x]
        list_y = list_x[::-1]
        output = "".join(list_y)

    output = int(output)
    return output


print(reverse_int(x))
