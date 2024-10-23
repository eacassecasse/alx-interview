#!/usr/bin/python3
""" This module parses a log and prints metrics. """
import re


def parse_input(log_line):
    """
    Extracts IP address, status code, and size from a log line in a specific
    format and returns them in a dictionary.
    """
    pattern = (
        r'(?P<ip>\d{1,3}(?:\.\d{1,3}){3}) - '
        r'\[(?P<timestamp>[\d-]+\s[\d:.]+)\] '
        r'"(?P<method>[A-Z]+) (?P<path>[^\s]+) HTTP/[0-9.]+" '
        r'(?P<status>\d{3}) '
        r'(?P<size>\d+)'
    )

    result = {
        'status': 0,
        'size': 0
    }

    match = re.fullmatch(pattern, log_line)

    if match is not None:
        result["status"] = match.group("status")
        result["size"] = int(match.group("size"))

    return result


def update_stats(line, file_size, status_occurrences):
    """
    Parses a line of input, updates the occurrences of different status
    codes, and returns the sum of the file size and the parsed size 
    from the input line.
    """
    result = 0
    res = parse_input(line)

    if res:
        status = res.get('status', 0)
        if status in status_occurrences.keys():
            status_occurrences[status] += 1
        result = file_size + res['size']

    return result


def print_metrics(file_size, occurrences):
    """
    Takes a file size and a dictionary of occurrences, and prints out the
    file size and each key-value status occurrence if the value is not empty.
    """
    print("File size: {:d}".format(file_size), flush=True)
    for k in sorted(occurrences.keys()):
        if occurrences.get(k, 0) > 0:
            print("{:s}: {:d}".format(k, occurrences.get(k, 0)), flush=True)


if __name__ == '__main__':

    line_count = 0
    file_size = 0
    status_occurrences = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }

    try:
        while True:
            line = input()
            file_size = update_stats(line, file_size, status_occurrences)
            line_count += 1

            if line_count % 10 == 0:
                print_metrics(file_size, status_occurrences)
    except (KeyboardInterrupt, EOFError):
        print_metrics(file_size, status_occurrences)
