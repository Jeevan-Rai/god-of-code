"""Day 01 machine check — byte order and CPython integer sizing.

Run:  python3 benchmarks/day01_endianness.py
"""
import struct
import sys

V = 0x12345678

print("little-endian :", struct.pack("<I", V).hex(" "))   # host order on Apple silicon
print("big-endian    :", struct.pack(">I", V).hex(" "))   # network order
print("native        :", struct.pack("=I", V).hex(" "))
print("byteorder     :", sys.byteorder)
print()

for n in (0, 1, 2**30 - 1, 2**30, 2**300):
    label = f"2**{n.bit_length()-1}" if n > 1 else str(n)
    print(f"getsizeof({label:>8}) = {sys.getsizeof(n):>4} bytes   "
          f"bit_length={n.bit_length():>4}  digits={-(-n.bit_length()//30)}")
