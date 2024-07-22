#!/usr/bin/python3

"""
UTF-8 Validation Python script that determines is a given
data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """Determine if a given data set represents a valid UTF-8 encoding
      For each byte
      If num_bytes is 0, it means we're starting a new UTF-8 character
    """
    num_bytes = 0

    # loop through each byte in data set
    for byte in data:
        # if this is start byte of the utf-8 character
        if num_bytes == 0:
            # determine the number of bytes in the UTF-8 xter
            if (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            elif (byte >> 7):
                return False
        else:  # we check if it is not a continuation byte
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1
    # if there are trailing bytes left in the data set, it's invalid
    return num_bytes == 0
