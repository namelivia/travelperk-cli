import click

from travelperk_cli.scim.discovery.commands import discovery
from travelperk_cli.scim.users.commands import users


@click.group()
def scim():
    pass


scim.add_command(discovery)
scim.add_command(users)
