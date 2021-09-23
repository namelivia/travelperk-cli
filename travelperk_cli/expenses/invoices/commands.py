import click
import json
from travelperk_cli.travelperk.travelperk import get_backend
from travelperk_http_python.exceptions.travelperk_http_exception import (
    TravelPerkHttpException,
)
from pydantic.json import pydantic_encoder


@click.group()
def invoices():
    pass


@click.command()
def all():
    try:
        click.echo(
            json.dumps(
                get_backend().expenses().invoices().query().get(),
                default=pydantic_encoder,
            )
        )
    except TravelPerkHttpException as e:
        click.echo(click.style(str(e), fg="red"))


invoices.add_command(all)


@click.command()
@click.option("--id", help="The id for the invoice.", required=True)
def get(id):
    try:
        click.echo(
            json.dumps(
                get_backend().expenses().invoices().get(id),
                default=pydantic_encoder,
            )
        )
    except TravelPerkHttpException as e:
        click.echo(click.style(str(e), fg="red"))


invoices.add_command(get)


@click.command()
def lines():
    try:
        click.echo(
            json.dumps(
                get_backend().expenses().invoices().lines_query().get(),
                default=pydantic_encoder,
            )
        )
    except TravelPerkHttpException as e:
        click.echo(click.style(str(e), fg="red"))


invoices.add_command(lines)
