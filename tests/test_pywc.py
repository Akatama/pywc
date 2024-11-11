from click.testing import CliRunner
from pywc.cli import cli, FileMetadata, _getFileMetadataFromFilename, _handleFile
import locale


def test_version():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ["--version"])
        assert result.exit_code == 0
        assert result.output.startswith("cli, version ")


def test_default():
    runner = CliRunner()
    result = runner.invoke(cli, ["test.txt"])
    assert result.exit_code == 0
    assert result.output == "\t7145\t58164\t342190\ttest.txt\n"


def test_default_stdin():
    locale.setlocale(locale.LC_ALL, "")
    runner = CliRunner()
    with open("test.txt", "r") as f:
        file = f.read()
        result = runner.invoke(cli, input=f"{file}")
        assert result.exit_code == 0
        assert result.output == "\t7145\t58164\t335045\n"
        # assert result.output == "\t1\t2\t12\n"


def test_bytes():
    runner = CliRunner()
    result = runner.invoke(cli, ["-c", "test.txt"])
    assert result.exit_code == 0
    assert result.output == "\t342190\ttest.txt\n"


def test_bytes_stdin():
    locale.setlocale(locale.LC_ALL, "")
    runner = CliRunner()
    with open("test.txt", "r") as f:
        file = f.read()
        result = runner.invoke(cli, ["-c"], input=file)
        assert result.exit_code == 0
        assert result.output == "\t335045\n"


def test_lines():
    runner = CliRunner()
    result = runner.invoke(cli, ["-l", "test.txt"])
    assert result.exit_code == 0
    assert result.output == "\t7145\ttest.txt\n"


def test_lines_stdin():
    runner = CliRunner()
    with open("test.txt", "r") as f:
        file = f.read()
        result = runner.invoke(cli, ["-l"], input=file)
        assert result.exit_code == 0
        assert result.output == "\t7145\n"


def test_words():
    runner = CliRunner()
    result = runner.invoke(cli, ["-w", "test.txt"])
    assert result.exit_code == 0
    assert result.output == "\t58164\ttest.txt\n"


def test_words_stdin():
    runner = CliRunner()
    with open("test.txt", "r") as f:
        file = f.read()
        result = runner.invoke(cli, ["-w"], input=file)
        assert result.exit_code == 0
        assert result.output == "\t58164\n"


def test_characters():
    runner = CliRunner()
    result = runner.invoke(cli, ["-m", "test.txt"])
    assert result.exit_code == 0
    assert result.output == "\t339292\ttest.txt\n"


def test_characters_stdin():
    runner = CliRunner()
    locale.setlocale(locale.LC_ALL, "")
    with open("test.txt", "r") as f:
        file = f.read()
        result = runner.invoke(cli, ["-m"], input=file)
        assert result.exit_code == 0
        assert result.output == "\t332147\n"


def test_all():
    runner = CliRunner()
    result = runner.invoke(cli, ["-clwm", "test.txt"])
    assert result.exit_code == 0
    assert result.output == "\t7145\t58164\t339292\t342190\ttest.txt\n"


def test_all_stdin():
    runner = CliRunner()
    locale.setlocale(locale.LC_ALL, "")
    with open("test.txt", "r") as f:
        file = f.read()
        result = runner.invoke(cli, ["-clwm"], input=file)
        assert result.exit_code == 0
        assert result.output == "\t7145\t58164\t332147\t335045\n"


def test_getFileMetadataFromFilename():
    fileMetadataExpected = FileMetadata(342190, 7145, 58164, 339292, True)
    fileMetadataActual = _getFileMetadataFromFilename("test.txt")
    assert fileMetadataActual == fileMetadataExpected


def test_handleFile():
    fileMetadataExpected = FileMetadata(342190, 7145, 58164, 339292, True)
    fileMetadataActual = _handleFile("test.txt")
    assert fileMetadataActual == fileMetadataExpected
