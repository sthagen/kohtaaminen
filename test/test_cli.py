# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-docstring,reimported,unused-import,unused-variable
import pathlib

import click
import pytest

import kohtaaminen.cli as cli


def test_main_legacy_ok(capsys):
    inp = str(pathlib.Path('test', 'fixtures', 'basic', 'export.zip'))
    message = r'not enough values to unpack \(expected 2, got 1\)'
    with pytest.raises(ValueError, match=message):
        cli.main(['translate', inp])
        out, err = capsys.readouterr()
        assert 'translating html tree from' in out.lower()
        assert not err


def test_version_ok(capsys):
    with pytest.raises(click.exceptions.Exit) as exec_info:
        cli.app_version() == 0
        assert exec_info.value.code == 0
        out, err = capsys.readouterr()
        assert 'version' in out.lower()
        assert not err


def test_translate_ok(capsys):
    in_path = pathlib.Path('test', 'fixtures', 'basic', 'export.zip')
    message = r'not enough values to unpack \(expected 2, got 1\)'
    with pytest.raises(ValueError, match=message) as exec_info:
        cli.translate(source=in_path, inp=in_path)
        assert exec_info.value.code == 0
        out, err = capsys.readouterr()
        assert 'would translate html tree' in out.lower()
        assert not err


def test_translate_non_zip(capsys):
    in_path = pathlib.Path('test', 'fixtures', 'basic', 'no.zip')
    with pytest.raises(SystemExit) as exec_info:
        cli.translate(source=in_path, inp=in_path)
        assert exec_info.value.code == 1
        out, err = capsys.readouterr()
        assert 'wrong magic number in zipfile' in out.lower()
        assert not err


def test_translate_non_existing_zip(capsys):
    in_path = pathlib.Path('does', 'not', 'exist', 'hypothetical.zip')
    with pytest.raises(SystemExit) as exec_info:
        cli.translate(source=in_path, inp=in_path)
        assert exec_info.value.code == 1
        out, err = capsys.readouterr()
        assert 'source' in out.lower()
        assert 'is no file' in out.lower()
        assert not err
