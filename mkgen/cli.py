import json
import os

import click

from mkgen.config import default_config
from mkgen.main import main

makefile_annotations = [
    "# -- mkgen targets start --\n",
    "# -- mkgen targets end --\n"
]

default_makefile_lines = [
    "# Update these depending on your system configuration"
    "R = /usr/local/bin/Rscript",
    "PYTHON = /usr/local/bin/python",
    "",
] + makefile_annotations


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

    if os.path.isfile(os.getcwd() + "/Makefile"):

        try:
            with open(os.getcwd() + "/Makefile", "r") as f:
                makefile_lines = f.readlines()
        except Exception:
            Exception("Unable to open existing Makefile.")

        makefile_lines = makefile_lines + makefile_annotations

        try:
            with open(os.getcwd() + "/Makefile", "w") as f:
                [f.write(x) for x in makefile_lines]
        except Exception:
            Exception("Unable to update existing Makefile.")
    else:

        try:
            with open(os.getcwd() + "/Makefile", "w") as f:
                [f.write(x) for x in default_makefile_lines]
        except Exception:
            Exception("Unable to create a new Makefile.")



# TODO: Generate a default makefile when starting a project or append
#  annotations to an existing file init can decide if a makefile is in
# the directory - if yes, append annotations, else write a new Makefile
# with default contents.


cli.add_command(init)
