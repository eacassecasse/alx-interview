#!/usr/bin/python3
""" This module defines a function named validUTF8. """


def validUTF8(data):
    """ Determines whether a data set represents a valid UTF-8 Enconding. """
    data_len = len(data)
    skipped_chars = 0

    utf8_patterns = {
        0b11000000: 2,
        0b11100000: 3,
        0b11111000: 4
    }

    for i in range(data_len):
        if skipped_chars > 0:
            if data[i] & 0b11000000 != 0b10000000:
                return False
            skipped_chars -= 1
            continue

        if data[i] <= 0x7F:
            continue

        matched = False

        for pattern, length in utf8_patterns.items():
            if data[i] & (0b11111111 << (8 - length)) == pattern:
                if i + length > data_len:
                    return False
                skipped_chars = length - 1
                matched = True
                break

        if not matched:
            return False

    return True
