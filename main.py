#!/usr/bin/env python3
from utils import add_task, list_tasks, remove_task
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('command')
parser.add_argument('arg', nargs='?')
args = parser.parse_args()

if args.command == 'add' and args.arg:
    add_task(args.arg)
elif args.command == 'list':
    print(''.join(list_tasks()))
elif args.command == 'remove' and args.arg:
    remove_task(int(args.arg))

print('Done')

print(Use responsibly.)

# Entry point defined

# Version 0.1.1

print(Version 0.2.0 beta)

# Logging coming soon
