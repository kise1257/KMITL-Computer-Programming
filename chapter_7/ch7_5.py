
print(" *** Mountains from strings ***")

text = input("Enter strings : ")
words = text.split()

height = 0
for word in words:
    if len(word) > height:
        height = len(word)

for row in range(height, 0, -1):
    print(f"{row:02d} |", end=" ")

    for word in words:
        length = len(word)

        if row > length:
            print("-" * (2 * length - 1), end=" | ")
        else:
            position = length - row
            dashes = row - 1
            dots = 2 * position - 1

            print("-" * dashes, end="")
            print(word[position], end="")

            if row < length:
                print("." * dots, end="")
                print(word[position], end="")

            print("-" * dashes, end=" | ")

    print()

print("===== End of Program =====")
