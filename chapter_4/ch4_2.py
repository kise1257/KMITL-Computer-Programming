print(" *** Arithmetic Sequence ***")
a, b = input("Enter 2 numbers : ").split()
a = int(a)
b = int(b)

count = 0
while count < 10:
    print(a, end=" ")
    a += b
    count += 1

print()
print("===== End of program =====")