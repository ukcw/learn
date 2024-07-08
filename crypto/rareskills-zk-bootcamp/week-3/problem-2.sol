// SPDX-License-Identifier: MIT
pragma solidity 0.8.25;

contract Problem2 {
    uint256 public constant N =
        21888242871839275222246405745257275088548364400416034343698204186575808495617;
    uint256 public constant Gx = 1;
    uint256 public constant Gy = 2;
    struct ECPoint {
        uint256 x;
        uint256 y;
    }

    function matmul(
        uint256[] calldata matrix,
        uint256 n, // n x n for the matrix
        ECPoint[] calldata s, // n elements
        uint256[] calldata o // n elements
    ) public view returns (bool verified) {
        // revert if dimensions don't make sense or the matrices are empty
        // return true if Ms == o elementwise. You need to do n equality checks. If you're lazy, you can hardcode n to 3, but it is suggested that you do this with a for loop

        require(matrix.length == n * n, "matrix is not of length n");
        require(s.length == n, "array of ECPoints not of length n");
        require(o.length == n, "array of outputs not of length n");

        ECPoint memory G = ECPoint(Gx, Gy);

        for (uint256 i = 0; i < n; i++) {
            ECPoint memory lh = ECPoint(0, 0);
            for (uint256 j = 0; j < n; j++) {
                lh = ecAdd(lh, ecMul(matrix[i * n + j], s[i]));
            }

            ECPoint memory rh = ecMul(o[i], G);

            if (lh.x != rh.x || lh.y != rh.y) {
                return false;
            }
        }
    }

    function ecAdd(
        ECPoint memory A,
        ECPoint memory B
    ) public view returns (ECPoint memory C) {
        (bool ok, bytes memory result) = address(6).staticcall(
            abi.encode(A.x, A.y, B.x, B.y)
        );
        require(ok, "ecAdd failed");
        (uint256 Cx, uint256 Cy) = abi.decode(result, (uint256, uint256));

        return ECPoint(Cx, Cy);
    }

    function ecMul(
        uint256 scalar,
        ECPoint memory A
    ) public view returns (ECPoint memory B) {
        (bool ok, bytes memory result) = address(7).staticcall(
            abi.encode(A.x, A.y, scalar)
        );
        require(ok, "ecMul failed");
        (uint256 Bx, uint256 By) = abi.decode(result, (uint256, uint256));
        return ECPoint(Bx, By);
    }
}
