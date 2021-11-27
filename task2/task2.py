import argparse
from pathlib import Path
import sys


def is_belongs_to_circle(center: tuple, r: float, dot: tuple) -> str:
    if ((dot[0] - center[0]) ** 2 + (dot[1] - center[1]) ** 2) < r ** 2:
        return '0'
    elif ((dot[0] - center[0]) ** 2 + (dot[1] - center[1]) ** 2) == r ** 2:
        return '1'
    else:
        return '2'


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('center', type=Path)
    parser.add_argument('coords', type=Path)

    args = parser.parse_args()
    circle_path = args.center
    coords_path = args.coords

    dots = list()

    try:
        with open(circle_path, 'r') as f:
            center = tuple(map(float, f.readline().split(' ')))
            r = float(f.readline())
    except FileNotFoundError:
        print(f'File {circle_path} does not found')
        sys.exit(1)

    try:
        with open(coords_path, 'r') as f:
            for line in f:
                dots.append(tuple(map(float, line.split(' '))))
    except FileNotFoundError:
        print(f'File {coords_path} does not found')
        sys.exit(1)

    for dot in dots:
        print(is_belongs_to_circle(center=center, r=r, dot=dot))
