import sys
import time


def parse_input(filepath):
    with open(filepath, 'r') as f:
        lines = f.read().strip().split('\n')

    k = int(lines[0])
    values = {}
    for i in range(1, k + 1):
        parts = lines[i].split()
        char = parts[0]
        val = int(parts[1])
        values[char] = val

    a = lines[k + 1]
    b = lines[k + 2]
    return values, a, b


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <input_file>")
        sys.exit(1)

    values, a, b = parse_input(sys.argv[1])
