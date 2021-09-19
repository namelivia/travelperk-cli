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
                get_backend().scim().users().query().get(),
                default=pydantic_encoder,
            )
        )
    except TravelPerkHttpException as e:
        click.echo(click.style(str(e), fg="red"))


users.add_command(all)


@click.command()
@click.option("--id", help="The id for the user.", required=True)
def get(id):
    try:
        click.echo(
            json.dumps(
                get_backend().scim().users().get(id),
                default=pydantic_encoder,
            )
        )
    except TravelPerkHttpException as e:
        click.echo(click.style(str(e), fg="red"))


users.add_command(get)


@click.command()
@click.option("--id", help="The id for the user.", required=True)
def delete(id):
    try:
        click.echo(
            json.dumps(
                get_backend().scim().users().delete(id),
                default=pydantic_encoder,
            )
        )
    except TravelPerkHttpException as e:
        click.echo(click.style(str(e), fg="red"))


users.add_command(delete)
