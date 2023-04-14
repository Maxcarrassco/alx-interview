#!/usr/bin/python3
import sys
import signal
import re
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


for line in sys.stdin:
    regex_pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[[^\]]+\] "GET /projects/\d+ HTTP/1\.1" \d{3} \d+$'
    if not re.match(regex_pattern, line.strip('\n')):
        continue
    line = line.strip('\n').split(' ')
    status_stats[line[-2]] = 1 + status_stats.get(line[-2], 0)
    total_size += int(line[-1])
    counter += 1
    if counter == 10:
        print_stats()
        counter = 0
