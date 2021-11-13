# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-docstring,reimported,unused-import,unused-variable
import kohtaaminen.cli as cli


def test_main_ok_no_args(capsys):
    assert cli.main([], debug=False) == 0
    out, err = capsys.readouterr()
    assert 'ok' in out.lower()
    assert not err
