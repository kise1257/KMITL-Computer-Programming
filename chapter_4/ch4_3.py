print("*********** Fibo / Caesar **************\n*           a0 a1 n for Fibo           *\n*          word  n for Caesar          *\n****************************************")
s = input("Enter something : ")
x = s.split()

if len(x) == 3:
    a0 = int(x[0])
    a1 = int(x[1])
    n = int(x[2])

    print(a0, end="")
    print(", ", end="")
    print(a1, end="")

    c = 2
    while c < n:
        t = a0 + a1
        print(", ", end="")
        print(t, end="")
        a0 = a1
        a1 = t
        c += 1

else:
    word = x[0]
    shift = int(x[1])

    print(word, end=" => ")

    i = 0
    while i < len(word):
        print(chr(ord(word[i]) + shift), end="")
        i += 1

print()
print("===== End of program =====")