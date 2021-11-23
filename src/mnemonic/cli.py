import click

from mnemonic import Mnemonic


@click.group()
def cli() -> None:
    pass


@cli.command()
@click.option(
    "-l",
    "--language",
    default="english",
    type=str,
    help="",
)
@click.option(
    "-s",
    "--strength",
    default=128,
    type=int,
    help="",
)
@click.option("-p", "--passphrase", default="", type=str, help="")
def create(
    language: str,
    passphrase: str,
    strength: int,
) -> None:
    """ """
    mnemo = Mnemonic(language)
    words = mnemo.generate(strength)
    seed = mnemo.to_seed(words, passphrase)
    click.secho("SUCCESS!", fg="green", bold=True)
    click.echo(f"Mnemonic: {words}")
    click.echo(f"Seed: {seed.hex()}")


if __name__ == "__main__":
    cli()
