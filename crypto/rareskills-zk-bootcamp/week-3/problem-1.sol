// SPDX-License-Identifier: MIT
pragma solidity 0.8.25;

contract Problem1 {
    uint256 public constant N =
        21888242871839275222246405745257275088548364400416034343698204186575808495617;
    uint256 public constant Gx = 1;
    uint256 public constant Gy = 2;

    struct ECPoint {
        uint256 x;
        uint256 y;
    }

    function rationalAdd(
        ECPoint calldata A,
        ECPoint calldata B,
        uint256 num,
        uint256 den
    ) public view returns (bool verified) {
        // return true if the prover knows two numbers that add up to num/den
        // ECPoint memory G = ECPoint(Gx, Gy);
        // (bool ok, bytes memory C) = address(6).staticcall(
        //     abi.encode(A.x, A.y, B.x, B.y)
        // );
        // require(ok, "ecAdd failed");
        // (uint256 Cx, uint256 Cy) = abi.decode(C, (uint256, uint256));

        ECPoint memory C = ecAdd(A, B);

        uint256 denInv = modExp(den, N - 2, N);
        ECPoint memory result = ecMul(mulmod(num, denInv, N), ECPoint(Gx, Gy));
        return C.x == result.x && C.y == result.y;
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

    function modExp(
        uint256 base,
        uint256 exponent,
        uint256 modulus
    ) public view returns (uint256) {
        (bool ok, bytes memory result) = address(5).staticcall(
            abi.encodePacked(
                abi.encodePacked(base).length,
                abi.encodePacked(exponent).length,
                abi.encodePacked(modulus).length,
                base,
                exponent,
                modulus
            )
        );
        require(ok, "modExp failed");
        return abi.decode(result, (uint256));
    }
}
