import click


@click.group(name='changelog')
def cli_changelog():
    """Generate changelog."""
    pass


@cli_changelog.command()
@click.pass_context
def markdown(ctx):
    """Generate changelog to markdown."""
    print(ctx.obj['test'])


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
