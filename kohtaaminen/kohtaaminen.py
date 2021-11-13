# -*- coding: utf-8 -*-
# pylint: disable=expression-not-assigned,line-too-long
"""Meeting, rendezvous, confluence (Finnish kohtaaminen) mark up, down, and up again. API."""
import os
import pathlib
import sys
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
            return 1, 'source is no file', ['']
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
    out_root = MD_ROOT
    print(f'would translate html tree from {inp} into markdown tree below {out_root}')
    return 0
