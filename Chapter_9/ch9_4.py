cipher_key = {
    ('A', 'A'): 'b',
    ('A', 'D'): 't',
    ('A', 'F'): 'a',
    ('A', 'G'): 'l',
    ('A', 'X'): 'p',

    ('D', 'A'): 'd',
    ('D', 'D'): 'h',
    ('D', 'F'): 'o',
    ('D', 'G'): 'z',
    ('D', 'X'): 'k',

    ('F', 'A'): 'q',
    ('F', 'D'): 'f',
    ('F', 'F'): 'v',
    ('F', 'G'): 's',
    ('F', 'X'): 'n',

    ('G', 'A'): 'g',
    ('G', 'D'): 'i/j',
    ('G', 'F'): 'c',
    ('G', 'G'): 'u',
    ('G', 'X'): 'x',

    ('X', 'A'): 'm',
    ('X', 'D'): 'r',
    ('X', 'F'): 'e',
    ('X', 'G'): 'w',
    ('X', 'X'): 'y',
}

string = input("Input ADFGX cipher text: ")
newtext = ""
failed = False

if len(string) % 2 != 0:
    failed = True
else:
    for i in range(0, len(string), 2):
        key = (string[i], string[i + 1])

        if key in cipher_key:
            newtext = newtext + cipher_key[key]
        else:
            failed = True
            break

if failed:
    print("FAILED TO DECRYPT")
else:
    print(newtext)
        
    
