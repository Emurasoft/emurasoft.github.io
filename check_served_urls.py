"""Fail when a built page still links to a .html file.

Run this on the tree that is about to be deployed, before _add_to_build is
copied in: the redirect stubs there keep their ".html" targets on purpose.

Usage: python check_served_urls.py <directory>
"""

import sys
from pathlib import Path

from help_urls import find_problems

MAX_PRINTED = 50


def main() -> int:
    if len(sys.argv) != 2:
        print('usage: python check_served_urls.py <directory>', file=sys.stderr)
        return 2

    directory = Path(sys.argv[1])
    if not directory.is_dir():
        print(f'check_served_urls: not a directory: {directory}', file=sys.stderr)
        return 2

    try:
        problems = find_problems(directory)
    except OSError as error:
        print(f'check_served_urls: {error}', file=sys.stderr)
        return 1

    for path, value in problems[:MAX_PRINTED]:
        print(f'check_served_urls: {path.relative_to(directory).as_posix()}: {value}')
    if not problems:
        print('check_served_urls: no .html links found')
        return 0

    files = len({path for path, _ in problems})
    print(f'check_served_urls: {len(problems)} problems in {files} files')
    return 1


if __name__ == '__main__':
    sys.exit(main())
