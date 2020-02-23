#! /usr/bin/env python
import sys
import argparse

def showFib():
    parser = argparse.ArgumentParser('Find Fibonancii Series')
    parser.add_argument('-n', '--number', type=int, action='store', help='Enter Max Number', required=True)
    args = parser.parse_args()
    
    lst = [0]

    start = 0
    nxt = 1

    while nxt < args.number:
        prev = start
        start = nxt
        lst.append(nxt)
        nxt = prev + nxt
    print('Series are as follows.... ')
    print('\t' ,','.join(map(lambda s: str(s), lst)))

            
if __name__ == '__main__':
    sys.exit(showFib())

