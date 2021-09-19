import click
import json
from travelperk_cli.travelperk.travelperk import get_backend
from travelperk_http_python.exceptions.travelperk_http_exception import (
    TravelPerkHttpException,
)
from pydantic.json import pydantic_encoder


@click.group()
def webhooks():
    pass


@click.command()
def all():
    try:
        click.echo(
            json.dumps(
                click.echo(get_backend().webhooks().webhooks().all()),
                default=pydantic_encoder,
            )
        )
    except TravelPerkHttpException as e:
        click.echo(click.style(str(e), fg="red"))


webhooks.add_command(all)


@click.command()
@click.option("--id", help="The id for the webhook.", required=True)
def get(id):
    try:
        click.echo(
            json.dumps(
                click.echo(get_backend().webhooks().webhooks().get(id)),
                default=pydantic_encoder,
            )
        )
    except TravelPerkHttpException as e:
        click.echo(click.style(str(e), fg="red"))


webhooks.add_command(get)


@click.command()
@click.option("--name", help="The name for the webhook.", required=True)
@click.option("--url", help="The url for the webhook.", required=True)
@click.option("--secret", help="The secret for the webhook.", required=True)
def create(name, url, secret):
    try:
        click.echo(
            json.dumps(
                get_backend()
                .webhooks()
                .webhooks()
                .create(name, url, secret, ["invoice.issued"]),  # TODO: Allow events
                default=pydantic_encoder,
            )
        )
    except TravelPerkHttpException as e:
        click.echo(click.style(str(e), fg="red"))


webhooks.add_command(create)


@click.command()
@click.option("--id", help="The id for the webhook.", required=True)
def delete(id):
    try:
        click.echo(
            json.dumps(
                click.echo(get_backend().webhooks().webhooks().delete(id)),
                default=pydantic_encoder,
            )
        )
    except TravelPerkHttpException as e:
        click.echo(click.style(str(e), fg="red"))


webhooks.add_command(delete)


@click.command()
@click.option("--id", help="The id for the webhook.", required=True)
def test(id):
    try:
        click.echo(
            click.echo(get_backend().webhooks().webhooks().test(id)),
        )
    except TravelPerkHttpException as e:
        click.echo(click.style(str(e), fg="red"))


webhooks.add_command(test)
