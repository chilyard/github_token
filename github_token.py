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
    return os.getenv(GITHUB_TOKEN, None)


  def user_input(self):
    pass


