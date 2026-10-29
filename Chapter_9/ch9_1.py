print(" *** Creating Dictionary ***")
text = input("Enter text : ")

items = text.split()
dictionary = {}

for i in range(0, len(items), 2):
    key = items[i]
    value = items[i + 1]
    dictionary[key] = value

print(dictionary)
print("===== End of program =====")
