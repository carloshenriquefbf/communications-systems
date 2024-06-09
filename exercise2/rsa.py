alph = {
    'A': 10,
    'B': 11,
    'C': 12,
    'D': 13,
    'E': 14,
    'F': 15,
    'G': 16,
    'H': 17,
    'I': 18,
    'J': 19,
    'K': 20,
    'L': 21,
    'M': 22,
    'N': 23,
    'O': 24,
    'P': 25,
    'Q': 26,
    'R': 27,
    'S': 28,
    'T': 29,
    'U': 30,
    'V': 31,
    'W': 32,
    'X': 33,
    'Y': 34,
    'Z': 35,
    ' ': 99
}

def modulo(a, b):
    return a % b

p = 17
q = 19
n = p * q
e = 5
d = 173

string = "carlos brito"
encrypted = []
decrypted = []

print("Encrypting the string: ", string)
for letter in string:
    if letter.upper() in alph:
        encrypted.append(modulo(alph[letter.upper()]**e, n))

print(encrypted)

print("Decrypting the string: ", string)
for letter in encrypted:
    for key, value in alph.items():
        if modulo(letter**d, n) == value:
            string = str(key) + " => " + str(value)
            decrypted.append(string)

print(decrypted)