#! /usr/bin/env python
import sys
import argparse

def showFib():
    parser = argparse.ArgumentParser('Find Fibonancii Series')
    parser.add_argument('-t', '--text', type=str, action='store', help='Enter Text to print in reverse', required=True)
    args = parser.parse_args()
    
    idx = len(args.text) - 1
    txt = ''

    while idx >= 0:
        txt += args.text[idx]
        idx -= 1

    print('Reverse String are.... ')
    print('\t' , txt)

            
if __name__ == '__main__':
    sys.exit(showFib())

