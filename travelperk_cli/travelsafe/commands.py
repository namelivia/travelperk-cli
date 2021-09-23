import click
import json
from travelperk_cli.travelperk.travelperk import get_backend
from travelperk_http_python.exceptions.travelperk_http_exception import (
    TravelPerkHttpException,
)
from pydantic.json import pydantic_encoder


@click.group()
def travelsafe():
    pass


@click.command()
@click.option("--origin", help="The location code for the origin.", required=True)
@click.option(
    "--origin-type",
    help="The type for the location code for the origin.",
    required=True,
)
@click.option(
    "--destination", help="The location code for the destination.", required=True
)
@click.option(
    "--destination-type",
    help="The type for the location code for the destination.",
    required=True,
)
@click.option(
    "--date",
    help="The date for the travel.",
    type=click.DateTime(formats=["%Y-%m-%d"]),
    required=True,
)
def restrictions(origin, destination, origin_type, destination_type, date):
    try:
        click.echo(
            json.dumps(
                get_backend()
                .travelsafe()
                .travelsafe()
                .travel_restrictions(
                    origin, destination, origin_type, destination_type, date
                ),
                default=pydantic_encoder,
            )
        )
    except TravelPerkHttpException as e:
        click.echo(click.style(str(e), fg="red"))


travelsafe.add_command(restrictions)


@click.command()
@click.option("--location", help="The location code.", required=True)
@click.option("--location-type", help="The type for the location code.", required=True)
def local_summary(location, location_type):
    try:
        click.echo(
            json.dumps(
                get_backend()
                .travelsafe()
                .travelsafe()
                .local_summary(location, location_type),
                default=pydantic_encoder,
            )
        )
    except TravelPerkHttpException as e:
        click.echo(click.style(str(e), fg="red"))


travelsafe.add_command(local_summary)


@click.command()
@click.option("--code", help="The airline code.", required=True)
def airline_measures(code):
    try:
        click.echo(
            json.dumps(
                get_backend().travelsafe().travelsafe().airline_safety_measures(code),
                default=pydantic_encoder,
            )
        )
    except TravelPerkHttpException as e:
        click.echo(click.style(str(e), fg="red"))


travelsafe.add_command(airline_measures)
