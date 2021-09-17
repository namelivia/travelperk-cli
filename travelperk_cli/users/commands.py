import click
from travelperk_cli.travelperk.travelperk import get_backend


@click.group()
def users():
    pass


@click.command()
def all():
    click.echo(get_backend().users().users().query().get())


users.add_command(all)
