import click

from app.src.group_run import cli_run


@click.group()
@click.pass_context
@click.option('--test', help='For test', hidden=True, is_flag=True, default=False, is_eager=True)
def cli(ctx, test):
    """Automatically generate change log from your tags."""
    if 'test' not in ctx.obj:
        ctx.obj = {
            'test': test
        }


cli.add_command(cli_run)

if __name__ == '__main__':
    cli(obj={})
