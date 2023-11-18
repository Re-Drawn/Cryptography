# RSA (Rivest-Shamir-Adleman) Algorithm

import math
import random

def is_prime(num):
    # O(sqrt(n)) algorithm
    for i in range(2, int(math.sqrt(num)) + 1):
        if (num % i) == 0:
            return False
    return True


def encrypt(plain, e, n):
    output = []
    for num in plain:
        # num^e % n
        output.append(pow(num, e, n))
    return output


def decrypt(cipher, d, n):
    return pow(cipher, d, n)


def generate_keys(p, q):
    n = p*q
    phi_n = (p-1)*(q-1)

    for i in range(2, phi_n):
        if math.gcd(i, n) == 1 and math.gcd(i, phi_n) == 1:
            e = i
    
    for i in range(n):
        if (5*i) % phi_n == 1:
            d = i
            break
    
    d += phi_n * random.randint(1, 100)
    return e, d, n


def rsa(p, q):
    # Given 2 primes, p and q
    # Generate public key pair (e, n) and private key (d, n)
    generate_keys(p, q)
    print("A")

e, d, n = generate_keys(2, 7)
cipher = encrypt([43,59,42,52,20,37,34,30,30], 3, 667)
print(cipher)

