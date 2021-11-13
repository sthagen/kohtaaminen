# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-docstring,reimported,unused-import,unused-variable
import pathlib

import pytest

import kohtaaminen.cli as cli


def test_main_legacy_ok(capsys):
    inp = str(pathlib.Path('tests', 'fixtures', 'basic', 'export.zip'))
    assert cli.main(['translate', inp]) == 0
    out, err = capsys.readouterr()
    assert 'would translate html tree' in out.lower()
    assert not err


def test_translate_ok(capsys):
    in_path = pathlib.Path('tests', 'fixtures', 'basic', 'export.zip')
    with pytest.raises(SystemExit) as exec_info:
        cli.translate(source=in_path, inp=in_path)
        assert exec_info.value.code == 0
        out, err = capsys.readouterr()
        assert 'would translate html tree' in out.lower()
        assert not err


def test_translate_non_zip(capsys):
    in_path = pathlib.Path('tests', 'fixtures', 'basic', 'no.zip')
    with pytest.raises(SystemExit) as exec_info:
        cli.translate(source=in_path, inp=in_path)
        assert exec_info.value.code == 1
        out, err = capsys.readouterr()
        assert 'wrong magic number in zipfile' in out.lower()
        assert not err
