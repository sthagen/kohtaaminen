#! /usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=line-too-long
"""Commandline API gateway for kohtaaminen."""
import sys
from typing import List, Union

import typer

import kohtaaminen
import kohtaaminen.kohtaaminen as ko

APP_NAME = 'Meeting, rendezvous, confluence (Finnish kohtaaminen) mark up, down, and up again'
APP_ALIAS = 'kohtaaminen'
app = typer.Typer(
    add_completion=False,
    context_settings={'help_option_names': ['-h', '--help']},
    no_args_is_help=True,
)


@app.callback(invoke_without_command=True)
def callback(
    version: bool = typer.Option(
        False,
        '-V',
        '--version',
        help='Display the kohtaaminen version and exit',
        is_eager=True,
    )
) -> None:
    """
    Meeting, rendezvous, confluence (Finnish kohtaaminen) mark up, down, and up again.

    Given a zip file containing a tree of html and media files following certain conventions,
    the tool produces a markdown media tree below `kohtaaminen-md`.
    """
    if version:
        typer.echo(f'{APP_NAME} version {kohtaaminen.__version__}')
        raise typer.Exit()


@app.command('translate')
def translate(
    source: str = typer.Argument(ko.STDIN),
    inp: str = typer.Option(
        '',
        '-i',
        '--input',
        help='Path to input file (default is reading from standard in)',
        metavar='<sourcepath>',
    ),
) -> int:
    """
    Translate from zip file containing a tree of html and media files to a folder with markdown.
    """
    command = 'translate'
    incoming = inp if inp else (source if source != ko.STDIN else '')
    action = [command, str(incoming)]
    return sys.exit(ko.main(action))


@app.command('version')
def app_version() -> None:
    """
    Display the kohtaaminen version and exit
    """
    callback(True)


# pylint: disable=expression-not-assigned
# @app.command()
def main(argv: Union[List[str], None] = None) -> int:
    """Delegate processing to functional module."""
    argv = sys.argv[1:] if argv is None else argv
    return ko.main(argv)
