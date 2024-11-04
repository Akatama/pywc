import locale

import click


@click.command()
@click.version_option()
@click.argument("filename", type=click.Path(exists=True))
@click.option(
    "-c", "countBytes", default=False, is_flag=True, help="print the byte counts"
)
@click.option(
    "-l", "countLines", default=False, is_flag=True, help="print the newline counts"
)
@click.option(
    "-w", "countWords", default=False, is_flag=True, help="print the word counts"
)
@click.option(
    "-m", "countChars", default=False, is_flag=True, help="print the character counts"
)
def cli(filename, countBytes, countLines, countWords, countChars):
    """Python version of wc command line tool.\n
    FILENAME is the file to perform wc operations on.
    """
    locale.setlocale(locale.LC_ALL, "")
    numBytes = getByteCount(filename)
    numLines, numWords, numChars = countLinesWordsChars(filename)
    result = ""

    # default case
    if not countBytes and not countLines and not countWords and not countChars:
        click.echo(f"\t{numLines}\t{numWords}\t{numBytes}\t{filename}")
        return

    if countLines:
        result = f"{result}\t{numLines}"
    if countWords:
        result = f"{result}\t{numWords}"
    if countChars:
        result = f"{result}\t{numChars}"
    if countBytes:
        result = f"{result}\t{numBytes}"
    click.echo(f"{result}\t{filename}")


def getByteCount(filename):
    numBytes = 0
    with open(filename, "rb") as f:
        while f.read(1):
            numBytes += 1
    return numBytes


def countLinesWordsChars(filename):
    numLines = 0
    numWords = 0
    numChars = 0
    with open(filename, "r") as f:
        while line := f.readline():
            numLines += 1
            numWords += len(line.split())
            # need to count the newline character
            numChars += len(line) + 1
    return numLines, numWords, numChars