import click
import json
from travelperk_cli.travelperk.travelperk import get_backend
from travelperk_http_python.exceptions.travelperk_http_exception import (
    TravelPerkHttpException,
)
from pydantic.json import pydantic_encoder


@click.group()
def cost_centers():
    pass


@click.command()
def all():
    try:
        click.echo(
            json.dumps(
                get_backend().cost_centers().cost_centers().all(),
                default=pydantic_encoder,
            )
        )
    except TravelPerkHttpException as e:
        click.echo(click.style(str(e), fg="red"))


cost_centers.add_command(all)


@click.command()
@click.option("--id", help="The id for the cost center.", required=True)
def get(id):
    try:
        click.echo(
            json.dumps(
                get_backend().cost_centers().cost_centers().get(id),
                default=pydantic_encoder,
            )
        )
    except TravelPerkHttpException as e:
        click.echo(click.style(str(e), fg="red"))


cost_centers.add_command(get)


@click.command()
@click.option("--name", help="The name for the cost center.", required=True)
def create(name):
    try:
        click.echo(
            json.dumps(
                get_backend().cost_centers().cost_centers().create(name),
                default=pydantic_encoder,
            )
        )
    except TravelPerkHttpException as e:
        click.echo(click.style(str(e), fg="red"))


cost_centers.add_command(create)
