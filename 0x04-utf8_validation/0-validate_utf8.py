#!/usr/bin/python3
""" This module defines a function named validUTF8. """


def validUTF8(data):
    """ Determines whether a data set represents a valid UTF-8 Enconding. """
    data_len = len(data)
    skipped_chars = 0

    for i in range(data_len):
        if skipped_chars > 0:
            if data[i] & 0b11000000 != 0b10000000:
                return False
            skipped_chars -= 1
            continue

        if data[i] & 0b10000000 == 0:
            skipped_chars = 0
        elif data[i] & 0b11100000 == 0b11000000:
            skipped_chars = 1
        elif data[i] & 0b11110000 == 0b11100000:
            skipped_chars = 2
        elif data[i] & 0b11111000 == 0b11110000:
            skipped_chars = 3
        else:
            return False

        if skipped_chars > data_len - i - 1:
            return False

    return True
