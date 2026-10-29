shopping_dict = {
    "egg": 1,
    "ham": 1,
    "water": 1,
    "soda": 1,
}

print("*** Shopping List 2 ***")
items = input("Enter some pairs of (operation, item): ").split(",")


for i in range(len(items)):
    a, b = items[i].strip().split()
    key = b.lower()
    if a != "a" and a != "r":
        print("Operation not supported!")
        break
    elif a == "a":
        if key in shopping_dict:
            shopping_dict[key] = shopping_dict[key] + 1
        else:
            shopping_dict[key] = 1
        
    elif a == "r":
        if key in shopping_dict:
            if shopping_dict[key] == 1:
                shopping_dict.pop(key)
            else:
                shopping_dict[key] = shopping_dict[key] - 1

else:
    print(f"Final shopping dict is {shopping_dict}")
        

