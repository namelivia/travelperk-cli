import click
from travelperk_cli.travelperk.travelperk import get_backend


@click.group()
def invoices():
    pass


@click.command()
def all():
    click.echo(get_backend().expenses().invoices().query().get())


invoices.add_command(all)


@click.command()
@click.option("--id", help="The id for the webhook.", required=True)
def get(id):
    click.echo(get_backend().expenses().invoices().get(id))


invoices.add_command(get)


@click.command()
def lines():
    click.echo(get_backend().expenses().invoices().lines_query().get())


invoices.add_command(lines)
