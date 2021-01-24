import click


@click.group(name='run')
def cli_run():
    """Run sample."""
    pass


@cli_run.command()
@click.pass_context
def hello(ctx):
    """Show hello world."""
    print(ctx.obj['test'])
