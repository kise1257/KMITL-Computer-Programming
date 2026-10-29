text = input("Enter : ")

items = text.split()
total = {}

for word in items:
    dictionary = {}

    for ch in word:
        if ch in dictionary:
            dictionary[ch] = dictionary[ch] + 1
        else:
            dictionary[ch] = 1

        if ch in total:
            total[ch] = total[ch] + 1
        else:
            total[ch] = 1

    print(word, "=", dictionary)

if len(items) > 1:
    print(text, "=", total)

max_char = ""
max_count = 0

for key in total:
    if total[key] > max_count:
        max_char = key
        max_count = total[key]

print("Maximum Character Count:", max_char, max_count)
print("===== End of program =====")
