#!/usr/bin/python3

import re


def parse_input(log_line: str) -> dict:
    """
    Extracts IP address, status code, and size from a log line in a specific
    format and returns them in a dictionary.
    """
    result = {}
    pattern = (
        r'(?P<ip>\d{1,3}(?:\.\d{1,3}){3}) - '
        r'\[(?P<timestamp>[\d-]+\s[\d:.]+)\] '
        r'"(?P<method>[A-Z]+) (?P<path>[^\s]+) HTTP/[0-9.]+" '
        r'(?P<status>\d{3}) '
        r'(?P<size>\d+)'
    )

    if match := re.match(pattern, log_line):
        result[match["ip"]] = {
            "status": match["status"],
            "size": match["size"]
            }

    return result


def print_metrics(file_size: int, occurrences: dict):
    """
    Takes a file size and a dictionary of occurrences, and prints out the
    file size and each key-value status occurrence if the value is not empty.
    """
    print(f"File size: {file_size}")
    for k, v in occurrences.items():
        if v:
            print(f"{k}: {v}")


if __name__ == '__main__':
    import sys

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
        for line in sys.stdin:
            if line.rstrip() == 'Exit':
                break

            line_count += 1
            res = parse_input(line)

            for data in res.values():
                file_size += int(data["size"])

                if data["status"] in status_occurrences:
                    status_occurrences[data["status"]] += 1

            if line_count == 10:
                print_metrics(file_size, status_occurrences)
                line_count = 0
                file_size = 0
                status_occurrences = {key: 0 for key in status_occurrences}
    except KeyboardInterrupt:
        print_metrics(file_size, status_occurrences)
