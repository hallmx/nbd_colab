# Welcome to nbd_colab
> nbd_colab is a thin wrapper around the nbdev library to facilitate the use of nbdev with Google Colab and Google Drive.  


## Install

`pip install nbd_colab`

## Overview

Nbdev is a system for exploratory programming using Jupyter notebooks developed by Jeremy Howard and Sylvain Gugger of fastai fame. It is aimed at helping python developers and software engineers practice literate programming. 

Ideally nbdev is used from within a virtual environment on a local machine with hardware acceleration. However, many deep learning practitioners and students use Google Colaboratory (Colab) to develop and run their GPU accelerated code, taking advantage of Colab's integration with Google Drive and it's free GPUs and TPUs.

While nbdev works fine with Colab's Jupyter notebook environment and code editor, a few considerations and customizations are required for the nbdev programming system as a whole to play nicely with Colab and Drive. This module describes an approach to using nbdev with Google Colab and Google Drive, provides some useful tools for setting up a new nbdev GitHub project repository on Google Drive and adds some nbdev-colab specific documentation including troubleshooting advice. 

Use of this module assumes the user is familiar with nbdev programming system, github, Google Colaboratory and Google Drive. Full nbdev documentation and excellent tutorial is at https://nbdev.fast.ai/.

## Approach to using nbdev with Colaboratory's Jupyter notebooks

Commonly, we write project code in a Jupyter notebook and manage the project from the command line. With Colab as our development environment, we don't have a command line as such, allthough we can, of course, make system calls from notebook cells using the os module and the ! or % prefixes.

Thus, it is quite possible to manage an nbdev project entirely from within development notebooks, but having code for two different purposes - project code and command line code - in the same notebook quickly becomes cumbersome and confusing. An alternative approach is to set up a Colab notebook outside of the project directory to use exclusively for executing command line commands and scripts. By making the project directory the current working directory (%cd <path_to_project_directory>) of this separate notebook, any commands and scripts run in the separate notebook will execute in respect to the project directory and files. Such a 'project management notebook' as we will call it, separate from the project itself, is used for running tests, nbdev and GitHub integration, making Pypi releases and anything else you would normally use the command line for in a project.

## Create a project management notebook.

The following assumes you are are logged in to Google Colaboratory and have access to Google Drive.

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
or 
```
from google.colab import drive
drive.mount('/content/drive')
```
5.  Save the notebook separate from other projects and repos on Google drive


You are now set up to manage an nbdev project. But first you need to create one! 

## Create a new project

1.  Follow the nbdev tutorial https://nbdev.fast.ai/tutorial/ to generate a new Github repository from the nbdev template repo https://github.com/fastai/nbdev_template/generate (you must be logged in to your Github account for this to work) and edit the settings.ini file of the new repository as instructed. Don't forget also to set up GitHub Pages for your new repository, selecting the 'master branch/docs folder' option.

2. If your project needs to install other libraries add these, separated by a spaces, to the requirements line in settings.ini.

3. From your project management notebook (created above) clone the new remote GitHub repository to your Google Drive by typing the following code and following the instructions to enter the required information. Successfully cloned repositories are automatically configured for integration with the remote repository and `nbdev_git_hooks` is installed. `Nbdev_git_hooks` gives smoother Github integration by cleaning up notebook metadata before git pushes. 
```
clone_new_repo()
```
> **CAUTION.** The users GitHub username and password are stored (unencrypted) in the cloned repository's `.git/config` file to allow automatic authentication when Colab interacts with GitHub during git pushes. They need to be stored in advance because Colab has no facility for prompting users for authentication details from within Colab notebooks. This is far from ideal but there appears no way around it and so users must be careful NOT to share the cloned repository folder or files from Google Drive as this risks exposing their GitHub credentials. 

4.  Swap into the newly cloned repository on Google Drive.
```
change_dir('path_to_repo') 
```
or
```
 %cd path_to_repo
```
Check cloning was successful by printing out the contents of the settings.ini file
```
! cat settings.ini
```

From here follow the instructions in the nbdev docs/tutorial (https: //nbdev.fast.ai/tutorial/) to make an initial build of the project library and documentation (i.e. run !nbdev_bulld_lib then !nb_build_docs from the project management notebook).

## Navigating your project

Change directory to your Google Drive/Colab home directory '/content/drive/My Drive'

`home_dir()`


Change directory to ```path```

```change_dir(path)```


## Adding a new notebook/module to your project

Adding a new Colab notebook to your project repository and configuring it to work with nbdev is described on the tutorial page in the nbd_colab documentation.

## Brief tour of nbdev project management

In the project management notebook, change directory to the root directory of the project repository on Google Drive ```change_dir('path_to_repo')``` or ```%cd path_to_repo```. From here, all nbdev and Github commands should work as expected on the project:

*    Build the library, build the docs and run tests with ```!nbdev_build_lib```, ```!nbdev_build_docs```, and ```nbdev_test_nbs```. See the nbdev docs and tutorial for all available commands. 

*    Push to github with  ```!git.status```, ```!git add -A```, ```!git commit -am "message"```, and ```!git push```. All other Github commands (prefixed by !) should also work normally.

*    Publish to PyPi by following the instructions in the nbdev tutorial https://nbdev.fast.ai/tutorial/. Creating a _pypirc file in the user's home directory must be done manually with a text editor but ```!pip install twine``` and ```!make release``` work normally from Colab notebooks with nbdev installed. 




## Copyright


Copyright 2020 onwards, Mathew Hall, Licensed under the Apache License, Version 2.0 (the "License"); you may not use this project's files except in compliance with the License. A copy of the License is provided in the LICENSE file in this repository
