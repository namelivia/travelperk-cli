import click

from travelperk_cli.cost_centers.commands import cost_centers
from travelperk_cli.trips.commands import trips
from travelperk_cli.users.commands import users
from travelperk_cli.webhooks.commands import webhooks
from travelperk_cli.travelsafe.commands import travelsafe
from travelperk_cli.scim.commands import scim
from travelperk_cli.expenses.commands import expenses


@click.group()
def cli():
    pass


cli.add_command(trips)
cli.add_command(webhooks)
cli.add_command(cost_centers)
cli.add_command(users)
cli.add_command(travelsafe)
cli.add_command(scim)
cli.add_command(expenses)

if __name__ == "__main__":
    cli()
