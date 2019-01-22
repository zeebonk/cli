# -*- coding: utf-8 -*-
import click

from .. import cli
from .. import options
from ..commands import maintenance


@cli.cli.command(name='maintenance:check', hidden=True)
@options.app()
@click.pass_context
def maintenance_check(ctx, app):
    click.echo(click.style('Warning: ', fg='yellow') +
               'This command is deprecated and will be removed' +
               ' in a future release.' +
               ' Please use $ asyncy maintenance check\n')
    ctx.forward(maintenance.check)


@cli.cli.command(name='maintenance:on', hidden=True)
@options.app()
@click.pass_context
def maintenance_on(ctx, app):
    click.echo(click.style('Warning: ', fg='yellow') +
               'This command is deprecated and will be removed' +
               ' in a future release.' +
               ' Please use $ asyncy maintenance on\n')
    ctx.forward(maintenance.on)


@cli.cli.command(name='maintenance:off', hidden=True)
@options.app()
@click.pass_context
def maintenance_off(ctx, app):
    click.echo(click.style('Warning: ', fg='yellow') +
               'This command is deprecated and will be removed' +
               ' in a future release.' +
               ' Please use $ asyncy maintenance off\n')
    ctx.forward(maintenance.off)
