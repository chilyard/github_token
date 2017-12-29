
import unittest
import github_token
import re
import os
from github_token import github_token
from unittest.mock import patch
from unittest.mock import MagicMock


class TestGithubToken(unittest.TestCase):

  def setUp(self):
    self.token = github_token.GithubToken()

  @unittest.skipIf(os.getenv('GITHUB_TOKEN'), "github_token is already set")
  def test_check_environment_variable_is_unset(self):
    gt = self.token.check_environment_var()
    self.assertIsNone(gt)

  @unittest.skipUnless(os.getenv('GITHUB_TOKEN'), "github_token is set, testing")
  def test_check_environment_variable_is_set(self):
    gt = self.token.check_environment_var()
    self.assertTrue(gt)

  #@patch('self.token.set_environment_var()', return_value="01281098102jl1kj1l320alj12o394u1023j")
  def test_set_token_in_env(self):
    self.token.set_environment_var = MagicMock(return_value="01281098102jl1kj1l320alj12o394u1023j")
    self.assertRegex(token, "^[a-z0-9]{39,42}")

  #def test_check_environment_variable_is_set(self):
  #  gt = self.token.check_environment_var()
  #  self.assertTrue(gt)

  def test_get_token_from_user(self):
    pass


if __name__ == '__main__':
  unittest.main()
