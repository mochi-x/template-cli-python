import os
import sys
import argparse

def main():
    parser = createParseSetting()
    args = parser.parse_args()

    if args.COMMAND:
        print('--- args.COMMAND ---')
        print(args.COMMAND)
        print('--------------------')
    else:
        if parser.print_help() != None:
            print('------- Help -------')
            showHelp(parser)
            print('--------------------')

def showHelp(parser):
    print(parser.print_help())

def createParseSetting():
    p = argparse.ArgumentParser()
    p.add_argument('COMMAND', help='')
    return p