import click
import json
from travelperk_cli.travelperk.travelperk import get_backend
from travelperk_http_python.exceptions.travelperk_http_exception import (
    TravelPerkHttpException,
)
from pydantic.json import pydantic_encoder


@click.group()
def trips():
    pass


@click.command()
def all():
    try:
        click.echo(
            json.dumps(
                get_backend().trips().trips().query().get(),
                default=pydantic_encoder,
            )
        )
    except TravelPerkHttpException as e:
        click.echo(click.style(str(e), fg="red"))


trips.add_command(all)


@click.command()
def bookings():
    try:
        click.echo(
            json.dumps(
                get_backend().trips().bookings().query().get(),
                default=pydantic_encoder,
            )
        )
    except TravelPerkHttpException as e:
        click.echo(click.style(str(e), fg="red"))


trips.add_command(bookings)
