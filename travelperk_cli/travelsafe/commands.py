import click


@click.group()
def travelsafe():
    pass


@click.command()
def restrictions():
    click.echo("Listing travel restrictions")


travelsafe.add_command(restrictions)


@click.command()
def local_summary():
    click.echo("Listing local summary")


travelsafe.add_command(local_summary)


@click.command()
def airline_measures():
    click.echo("Listing airline measures")


travelsafe.add_command(airline_measures)
