"""Day 01 — Bits, bytes & endianness.

Two problems. State complexity before writing the body.

Reference: https://portfolio.kronos-nexus.com/metal/days/day-01-bits-bytes-endianness.html
"""


def two_unpaired(nums: list[int]) -> list[int]:
    """Every element appears twice except two, which appear once.

    Constraints: O(n) time, O(1) extra space. No hash map, no sorting.

    Time:  ?
    Space: ?
    """
    raise NotImplementedError


def max_xor_pair(nums: list[int]) -> int:
    """Maximum nums[i] ^ nums[j] over all pairs.

    Target O(32n). The O(n^2) double loop is correct and too slow.

    Time:  ?
    Space: ?
    """
    raise NotImplementedError


def popcount_kernighan(n: int) -> int:
    """Count set bits in O(popcount(n)) rather than O(bit_length(n))."""
    raise NotImplementedError


if __name__ == "__main__":
    assert sorted(two_unpaired([1, 2, 1, 3, 2, 5])) == [3, 5]
    assert max_xor_pair([3, 10, 5, 25, 2, 8]) == 28
    assert popcount_kernighan(0b1001_0000) == 2
    print("day 01 ok")
