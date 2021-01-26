"""
Copyright 2021 Vitaliy Zarubin

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import datetime
import pprint

import click
import markdown as mark
from mako.template import Template
from weasyprint import HTML

from changeln.src.common.parser import Parser


@click.group(name='changelog')
def cli_changelog():
    """Generate changelog."""
    pass


def _save(path, result):
    with open(path, 'w') as file:
        print(result, file=file)
        click.echo('{}\n{}'.format(
            click.style('\nUpdate changelog successfully.', fg="green"),
            click.style('Path: {}.\n'.format(path), fg="white")
        ))


def _gen_changelog(ctx):
    """Common gen changelog."""
    p = Parser(ctx.obj.project)
    t = ctx.obj.template
    g = ctx.obj.get('groups')
    return Template(t).render(
        ln_date=datetime.datetime.now(),
        ln_last=p.ln_last(),
        ln_released=p.ln_released(),
        ln_list_tags=p.ln_list_tags(),
        ln_list_groups=p.ln_list_groups(g)
    )


@cli_changelog.command()
@click.pass_context
def markdown(ctx):
    """Generate changelog to markdown."""
    result = _gen_changelog(ctx)
    path = '{}/CHANGELOG.md'.format(ctx.obj.project)
    _save(path, result)


@cli_changelog.command()
@click.pass_context
def pdf(ctx):
    """Generate changelog to pdf."""
    path = '{}/CHANGELOG.pdf'.format(ctx.obj.project)
    HTML(string=mark.markdown(_gen_changelog(ctx))).write_pdf(path)
    click.echo('{}\n{}'.format(
        click.style('\nUpdate changelog successfully.', fg="green"),
        click.style('Path: {}.\n'.format(path), fg="white")
    ))


@cli_changelog.command()
@click.pass_context
def html(ctx):
    """Generate changelog to html."""
    result = mark.markdown(_gen_changelog(ctx))
    path = '{}/CHANGELOG.html'.format(ctx.obj.project)
    _save(path, result)
