import numpy as np

"""
Problem: Create a graph with 3 nodes and 3 edges and write constraints for a 3-coloring. Conver the 3-coloring to a rank 1 constraint system.

-- three-coloring constraint map
color A = 1
color B = 2
color C = 3

-- three nodes: x, y, z
(x-1) * (x-2) * (x-3) = 0
(y-1) * (y-2) * (y-3) = 0
(z-1) * (z-2) * (z-3) = 0

expand this out:
x^3 - 6x^2 + 11x - 6
y^3 - 6y^2 + 11y - 6
z^3 - 6z^2 + 11z - 6

example: x^3 - 6x^2 + 11x - 6

let a = x * x

then

a * x - 6a + 11x - 6

duplicating this work for the remaining two nodes:

let b = y * y
let c = z * z

-- a recap of the constraints we have now:

x * x = a
y * y = b
z * z = c
a * x = 6a - 11x + 6
b * y = 6b - 11y + 6
c * z = 6c - 11z + 6

-- three edges: xy, xz, yz
(xy - 2) * (xy - 3) * (xy - 6) = 0
(xz - 2) * (xz - 3) * (xz - 6) = 0
(yz - 2) * (yz - 3) * (yz - 6) = 0

example: (xy - 2) * (xy - 3) * (xy - 6) = 0

let xy = d

then

(d - 2) * (d - 3) * (d - 6) = 0
=> d^3 -11d^2 + 36d - 36 = 0

let d * d = e

then

ed = 11e - 36d + 36

duplicating this work for the remaining two edges:

let f = xz
let h = yz
let g = f * f
let i = h * h

then

gf = 11g - 36f + 36
ih = 11i - 36h + 36

-- all our constraints
=nodes=
x * x = a
y * y = b
z * z = c
a * x = 6a - 11x + 6
b * y = 6b - 11y + 6
c * z = 6c - 11z + 6

=edges=
xy = d
xz = f
yz = h
d * d = e
f * f = g
h * h = i
ed = 11e - 36d + 36
gf = 11g - 36f + 36
ih = 11i - 36h + 36

witness = [1, x, y, z, a, b, c, d, f, h, e, g, i]
"""


def validateR1CSForThreeColoring(x, y, z):
    a = x * x
    b = y * y
    c = z * z
    d = x * y
    f = x * z
    h = y * z
    e = d * d
    g = f * f
    i = h * h

    witness = np.array([1, x, y, z, a, b, c, d, f, h, e, g, i])
    L = np.array(
        [
            # [1, x, y, z, a, b, c, d, f, h, e, g, i]
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        ]
    )
    R = np.array(
        [
            # [1, x, y, z, a, b, c, d, f, h, e, g, i]
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        ]
    )

    O = np.array(
        [
            # [1, x, y, z, a, b, c, d, f, h, e, g, i]
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
            [6, -11, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0],
            [6, 0, -11, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0],
            [6, 0, 0, -11, 0, 0, 6, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [36, 0, 0, 0, 0, 0, 0, -36, 0, 0, 11, 0, 0],
            [36, 0, 0, 0, 0, 0, 0, 0, -36, 0, 0, 11, 0],
            [36, 0, 0, 0, 0, 0, 0, 0, 0, -36, 0, 0, 11],
        ]
    )

    A = np.dot(L, witness)
    B = np.dot(R, witness)
    C = np.dot(O, witness)

    return np.array_equal(A * B, C)


if __name__ == "__main__":
    result = validateR1CSForThreeColoring(1, 2, 3)
    print(f"Expect true, got result {result}")
    result = validateR1CSForThreeColoring(2, 2, 3)
    print(f"Expect false, got result {result}")
    result = validateR1CSForThreeColoring(1, 3, 3)
    print(f"Expect false, got result {result}")
