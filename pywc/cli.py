import locale

import click

from collections import namedtuple

import os

FileMetadata = namedtuple("FileMetadata", ["numBytes", "numLines", "numWords", "numChars", "knownFilename"])


@click.command()
@click.version_option()
@click.argument("filename", type=click.Path(), required=False)
@click.option("-c", "countBytes", default=False, is_flag=True, help="print the byte counts")
@click.option("-l", "countLines", default=False, is_flag=True, help="print the newline counts")
@click.option("-w", "countWords", default=False, is_flag=True, help="print the word counts")
@click.option("-m", "countChars", default=False, is_flag=True, help="print the character counts")
def cli(filename, countBytes, countLines, countWords, countChars):
    """Python version of wc command line tool.\n
    FILENAME is the file to perform wc operations on.
    """
    locale.setlocale(locale.LC_ALL, "")
    data = handleFile(filename)
    result = ""

    # default case
    if not countBytes and not countLines and not countWords and not countChars:
        result = f"\t{data.numLines}\t{data.numWords}\t{data.numBytes}"

    if countLines:
        result = f"{result}\t{data.numLines}"
    if countWords:
        result = f"{result}\t{data.numWords}"
    if countChars:
        result = f"{result}\t{data.numChars}"
    if countBytes:
        result = f"{result}\t{data.numBytes}"
    if data.knownFilename:
        click.echo(f"{result}\t{filename}")
    else:
        click.echo(f"{result}")


def getByteCount():
    numBytes = 0
    with click.open_file("-", "rb") as f:
        while f.read(1):
            numBytes += 1
    return numBytes


def getFileMetadataFromFilename(filename):
    numBytes = os.path.getsize(filename)
    numLines = 0
    numWords = 0
    numChars = 0
    with click.open_file(filename, "r") as f:
        while line := f.readline():
            numLines += 1
            numWords += len(line.split())
            # need to count the newline character
            numChars += len(line) + 1
    return FileMetadata(numBytes, numLines, numWords, numChars, True)


def getFileMetadataFromStdin():
    numBytes = 0
    numLines = 0
    numWords = 0
    numChars = 0
    with click.open_file("-", "r") as f:
        click.echo(f.read())
        while line := f.readline():
            click.echo(f"{line}")
            numLines += 1
            numWords += len(line.split())
            # need to count the newline character
            numChars += len(line)
            lineBytes = line.encode()
            numBytes += len(lineBytes)
    return FileMetadata(numBytes, numLines, numWords, numChars, False)


def handleFile(filename):
    # read from STDIN
    if filename is None:
        return getFileMetadataFromStdin()
    else:
        return getFileMetadataFromFilename(filename)
