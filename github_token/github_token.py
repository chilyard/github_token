import os


class GithubToken():

  GITHUB_TOKEN = ""

  def __init__(self):
    print("in GithubToken.init")

  def set_environment_var(self):
    user_input = input('set GITHUB_TOKEN: ')
    os.environ['GITHUB_TOKEN'] = user_input

  def check_environment_var(self):
    gt = os.getenv('GITHUB_TOKEN')
    if not gt:
      return
    else:
      print("GITHUB_TOKEN environment var is unset")
      return gt

  def user_input(self):
    pass


