#!/usr/bin/env python3
from pathlib import Path
from setuptools import setup

CWD = Path(__file__).resolve().parent
EXTRA_REQUIREMENTS = {"cli": ["click"], "dev": ["black", "flake8", "isort"]}

setup(
    name="mnemonic",
    version="0.20",
    author="Trezor",
    author_email="info@trezor.io",
    description="Implementation of Bitcoin BIP-0039",
    long_description=(CWD / "README.rst").read_text(),
    long_description_content_type="text/x-rst",
    url="https://github.com/trezor/python-mnemonic",
    packages=["mnemonic"],
    package_dir={"mnemonic": "src/mnemonic"},
    package_data={"mnemonic": ["mnemonic/wordlist/*.txt"]},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.5",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "Programming Language :: Python :: 3",
    ],
)
