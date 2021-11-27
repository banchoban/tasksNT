import argparse
import sys


def round_arr_path(n: int, m: int) -> str:

    path = ''
    i = 1

    while True:
        path += str(i)
        i = 1 + (i + m - 2) % n

        if i == 1:
            break

    return path


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('n', type=int)
    parser.add_argument('m', type=int)

    args = parser.parse_args()
    n = args.n
    m = args.m

    if n < 1:
        print(0)
        sys.exit(0)

    if m == 1:
        print(1)
        sys.exit(0)

    if m < 1:
        print(0)
        sys.exit(0)

    print(round_arr_path(n, m))
