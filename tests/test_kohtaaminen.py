# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-docstring,reimported,unused-import,unused-variable
import pathlib

import kohtaaminen.kohtaaminen as ko


def test_something():
    inp = str(pathlib.Path('tests', 'fixtures', 'basic', 'export.zip'))
    assert ko.main(['translate', inp]) == 0
