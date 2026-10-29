print(" *** String Diamond ***")

text = input("Enter string : ")

length = len(text)
middle = length // 2

if length % 2 == 0:
    for i in range(1, length):
        if i <= middle:
            part = text[middle - i : middle + i]
            space = " " * (middle - i)
        else:
            part = text[i - middle : length - (i - middle)]
            space = " " * (i - middle)
        print(space + part)
else:
    for i in range(length):
        if i <= middle:
            part = text[middle - i : middle + i + 1]
            space = " " * (middle - i)
        else:
            part = text[i - middle : length - (i - middle)]
            space = " " * (i - middle)
        print(space + part)

print("===== End of program =====")