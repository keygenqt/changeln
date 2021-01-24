from unittest import TestCase

from click.testing import CliRunner

from ..__main__ import cli

runner = CliRunner()


class Test(TestCase):
    # test output
    def test_hello(self):
        result = runner.invoke(cli, ['run', 'hello'], obj={'test': True})
        self.assertEqual(result.exit_code, 0)
        self.assertEqual('True', str(result.output).strip())
