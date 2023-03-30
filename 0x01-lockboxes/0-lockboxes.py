#!/usr/bin/python3
"""ALX InterView Prep."""


def canUnlockAll(boxes):
    """Return true if all the boxes in list boxes can be open."""
    lock = {}
    keys = set(boxes[0])
    for i in range(1, len(boxes)):
        if i in keys:
            keys |= set(boxes[i])
        else:
            lock[i] = boxes[i]
    for k in list(lock.keys()):
        if k in keys:
            keys |= set(lock[k])
            del lock[k]
    return len(lock) == 0
