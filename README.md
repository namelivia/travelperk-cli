# travelperk-cli [![tag](https://img.shields.io/github/tag/namelivia/travelperk-cli.svg)](https://github.com/namelivia/travelperk-cli/releases) [![build](https://github.com/namelivia/travelperk-cli/actions/workflows/build.yml/badge.svg)](https://github.com/namelivia/travelperk-cli/actions/workflows/build.yml) [![codecov](https://codecov.io/gh/namelivia/travelperk-cli/branch/main/graph/badge.svg?token=vslGEYGDfV)](https://codecov.io/gh/namelivia/travelperk-cli) [![Lint](https://github.com/namelivia/travelperk-cli/actions/workflows/black.yml/badge.svg)](https://github.com/namelivia/travelperk-cli/actions/workflows/black.yml)

<p align="center">
  <img src="https://user-images.githubusercontent.com/1571416/133829819-5fc4a27d-f943-47d1-86c4-72e66a19f5cc.png" alt="TravelPerk Cli" />
</p>

## Disclaimer

This is in a ver WIP stage and not very usable

## About

This is an unofficial command line tool for acessing the [TravelPerk official Web API](https://developers.travelperk.com). It is designed so you can query and retrieve all data hold on their platform and accessible through the API form the command line.

## Operations included

### Expenses

#### Invoices

 - List all invoices :heavy_check_mark:
 - Retrieve an invoice :heavy_check_mark:
 - Retrieve invoice PDF :heavy_multiplication_x:
 - List all invoice lines :heavy_check_mark:

#### Invoice Profiles
 - List all invoice profiles :heavy_check_mark:

### SCIM
 - List users :heavy_check_mark:
 - Create a new user :heavy_multiplication_x:
 - Retrieve a user :heavy_check_mark:
 - Replace a user :heavy_multiplication_x:
 - Delete a user :heavy_check_mark:

#### Discovery
 - Service provider configuration :heavy_check_mark:
 - List resource types :heavy_check_mark:
 - List all schemas :heavy_check_mark:
 - User schema details :heavy_check_mark:
 - Enterprise user schema details :heavy_check_mark:

### Webhooks
 - List all webhooks :heavy_check_mark:
 - Create a webhook :heavy_check_mark:
 - Retrieve a webhook :heavy_check_mark:
 - Update a webhook :heavy_multiplication_x:
 - Test a webhook :heavy_check_mark:
 - Delete a webhook :heavy_check_mark:

### TravelSafe
 - Get travel restrictions :heavy_check_mark:
 - Get local summary :heavy_check_mark:
 - Get airline safety measures :heavy_check_mark:
 - Get location types :heavy_check_mark:

### Cost Centers
 - List cost centers :heavy_check_mark:
 - Creating a cost center :heavy_check_mark:
 - Cost center details :heavy_check_mark:
 - Update a cost center :heavy_multiplication_x:
 - Bulk update cost centers :heavy_multiplication_x:
 - Set users to a cost center :heavy_multiplication_x:
 
### Trips
 - List trips :heavy_check_mark:
 - List bookings :heavy_check_mark:

### Users (non SCIM)
 - List users :heavy_check_mark:

## Getting started

Before getting started retrieving querying information from the TravelPerk Web API you first need to [get an API Key](https://developers.travelperk.com/reference#authentication).
Then put your API key on the following path: `~/.travelperk/credentials`

### Retrieving data

Everything is ready, you can start asking for the data.
```python
pipenv run python cli.py scim discovery enterprise-schema
```

## License

[MIT](LICENSE)

## Contributing
Any suggestion, bug reports, prs or any other kind enhacements are welcome. Just [open an issue first](https://github.com/namelivia/travelperk-cli/issues/new), for creating a PR remember this project has linting checkings and unit tests so any PR should comply with both before beign merged, this checks will be automatically applied when opening or modifying the PRs.

## Local development

This project comes with a `docker-compose.yml` file so if you use Docker and docker-compose you can develop without installing anything on your local environment. Just run `docker-compose up --build` for the first time to setup the container and launch the tests. Pytest is configured as the entrypoint so just run `docker-compose up` everytime you want the tests to execute on the Dockerized Python development container.
