import click
from travelperk_cli.travelperk.travelperk import get_backend
from travelperk_http_python.exceptions.travelperk_http_exception import (
    TravelPerkHttpException,
)


@click.group()
def discovery():
    pass


@click.command()
def service_provider_configuration():
    try:
        click.echo(get_backend().scim().discovery().service_provider_config())
    except TravelPerkHttpException as e:
        click.echo(click.style(str(e), fg="red"))


discovery.add_command(service_provider_configuration)


@click.command()
def resource_types():
    try:
        click.echo(get_backend().scim().discovery().resource_types())
    except TravelPerkHttpException as e:
        click.echo(click.style(str(e), fg="red"))


discovery.add_command(resource_types)


@click.command()
def schemas():
    try:
        click.echo(get_backend().scim().discovery().schemas())
    except TravelPerkHttpException as e:
        click.echo(click.style(str(e), fg="red"))


discovery.add_command(schemas)


@click.command()
def user_schema():
    try:
        click.echo(get_backend().scim().discovery().user_schema())
    except TravelPerkHttpException as e:
        click.echo(click.style(str(e), fg="red"))


discovery.add_command(user_schema)


@click.command()
def enterprise_schema():
    try:
        click.echo(get_backend().scim().discovery().enterprise_user_schema())
    except TravelPerkHttpException as e:
        click.echo(click.style(str(e), fg="red"))


discovery.add_command(enterprise_schema)
