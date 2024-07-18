from py_ecc.bn128.bn128_curve import neg, multiply, G1, G2
from py_ecc.bn128.bn128_pairing import pairing

# 0 = e(−A₁, B₂) + e(α₁, β₂) + e(L₁, γ₂) + e(C₁, δ₂)
# without greek chars
# 0 = e(-A1, B2) + e(D1, E2) + e(L1, Y2) + e(C1, F2)
# this simply says that -A1 * B2 is equivalent to whatever is on the right of it

# some numbers to create a balanced equation

"""
A = 3
B = 5
D = 2
E = 3
L = 5
Y = 1
C = 4
F = 1
"""

# 0 = -3 * 5 + 2 * 3 + 5 * 1 + 4 * 1
# or
# 15 = 6 + 5 + 4
#
# in our exercise, we have the equation
# 0 = -A1 * B2 + D1 * E2 + L1 * Y2 + C1 * F2
# where L1 = (x1 * G1 + x2 * G1 + x3 * G1)
#
# in EC arithmetic, x1 * x2 * G1 is the same as
# x1 * G1 + x2 * G1
# in bilinear pairings,
# f(aG,bG) = f(abG,G) = f(G,abG)

A1 = multiply(G1, 3)
B2 = multiply(G2, 5)
D1 = multiply(G1, 2)
E2 = multiply(G2, 3)
Y2 = multiply(G2, 1)
C1 = multiply(G1, 4)
F2 = multiply(G2, 1)

print("A1", A1)
print("B2", B2)
print("D1", D1)
print("E2", E2)
print("Y2", Y2)
print("C1", C1)
print("F2", F2)


def verify(x1, x2, x3, A1, B2, C1):
    AB = pairing(B2, neg(A1))
    DE = pairing(E2, D1)

    L1 = multiply(G1, x1 + x2 + x3)
    print("L1", L1)
    LY = pairing(Y2, L1)

    CF = pairing(F2, C1)

    result = AB + DE + LY + CF
    print(f"verification result: {result}")


if __name__ == "__main__":
    verify(1, 2, 3, A1, B2, C1)
