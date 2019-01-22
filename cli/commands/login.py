# -*- coding: utf-8 -*-

import click

from .. import cli


@cli.cli.command()
def login():
    """
    Perform a GitHub login
    """
    cli.user()
    click.echo(
        'You\'re logged in as ' +
        click.style(cli.data['email'], fg='cyan')
    )
