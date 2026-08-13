print(" *** Pyramid-V ***")
h = int(input("Enter height : "))

i = 1
while i <= h:
    s = 1
    while s <= h - i:
        print(" ", end="")
        s += 1

    print("/", end="")

    if i == h:
        u = 1
        while u <= (2 * h - 2):
            print("_", end="")
            u += 1
    else:
        d = 1
        while d <= (2 * i - 2):
            print(".", end="")
            d += 1

    print("\\")
    i += 1

print("===== End of program =====")