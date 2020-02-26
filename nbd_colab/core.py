# AUTOGENERATED! DO NOT EDIT! File to edit: 00_core.ipynb (unless otherwise specified).

__all__ = ['drive_setup', 'clone_new_repo', 'change_dir', 'home_dir']

# Cell
#test_flag_imports
import os
from google.colab import drive
from nbdev import *
from nbdev.showdoc import *
from pathlib import Path
from getpass import getpass
import urllib
from subprocess import Popen, PIPE

# Cell
def drive_setup():
  "Connect the current Colab instance to the users Google Drive"
  drive.mount('/content/drive', force_remount=True)

# Cell
class _StopExecution(Exception):
    "Gracefully stop cell execution"
    def _render_traceback_(self):
        pass

# Cell
def _run_subprocess(cmd):
  "Run a subprocess and return success (0) or error (!0)"
  process = Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  return process.returncode

# Cell
def _check_input(type, input):
  "Utility function to check user input and raises a _stopExecution exception if invalid"
  if input == "":
    print(f'Error: {type} required ')
    raise _StopExecution
  else: return input

def _get_dest_dir():
  "Prompts the user to input the destination folder for the cloned repo and checks it exists"

  # set home directory
  home_dir = "/content/drive/My Drive"

  dir = input(f'Destination directory {home_dir}/')
  dest_dir = home_dir+"/"+dir
  dir_exists = os.path.isdir(dest_dir)
  if dir_exists:
    return dest_dir
  else:
    print(f"Error: Destination directory {dest_dir} does not exist\n")
    raise _StopExecution

def _get_repo(dir):
  "prompts the user to enter the repo name and checks it doesn't already exist"
  repo = _check_input('repository name', input('Repo name: '))
  repo_path = dir+"/"+repo
  path_exists = os.path.exists(repo_path)
  if path_exists:
    print(f"Error: file/folder {repo} already exists at destination {dir}. Function can only be used to create new repo\n")
    raise _StopExecution
  else:
     return repo

# Cell
def clone_new_repo():
  "Clone nbdev template repo from github to google drive and configure"

  print('  Important Information:\n\
  nbd_dev does not store user details but users Github username and password are stored in the cloned\n\
  repository on Google Drive to allow automatic authentication from Colaboratory notebooks.Take care\n\
  therefore, NOT to share the cloned repository with anyone as this risks exposing user credentials.\n')

  dest_dir = _get_dest_dir()
  repo = _get_repo(dest_dir)
  user = _check_input('Username', input('Username: '))
  user_email = _check_input('User email', input('User email: '))
  password = getpass('Password: ')

  # converts password into url format
  password = urllib.parse.quote(password)

  confirm = input('Confirm and clone y/n?')
  if confirm == 'y':
    #cd to destination target directory
    change_dir(dest_dir)

    # clone the repo
    cmd_string = f'git clone https://{user}:{password}@github.com/{user}/{repo}.git'
    ret = _run_subprocess(cmd_string)
    # purge password containing variables straight away
    cmd_string, password = None, None
    #raise exception if error
    assert ret, 'Error: Clone failed. Please review entries and try again. User details purged'

    # check new repo exists and raise exception if not
    repo_exists = os.path.exists(dest_dir+"/"+repo)
    assert repo_exists, 'Error: Clone failed. Please review entries and try again. User details purged'

    # if clone exists continue
    print(f'{repo} successfully cloned into {dest_dir}')

    # cd into new repo
    change_dir(dest_dir+"/"+repo)

    # save user email and username into local git repo to identify user to git
    ret = _run_subprocess(f'git config user.name {user}')
    ret += -run_subprocess(f'git config user.email {user_email}')
    if ret:
     print(f'Git configuration failed. Please manually configure the local repo with username and email\n{e}')

    # install git hooks to automatically clean up notebook metadata
    ret = _run_subprocess('nbdev_install_git_hooks')
    if not ret:
      msg = 'nbdev git hooks successfully installed'
    else:
      msg = f'Failed to install git hooks. Try manually installing with !nbdev_install_git_hooks\n{e}'
    print(msg)

  else:
    cmd_string, password = None, None
    print('Clone cancelled\n')
    raise _StopExecution

  return None

# Cell
def change_dir(path):
  "Change directory to 'path'"
  p = Path(path)
  os.chdir(p)

# Cell
def home_dir():
  "Change directory to the users home directory on Google Drive '/content/drive/My Drive'"
  home_dir = "/content/drive/My Drive"
  p = Path(home_dir)
  os.chdir(p)