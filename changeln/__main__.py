from pathlib import Path

import click

from changeln.src.click.group_changelog import cli_changelog
from changeln.src.common.config import Config
from changeln.src.components.helper import get_app_name, get_app_version

Config.init_template()
Config.init_conf()


@click.group()
@click.pass_context
@click.version_option(version=get_app_version(), prog_name=get_app_name())
@click.option('--project', '-p', help='Path to git project for generate changelog.', type=click.STRING, required=True)
@click.option('--test', help='For test.', hidden=True, is_flag=True, default=False, is_eager=True)
@click.option('--conf', '-c', default=None, help='Specify config path.', type=click.STRING, required=False)
@click.option('--template', '-t', default=None, help='Specify template path.', type=click.STRING, required=False)
@click.option('--output', '-o', default=None, help='Output file path.', type=click.STRING, required=False)
def main(ctx, test, conf, template, project, output):
    """Automatically generate change log from your tags."""
    if not Path(project).is_dir():
        click.echo(click.style("\nNot found dir {}.\n".format(project), fg="red"))
        exit(1)
    if not Path('{}/.git'.format(project)).is_dir():
        click.echo(click.style("\nNot found git {}/.git.\n".format(project), fg="red"))
        exit(1)
    if not test:
        ctx.obj = Config(test, conf, template, project, output)


main.add_command(cli_changelog)

if __name__ == '__main__':
    main(obj={})
