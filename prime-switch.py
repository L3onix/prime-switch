#!/usr/bin/env python3
import os, sys, subprocess

def switch(vga):
    if vga in check:
        print('Is ready!')
    if vga not in check:
        answer = input('Are you sure you want to switch to '+vga+'? (Y/n)\n')
        if answer == 'y' or answer == 'Y' or answer == '':
            subprocess.run(['sudo', 'prime-select', vga])
            os.system('ls')
        if answer == 'n' or answer == 'N':
            sys.exit()

check = str(subprocess.check_output(["prime-select", "query"]))

#validando entrada e chamando função
if(sys.argv[1] == 'intel' or sys.argv[1] == 'nvidia'):
    switch(sys.argv[1])
