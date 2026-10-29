print(" *** Lower-case Camel String ***")

text = input("Enter some words: ")

words = text.split()

result = ""

for i in range(len(words)):
    word = words[i].lower()

    if i == 0:
        result += word
    else:
        result += word.capitalize()

print("lowerCamelCase:", result)
print("===== End of program =====")