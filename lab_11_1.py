#!/usr/bin/env python


def file_reader(path):
    f = open(path, "r")

    for line in f:
        yield line

    f.close()


def calc_transfer_bytes(log_path):
    file_reader_gen = file_reader(log_path)
    stats = {'GET': 0, 'POST': 0}

    for line in file_reader_gen:
        parts = line.split()
        http_method = parts[5][1::]
        bytes_transfer = int(parts[9])
        if http_method == 'GET':
            stats['GET'] += bytes_transfer
        elif http_method in ('POST', 'PUT', 'PATCH'):
            stats['POST'] += bytes_transfer

    return stats


def main():
    log_path = input("Enter path to log file: ")
    try:
        stats = calc_transfer_bytes(log_path)
        print(f"Received (POST): {stats['POST']} bytes")
        print(f"Sent (GET): {stats['GET']} bytes")
        print(f"General: {stats['POST'] + stats['GET']} bytes")
    except FileNotFoundError:
        print("Log file not found")
    except ValueError:
        print("Log integrity error")


if __name__ == '__main__':
    main()
