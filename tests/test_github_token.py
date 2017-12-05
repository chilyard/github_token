
import unittest
import github_token


class TestGithubToken(unittest.TestCase):

  def setUp(self):
    self.token = github_token.GithubToken()

  def test_get_token(self):
    self.assertIsNone(self.token.get_token())

  #def test_set_token(self):
  #  self.assert


if __name__ == '__main__':
  unittest.main()
