print(" *** Sum odd / Subtract even ***")

numbers = input("Enter numbers : ").split()

total = 0

for x in numbers:
    x = int(x)

    if x == -1:
        break
    elif x % 2 == 1:
        total += x
    else:
        total -= x

print("Sum is", f"{total:,}")
print("===== End of program =====")