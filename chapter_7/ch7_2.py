print(" *** Reverse Vowels ***")

text = input("Enter a string : ")

vowels = "aeiouAEIOU"
vowel = ""

for i in range(len(text)):
    if text[i] in vowels:
        vowel += text[i]

result = ""
position = len(vowel) - 1

for i in range(len(text)):
    if text[i] in vowels:
        result += vowel[position]
        position -= 1
    else:
        result += text[i]

print("Result :", result)
print("===== End of Program =====")