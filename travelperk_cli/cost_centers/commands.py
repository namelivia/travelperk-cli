import click
from travelperk_cli.travelperk.travelperk import get_backend
from travelperk_http_python.exceptions.travelperk_http_exception import (
    TravelPerkHttpException,
)


@click.group()
def cost_centers():
    pass


@click.command()
def all():
    try:
        click.echo(get_backend().cost_centers().cost_centers().all())
    except TravelPerkHttpException as e:
        click.echo(click.style(str(e), fg="red"))


cost_centers.add_command(all)


@click.command()
@click.option("--id", help="The id for the cost center.", required=True)
def get(id):
    try:
        click.echo(get_backend().cost_centers().cost_centers().get(id))
    except TravelPerkHttpException as e:
        click.echo(click.style(str(e), fg="red"))


cost_centers.add_command(get)


@click.command()
@click.option("--name", help="The name for the cost center.", required=True)
def create(name):
    try:
        click.echo(get_backend().cost_centers().cost_centers().create(name))
    except TravelPerkHttpException as e:
        click.echo(click.style(str(e), fg="red"))


cost_centers.add_command(create)
