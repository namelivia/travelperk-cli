from click.testing import CliRunner
from cli import cli
from mock import Mock, patch
from travelperk_http_python.api.travelperk import TravelPerk
from travelperk_cli.travelperk.travelperk import get_backend


class TestCli:
    def setup(self):
        self.runner = CliRunner()
        self.travelperk = Mock(spec=TravelPerk)

    @patch("travelperk_cli.travelperk.travelperk.build")
    def test_testing_a_backend_instance(self, build_mock):
        build_mock.return_value = self.travelperk
        backend = get_backend()
        assert backend == self.travelperk
        # TODO
        # asserting the function parameters

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

    @patch("travelperk_cli.cost_centers.commands.get_backend")
    def test_listing_all_cost_centers(self, get_backend_mock):
        get_backend_mock.return_value = self.travelperk
        self.travelperk.cost_centers.return_value.cost_centers.return_value.all.return_value = (
            "All cost centers list"
        )
        result = self.runner.invoke(cli, ["cost-centers", "all"])
        assert result.exit_code == 0
        assert "All cost centers list" in result.output

    @patch("travelperk_cli.cost_centers.commands.get_backend")
    def test_getting_details_of_a_cost_center(self, get_backend_mock):
        get_backend_mock.return_value = self.travelperk
        self.travelperk.cost_centers.return_value.cost_centers.return_value.get.return_value = (
            "Cost center details"
        )
        cost_center_id = "some_id"
        result = self.runner.invoke(
            cli, ["cost-centers", "get", "--id", cost_center_id]
        )
        assert result.exit_code == 0
        assert "Cost center details" in result.output
        # TODO
        # asserting the function was called with the id

    @patch("travelperk_cli.cost_centers.commands.get_backend")
    def test_creating_a_cost_center(self, get_backend_mock):
        get_backend_mock.return_value = self.travelperk
        self.travelperk.cost_centers.return_value.cost_centers.return_value.create.return_value = (
            "New cost center"
        )
        cost_center_name = "new_cost_center"
        result = self.runner.invoke(
            cli, ["cost-centers", "create", "--name", cost_center_name]
        )
        assert result.exit_code == 0
        assert "New cost center" in result.output
        # TODO
        # asserting the function was called with the id

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

    @patch("travelperk_cli.expenses.invoice_profiles.commands.get_backend")
    def test_listing_all_invoice_profiles(self, get_backend_mock):
        get_backend_mock.return_value = self.travelperk
        self.travelperk.expenses.return_value.invoice_profiles.return_value.query.return_value.get.return_value = (
            "All invoice profiles list"
        )
        result = self.runner.invoke(cli, ["expenses", "invoice-profiles", "all"])
        assert result.exit_code == 0
        assert "All invoice profiles list" in result.output

    # Invoices
    def test_listing_invoices_operations(self):
        result = self.runner.invoke(cli, ["expenses", "invoices"])
        assert result.exit_code == 0
        assert "all" in result.output
        assert "get" in result.output
        assert "lines" in result.output

    @patch("travelperk_cli.expenses.invoices.commands.get_backend")
    def test_listing_all_invoices(self, get_backend_mock):
        get_backend_mock.return_value = self.travelperk
        self.travelperk.expenses.return_value.invoices.return_value.query.return_value.get.return_value = (
            "All invoices list"
        )
        result = self.runner.invoke(cli, ["expenses", "invoices", "all"])
        assert result.exit_code == 0
        assert "All invoices list" in result.output

    @patch("travelperk_cli.expenses.invoices.commands.get_backend")
    def test_getting_details_of_an_invoice(self, get_backend_mock):
        get_backend_mock.return_value = self.travelperk
        self.travelperk.expenses.return_value.invoices.return_value.get.return_value = (
            "Invoice details"
        )
        invoice_id = "some_id"
        result = self.runner.invoke(
            cli, ["expenses", "invoices", "get", "--id", invoice_id]
        )
        assert result.exit_code == 0
        assert "Invoice details" in result.output
        # TODO
        # asserting the function was called with the id

    @patch("travelperk_cli.expenses.invoices.commands.get_backend")
    def test_listing_all_invoice_lines(self, get_backend_mock):
        get_backend_mock.return_value = self.travelperk
        self.travelperk.expenses.return_value.invoices.return_value.lines_query.return_value.get.return_value = (
            "All invoice lines list"
        )
        result = self.runner.invoke(cli, ["expenses", "invoices", "lines"])
        assert result.exit_code == 0
        assert "All invoice lines list" in result.output

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

    @patch("travelperk_cli.scim.users.commands.get_backend")
    def test_listing_all_users_scim(self, get_backend_mock):
        get_backend_mock.return_value = self.travelperk
        self.travelperk.scim.return_value.users.return_value.query.return_value.get.return_value = (
            "All users list"
        )
        result = self.runner.invoke(cli, ["scim", "users", "all"])
        assert result.exit_code == 0
        assert "All users list" in result.output

    @patch("travelperk_cli.scim.users.commands.get_backend")
    def test_getting_details_of_a_user(self, get_backend_mock):
        get_backend_mock.return_value = self.travelperk
        self.travelperk.scim.return_value.users.return_value.get.return_value = (
            "Details of a user"
        )
        user_id = "some_id"
        result = self.runner.invoke(cli, ["scim", "users", "get", "--id", user_id])
        assert result.exit_code == 0
        assert "Details of a user" in result.output
        # TODO
        # asserting the function was called with the id

    @patch("travelperk_cli.scim.users.commands.get_backend")
    def test_deleting_a_user(self, get_backend_mock):
        get_backend_mock.return_value = self.travelperk
        self.travelperk.scim.return_value.users.return_value.delete.return_value = (
            "Delete user response"
        )
        user_id = "some_id"
        result = self.runner.invoke(cli, ["scim", "users", "delete", "--id", user_id])
        assert result.exit_code == 0
        assert "Delete user response" in result.output
        # TODO
        # asserting the function was called with the id

    # Discovery
    def test_listing_discovery_operations(self):
        result = self.runner.invoke(cli, ["scim", "discovery"])
        assert result.exit_code == 0
        assert "service-provider-configuration" in result.output
        assert "resource-types" in result.output
        assert "schemas" in result.output
        assert "user-schema" in result.output
        assert "enterprise-schema" in result.output

    @patch("travelperk_cli.scim.discovery.commands.get_backend")
    def test_getting_service_provider_configuration(self, get_backend_mock):
        get_backend_mock.return_value = self.travelperk
        self.travelperk.scim.return_value.discovery.return_value.service_provider_config.return_value = (
            "Service provider configuration"
        )
        result = self.runner.invoke(
            cli, ["scim", "discovery", "service-provider-configuration"]
        )
        assert result.exit_code == 0
        assert "Service provider configuration" in result.output

    @patch("travelperk_cli.scim.discovery.commands.get_backend")
    def test_getting_resource_types(self, get_backend_mock):
        get_backend_mock.return_value = self.travelperk
        self.travelperk.scim.return_value.discovery.return_value.resource_types.return_value = (
            "Resource types"
        )
        result = self.runner.invoke(cli, ["scim", "discovery", "resource-types"])
        assert result.exit_code == 0
        assert "Resource types" in result.output

    @patch("travelperk_cli.scim.discovery.commands.get_backend")
    def test_getting_schemas(self, get_backend_mock):
        get_backend_mock.return_value = self.travelperk
        self.travelperk.scim.return_value.discovery.return_value.schemas.return_value = (
            "List of schemas"
        )
        result = self.runner.invoke(cli, ["scim", "discovery", "schemas"])
        assert result.exit_code == 0
        assert "List of schemas" in result.output

    @patch("travelperk_cli.scim.discovery.commands.get_backend")
    def test_getting_user_schema(self, get_backend_mock):
        get_backend_mock.return_value = self.travelperk
        self.travelperk.scim.return_value.discovery.return_value.user_schema.return_value = (
            "User schema"
        )
        result = self.runner.invoke(cli, ["scim", "discovery", "user-schema"])
        assert result.exit_code == 0
        assert "User schema" in result.output

    @patch("travelperk_cli.scim.discovery.commands.get_backend")
    def test_getting_enterprise_schema(self, get_backend_mock):
        get_backend_mock.return_value = self.travelperk
        self.travelperk.scim.return_value.discovery.return_value.enterprise_user_schema.return_value = (
            "Enterprise schema"
        )
        result = self.runner.invoke(cli, ["scim", "discovery", "enterprise-schema"])
        assert result.exit_code == 0
        assert "Enterprise schema" in result.output

    # TravelSafe
    def test_listing_travelsafe_operations(self):
        result = self.runner.invoke(cli, ["travelsafe"])
        assert result.exit_code == 0
        assert "restrictions" in result.output
        assert "local-summary" in result.output
        assert "airline-measures" in result.output

    @patch("travelperk_cli.travelsafe.commands.get_backend")
    def test_getting_restrictions(self, get_backend_mock):
        get_backend_mock.return_value = self.travelperk
        self.travelperk.travelsafe.return_value.travelsafe.return_value.travel_restrictions.return_value = (
            "Travel restrictions"
        )
        result = self.runner.invoke(
            cli,
            [
                "travelsafe",
                "restrictions",
                "--origin",
                "FR",
                "--origin-type",
                "country_code",
                "--destination",
                "ES",
                "--destination-type",
                "country_code",
                "--date",
                "2020-05-02",
            ],
        )
        assert result.exit_code == 0
        assert "Travel restrictions" in result.output
        # TODO
        # asserting the function was called with the id

    @patch("travelperk_cli.travelsafe.commands.get_backend")
    def test_getting_local_summary(self, get_backend_mock):
        get_backend_mock.return_value = self.travelperk
        self.travelperk.travelsafe.return_value.travelsafe.return_value.local_summary.return_value = (
            "Local Summary"
        )
        result = self.runner.invoke(
            cli,
            [
                "travelsafe",
                "local-summary",
                "--location",
                "FR",
                "--location-type",
                "country_code",
            ],
        )
        assert result.exit_code == 0
        assert "Local Summary" in result.output
        # TODO
        # asserting the function was called with the id

    @patch("travelperk_cli.travelsafe.commands.get_backend")
    def test_getting_airline_measures(self, get_backend_mock):
        get_backend_mock.return_value = self.travelperk
        self.travelperk.travelsafe.return_value.travelsafe.return_value.airline_safety_measures.return_value = (
            "Airline Measures"
        )
        result = self.runner.invoke(
            cli,
            [
                "travelsafe",
                "airline-measures",
                "--code",
                "LH",
            ],
        )
        assert result.exit_code == 0
        assert "Airline Measures" in result.output
        # TODO
        # asserting the function was called with the id

    # Trips
    def test_listing_trips_operations(self):
        result = self.runner.invoke(cli, ["trips"])
        assert result.exit_code == 0
        assert "all" in result.output
        assert "bookings" in result.output

    @patch("travelperk_cli.trips.commands.get_backend")
    def test_listing_all_trips(self, get_backend_mock):
        get_backend_mock.return_value = self.travelperk
        self.travelperk.trips.return_value.trips.return_value.query.return_value.get.return_value = (
            "All trips list"
        )
        result = self.runner.invoke(cli, ["trips", "all"])
        assert result.exit_code == 0
        assert "All trips list" in result.output

    @patch("travelperk_cli.trips.commands.get_backend")
    def test_listing_all_bookings(self, get_backend_mock):
        get_backend_mock.return_value = self.travelperk
        self.travelperk.trips.return_value.bookings.return_value.query.return_value.get.return_value = (
            "All bookings list"
        )
        result = self.runner.invoke(cli, ["trips", "bookings"])
        assert result.exit_code == 0
        assert "All bookings list" in result.output

    # Users
    def test_listing_users_operations(self):
        result = self.runner.invoke(cli, ["users"])
        assert result.exit_code == 0
        assert "all" in result.output

    @patch("travelperk_cli.users.commands.get_backend")
    def test_listing_all_users(self, get_backend_mock):
        get_backend_mock.return_value = self.travelperk
        self.travelperk.users.return_value.users.return_value.query.return_value.get.return_value = (
            "All users list"
        )
        result = self.runner.invoke(cli, ["users", "all"])
        assert result.exit_code == 0
        assert "All users list" in result.output

    # Webhooks
    def test_listing_webhook_operations(self):
        result = self.runner.invoke(cli, ["webhooks"])
        assert result.exit_code == 0
        assert "all" in result.output
        assert "get" in result.output
        assert "create" in result.output
        assert "delete" in result.output
        assert "test" in result.output

    @patch("travelperk_cli.webhooks.commands.get_backend")
    def test_listing_all_webhooks(self, get_backend_mock):
        get_backend_mock.return_value = self.travelperk
        self.travelperk.webhooks.return_value.webhooks.return_value.all.return_value = (
            "All webhooks list"
        )
        result = self.runner.invoke(cli, ["webhooks", "all"])
        assert result.exit_code == 0
        assert "All webhooks list" in result.output

    @patch("travelperk_cli.webhooks.commands.get_backend")
    def test_getting_details_of_a_webhook(self, get_backend_mock):
        get_backend_mock.return_value = self.travelperk
        self.travelperk.webhooks.return_value.webhooks.return_value.get.return_value = (
            "Details of a webhook"
        )
        webhook_id = "some_id"
        result = self.runner.invoke(cli, ["webhooks", "get", "--id", webhook_id])
        assert result.exit_code == 0
        assert "Details of a webhook" in result.output
        # TODO
        # asserting the function was called with the id

    @patch("travelperk_cli.webhooks.commands.get_backend")
    def test_deleting_a_webhook(self, get_backend_mock):
        get_backend_mock.return_value = self.travelperk
        self.travelperk.webhooks.return_value.webhooks.return_value.delete.return_value = (
            "Delete webhook response"
        )
        webhook_id = "some_id"
        result = self.runner.invoke(cli, ["webhooks", "delete", "--id", webhook_id])
        assert result.exit_code == 0
        assert "Delete webhook response" in result.output
        # TODO
        # asserting the function was called with the id

    @patch("travelperk_cli.webhooks.commands.get_backend")
    def test_creating_a_webhook(self, get_backend_mock):
        get_backend_mock.return_value = self.travelperk
        self.travelperk.webhooks.return_value.webhooks.return_value.create.return_value = (
            "New webhook"
        )
        result = self.runner.invoke(
            cli,
            [
                "webhooks",
                "create",
                "--name",
                "Some name",
                "--url",
                "Some url",
                "--secret",
                "Some secret",
            ],
        )
        assert result.exit_code == 0
        assert "New webhook" in result.output
        # TODO
        # asserting the function was called with the id

    @patch("travelperk_cli.webhooks.commands.get_backend")
    def test_testing_a_webhook(self, get_backend_mock):
        get_backend_mock.return_value = self.travelperk
        self.travelperk.webhooks.return_value.webhooks.return_value.test.return_value = (
            "Testing webhook response"
        )
        webhook_id = "some_id"
        result = self.runner.invoke(cli, ["webhooks", "test", "--id", webhook_id])
        assert result.exit_code == 0
        assert "Testing webhook response" in result.output
        # TODO
        # asserting the function was called with the id
