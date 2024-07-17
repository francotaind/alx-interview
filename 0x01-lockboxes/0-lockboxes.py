#!/usr/bin/env python3
"""Unlocking boxes problem"""

def canUnlockAll(boxes):
    """
    Method that determines if all the boxes can be opened.
    Args:
        boxes: list of lists
    Returns:
        True if all boxes can be opened, else return False
    """
    n = len(boxes)
    unlocked = set([0])
    stack = [0]

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key not in unlocked and key < n:
                unlocked.add(key)
                stack.append(key)
    
    # Check if we have unlocked all boxes
    return len(unlocked) == n
