
import unittest
import github_token
from github_token import github_token


class TestGithubToken(unittest.TestCase):

  def setUp(self):
    self.token = github_token.GithubToken()

  def test_check_environment_variable(self):
    self.assertIsNone(self.token.check_environment_var())

  def test_set_token_in_env(self):
    self.assertIsNotNone(self.token.set_environment_var())
    token = self.token.check_environment_var()
    self.assertRegex(token, "^[a-z0-9]{39,42}")


if __name__ == '__main__':
  unittest.main()
