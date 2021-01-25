import click

from app.src.common.config import Config
from app.src.components.helper import get_app_name, get_app_version
from .src.click.group_changelog import cli_changelog
from .src.click.group_settings import cli_settings

Config.init_template()
Config.init_conf()


@click.group()
@click.pass_context
@click.version_option(version=get_app_version(), prog_name=get_app_name())
@click.option('--test', help='For test.', hidden=True, is_flag=True, default=False, is_eager=True)
@click.option('--conf', default=None, help='Specify config path.', type=click.STRING, required=False)
@click.option('--template', default=None, help='Specify template path.', type=click.STRING, required=False)
def cli(ctx, test, conf, template):
    """Automatically generate change log from your tags."""
    if 'test' not in ctx.obj:
        ctx.obj = Config(test, conf, template)


cli.add_command(cli_changelog)
cli.add_command(cli_settings)

if __name__ == '__main__':
    cli(obj={})
