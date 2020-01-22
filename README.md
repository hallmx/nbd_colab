# Welcome to nbd_colab
> nbd_colab is a thin wrapper around the nbdev library to facilitate the use of nbdev with Google Colab and Google Drive.  


## Install

`pip install nbd_colab`

## Overview

Nbdev is a system for exploratory programming using Jupyter notebooks developed by Jeremy Howard and Sylvian Gugger of fastai fame. It is aimed at helping python developers practice literate programming. 

Ideally nbdev is used from within a python/linux environment on a local machine,but many machine learning and deep learning practitioners use Google Colaboratory (Colab)  to develop and run their projects taking advantage of Colab's free GPUs and TPUs.

While nbdev works perfectly well with Colab there are a few quirks and twists to getting the nbdev programming system integrating smoothly with Colab and Google Drive and this is where nbd_colab comes in. This module provides some useful tools for setting up nbdev with Google Colab and Google Drive together with additional documentation for developers to get the most out of using nbdev with Google Colab. 

Use of this module assumes the user is familiar with nbdev programming system, github, Google Colaboratory and Google Drive. Full nbdev documentation and excellent tutorial is at https://nbdev.fast.ai/.

## Approach to using nbdev with Colaboratory's Jupyter notebooks

Normally, when developing using Jupyter we would write project code in a notebook and manage the project from the command line. With Colab as our development environment, we don't have a command line as such, but we can make system calls from notebook cells using the os module and ! or % prefixes.

It is, therefore,  quite possible to manage an nbdev project entirely from within your development notebooks, but having code for two different purposes - project code and command line code - in the same notebook quickly becomes cumbersome and confusing. An alternative approach is to set up a Colab notebook outside of the project directory to be used exclusively for command line tasks. Such a project management notebook, separate from the project itself, is used for running tests, for Github and nbdev integration, making Pypi releases and anything else you would normally use the command line

## Create a project management notebook.

To create a project management notebook that can use nbdev and nbd_colab follow the instructions below. The following assumes you are are logged in to Google Colaboratory and have access to Google Drive.

1.  Create a new python 3 Jupyter notebook from Google Colaboratory.
2.  Install nbd_colab. This will also install nbdev and fastcore. Fastcore is required to run tests.
```
!pip install nbd-colab
```
3.  Import os, nbd_colab and nbdev as a minimum. Imports further modules as the need arises
```
from nbd_colab import *
from nbdev import *
``` 
4.  Connect to Google Drive 
```
drive_setup()
```
5.  Make sure the new notebook is saved separate from other projects or repos on Google drive

You are now set up to manage an nbdev project. But first you need to create one! 

## Create a new project

First, follow the nbdev tutorial https://nbdev.fast.ai/tutorial/ to generate a new Github repository from the nbdev template repo https://github.com/fastai/nbdev_template/generate (you must be logged in to your Github account for this to work) and edit the settings.ini file of the new repository as instructed. 

If your project needs to install other libraries add these to the requirements line in settings.ini.

Then, from within your project management notebook (see above) clone the remote Github repository you have created on Githuib to your Google Drive:

```clone_new_repo()```

Follow the instructions and input the required details at the prompts. The remote repository wil be cloned to the users home directory on Google Drive, usually '/content/drive/My Drive', by default but this can be customized to anywhere on the users Google Drive at the first prompt. 

Successfully cloned repositories are automatically configured for integration with the remote Github repository and git hooks are installed with ```nbdev_git_hooks```. Nbdev git hooks gives smoother Github integration by cleaning up notebook metadata before pushes. 

NB. The users Github username and password are stored (unencrypted) in the cloned repository .git/config file to allow automatic authentication when Colab interacts with Github during git pushes. They need to be stored in advance because Colab has no facility for prompting users for authentication details from within Colab notebooks. This is far from ideal but there appears no way around it and so users must be careful NOT to share the cloned repository folder or files from Google Drive as this risks exposing their Github credentials. 



Swap into the newly cloned repository folder on Google Drive:

```change_dir('path-to-repo')``` or ```%cd path-to-repo```

Check cloning was successful by printing out the contents of the settings.init file

```! cat settings.ini```

From here follow the instructions in the nbdev docs/tutorial (https://nbdev.fast.ai/tutorial/) to make an initial build of the project library and documentation (i.e. run ```!nbdev_bulld_lib``` then ```!nb_build_docs``` from the project management notebook).



## Navigating your project

Change directory to your Google Drive/Colab home directory '/content/drive/My Drive'

`home_dir()`


Change directory to ```path```

```change_dir(path)```


## Adding a new notebook/module to your project

Adding a new Colab notebook to your project repository and configuring it to work wit nbdev is described on the tutorial page in the nbd_colab documentation.

## Managing your project

In the project management notebook, change directory root directory of the project repository on Google Drive. 

```change_dir('path-to-repo')```  or  ```% cd path-to-repo```

From here, all nbdev and Github commands should work as expected on the project:

*    Build the library, build the docs and run tests with ```!nbdev_build_lib```, ```!nbdev_build_docs```, and ```nbdev_test_nbs```. See the nbdev docs and tutorial for all available commands. 

*    Push to github with  ```!git.status```, ```!git add -A```, ```!git commit -am "message"```, and ```!git push```. All other Github commands (prefixed by !) should also work normally.

*    Publish to pypi by following the instructions in the nbdev tutorial https://nbdev.fast.ai/tutorial/. Creating a _pypirc file i the user's home directory must be done manually but ```!pip install twine``` and ```!make release``` work normally from Colab notebooks with nbdev installed. 




## Quirks and tips for using nbdev with Colab and Google Drive



*   To use nbdev/Github/pypi functionality it is necessary to ```%cd``` into the project repository on Google Drive. 

*   Use ```%cd``` for changing directory but ```!cmd``` for other command line actions.

*   Google Colab can't edit text files so editing text files (for example 'settings.init' or '__init__.py') requires either linking a text editor to your Google Drive or simply downloading the text file from the project reposotory on Google Drive to your local machine, editing it there with your chosen text editor, followed by re-uploading it when done.

*   ```show_doc(class.method)``` doesn't give the expected notebook output in Colab notebook cells. However, it works fine when the documentation is built with ```!nbdev_build_docs``` so do continue to use it as per the nbdev docs/tutorial (https://nbdev.fast.ai/) 

*   Exceptions (errors) arising during execution of command line actions from Colab notebooks, sometimes results in a runtime reset and return to the Google drive root diectory '/content'. Check the current directory after exceptions with ```!pwd``` and cd back to the repo if needed to continue working. 

*   Running ```!nbdev_test_nbs``` runs tests on all notebooks in the project. As well as passing all specific tests, project notebooks must also be able to run from start to finish independently to pass. For example, if a notebook contains code to connect to Google Drive (e.g. ```drive.mount("/content/drive")```,  but is not connected to Google Drive at the time of the test, it may fail because notebook execution will stall at this point pending user input. 

*   Notebook cells relying on installs specifically within the Colab environment will cause Github tests to fail during git push. The push to the re,lot erepository and building the documenation on Githubpages will still proceed, but the push is marked as a fail with a red cross because of the failed tests. A common culprit is ```from google.colab import drive```. Comment this out if you want the Github tests to succeed during a push

*   There are probably others. I'll add to the list as I become aware of them!


## Copyright


Copyright 2020 onwards, Mathew Hall, Licensed under the Apache License, Version 2.0 (the "License"); you may not use this project's files except in compliance with the License. A copy of the License is provided in the LICENSE file in this repository
