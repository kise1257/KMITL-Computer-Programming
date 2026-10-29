print(" *** Encoding (for) ***")

s = input("Enter a word and a number: ")
word, key = s.split()

key = int(key)

if key < 1 or key > 26:
    print("Number must be between 1-26")
else:
    result = ""

    for i in range(len(word)):
        n = ord(word[i])

        # Change lowercase to uppercase
        if n >= 97 and n <= 122:
            n = n - 32

        # Shift backward
        n = n - key

        # Wrap around
        if n < 65:
            n = n + 26

        result = result + chr(n)

    print(result)

print("===== End of program =====")