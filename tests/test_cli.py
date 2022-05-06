import unittest

from click.testing import CliRunner

from yeison_todo import cli


class TestYeisonTODOCLI(unittest.TestCase):

    def setUp(self):
        self.runner = CliRunner(mix_stderr=False)

    def test_command_line_interface(self):
        runner = CliRunner()
        result = runner.invoke(cli.cli)
        assert result.exit_code == 0
        assert 'Usage:' in result.output

        help_result = runner.invoke(cli.cli, ['--help'])
        assert help_result.exit_code == 0
        assert '--help' in help_result.output