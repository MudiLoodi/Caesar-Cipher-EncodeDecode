import string

alphabet = list(string.ascii_uppercase)

encrypt_decrypt = input("Encrypt/Decrypt? (E/D): ").upper()

method = ""
shift = ""
word = ""
if (encrypt_decrypt == "E"):
    word = input("Text to encrpyt: ").upper()
    shift = int(input("Number of positions?: "))

if (encrypt_decrypt == "D"):
    word = input("Text to decrypt: ").upper()
    method = input("Bruteforce? (Y/N): ").upper()
if (method != "Y" and encrypt_decrypt == "D"):
    shift = int(input("Number of positions?: "))

def getSpace(word):
    li = list(word)
    spaceIndex = [i for i, x in enumerate(li) if x == " "]
    return spaceIndex

def getReplacement(word, shift):
    replaceIndices=[]
    li = list(word)
    for i in li:
        if (i == " "):
            continue
        if (encrypt_decrypt == "E"):
            replaceIndices.append((alphabet.index(i) + shift) % 26)
        else:
            replaceIndices.append((alphabet.index(i) - shift) % 26)
    return replaceIndices

def sub(word, shift):
    result = []
    for i in getReplacement(word, shift):
        li = alphabet[i]
        result.append(li)
    for j in getSpace(word):
        result.insert(j, " ")
    result = "".join(result)
    if (encrypt_decrypt == "E"):
        return (f"Encrypted with a shift of {shift}: {result}")
    else:
        return (f"Decrypted with a shift of {shift}: {result}")

if (method == "y".upper()):
    for i in range(1, 27):
        print(sub(word, i))
else:
    print(sub(word, shift))
