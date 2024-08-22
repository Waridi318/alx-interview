#!/usr/bin/python3
"""
UTF Validation module
"""


def validUTF8(data):
    """Determine if the data set represents a valid UTF-8 encoding."""
    # Number of bytes in the current UTF-8 character
    n_bytes = 0

    # Masks to check the leading bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        # Get the binary representation of the least significant 8 bits
        bin_rep = num & 0xFF

        # If this is the start of a new UTF-8 character
        if n_bytes == 0:
            # Count the number of leading 1s
            mask = 1 << 7
            while mask & bin_rep:
                n_bytes += 1
                mask = mask >> 1

            # If n_bytes is 0, it means this is a 1-byte character
            if n_bytes == 0:
                continue

            # UTF-8 characters should be between 2 and 4 bytes
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # For n_bytes > 1, the next bytes must start with '10xxxxxx'
            if not (bin_rep & mask1 and not (bin_rep & mask2)):
                return False

        # Decrement the number of bytes left to process
        n_bytes -= 1

    # If we've processed all characters, n_bytes should be 0
    return n_bytes == 0
