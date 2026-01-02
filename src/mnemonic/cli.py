import sys

import click

from mnemonic import Mnemonic


@click.group()
def cli() -> None:
    """BIP-39 mnemonic phrase generator and validator."""
    pass


@cli.command()
@click.option(
    "-l",
    "--language",
    default="english",
    type=str,
    help="Language for the mnemonic wordlist.",
)
@click.option(
    "-s",
    "--strength",
    default=128,
    type=int,
    help="Entropy strength in bits (128, 160, 192, 224, or 256).",
)
@click.option(
    "-p",
    "--passphrase",
    default="",
    type=str,
    help="Optional passphrase for seed derivation.",
)
def create(
    language: str,
    passphrase: str,
    strength: int,
) -> None:
    """Generate a new mnemonic phrase and its derived seed."""
    mnemo = Mnemonic(language)
    words = mnemo.generate(strength)
    seed = mnemo.to_seed(words, passphrase)
    click.echo(f"Mnemonic: {words}")
    click.echo(f"Seed: {seed.hex()}")


@cli.command()
@click.option(
    "-l",
    "--language",
    default=None,
    type=str,
    help="Language for the mnemonic wordlist. Auto-detected if not specified.",
)
@click.argument("words", nargs=-1)
def check(language: str | None, words: tuple[str, ...]) -> None:
    """Validate a mnemonic phrase's checksum.

    WORDS can be provided as arguments or piped via stdin.
    """
    if words:
        mnemonic = " ".join(words)
    else:
        mnemonic = sys.stdin.read().strip()

    if not mnemonic:
        click.secho("Error: No mnemonic provided.", fg="red", err=True)
        sys.exit(1)

    try:
        if language is None:
            language = Mnemonic.detect_language(mnemonic)
        mnemo = Mnemonic(language)
        if mnemo.check(mnemonic):
            click.secho("Valid mnemonic.", fg="green")
            sys.exit(0)
        else:
            click.secho("Invalid mnemonic checksum.", fg="red", err=True)
            sys.exit(1)
    except Exception as e:
        click.secho(f"Error: {e}", fg="red", err=True)
        sys.exit(1)


@cli.command("to-seed")
@click.option(
    "-p",
    "--passphrase",
    default="",
    type=str,
    help="Optional passphrase for seed derivation.",
)
@click.argument("words", nargs=-1)
def to_seed(passphrase: str, words: tuple[str, ...]) -> None:
    """Derive a seed from a mnemonic phrase.

    WORDS can be provided as arguments or piped via stdin.
    Outputs the 64-byte seed in hexadecimal format.
    """
    if words:
        mnemonic = " ".join(words)
    else:
        mnemonic = sys.stdin.read().strip()

    if not mnemonic:
        click.secho("Error: No mnemonic provided.", fg="red", err=True)
        sys.exit(1)

    seed = Mnemonic.to_seed(mnemonic, passphrase)
    click.echo(seed.hex())


if __name__ == "__main__":
    cli()
