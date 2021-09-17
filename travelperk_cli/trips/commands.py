import click
from travelperk_cli.travelperk.travelperk import get_backend


@click.group()
def trips():
    pass


@click.command()
def all():
    click.echo(get_backend().trips().trips().query().get())


trips.add_command(all)


@click.command()
def bookings():
    click.echo(get_backend().trips().bookings().query().get())


trips.add_command(bookings)
