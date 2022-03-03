import click
import json
from travelperk_cli.travelperk.travelperk import get_backend
from travelperk_http_python.exceptions.travelperk_http_exception import (
    TravelPerkHttpException,
)
from pydantic.json import pydantic_encoder


@click.group()
def greenperk():
    pass


@click.command()
@click.option("--origin", help="The location code for the origin.", required=True)
@click.option(
    "--destination", help="The location code for the destination.", required=True
)
@click.option("--cabin_class", help="The cabin class for the flight", required=True)
@click.option(
    "--airline_code",
    help="The code of the airline for the flight",
    required=True,
)
def flight_emissions(origin, destination, cabin_class, airline_code):
    try:
        click.echo(
            json.dumps(
                get_backend()
                .greenperk()
                .greenperk()
                .flight_emissions(origin, destination, cabin_class, airline_code),
                default=pydantic_encoder,
            )
        )
    except TravelPerkHttpException as e:
        click.echo(click.style(str(e), fg="red"))


greenperk.add_command(flight_emissions)


@click.command()
@click.option("--origin_id", help="The id for the origin train station.", required=True)
@click.option(
    "--destination_id", help="The id for the destination train station.", required=True
)
@click.option("--vendor", help="Vendor for the train.", required=False)
def train_emissions(origin_id, destination_id, vendor):
    try:
        click.echo(
            json.dumps(
                get_backend()
                .greenperk()
                .greenperk()
                .train_emissions(origin_id, destination_id, vendor),
                default=pydantic_encoder,
            )
        )
    except TravelPerkHttpException as e:
        click.echo(click.style(str(e), fg="red"))


greenperk.add_command(train_emissions)


@click.command()
@click.option(
    "--acriss_code", help="The acriss code for the car rental.", required=True
)
@click.option(
    "--num_days", help="The duration in the days for the rental.", required=True
)
@click.option("--distance_per_day", help="The distance per day.", required=False)
def car_emissions(acriss_code, num_days, distance_per_day):
    try:
        click.echo(
            json.dumps(
                get_backend()
                .greenperk()
                .greenperk()
                .car_emissions(acriss_code, num_days, distance_per_day),
                default=pydantic_encoder,
            )
        )
    except TravelPerkHttpException as e:
        click.echo(click.style(str(e), fg="red"))


greenperk.add_command(car_emissions)


@click.command()
@click.option("--country_code", help="The country code for the hotel.", required=True)
@click.option(
    "--num_nights", help="The duration in nights for the stay.", required=True
)
def hotel_emissions(country_code, num_nights):
    try:
        click.echo(
            json.dumps(
                get_backend()
                .greenperk()
                .greenperk()
                .hotel_emissions(country_code, num_nights),
                default=pydantic_encoder,
            )
        )
    except TravelPerkHttpException as e:
        click.echo(click.style(str(e), fg="red"))


greenperk.add_command(hotel_emissions)
