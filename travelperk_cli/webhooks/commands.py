import click
from travelperk_cli.travelperk.travelperk import get_backend


@click.group()
def webhooks():
    pass


@click.command()
def all():
    click.echo(get_backend().webhooks().webhooks().all())


webhooks.add_command(all)


@click.command()
@click.option("--id", help="The id for the webhook.", required=True)
def get(id):
    click.echo(get_backend().webhooks().webhooks().get(id))


webhooks.add_command(get)


@click.command()
@click.option("--name", help="The name for the webhook.", required=True)
@click.option("--url", help="The url for the webhook.", required=True)
@click.option("--secret", help="The secret for the webhook.", required=True)
def create(name, url, secret):
    click.echo(
        get_backend()
        .webhooks()
        .webhooks()
        .create(name, url, secret, [])  # TODO: Allow events
    )


webhooks.add_command(create)


@click.command()
@click.option("--id", help="The id for the webhook.", required=True)
def delete(id):
    click.echo(get_backend().webhooks().webhooks().delete(id))


webhooks.add_command(delete)


@click.command()
@click.option("--id", help="The id for the webhook.", required=True)
def test(id):
    click.echo(get_backend().webhooks().webhooks().test(id))


webhooks.add_command(test)
