print(" *** Number Fun ***")
x = input("Enter a 3-digit number : ")
num = int(x)
digit3 = num % 10
digit2 = (num // 10) % 10
digit1 = num // 100
flipped = (digit3 * 100) + (digit2 * 10) + digit1
last_8 = num & 255
high_4 = last_8 // 16
low_4 = last_8 % 16
split_binary = f"{high_4:04b} {low_4:04b}"
print(f"""
You have entered     => {num}
Square               => {num * num:,}
25% 3 decimal places => {num * 0.25:.3f}%
Flipping             => {flipped}
Hexadecimal          => {num:x} or {num:X}
Binary               => {num:b}
Binary right 8-digit => {split_binary}
""")