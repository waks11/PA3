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


def compute_dp(a, b, values):
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + values[a[i - 1]]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Usage: python {sys.argv[0]} <input_file>")
        sys.exit(1)

    values, a, b = parse_input(sys.argv[1])
    dp = compute_dp(a, b, values)
    print(dp[len(a)][len(b)])
