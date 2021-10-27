import json
import os

import click

from mkgen.config import default_config
from mkgen.main import main


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        main()


@click.command()
def init():
    try:
        with open(os.getcwd() + "/mkgen.json", "w") as f:
            json.dump(default_config, f)
    except Exception:
        Exception("Unable to write mkgen.json file.")


# TODO: Generate a default makefile when starting a project or append
#  annotations to an existing file init can decide if a makefile is in
# the directory - if yes, append annotations, else write a new Makefile
# with default contents.


cli.add_command(init)
