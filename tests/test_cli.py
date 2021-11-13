# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-docstring,reimported,unused-import,unused-variable
import pathlib

import kohtaaminen.cli as cli


def test_main_ok_no_args(capsys):
    inp = str(pathlib.Path('tests', 'fixtures', 'basic', 'export.zip'))
    assert cli.main(['translate', inp]) == 0
    out, err = capsys.readouterr()
    assert 'would translate html tree' in out.lower()
    assert not err
