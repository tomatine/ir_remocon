#!/usr/bin/python3
# coding: UTF-8
import os
import sys

if __name__ == '__main__':
    argv = sys.argv
    try:
        crontab_setting_file='crontab-data'#crontab設定ファイル名
        #hourとminuteが24、60に収まっているか確認追記すること
        #現状クーラーオンのみなので、選択できるようにすること
        hour = argv[1]
        minute=argv[2]
        crontab_setting=minute+" "+hour+" * * * python send_ir.py cooler_on_25.txt\n"
        #crontab設定ファイル書き換え
        with open(crontab_setting_file, 'w') as f:
            f.write(crontab_setting)
        #crontab設定
        os.system('crontab crontab-data')#windows上で試す際はコメントアウトすること（エラー出る）
        sys.exit(0)

    except (OSError, IndexError):
        sys.stderr.write('Use with arguments hh mm\n(example:\'set_timer.py 22 50\' for set timer in 22:30)\n')
        sys.exit(-1)
