import click
from src.config import write_config


@click.group()
def cli():
    pass


@click.command()
def init():
    write_config()


cli.add_command(init)
