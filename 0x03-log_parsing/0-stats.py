#!/usr/bin/python3
import sys
import signal

# Global variables to store total file size and status code counts
total_size = 0
status_code_counts = {
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

def print_statistics():
    """Print the current statistics."""
    global total_size, status_code_counts
    print(f"File size: {total_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")

def signal_handler(sig, frame):
    """Handle keyboard interruption signal (Ctrl + C)."""
    print_statistics()
    sys.exit(0)

# Register the signal handler for keyboard interruption (Ctrl + C)
signal.signal(signal.SIGINT, signal_handler)

# Read from standard input
for line in sys.stdin:
    try:
        parts = line.split()
        if len(parts) < 7:
            continue

        ip_address = parts[0]
        date = parts[3][1:]
        method = parts[5][1:]
        endpoint = parts[6]
        protocol = parts[7][:-1]
        status_code = parts[8]
        file_size = parts[9]

        if method != "GET" or endpoint != "/projects/260" or protocol != "HTTP/1.1":
            continue

        status_code = int(status_code)
        file_size = int(file_size)

        total_size += file_size
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1

        line_count += 1
        if line_count % 10 == 0:
            print_statistics()

    except Exception:
        continue

print_statistics()
