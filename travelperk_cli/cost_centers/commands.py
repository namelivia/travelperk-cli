import click
from travelperk_cli.travelperk.travelperk import get_backend


@click.group()
def cost_centers():
    pass


@click.command()
def all():
    click.echo(get_backend().cost_centers().cost_centers().all())


cost_centers.add_command(all)


@click.command()
@click.option("--id", help="The id for the cost center.", required=True)
def get(id):
    click.echo(get_backend().cost_centers().cost_centers().get(id))


cost_centers.add_command(get)


@click.command()
@click.option("--name", help="The name for the cost center.", required=True)
def create(name):
    click.echo(get_backend().cost_centers().cost_centers().create(name))


cost_centers.add_command(create)
