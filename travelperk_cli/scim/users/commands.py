import click
from travelperk_cli.travelperk.travelperk import get_backend


@click.group()
def users():
    pass


@click.command()
def all():
    click.echo(get_backend().scim().users().query().get())


users.add_command(all)


@click.command()
@click.option("--id", help="The id for the user.", required=True)
def get(id):
    click.echo(get_backend().scim().users().get(id))


users.add_command(get)


@click.command()
@click.option("--id", help="The id for the user.", required=True)
def delete(id):
    click.echo(get_backend().scim().users().delete(id))


users.add_command(delete)
