# Key Stream must be same length as plaintext
def generate_keystream(text, key):
    key = ''.join(filter(str.isalpha, key))
    return key * (len(text) // len(key)) + key[0:len(text) % len(key)]


def encrypt(plaintext, key):
    keystream = generate_keystream(plaintext, key)
    ciphertext = ""

    # Fallback for keystream when it moves on non alpha char
    fallback = 0

    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            encoded = (ord(plaintext[i].upper()) + ord(keystream[i-fallback].upper())) % 26 + ord('A')
            if plaintext[i].islower():
                ciphertext += chr(encoded).lower()
            else:
                ciphertext += chr(encoded)
        else:
            fallback += 1
            ciphertext += plaintext[i]
    return ciphertext

        

def decrypt(ciphertext, key):
    plaintext = ""
    keystream = generate_keystream(ciphertext, key)
    
    fallback = 0

    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            decoded = (ord(ciphertext[i].upper()) - ord(keystream[i-fallback].upper())) % 26 + 65
            if ciphertext[i].islower():
                plaintext += chr(decoded).lower()
            else:
                plaintext += chr(decoded)
        else:
            fallback += 1
            plaintext += ciphertext[i]
    return plaintext

print(encrypt("Hello World! How are you today?", "abc"))
print(decrypt("Hfnlp Yosnd! Iqw bte zqu uqdba?", "abc"))