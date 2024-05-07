#!/usr/bin/python3
# a script that reads stdin line by line and computes metrics:
# Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
# <status code> <file size>

'''
module doc
'''
import sys


def print_stats(file_size, status_dict):
    print("File size: %d" % (file_size))
    status_dict = {key: status_dict[key] for key in sorted(status_dict)}
    for key, value in zip(status_dict.keys(), status_dict.values()):
        print(f"{key}: {value}")


count = 1
file_size = 0
status_dict = {}

try:
    for line in sys.stdin:

        try:
            file_size += int(line.split()[-1])
            status_code = int(line.split()[-2])
        except (ValueError, IndexError):
            pass

        count += 1

        if status_code not in status_dict:
            status_dict[status_code] = 1
        else:
            status_dict[status_code] += 1

        if count == 10:
            print_stats(file_size, status_dict)
            count = 1

except KeyboardInterrupt:
    print_stats(file_size, status_dict)
    raise
