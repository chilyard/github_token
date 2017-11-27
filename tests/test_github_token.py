
import github_token
import unittest



class TestGithubToken(unittest.TestCase):

  def test_get_token(self):
    token = github_token.GithubToken()
    self.assertTrue(token.get_token()) 



if __name__ == '__main__':
  unittest.main()
