print(" *** Integer Property ***")
num = int(input("Enter a whole number : "))

if num > 0:
    numtype = "positive integer"
elif num == 0:
    numtype = "zero integer"
else:
    numtype = "negative integer"

if num < 0:
    magnitude = num * (-1)
else:
    magnitude = num

if num % 2 == 0:
    parity = "Even"
else:
    parity = "Odd"

print(f"        type => {numtype}")
print(f"   Magnitude => {magnitude}")
print(f"      Parity => {parity}")
print("===== End of program =====")