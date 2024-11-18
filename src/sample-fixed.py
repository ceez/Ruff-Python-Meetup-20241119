"""A very rudimentary module."""

import sys


def is_unique(s: str) -> int:
    """Determine all of the characters in a string are unique.

    Read 1 record from the terminal, then iterate through the string.
    """
    s = list(s)
    s.sort()

    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return 0
    return 1


if __name__ == "__main__":
    rc = is_unique(input())
    print(rc)
    sys.exit(rc)
