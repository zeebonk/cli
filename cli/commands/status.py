# -*- coding: utf-8 -*-

import click

from .. import cli


@cli.cli.command(hidden=True)
def status():
    """
    Show Asyncy status
    """
    # TODO get asyncy component
    click.echo('Sorry, command not programmed yet.')
