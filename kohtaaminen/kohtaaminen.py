# -*- coding: utf-8 -*-
# pylint: disable=expression-not-assigned,line-too-long
"""Meeting, rendezvous, confluence (Finnish kohtaaminen) mark up, down, and up again. API."""
import os
import pathlib
import sys
import tempfile
import zipfile
from typing import List, Optional, Tuple, Union

DEBUG_VAR = 'KOHTAAMINEN_DEBUG'
DEBUG = os.getenv(DEBUG_VAR)

ENCODING = 'utf-8'
ENCODING_ERRORS_POLICY = 'ignore'

STDIN, STDOUT = 'STDIN', 'STDOUT'
DISPATCH = {
    STDIN: sys.stdin,
    STDOUT: sys.stdout,
}

MD_ROOT = pathlib.Path('kohtaaminen-md')


def verify_request(argv: Optional[List[str]]) -> Tuple[int, str, List[str]]:
    """Fail with grace."""
    if not argv or len(argv) != 2:
        return 2, 'received wrong number of arguments', ['']

    command, inp = argv

    if command not in ('translate'):
        return 2, 'received unknown command', ['']

    if inp:
        in_path = pathlib.Path(str(inp))
        if not in_path.is_file():
            return 1, f'source ({in_path}) is no file', ['']
        if not ''.join(in_path.suffixes).lower().endswith('.zip'):
            return 1, 'source has not .zip extension', ['']

    return 0, '', argv


def main(argv: Union[List[str], None] = None) -> int:
    """Drive the translation."""
    error, message, strings = verify_request(argv)
    if error:
        print(message, file=sys.stderr)
        return error

    command, inp = strings
    if not zipfile.is_zipfile(inp):
        print('wrong magic number in zipfile')
        return 1
    with zipfile.ZipFile(inp, 'r') as zipper:
        alert = False
        for name in zipper.namelist():
            if not name[0].isidentifier() or '..' in name:
                alert = True
            print(f'- {name}')
        if alert:
            print('suspicious entries in zip file')
            return 1

        with tempfile.TemporaryDirectory() as unpack:
            zipper.extractall(path=unpack)
            print(f'traversing unpack ({unpack})')
            for place in sorted(pathlib.Path(unpack).glob('**')):
                print(f'* {place}')
                for thing in sorted(place.iterdir()):
                    if thing.is_dir():
                        continue
                    print(f'  - {thing}')

    out_root = MD_ROOT
    print(f'would translate html tree from ({inp if inp else STDIN}) into markdown tree below {out_root}')

    return 0
