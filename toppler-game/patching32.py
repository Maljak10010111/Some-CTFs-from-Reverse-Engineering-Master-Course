#!/usr/bin/env python3
from pwn import *

e = ELF('./toppler32')


TARGET_ADDR1 = 0x804c4f1
TARGET_ADDR2 = 0x8056417

if e.read(TARGET_ADDR1, 3) != b'\x83\xe8\x01' and e.read(TARGET_ADDR2, 7) != b'\x83-\x9c\x91\x06\x08\x01':
	print("Wrong binary or already patched!")
else:
	e.asm(TARGET_ADDR1, "sub eax, 0x0")
	e.asm(TARGET_ADDR2, "sub    DWORD PTR ds:0x806919c, 0x0")
	e.save('./final_patch32')
	print("Successfully done")
