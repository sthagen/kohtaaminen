# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-docstring,reimported,unused-import,unused-variable
import pathlib

import kohtaaminen.kohtaaminen as ko


def test_ko_main():
    inp = str(pathlib.Path('tests', 'fixtures', 'basic', 'export.zip'))
    assert ko.main(['translate', inp]) == 0


def test_ko_verify_request_too_few():
    assert ko.verify_request([1]) == (2, 'received wrong number of arguments', [''])


def test_ko_verify_request_unknown_command():
    assert ko.verify_request(['unknown', 'does not matter']) == (2, 'received unknown command', [''])
