import galois

GF = galois.GF(17)

three_quarters = GF(3) / GF(4)
one_half = GF(1) / GF(2)
three_eighths = GF(3) / GF(8)

# Exercise 2
GF = galois.GF(11)

assert GF(0) * GF(0) == GF(0)
assert GF(1) == GF(1) * GF(1) and GF(1) == GF(10) * GF(10)
assert GF(3) == GF(5) * GF(5) and GF(3) == GF(6) * GF(6)
assert GF(4) == GF(2) * GF(2) and GF(4) == GF(9) * GF(9)
assert GF(5) == GF(4) * GF(4) and GF(5) == GF(7) * GF(7)
assert GF(9) == GF(3) * GF(3) and GF(9) == GF(8) * GF(8)

if __name__ == "__main__":
    assert three_quarters * one_half == three_eighths
