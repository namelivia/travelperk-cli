import click
from travelperk_cli.travelperk.travelperk import get_backend


@click.group()
def invoice_profiles():
    pass


@click.command()
def all():
    click.echo(get_backend().expenses().invoice_profiles().query().get())


invoice_profiles.add_command(all)
