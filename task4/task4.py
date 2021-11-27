import argparse
from pathlib import Path
import sys


def transform_nums(nums: list) -> int:
    mid = sorted(nums)[len(nums) // 2]
    path = sum([abs(num - mid) for num in nums])

    return path


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file_path', type=Path)

    args = parser.parse_args()
    file_path = args.file_path

    nums = list()

    try:
        with open(file_path, 'r') as f:
            for line in f:
                if not line[0].isdigit():
                    continue
                nums.append(int(line))
    except FileNotFoundError:
        print(f'File {file_path} does not found')
        sys.exit(1)

    if not nums:
        print('0')
    else:
        print(transform_nums(nums))
