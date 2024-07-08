import os
import hashlib
from ecpy.curves import Curve, Point

# secp256k1 curve parameters
# p = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFC2F
# a = 0
# b = 7
# G = (
#     0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798,
#     0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8,
# )
# n = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141

SECP256K1 = Curve.get_curve("secp256k1")
G = SECP256K1.generator
N = SECP256K1.order


def generate_keys():
    private_key = int.from_bytes(os.urandom(32), "big") % N
    public_key = private_key * G
    return private_key, public_key


def hash_message(message):
    """Hash the message using SHA-256."""
    message_hash = hashlib.sha256(str.encode(message)).digest()
    return int.from_bytes(message_hash, "big")


def sign_message(private_key, message):
    # 1. Calculate message hash
    hashed_message = hash_message(message)

    # 2. Generate random number k
    k = int.from_bytes(os.urandom(32), "big") % N

    # 3. Calculate random point R = k * G and take its x-coordinate: r = R.x
    R = k * G
    Rx = R.x

    # 4. Calculate signature proof s
    s = (pow(k, -1, N) * (hashed_message + Rx * private_key)) % N

    return (Rx, s)


def verify_signature(message, public_key, r, signature):
    hashed_message = hash_message(message)

    # 2. Calculate the modular inverse of the signature proof
    s_inv = pow(signature, -1, N)

    # 3. Recover the random point used during the signing
    r_prime = (hashed_message * s_inv) * G + (r * s_inv) * public_key
    rx = r_prime.x

    return r == rx


if __name__ == "__main__":
    private_key, public_key = generate_keys()
    print("private key", private_key)
    print("public key", public_key)
    message = "hello world!"
    print("hashed message", hash_message(message))
    r, s = sign_message(private_key, message)
    print("r", r)
    print("s", s)
    print("Testing correct signature...")
    print(verify_signature(message, public_key, r, s))
    print("Testing false signature...")
    r, s = sign_message(private_key - 10, message)
    print(verify_signature(message, public_key, r, s))
