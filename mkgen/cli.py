import os
import click
import json
from mkgen.config import default_config


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        # put main() execution here
        print("main()")


@click.command()
def init():
    try:
        with open(os.getcwd() + "/mkgen.json", "w") as f:
            json.dump(default_config, f)
    except Exception:
        Exception("Unable to write mkgen.json file.")


cli.add_command(init)
