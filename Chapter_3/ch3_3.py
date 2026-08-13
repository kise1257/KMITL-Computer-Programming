print("============================================================")
print("                32-BIT NUMBER REPRESENTATION                ")
print("============================================================")

num = input("Enter a number : ")

try:
    int(num)
    print("------------------------------------------------------------")
    print("INPUT INFORMATION")
    print("------------------------------------------------------------")
    print("Data type             : Integer")
    print(f"Decimal value         : {num}")
    if int(num) > 2147483647 or int(num) < -2147483648:
        print("------------------------------------------------------------")
        print("ERROR")
        print("------------------------------------------------------------")
        print("The entered value is outside the range of a\n32-bit signed integer.")
        print("Minimum value         : -2147483648")
        print("Maximum value         : 2147483647")
    else:
        if int(num) > 0:
            print("Sign                  : Positive")
            print("Sign bit              : 0")
            print(f"Magnitude             : {num}")
        elif int(num) < 0:
            print("Sign                  : Negative")
            print("Sign bit              : 1")
            x = int(num)*-1
            print(f"Magnitude             : {x}")
        elif int(num) == 0:
            print("Sign                  : Zero")
            print("Sign bit              : 0")
            print(f"Magnitude             : {num}")
        print("------------------------------------------------------------")
        print("               32-BIT BINARY REPRESENTATIONS                ")
        print("------------------------------------------------------------")
        print("Format: sign_bit_7bits_8bits_8bits_8bits")
        print()
        if int(num) == 0:
            print("Sign-magnitude        : 0_0000000_00000000_00000000_00000000")
            print("One's complement      : 0_0000000_00000000_00000000_00000000")
            print("Two's complement      : 0_0000000_00000000_00000000_00000000")
        else:
            if int(num) < 0:
                mag = int(num) * -1
            else:
                mag = int(num)
            signmag = mag
            sign = 0
            if int(num) < 0:
                sign = 1
            else:
                sign = 0
            group1 = (signmag // (2**24)) % 128
            group2 = (signmag // (2**16)) % 256
            group3 = (signmag // (2**8)) % 256
            group4 = signmag % 256
            print(f"Sign-magnitude        : {sign}_{group1:07b}_{group2:08b}_{group3:08b}_{group4:08b}")
            if int(num) >= 0:
                ones = mag
            else:
                ones = (~mag) & 0xFFFFFFFF
            sign = ones // (2**31)
            group1 = (ones // (2**24)) % 128
            group2 = (ones // (2**16)) % 256
            group3 = (ones // (2**8)) % 256
            group4 = ones % 256
            print(f"One's complement      : {sign}_{group1:07b}_{group2:08b}_{group3:08b}_{group4:08b}")
            if int(num) >= 0:
                twos = mag
            else:
                twos = (ones + 1) & 0xFFFFFFFF
            sign = twos // (2**31)
            group1 = (twos // (2**24)) % 128
            group2 = (twos // (2**16)) % 256
            group3 = (twos // (2**8)) % 256
            group4 = twos % 256
            print(f"Two's complement      : {sign}_{group1:07b}_{group2:08b}_{group3:08b}_{group4:08b}")
except ValueError:
    try:
        float(num)
        print("------------------------------------------------------------")
        print("INPUT INFORMATION")
        print("------------------------------------------------------------")
        print("Data type             : Floating-point number")
        print(f"Value                 : {num}")
        print()
        print("Integer representations are not applicable to this value.")
    except ValueError:
        print("------------------------------------------------------------")
        print("INVALID INPUT")
        print("------------------------------------------------------------")
        print(f'"{num}" is not a valid number.')
print("============================================================")
print("                       END OF PROGRAM                       ")
print("============================================================")
