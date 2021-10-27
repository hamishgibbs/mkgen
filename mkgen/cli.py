import click
from mkgen.config import write_config, default_config


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        # put main() execution here
        print("main()")


@click.command()
def init():
    write_config(default_config)


cli.add_command(init)
