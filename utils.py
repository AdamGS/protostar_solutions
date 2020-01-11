from subprocess import Popen, PIPE

def run_file_with_stdin(bin_path, arg):
    p = Popen(bin_path, stdin=PIPE)
    return p.communicate(arg)

def run_file_with_args(bin_path, arg):
    p = Popen([bin_path, arg])