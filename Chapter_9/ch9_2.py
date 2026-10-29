print(" *** Creating Dictionary ***")
text = input("Enter text : ")

items = text.split()
dictionary = {}


for i in range(0, len(items) ,2):
        key = items[i]
        value = int(items[i + 1])

        if key in dictionary:
            dictionary[key] = dictionary[key] + value
        else:
            dictionary[key] = value

print(dictionary)
print("===== End of program =====")
