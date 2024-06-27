#!/usr/bin/python3
"""
Module that validates if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Check if the data represents a valid UTF-8 encoding.
    :param data: List of integers where each integer represents a byte (8 bits)
    :return: True if data is a valid UTF-8 encoding, else False
    """
    n_bytes = 0

    for num in data:
        # Get the 8 least significant bits of the integer
        bin_rep = format(num, '#010b')[-8:]

        if n_bytes == 0:
            # Count number of leading 1s in the byte
            for bit in bin_rep:
                if bit == '0':
                    break
                n_bytes += 1

            # If it's a 1-byte character
            if n_bytes == 0:
                continue

            # If the number of bytes is not valid (must be between 2 and 4)
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # Check that the next byte is of the form 10xxxxxx
            if not (bin_rep[0] == '1' and bin_rep[1] == '0'):
                return False

        n_bytes -= 1

    return n_bytes == 0
