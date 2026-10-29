print("*** Clockwise Spiral Rectangle ***")

width, height = input("Enter width height : ").split()

width = int(width)
height = int(height)

table = [[0] * width for i in range(height)]

number = 1
top = 0
bottom = height - 1
left = 0
right = width - 1

max_steps = (width + height) // 2 + 1

for step in range(max_steps):
    if top <= bottom and left <= right:
        for j in range(left, right + 1):
            table[top][j] = number
            number += 1
        top += 1

    if top <= bottom and left <= right:
        for j in range(top, bottom + 1):
            table[j][right] = number
            number += 1
        right -= 1

    if top <= bottom and left <= right:
        for j in range(right, left - 1, -1):
            table[bottom][j] = number
            number += 1
        bottom -= 1

    if top <= bottom and left <= right:
        for j in range(bottom, top - 1, -1):
            table[j][left] = number
            number += 1
        left += 1

max_num = width * height
max_digits = len(str(max_num))

for i in range(height):
    for j in range(width):
        val = table[i][j]
        num_digits = len(str(val))
        padding = max_digits - num_digits

        for p in range(padding):
            print(" ", end="")

        if j == width - 1:
            print(val, end="")
        else:
            print(val, end=" ")
    print()

print("===== End of program ======")