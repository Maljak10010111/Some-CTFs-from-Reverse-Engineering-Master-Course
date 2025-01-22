#!/usr/bin/env python3
from pwn import *

e = ELF('./toppler64')

TARGET_ADDR1 = 0x414005
TARGET_ADDR2 = 0x4063fe

if e.read(TARGET_ADDR1, 3) != b'\x83\xe8\x01' and e.read(TARGET_ADDR2,3) != b'\x8dP\xff':
    print("Wrong binary or already patched!")
else:
    e.asm(TARGET_ADDR1, "sub eax, 0x0")
    e.asm(TARGET_ADDR2, "lea    edx, [rax + 0x1]")
    e.save('./final_patch64_2nd_version')
    print("Successfully done")
