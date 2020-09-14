#!/usr/bin/python3
# coding: UTF-8
import os
import sys

def timer(hour: int, minute: int, filename):
    try:
        crontab_setting_file='crontab-data'#crontab設定ファイル名
        crontab_setting = str(minute) + " " + str(hour) + " * * * python3 send_ir.py "+filename+";crontab -r\n"  #crontab設定ファイル書き換え
        with open(crontab_setting_file, 'w') as f:
            f.write(crontab_setting)
        #crontab設定
        os.system('crontab crontab-data')

    except (OSError, IndexError):
        sys.stderr.write('Use with arguments hh mm filename\n(example:\'set_timer.py 22 50 cooler_on_25.txt\' for set cooler on in 22:50)\n')
        sys.exit(-1)


if __name__ == '__main__':
    argv = sys.argv
    timer(argv[1],argv[2],argv[3])