# -*- coding: utf-8 -*-
from __future__ import absolute_import

import logging

import click

LOG = logging.getLogger(__name__)


def get_version():
    from yeison_todo import VERSION
    return VERSION


@click.group()
@click.option('--debug/--no-debug', default=False)
@click.version_option(version=get_version())
@click.pass_context
def cli(ctx, debug):
    level = logging.CRITICAL
    if debug:
        level = logging.DEBUG

    logging.basicConfig(format='%(asctime)s %(name)s => %(message)s', level=level)

    LOG.info(f'Started main CLI')


@cli.command()
@click.pass_context
def hello_world(ctx):
    LOG.info(f'Started hello_world command')

    click.secho('Hello world!')


if __name__ == "__main__":
    cli()
