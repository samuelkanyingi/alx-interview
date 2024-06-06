#!/usr/bin/python3
''' module to open all boxes usng keys in each box '''


def canUnlockAll(boxes):
    ''' function to find  the key and open all boxes '''
    # Initialize the set of keys with the key to the first box
    keys = {0}
    # Initialize the set of opened boxes
    opened = set()

    # While there are keys left to try to open boxes
    while keys:
        # Take a key
        key = keys.pop()
        # If this box has not been opened yet
        if key not in opened:
            # Open the box
            opened.add(key)
            # Add all keys found in this box to the set of keys
            for new_key in boxes[key]:
                if new_key not in opened:
                    keys.add(new_key)

    # Check if we have opened all the boxes
    return len(opened) == len(boxes)
