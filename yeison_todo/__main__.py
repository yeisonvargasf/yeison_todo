"""Allow yeison_todo to be executable through `python -m yeison_todo`."""
from __future__ import absolute_import

from .cli import cli


if __name__ == "__main__":  # pragma: no cover
    cli(prog_name="yeison_todo")
