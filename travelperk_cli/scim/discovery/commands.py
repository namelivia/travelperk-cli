import click
from travelperk_cli.travelperk.travelperk import get_backend


@click.group()
def discovery():
    pass


@click.command()
def service_provider_configuration():
    click.echo(get_backend().scim().discovery().service_provider_config())


discovery.add_command(service_provider_configuration)


@click.command()
def resource_types():
    click.echo(get_backend().scim().discovery().resource_types())


discovery.add_command(resource_types)


@click.command()
def schemas():
    click.echo(get_backend().scim().discovery().schemas())


discovery.add_command(schemas)


@click.command()
def user_schema():
    click.echo(get_backend().scim().discovery().user_schema())


discovery.add_command(user_schema)


@click.command()
def enterprise_schema():
    click.echo(get_backend().scim().discovery().enterprise_user_schema())


discovery.add_command(enterprise_schema)
