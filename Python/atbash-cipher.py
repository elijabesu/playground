import string

upper = list(string.ascii_uppercase)
reversed_upper = upper[::-1]

user = input("    String to encode:\n        ")

user = user.upper()
encrypted = list()
for letter in user:
    if letter in upper:
        index = upper.index(letter)
        encrypted.append(reversed_upper[index])
    else:
        encrypted.append(letter)

encrypted = "".join(encrypted)
print("   ", encrypted)