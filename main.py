# ASSIGNMENT 3
# Dandibayeva Dinara - SE-2108

#--------------------------------------------------------------------
# PART 1

import random

def extended_precision_integer(input_str):
    ep_integer = int(input_str)
    print(ep_integer)

def XPadd(a, b):
    sum_result = a + b
    return sum_result

def random_num_gen(n):
    random_digits = [str(random.randint(0, 9)) for _ in range(n)]
    random_integer = int(''.join(random_digits))
    return random_integer

def parity_f(a):
    return a % 2 == 1

def comparison_f(a, b):
    if (a > b):
        return 1
    elif (a < b):
        return -1
    else:
        return 0

def subtraction_f(a, b):
    if (a > b or a == b):
        return (a-b)
    else:
        print ("error in subtraction_f")

def multiplication_f (a, b):
    return a*b
    
def division_f(a, b):
    if (b != 0):
        q = a / b
        r = a % b
        print("q: ", q," r: ", r)
    else:
        print ("error in division_f")
    
    
#--------------------------------------------------------------------
# PART 2

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# greatest common divider funtion
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# modular inverse of 'a' modulo 'm'
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def generate_keys(p, q):
    
    if not (is_prime(p) and is_prime(q)):
        return "Numbers are not prime, choose other"

    # to find n = p x q
    n = p * q

    # calculate φ(n)
    phi_n = (p - 1) * (q - 1)

    # choose e such that 1 < e < φ(n) and gcd(e, φ(n)) = 1
    e = 2
    while gcd(e, phi_n) != 1:
        e += 1

    # public Key
    public_key = (e, n)

    # calculate private key's d
    d = mod_inverse(e, phi_n)

    # private Key
    private_key = (d, n)

    return public_key, private_key

def encrypt(plaintext, public_key):
    e, n = public_key
    ciphertext = pow(plaintext, e, n)
    return ciphertext

def decrypt(ciphertext, private_key):
    d, n = private_key
    plaintext = pow(ciphertext, d, n)
    return plaintext


# get p and q from user
p = int(input("Enter p number: "))
q = int(input("Enter q number: "))
n = p * q

# show keys
public_key, private_key = generate_keys(p, q)
print(f"Public Key: {public_key}")
print(f"Private Key: {private_key}")


plaintext_message = int(input("Enter the plaintext message: "))
if ((plaintext_message <= (n-1)) and (plaintext_message > 0)):
    # encypt the message
    ciphertext_message = encrypt(plaintext_message, public_key)
    print(f"Ciphertext: {ciphertext_message}")
    
    # decrypt the message
    decrypted_message = decrypt(ciphertext_message, private_key)
    print(f"Decrypted Message: {decrypted_message}")
else:
    print("Error. Plaintext message is greater than n")

