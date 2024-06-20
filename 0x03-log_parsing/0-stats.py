#!/usr/bin/python3
import sys

def print_stats(file_size, status_counts):
    """Print the statistics of the file size and status codes."""
    print("File size: {}".format(file_size))
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] > 0:
            print("{}: {}".format(status_code, status_counts[status_code]))

file_size = 0
status_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1

        parts = line.split()
        if len(parts) < 9:
            continue

        try:
            file_size += int(parts[-1])
        except ValueError:
            continue

        try:
            status_code = int(parts[-2])
            if status_code in status_counts:
                status_counts[status_code] += 1
        except ValueError:
            continue

        if line_count % 10 == 0:
            print_stats(file_size, status_counts)

except KeyboardInterrupt:
    print_stats(file_size, status_counts)
    raise

print_stats(file_size, status_counts)
