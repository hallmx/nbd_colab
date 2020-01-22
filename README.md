# Welcome to nbd_colab
> nbd_colab is a thin wrapper around the nbdev library to facilitate the use of nbdev with Google Colab and Google Drive.  


## Install

`pip install nbd_colab`

## Overview

nbdev is a system for exploratory programming using Jupyter notebooks aimed at helping python developers practice truely literate programming. Ideally nbdev is used along with a python/linux environment on a local machine, but many machine learning and deep learning practitioners use GPUs via cloud providers, one of the most popular of which is Google Colaboratory. 

nbdev can work perfectly well with Colaboratory but their are a few quirks and twists to getting the nbdev programming system integrating smoothly with Colab abd Google Drive and this is where nbd_colab comes in. 

This module provides some useful tools for setting up nbdev with Google Colab and Drive and some helpful documentation for developers to get the most out of nbdev with Colab. 

## How to use nbd_colab

Normally, when developing on a local machine we would program in a Jupyter notebook and manage the project on the command line. While there is no command line as such when using Colab, we can still access the operating system and use the command line from Jupyter cells using the os module or  ! and % prefixes. 

Thus, is is entirely possible to manage an nbdev project from within the notebook you are using for development, but this can become confusing and cumbersome quite quickly. An alternative approach is to set up a Colab notebook outside of the project repo to act exclusively as the 'command line'. This notebook is not part of the project itself and instead is used for running tests, for Github and nbdev integration, making Pypi releases and anything else you would normally use the command line for during project development. 

To create a project management notebook,  the following assumes you are are logged in to Google Colaboratory and have access to Google Drive.

*   Create a new python 3 Jupyter notebook in Colab.
*   Install nbd_colab ```!pip install nbd-colab```
*   Import nbd_dev ```from nbd_colab import *```. This will also import nbdev and fastcore for unit testing
*   Connect to Google Drive ```drive_setup()```.
*   Make sure the new notebook is saved separately from other projects or repos on Google drive

You are now set up to manage an nbdev project from this project management notebook. But first you need to create one! 

## Create a new project

First, follow the nbdev tutorial https://nbdev.fast.ai/tutorial/ to generate a new Github repository from the nbdev template repo https://github.com/fastai/nbdev_template/generate (you must be logged in to your Github account for this to work) and edit the settings.init file of the new repository as instructed. 

If your project needs to install other libraries add these to the requirements line in settings.init.

Then, from within your project management notebook (see above) clone the github repo to a location on Google Drive.

```clone_new_repo()```

Follow the instructions and enter the required details when prompted. The repo wil be cloned to the users home directory on Google Drive, usually '/content/drive/My Drive',  by default. 

After successful cloning, the new local repo is automatically configured for integration with the remote repo and ```nbdev_git_hooks``` is installed (gives smoother Github integration by cleaning up notebook metadata before pushes). 

NB. Github authentication credentials are required to allow automatic authentication when authentication is required by github (i.e. for git pushes). This is because Colab has no facility for prompting users for authentication details from within Colab notebooks. To enable automatic authentication, username and passwords are stored, unencrypted, in the local repo on Google Drive (in the .git/config file). Thus users must be careful NOT to share the local repo to avoid exposing their Github password. 



Swap into the newly created repo with:

```change_dir('path-to-repo')``` or ```%cd path-to-repo```

and check cloning was successful by printing out the contents of the settings.init file

```! cat settings.init```

From here follow the instructions in the nbdev docs/tutorial (https://nbdev.fast.ai/tutorial/) to make an initial build of the project library and documentation. In short, run ```!nbdev_bulld_lib``` then ```!nb_build_docs``` from the project management notebook.



## Navigating your project

Change directory to your Googel Drive/Colab home directory '/content/drive/My Drive'

`home_dir()`


Change directory to ```path```

```change_dir(path)```


## Add a new Colab notebook to your project

It is good practice to bundle related functions and classes together in a separate notebook, which then forms the basis of a importable module.

Create a new python 3 notebook in Colab and name it according to the nbdev convention of incremental numbering followed by an underscore and a name describing its contents. For example, if this is the third notebook added to the project, and it contains syncing functions and code a conforming name might be '03_sync.ipynb'. 

The new notebook may not be created in the project repo on google drive. If not, locate it in the default location where new notebooks are created (commonly the 'Colab Notebooks' folder in /My Drive), then right click the notebook and select 'move'. Use the pop up box to move it to the right location in the project repo. 

Then add and run the following code snippets in seperate cells in order to set up the notebook for nbdev integration.

In the first cell add:

```# default_exp <module>```

Where <module> is the name of the .py file that the notebook will create. IN the case of the 03_sync.ipynb notebook, the module name should be 'sync'. Submodules can be specified with <module.submodule'.

Add autoreload functionality to any changes in one notebook module are automatically updated in linked module notebooks:

```
#hide
%load_ext autoreload
%autoreload 2
```

Then code to connect your Colab instance to Google Drive:
```
# hide
from google.colab import drive
drive.mount('/content/drive')
```

Required installs. Fastcore is required for running tests from nbdev.
```
# hide
!pip install nbdev
!pip install fastcore
```

Import modules:
```
#export
import os
from nbdev import *
from nbdev.showdoc import *
```

Add the in-notebook export cell. Running this cell exports modules directly from the notebook (without having to go to the command line). The nbdev docs suggest adding it as the final cell in the notebook.
```
#hide
from nbdev.export import notebook2script
notebook2script()
```

Finally, cd into the root directoryof your ```repo``` on Google Drive ```cd /content/drive/My drive/repo``` and your ready to code your project.

## Managing your project

In the project management notebook, change directory to the local repo root directory on Google Drive. 

```change_dir('path-to-repo')```  or  ```% cd path-to-repo```

From here, all nbdev and github commands work as expected.

Build the library, build the docs and run tests with ```!nbdev_build_lib```, ```!nbdev_build_docs```, and ```nbdev_test_nbs```. See the nbdev docs and tutorial for all available commands. 

Push to github with  ```!git.status```, ```!git add -A```, ```!git commit -am "message"```, and ```!git push```. The full range of Github commands (prefixed by !) will work normally.

Publish to pypi by following the instructions in the nbdev tutorial https://nbdev.fast.ai/tutorial/. Creating a _pypirc file must be done manually but ```!pip install twine``` and ```!make release``` work normally from any Colab notebook with nbdev installed. 




## Quirks and tips for using nbdev system with Colab and Google Drive



*   To use nbdev/Github/pypi functionality it is necessary to ```!cd``` into the local project repo on Google Drive

*   There is no facility in Google Colab to edit text files so editing text files (suchj as for example 'settings.init' or '__init__.py' etc) requires either linking a text editor to your Google Drive or simply downloading the text file from Google drive to your local machine, editing it locally with your text editor of choice, then re-uploading it to Google Drive when done. Same named files will overide previous versions when uploaded.

*   ```show_doc(class.method)``` doesn't give the expected notebook output due (I think) to Colab's limited interactivity. However, it works fine when the documentation is built with ```!nbdev_build_docs``` so do continue use it as instructed in the nbdev docs/tutorial.

*   Exceptions (errors)  during execution of nbdev commands in a Colab notebook, often result in a runtime reset and a return to the Google drive root diectory '/content'. Check the current directory after exceptions with ```!pwd``` and cd back to the repo if needed. 

*   Running ```!nbdev_test_nbs``` runs tests on all notebooks in the project. As well as passing specific tests, project notebooks must also be able to run from start to finish independently to pass. For example, if a notebook contains code to connect to Google Drive (e.g. ```drive.mount("/content/drive")```,  but is not connected to Google Drive at the time of the test, it will fail because notebook execution will stall at this point pending user input. 

*   Notebook cells relying on installs specifically within the Colab environment will cause Github tests to fail during a github push. The push and githubpages build still works fine, but the push is marked as failed with a red cross. A common culprit is ```from google.colab import drive```. Comment this out if you want the github tests to succeed during a push

*   There must be others - I'll add to the list as I become aware of them!

