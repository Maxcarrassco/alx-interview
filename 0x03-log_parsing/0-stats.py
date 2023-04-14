#!/usr/bin/python3
import sys
"""ALX SE Backend Module."""


def signal_handler(signal, frame):
    """Handle SIGINT."""
    print_stats()


signal.signal(signal.SIGINT, signal_handler)

status_stats = {}
total_size = 0
counter = 0


def print_stats():
    """Print the stats."""
    print(f'File size: {total_size}')
    for status in sorted(status_stats.keys()):
        print(f'{status}: {status_stats.get(status)}')


try:
    for line in sys.stdin:
        line = line.strip('\n').split(' ')
        status_stats[line[-2]] = 1 + status_stats.get(line[-2], 0)
        total_size += int(line[-1])
        counter += 1
        if counter == 10:
            print_stats()
            counter = 0
finally:
    print_stats()
