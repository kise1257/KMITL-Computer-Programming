print(" *** Filter only even number ***")

list = input("Enter some numbers: ").split()
print(list)

for number in list:
    number = int(number)

    if number % 2 == 0:
        print(number, end=" ")