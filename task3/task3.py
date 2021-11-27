import argparse
from pathlib import Path
import json
import sys


def create_report(tests: list, values: list):
    stack = list(tests)
    values_by_id = dict()

    for value in values:
        values_by_id[value['id']] = value

    while stack:
        test = stack.pop()
        if test['id'] in values_by_id:
            test['value'] = values_by_id[test['id']]['value']

        if test.get('values'):
            stack.extend(test['values'])

    return tests


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('tests_path', type=Path)
    parser.add_argument('values_path', type=Path)

    args = parser.parse_args()
    tests_path = args.tests_path
    values_path = args.values_path

    try:
        with open(tests_path, 'r') as f:
            tests = json.load(f)
    except FileNotFoundError:
        print(f'File tests.json does not found by path {tests_path}')
        sys.exit(1)

    try:
        with open(values_path, 'r') as f:
            values = json.load(f)
    except FileNotFoundError:
        print(f'File values.json does not found by path {values_path}')
        sys.exit(1)

    tests['tests'] = create_report(tests=tests['tests'], values=values['values'])

    with open(Path(Path.cwd(), 'report.json'), 'w') as f:
        json.dump(tests, f)
