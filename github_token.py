import os


class GithubToken():

  GITHUB_TOKEN = ""

  def __init__(self):
    print("in GithubToken.init") 

  def set_token(self):
    print("in set_token")
    #get user input
    # set os.environ['GITHUB_TOKEN']

  def check_environment_var(self):
    gt = os.getenv('GITHUB_TOKEN')
    if not gt:
      return
    else:
      return gt

  def user_input(self):
    pass


