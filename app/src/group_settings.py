import click


@click.group(name='settings')
def cli_settings():
    """Run sample."""
    pass


@cli_settings.command()
@click.pass_context
def project_add(ctx):
    """Add a project."""
    print(ctx.obj['test'])

@cli_settings.command()
@click.pass_context
def project_del(ctx):
    """Del a project."""
    print(ctx.obj['test'])

@cli_settings.command()
@click.pass_context
def project_list(ctx):
    """Show added projects list."""
    print(ctx.obj['test'])

@cli_settings.command()
@click.pass_context
def info(ctx):
    """Application Setting Information."""
    print(ctx.obj['test'])
