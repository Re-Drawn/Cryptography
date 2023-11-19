def caesar_cipher(plaintext, shift):
    shift %= 26
    ciphertext = ""

    for char in plaintext:
        if char == " ":
            ciphertext += " "
            continue
        shifted = ord(char) + shift
        if char.isupper() and shifted > 90 or char.islower() and shifted > 122:
            shifted -= 26
        ciphertext += chr(shifted)

    return ciphertext

def brute_force(cipher):
    for i in range(25):
        caesar_cipher(cipher, i+1)
