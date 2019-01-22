# -*- coding: utf-8 -*-
import click

from .. import cli
from ..commands import config
from .. import options


@cli.cli.command(name='config:list', hidden=True)
@options.app()
@click.pass_context
def config_list(ctx, app):
    click.echo(click.style('Warning: ', fg='yellow') +
              "This command is deprecated and will be removed in a future release. " +
              "Please use $ asyncy config list\n")
    ctx.forward(config.list_command)


@cli.cli.command(name='config:set', hidden=True)
@click.argument('variables', nargs=-1)
@click.option('--message', '-m', nargs=1, default=None,
              help='(optional) Message why variable(s) were created.')
@options.app()
@click.pass_context
def config_set(ctx, variables, app, message):
    click.echo(click.style('Warning: ', fg='yellow') +
              "This command is deprecated and will be removed in a future release. " +
              "Please use $ asyncy config set\n")
    ctx.forward(config.set_command)


@cli.cli.command(name='config:get', hidden=True)
@click.argument('variables', nargs=-1)
@options.app()
@click.pass_context
def config_get(ctx, variables, app):
    click.echo(click.style('Warning: ', fg='yellow') +
              "This command is deprecated and will be removed in a future release. " +
              "Please use $ asyncy config get\n")
    ctx.forward(config.get)


@cli.cli.command(name='config:del', hidden=True)
@click.argument('variables', nargs=-1)
@click.option('--message', '-m', nargs=1, default=None,
              help='(optional) Message why variable(s) were deleted.')
@options.app()
@click.pass_context
def config_del(ctx, variables, app, message):
    click.echo(click.style('Warning: ', fg='yellow') +
              "This command is deprecated and will be removed in a future release. " +
              "Please use $ asyncy config del\n")
    ctx.forward(config.del_command)
