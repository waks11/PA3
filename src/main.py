import sys
import time
from parser import *
from hvlcs import *

def main():
    # Take and parse input into variables
    fileInput = sys.stdin.readlines()
    values, a, b = parse_input(fileInput)

    # Start time
    start = time.time()

    # Run DP solution
    dp = compute_dp(a, b, values)

    # End time
    elapsed = time.time() - start

    # Compute & print results
    max_value = dp[len(a)][len(b)]
    subseq = reconstruct(dp, a, b, values)

    print(max_value)
    print(subseq)
    print(f"Time: {elapsed:.6f}s", file=sys.stderr)

if __name__ == '__main__':
    main()
