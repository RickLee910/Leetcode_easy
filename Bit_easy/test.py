a = 2147483650
print(a if a < 0x80000000 else ~(a^0xFFFFFFFF))