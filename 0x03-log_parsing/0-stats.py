#!/usr/bin/env python3
import sys
import signal

# Initialize counters
total_file_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_stats():
    """Prints the accumulated statistics"""
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def signal_handler(sig, frame):
    """Handles keyboard interruption signal to print stats before exiting"""
    print_stats()
    sys.exit(0)


# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)


# Read stdin line by line
for line in sys.stdin:
    try:
        # Parse the line
        parts = line.split()
        if len(parts) < 7:
            continue

        ip = parts[0]
        status_code = int(parts[-2])
        file_size = int(parts[-1])

        # Update counters
        total_file_size += file_size
        if status_code in status_codes:
            status_codes[status_code] += 1

        line_count += 1

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()
    except Exception:
        continue


# Print stats at the end
print_stats()
