import click

from travelperk_cli.expenses.invoice_profiles.commands import invoice_profiles
from travelperk_cli.expenses.invoices.commands import invoices


@click.group()
def expenses():
    pass


expenses.add_command(invoice_profiles)
expenses.add_command(invoices)
