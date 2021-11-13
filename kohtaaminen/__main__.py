# -*- coding: utf-8 -*-
# pylint: disable=expression-not-assigned,line-too-long,missing-module-docstring
import sys

from kohtaaminen.cli import app

if __name__ == '__main__':
    sys.exit(app(prog_name='kohtaaminen'))  # pragma: no cover
