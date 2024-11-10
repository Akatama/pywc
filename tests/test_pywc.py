from click.testing import CliRunner
from pywc.cli import cli


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
    runner = CliRunner()
    result = runner.invoke(cli, input='cat test.txt')
    assert result.exit_code == 0
    # assert result.output == "\t7145\t58164\t342190\n"
    assert result.output == "\t1\t2\t12\n"


def test_bytes():
    runner = CliRunner()
    result = runner.invoke(cli, ["-c", "test.txt"])
    assert result.exit_code == 0
    assert result.output == "\t342190\ttest.txt\n"


def test_bytes_stdin():
    runner = CliRunner()
    result = runner.invoke(cli, ["-c"], input="cat test.txt")
    assert result.exit_code == 0
    assert result.output == "\t12\n"


def test_lines():
    runner = CliRunner()
    result = runner.invoke(cli, ["-l", "test.txt"])
    assert result.exit_code == 0
    assert result.output == "\t7145\ttest.txt\n"


def test_lines_stdin():
    runner = CliRunner()
    result = runner.invoke(cli, ["-l"], input="cat test.txt")
    assert result.exit_code == 0
    assert result.output == "\t1\n"


def test_words():
    runner = CliRunner()
    result = runner.invoke(cli, ["-w", "test.txt"])
    assert result.exit_code == 0
    assert result.output == "\t58164\ttest.txt\n"


def test_words_stdin():
    runner = CliRunner()
    result = runner.invoke(cli, ["-w"], input="cat test.txt")
    assert result.exit_code == 0
    assert result.output == "\t2\n"


def test_characters():
    runner = CliRunner()
    result = runner.invoke(cli, ["-m", "test.txt"])
    assert result.exit_code == 0
    assert result.output == "\t339292\ttest.txt\n"


def test_characters_stdin():
    runner = CliRunner()
    result = runner.invoke(cli, ["-m"], input="cat test.txt")
    assert result.exit_code == 0
    assert result.output == "\t12\n"


def test_all():
    runner = CliRunner()
    result = runner.invoke(cli, ["-clwm", "test.txt"])
    assert result.exit_code == 0
    assert result.output == "\t7145\t58164\t339292\t342190\ttest.txt\n"


def test_all_stdin():
    runner = CliRunner()
    result = runner.invoke(cli, ["-clwm"], input="cat test.txt")
    assert result.exit_code == 0
    assert result.output == "\t1\t2\t12\t12\n"
