print(" *** Maximum value ***")

numbers = input("Enter some numbers : ").split()

maximum = None

for word in numbers:
    if word == "stop":
        break
    if word == "-1":
        break
    try:
        number = float(word)
        if maximum is None or number > maximum:
            maximum = number
    except:
        continue

if maximum is not None:
    if maximum == int(maximum):
        maximum = int(maximum)

print("Max value =", maximum)
print("===== End of program =====")