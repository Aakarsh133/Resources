#!/bin/python3

flag = b"TUaP^IOMQTe\r\\\x11eV\x13\x0e\\\re\x13\x0fe`\x10RYG"

for i in range(len(flag)):
   print(chr((flag[i]^0x3f)+5), end= "");
