print(" *** Odd integer summation from 1 to n ***")
x = input("Enter an integer(n) : ")

try:
    n = int(x)

    if n <= 0:
        print("Summation => 0 = 0")
    else:
        i = 1
        s = 0
        text = ""

        while i <= n:
            s += i
            if text == "":
                text = str(i)
            else:
                text += "+" + str(i)
            i += 2

        print("Summation =>", text, "=", s)

except:
    print(x, "==> Invalid input !!!")

print("===== End of program =====")