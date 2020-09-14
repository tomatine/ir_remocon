#!/usr/bin/python3
# coding: UTF-8
import os
import sys

def send(code):
    os.system('/usr/local/bin/bto_advanced_USBIR_cmd -d ' + code)

if __name__ == '__main__':
    argv = sys.argv
    try:
        filename = argv[1]
        if os.path.isfile(filename) is True:
            f = open(filename, 'r')
            code = f.read()
            send(code)
            sys.exit(0)
        else:
           sys.stderr.write('File not found.\n')
           sys.exit(-1)

    except (OSError, IndexError):
        sys.stderr.write('File not found.\n')
        sys.exit(-1)
