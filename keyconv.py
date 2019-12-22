#!/usr/bin/env python3

"""
Convert ssh keys to DER format required by
HP Comware 5.
"""

import subprocess
import binascii
import textwrap
import argparse


def parse_args():
    """Parse commandline arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument("keyfile")

    return parser.parse_args()


def convert_der(keyfile):
    """
    Convert an ssh key stored in a keyfile
    to DER encoding.
    """
    ssh_keygen = subprocess.Popen((
        "ssh-keygen", "-f", keyfile,
        "-e", "-m", "PKCS8"), stdout=subprocess.PIPE)
    result = subprocess.check_output((
        "openssl", "pkey", "-pubin", "-outform", "DER"),
        stdin=ssh_keygen.stdout)

    return result


def format_key(key):
    """Format key and wrap after 74 chars."""
    return "\n".join(
        textwrap.wrap(
            str(binascii.hexlify(key), "utf-8").upper(),
            width=74)) + "\n"


def cli_main():
    """Convert the ssh key provided as file"""
    args = parse_args()
    key = convert_der(args.keyfile)
    print(format_key(key))


if __name__ == "__main__":
    """Convert a key"""
    cli_main()

