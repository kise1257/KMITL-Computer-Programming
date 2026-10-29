print(" *** Reverse Odd ***")

numbers = input("Enter integers : ").split()

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

print(numbers)

odd = list()

for i in range(len(numbers)):
    if numbers[i] % 2 != 0:
        odd = odd + [numbers[i]]

for i in range(len(numbers)):
    if numbers[i] % 2 != 0:
        numbers[i] = odd[len(odd) - 1]
        odd = odd[:len(odd) - 1]

print(numbers)
print("===== End of program =====")