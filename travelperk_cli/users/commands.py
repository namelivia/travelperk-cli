import click
import json
from travelperk_cli.travelperk.travelperk import get_backend
from travelperk_http_python.exceptions.travelperk_http_exception import (
    TravelPerkHttpException,
)
from pydantic.json import pydantic_encoder


@click.group()
def users():
    pass


@click.command()
def all():
    try:
        click.echo(
            json.dumps(
                get_backend().users().users().query().get(),
                default=pydantic_encoder,
            )
        )
    except TravelPerkHttpException as e:
        click.echo(click.style(str(e), fg="red"))


users.add_command(all)
