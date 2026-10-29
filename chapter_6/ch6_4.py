print(" *** The number of distinct remainders ***")

data = input("Enter a divisor / a sequence : ").split("/")

divisor = int(data[0])
numbers = [int(x) for x in data[1].split()]

remainders = []

for number in numbers:
    remainder = number % divisor

    if remainder not in remainders:
        remainders += [remainder]

print("Distinct remainders =", len(remainders))

print("===== End of program =====")