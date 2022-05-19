x = input("Adres IP: ")

list_x = [y for y in x]

while True:
    try:
        if list_x.index("."):
            list_x[list_x.index(".")] = "[.]"
    except ValueError:
        break

print("".join(list_x))