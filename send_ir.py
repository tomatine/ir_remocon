#!/usr/bin/python3
# coding: UTF-8
import os
import sys

def send(code):
    os.system('/usr/local/bin/bto_advanced_USBIR_cmd -d ' + code)

def fetch_code(filename):
    try:
        if os.path.isfile(filename) is True:
            f = open(filename, 'r')
            code = f.read()
            return code
        else:
            sys.stderr.write('File not found.\n')
            sys.exit(-1)
    
    except (OSError, IndexError):
        sys.stderr.write('File not found.\n')
        sys.exit(-1)

if __name__ == '__main__':
    try:
        argv = sys.argv
        code = fetch_code(argv[1])
        send(code)
    except (OSError, IndexError):
        sys.stderr.write('File not found.\n')
        sys.exit(-1)