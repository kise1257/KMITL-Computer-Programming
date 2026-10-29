print("*** Maximum Occurrence ***")

numbers = [int(x) for x in input("Enter some numbers: ").split()]

max_count = 0
max_number = numbers[0]

for number in numbers:
    count = numbers.count(number)

    if count > max_count:
        max_count = count
        max_number = number

print(max_number)

print("===== End of program =====")