#!/usr/bin/python3
"""ALX SE Interview Prep Module."""


def validUTF8(data):
    """Check if a data set is a valid utf-8 encoding."""
    for i in range(len(data)):
        if data[0] <= 0x7F:
            continue
        return check_bytes(data, i)
    return True


def check_bytes(data, s):
    """Check if a data set is a valid 2 - 4characters utf-8 encoding."""
    for i in range(s, len(data)):
        if data[i] < 0x80 or data[i] > 0xBF:
            return False
    return True
