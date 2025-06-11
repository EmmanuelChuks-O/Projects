# Encryption Program
import random
import string

characters = " " + string.ascii_letters + string.punctuation + string.digits
characters = list(characters)
key = characters.copy()

random.shuffle(key)

# print(f"characters: {characters}")
# print(f"key       : {key}")

# Encryption
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = characters.index(letter)
    cipher_text += key[index]

print(f"original message: {plain_text}")
print(f"encrypted message: {cipher_text}")

# Decryption
cipher_text = input("Enter a message to encrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += characters[index]


print(f"encrypted message: {cipher_text}")
print(f"original message: {plain_text}")
