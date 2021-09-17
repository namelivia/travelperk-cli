# travelperk-cli
[![tag](https://img.shields.io/github/tag/namelivia/travelperk-cli.svg)](https://github.com/namelivia/travelperk-cli/releases)[![build](https://github.com/namelivia/travelperk-cli/actions/workflows/build.yml/badge.svg)](https://github.com/namelivia/travelperk-cli/actions/workflows/build.yml)[![Lint](https://github.com/namelivia/travelperk-cli/actions/workflows/black.yml/badge.svg)](https://github.com/namelivia/travelperk-cli/actions/workflows/black.yml)

<p align="center">
  <img src="https://user-images.githubusercontent.com/1571416/133829819-5fc4a27d-f943-47d1-86c4-72e66a19f5cc.png" alt="TravelPerk Cli" />
</p>

## Disclaimer

This is in a ver WIP stage and not very usable

## About

This is an unofficial console line tool for acessing the [TravelPerk official Web API](https://developers.travelperk.com). It is designed so you can query and retrieve all data hold on their platform and accessible through the API form the command line.

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
