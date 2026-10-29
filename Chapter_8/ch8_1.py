
print("*** Permutation ***")

def are_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    return sorted(str1) == sorted(str2)


inp = input("Enter two strings: ").split("/")

if are_permutation(inp[0], inp[1]):
    print("String1 and String2 are permutation")
else:
    print("String1 and String2 are not permutation")

print("===== End of program =====")