import click

from changeln.src.features.group_make import group_make
from changeln.src.support.conf import Conf, OutType
from changeln.src.support.dependency import check_dependency_init

check_dependency_init()


@click.group(invoke_without_command=True)
@click.version_option(version=Conf.get_app_version(), prog_name=Conf.get_app_name())
@click.option(
    '--conf',
    default=None,
    help='Specify config path.',
    type=click.STRING,
    required=False)
@click.option(
    '--out',
    default=str(OutType.markdown),
    type=click.Choice([str(OutType.markdown), str(OutType.html), str(OutType.pdf)], case_sensitive=False),
    help='Type format output.')
@click.pass_context
def main(ctx: {}, conf: str, out: str):
    ctx.obj = Conf(conf)
    group_make(ctx, out)


if __name__ == '__main__':
    main(obj={})
