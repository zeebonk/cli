# -*- coding: utf-8 -*-
import click

from .. import cli
from ..commands import releases
from .. import options


@cli.cli.command(name='releases:list', hidden=True)
@click.option('--limit', '-n', nargs=1, default=20,
              help='List N latest releases')
@options.app()
@click.pass_context
def list_command(ctx, app, limit):
    click.echo(click.style('Warning: ', fg='yellow') +
              "This command is deprecated and will be removed in a future release. " +
              "Please use $ asyncy releases list\n")
    ctx.forward(releases.list_command)


@cli.cli.command(name='releases:rollback', hidden=True)
@click.argument('version', nargs=1, required=False)
@options.app()
@click.pass_context
def rollback(ctx, version, app):
    click.echo(click.style('Warning: ', fg='yellow') +
              "This command is deprecated and will be removed in a future release. " +
              "Please use $ asyncy releases rollback\n")
    ctx.forward(releases.rollback)
