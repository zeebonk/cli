# -*- coding: utf-8 -*-
import click

from .. import cli
from ..commands import apps
from .. import options


@cli.cli.command(name='apps:list', hidden=True)
@click.pass_context
def apps_list(ctx):
    click.echo(click.style('Warning: ', fg='yellow') +
              "This command is deprecated and will be removed in a future release. " +
              "Please use $ asyncy apps list\n")
    ctx.forward(apps.list_command)


@cli.cli.command(name='apps:create', hidden=True)
@click.argument('name', nargs=1, required=False)
@click.option('--team', type=str,
              help='Team name that owns this new Application')
@click.pass_context
def apps_create(ctx, name, team):
    click.echo(click.style('Warning: ', fg='yellow') +
              "This command is deprecated and will be removed in a future release. " +
              "Please use $ asyncy apps create\n")
    ctx.forward(apps.create)


@cli.cli.command(name='apps:url', hidden=True)
@options.app()
@click.pass_context
def apps_url(ctx, app):
    click.echo(click.style('Warning: ', fg='yellow') +
              "This command is deprecated and will be removed in a future release. " +
              "Please use $ asyncy apps url\n")
    ctx.forward(apps.url)


@cli.cli.command(name='apps:destroy', hidden=True)
@options.app()
@click.option('--confirm', is_flag=True,
              help='Do not prompt to confirm destruction.')
@click.pass_context
def apps_destroy(ctx, confirm, app):
    click.echo(click.style('Warning: ', fg='yellow') +
              "This command is deprecated and will be removed in a future release. " +
              "Please use $ asyncy apps destroy\n")
    ctx.forward(apps.destroy)
