from travelperk_http_python.builder.builder import build
from pathlib import Path


def _get_api_key():
    try:
        return (
            Path(Path.home() / ".travelperk" / "credentials")
            .read_text()
            .replace("\n", "")
        )
    except Exception:
        pass


def _get_if_sandbox():
    # TODO: This should go on the config file
    return False


def get_backend():
    return build(_get_api_key(), _get_if_sandbox())
