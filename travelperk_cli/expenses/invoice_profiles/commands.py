import click
import json
from travelperk_cli.travelperk.travelperk import get_backend
from travelperk_http_python.exceptions.travelperk_http_exception import (
    TravelPerkHttpException,
)
from pydantic.json import pydantic_encoder


@click.group()
def invoice_profiles():
    pass


@click.command()
def all():
    try:
        click.echo(
            json.dumps(
                get_backend().expenses().invoice_profiles().query().get(),
                default=pydantic_encoder,
            )
        )
    except TravelPerkHttpException as e:
        click.echo(click.style(str(e), fg="red"))


invoice_profiles.add_command(all)
