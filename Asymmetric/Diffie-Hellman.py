# Diffie-Hellman Algorithm
# Public numbers: P, G
# P = prime, G = primitive root of P
# Private Key: Alice chooses a, Bob chooses b
# Generated public key: Alice: x = G^a % P and Bob: y = G^b % P
# Exchange public keys x, y
# Private symmetric key generated: Alice: y^a % P and Bob: x^b % P
import random


def is_primitive_root(prime, g):
    distinct_nums = set()
    for i in range(1, prime):
        if g**i % prime in distinct_nums:
            return False
        else:
            distinct_nums.add(g**i % prime)
    return True


def compute_public(g, private, p):
    return pow(g, private, p)


def compute_shared(public, private, p):
    return pow(public, private, p)


def diffie_hellman(g, p):

    # Keep keys private
    alice_private = random.randint(1,100)
    bob_private = random.randint(1,100)

    # Exchange keys publically
    alice_public = compute_public(g, alice_private, p)
    bob_public = compute_public(g, bob_private, p)

    # Calculate
    alice_shared_private = compute_shared(bob_public, alice_private, p)
    bob_shared_private = compute_shared(alice_public, bob_private, p)
    print(alice_shared_private)
    print(bob_shared_private)

diffie_hellman(10, 541)
print(is_primitive_root(541, 10))