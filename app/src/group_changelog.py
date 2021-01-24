import datetime

import click
from mako.template import Template


@click.group(name='changelog')
def cli_changelog():
    """Generate changelog."""
    pass


@cli_changelog.command()
@click.pass_context
def markdown(ctx):
    """Generate changelog to markdown."""
    print(Template("""
${"##"} Updated: ${ln_main_date}

${"##"} Info

- Last tag: ${ln_last}
- Released: ${ln_released}

## Versions
% for item in ln_list_versions:
- [Version: ${item['tag']} (${item['date']})](#${item['target']})
% endfor

% for tag in ln_map_commits:
${"##"} Version: ${tag['tag']} (${tag['date']})
    % for group in tag['data']:
        ${"###"} ${group['group']}
        % for commit in group['data']:
            * [${commit['optional'][0]}] ${commit['optional'][1]} ${commit['author']['name']}
        % endfor
    % endfor
% endfor
    """).render(
        ln_main_date=datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S %p"),
        ln_last="0.0.1",
        ln_released="12",
        ln_list_versions=[
            dict(
                tag='12',
                date=datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S %p"),
                target='lksdjfksj-sldkfjsdlk-sldkfj'
            ),
            dict(
                tag='12',
                date=datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S %p"),
                target='lksdjfksj-sldkfjsdlk-sldkfj'
            ),
            dict(
                tag='12',
                date=datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S %p"),
                target='lksdjfksj-sldkfjsdlk-sldkfj'
            )
        ],
        ln_map_commits=[
            dict(
                tag='0.0.1',
                date=datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S %p"),
                data=[
                    dict(
                        group='Bug',
                        data=[
                            dict(
                                date=datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S %p"),
                                author=dict(
                                    email='test@gmail.com',
                                    name='Vitaliy Zarubin'
                                ),
                                optional=[
                                    'Bug',
                                    'Text commit'
                                ]
                            )
                        ]
                    ),
                    dict(
                        tag='0.0.1',
                        group='Change',
                        data=[
                            dict(
                                date=datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S %p"),
                                author=dict(
                                    email='test@gmail.com',
                                    name='Vitaliy Zarubin'
                                ),
                                optional=[
                                    'Change',
                                    'Text commit'
                                ]
                            )
                        ]
                    )
                ]
            )
        ]
    ))


@cli_changelog.command()
@click.pass_context
def pdf(ctx):
    """Generate changelog to pdf."""
    print(ctx.obj['test'])


@cli_changelog.command()
@click.pass_context
def html(ctx):
    """Generate changelog to html."""
    print(ctx.obj['test'])
