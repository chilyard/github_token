import os
import re


class GithubToken():

  GITHUB_TOKEN = ""

  def __init__(self):
    print("in GithubToken.init")

  def set_environment_var(self):
    user_input = input('set GITHUB_TOKEN: ')
    os.environ['GITHUB_TOKEN'] = user_input

  def check_environment_var(self):
    gt = os.getenv('GITHUB_TOKEN')
    #gtre = re.search("^[a-z0-9]{39,42}", gt)
    if gt:
      return gt
    else:
      print("GITHUB_TOKEN environment var is unset")
      return


