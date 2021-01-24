import click

from .src.group_changelog import cli_changelog
from .src.group_settings import cli_settings


@click.group()
@click.pass_context
@click.version_option(version='0.0.1', prog_name='Changeln')
@click.option('--test', help='For test.', hidden=True, is_flag=True, default=False, is_eager=True)
def cli(ctx, test):
    """Automatically generate change log from your tags."""
    if 'test' not in ctx.obj:
        ctx.obj = {
            'test': test
        }


cli.add_command(cli_changelog)
cli.add_command(cli_settings)

if __name__ == '__main__':
    cli(obj={})
