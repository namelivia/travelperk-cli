from click.testing import CliRunner
from cli import cli


class TestCli:
    def setup(self):
        self.runner = CliRunner()

    def test_listing_all_sections(self):
        result = self.runner.invoke(cli, [])
        assert result.exit_code == 0
        assert "cost-centers" in result.output
        assert "expenses" in result.output
        assert "scim" in result.output
        assert "travelsafe" in result.output
        assert "trips" in result.output
        assert "users" in result.output
        assert "webhooks" in result.output

    # Cost centers
    def test_listing_cost_center_operations(self):
        result = self.runner.invoke(cli, ["cost-centers"])
        assert result.exit_code == 0
        assert "all" in result.output
        assert "get" in result.output

    def test_listing_all_cost_centers(self):
        result = self.runner.invoke(cli, ["cost-centers", "all"])
        assert result.exit_code == 0
        assert "Listing all cost centers" in result.output

    def test_getting_details_of_a_cost_center(self):
        result = self.runner.invoke(cli, ["cost-centers", "get"])
        assert result.exit_code == 0
        assert "Details of a cost center" in result.output

    # Expenses
    def test_listing_expenses_operations(self):
        result = self.runner.invoke(cli, ["expenses"])
        assert result.exit_code == 0
        assert "invoice-profiles" in result.output
        assert "invoices" in result.output

    # Invoice Profiles
    def test_listing_invoice_profiles_operations(self):
        result = self.runner.invoke(cli, ["expenses", "invoice-profiles"])
        assert result.exit_code == 0
        assert "all" in result.output

    # Invoices
    def test_listing_invoices_operations(self):
        result = self.runner.invoke(cli, ["expenses", "invoices"])
        assert result.exit_code == 0
        assert "all" in result.output
        assert "get" in result.output
        assert "lines" in result.output

    # SCIM
    def test_listing_scim_operations(self):
        result = self.runner.invoke(cli, ["scim"])
        assert result.exit_code == 0
        assert "users" in result.output
        assert "discovery" in result.output

    # Users (SCIM)
    def test_listing_scim_users_operations(self):
        result = self.runner.invoke(cli, ["scim", "users"])
        assert result.exit_code == 0
        assert "all" in result.output
        assert "get" in result.output
        assert "delete" in result.output

    # Discovery
    def test_listing_discovery_operations(self):
        result = self.runner.invoke(cli, ["scim", "discovery"])
        assert result.exit_code == 0
        assert "service-provider-configuration" in result.output
        assert "resource-types" in result.output
        assert "schemas" in result.output
        assert "user-schema" in result.output
        assert "enterprise-schema" in result.output

    # TravelSafe
    def test_listing_travelsafe_operations(self):
        result = self.runner.invoke(cli, ["travelsafe"])
        assert result.exit_code == 0
        assert "restrictions" in result.output
        assert "local-summary" in result.output
        assert "airline-measures" in result.output

    # Trips
    def test_listing_trips_operations(self):
        result = self.runner.invoke(cli, ["trips"])
        assert result.exit_code == 0
        assert "all" in result.output
        assert "bookings" in result.output

    # Users
    def test_listing_users_operations(self):
        result = self.runner.invoke(cli, ["users"])
        assert result.exit_code == 0
        assert "all" in result.output

    # Webhooks
    def test_listing_webhook_operations(self):
        result = self.runner.invoke(cli, ["webhooks"])
        assert result.exit_code == 0
        assert "all" in result.output
        assert "get" in result.output
        assert "create" in result.output
        assert "delete" in result.output
        assert "test" in result.output

    def test_listing_all_webhooks(self):
        result = self.runner.invoke(cli, ["webhooks", "all"])
        assert result.exit_code == 0
        assert "Details of a webhook" in result.output

    def test_getting_details_of_a_webhook(self):
        result = self.runner.invoke(cli, ["webhooks", "get"])
        assert result.exit_code == 0
        assert "Details of a webhook" in result.output

    def test_deleting_a_webhook(self):
        result = self.runner.invoke(cli, ["webhooks", "delete"])
        assert result.exit_code == 0
        assert "Delete a webhook" in result.output

    def test_testing_a_webhook(self):
        result = self.runner.invoke(cli, ["webhooks", "test"])
        assert result.exit_code == 0
        assert "Test a webhook" in result.output
