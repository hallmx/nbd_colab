# Welcome to nbd_colab
> nbd_colab is a thin wrapper around the nbdev library to facilitate the use of nbdev with Google Colab and Google Drive.  


## Install

`pip install nbd_colab`

## Overview

Fastai.nbdev is a system for exploratory programming using Jupyter notebooks developed by Jeremy Howard and Sylvian Gugger of fastai. It is aimed at helping python developers practice literate programming. Ideally nbdev is used from within a python/linux environment on a local machine, but many machine learning and deep learning practitioners use Google Colaboratory (Colab)  to develop and run their projects taking advantage of Colab's free GPUs and TPUs.

nbdev works perfectly well with Colab but there are a few quirks and twists to getting the nbdev programming system integrating smoothly with Colab and Google Drive and this is where nbd_colab comes in. This module provides some useful tools for setting up nbdev with Google Colab and Google Drive with additional documentation for developers to get the most out of using nbdev with Colab. 

Read the full nbdev documention and tutorial at https://nbdev.fast.ai/.

## How to use nbd_colab

Normally, when developing using Jupyter notebooks we would write project code in the notebook and manage the project from the command line. Using Colab as our development environment we don't have a command line as such but can of course access the operating system and command line from Jupyter cells using the os module or ! and % prefixes. 

It is therefore entirely possible to manage an nbdev project from within notebooks you are using for development, but having code for two differet purposes - project code and command line code - in the smae notebook can become confusing and cumbersome quite quickly. An alternative approach is to set up a Colab notebook outside of the project directory to act exclusively as the 'command line' and manage the project from there. Such a project managemnt notebook, separate from the project itself, is used for running tests, for Github and nbdev integration, making Pypi releases and anything else you would normally use the command line. 

To create a project management notebook that can use nbd_colab follow the code below. The following assumes you are are logged in to Google Colaboratory and have access to Google Drive.

1.  Create a new python 3 Jupyter notebook in Colab.
2.  Install nbd_colab 
```
!pip install nbd-colab
```
3.  Import nbd_dev. This will also import nbdev and fastcore (for unit testing)
```
from nbd_colab import *
``` 
4.  Connect to Google Drive 
```
drive_setup()
```
5.  Make sure the new notebook is saved separately from other projects or repos on Google drive

You are now set up to manage an nbdev project. But first you need to create one! 

## Create a new project

First, follow the nbdev tutorial https://nbdev.fast.ai/tutorial/ to generate a new Github repository from the nbdev template repo https://github.com/fastai/nbdev_template/generate (you must be logged in to your Github account for this to work) and edit the settings.ini file of the new repository as instructed. 

If your project needs to install other libraries add these to the requirements line in settings.ini.

Then, from within your project management notebook (see above) clone the github repo to a location on Google Drive.

```clone_new_repo()```

Follow the instructions and input the required details when prompted. The repo wil be cloned to the users home directory on Google Drive, usually '/content/drive/My Drive', by default but this can be customized at the promts. 

After successful cloning, the new local repo is automatically configured for integration with the remote repo on Github and ```nbdev_git_hooks``` is installed. Git hooks gives smoother Github integration by cleaning up notebook metadata before git pushes. 

NB. github authentication credentials are required to allow automatic authentication when authentication is required by github (i.e. for git pushes). This is because Colab has no facility for prompting users for authentication details from within Colab notebooks. To enable automatic authentication, nbdev_colab stores username and passwords, unencrypted, in the local repo on Google Drive (in the .git/config file). This is not ideal and users must be careful NOT to share the local repo with anyone to avoid exposing their Github password. 



Swap into the newly created repo with:

```change_dir('path-to-repo')``` or ```%cd path-to-repo```

and check cloning was successful by printing out the contents of the settings.init file

```! cat settings.ini```

From here follow the instructions in the nbdev docs/tutorial (https://nbdev.fast.ai/tutorial/) to make an initial build of the project library and documentation (i.e. run ```!nbdev_bulld_lib``` then ```!nb_build_docs``` from the project management notebook).



## Navigating your project

Change directory to your Googel Drive/Colab home directory '/content/drive/My Drive'

`home_dir()`


Change directory to ```path```

```change_dir(path)```


## Add a new Colab notebook to your project

Often we bundle related functionality together into separate notebooks, which then form the basis of a importable modules.

Create a new python 3 notebook in Colab and name it according to the nbdev convention of incremental numbering (00, 01, 02 etc) followed by an underscore and a name describing its contents. For example, if this is the third notebook added to the project, and it contains networking functionality, an appropriate name might be '03_network.ipynb'. 

Note that Colab may not create the notebook directly in the project repo on google drive. If not, locate it at the default location where new notebooks are created (commonly the 'Colab Notebooks' folder in /My Drive), then right click the notebook and select 'move'. Use the pop up box to move it to the desired location in the local project directory. 

Then add and run the following code snippets in seperate cells in order to set up the notebook for nbdev integration.

1.   In the first cell add:

 ```# default_exp <module>```

  Where <module> is the name of the .py file that the notebook will create. IN the case of the 03_sync.ipynb notebook, the module name should be 'sync'. Submodules can be specified with <module.submodule'.

2.   Add autoreload functionality to any changes in one notebook module are automatically updated in linked module notebooks:
```
#hide
%load_ext autoreload
%autoreload 2
```

3.   Then code to connect your Colab instance to Google Drive:
```
# hide
from google.colab import drive
drive.mount('/content/drive')
```

4.   Required installs. Fastcore is required for running tests from nbdev.
```
# hide
!pip install nbdev
!pip install fastcore
```

5.   Import modules:
```
#export
from nbdev import *
from nbdev.showdoc import *
```

6.   Add the in-notebook export cell. Running this cell exports modules directly from the notebook (without having to go to the command line). The nbdev docs suggest adding it as the final cell in the notebook.
```
#hide
from nbdev.export import notebook2script
notebook2script()
```

 Finally, cd into the root directoryof your ```repo``` on Google Drive ```cd /content/drive/My drive/repo``` and your ready to code your project.

## Managing your project

In the project management notebook, change directory to the project root directory on Google Drive. 

```change_dir('path-to-repo')```  or  ```% cd path-to-repo```

From here, all nbdev and Github commands work as expected for the project:

*    Build the library, build the docs and run tests with ```!nbdev_build_lib```, ```!nbdev_build_docs```, and ```nbdev_test_nbs```. See the nbdev docs and tutorial for all available commands. 

*    Push to github with  ```!git.status```, ```!git add -A```, ```!git commit -am "message"```, and ```!git push```. All other Github commands (prefixed by !) should also work normally.

*    Publish to pypi by following the instructions in the nbdev tutorial https://nbdev.fast.ai/tutorial/. Creating a _pypirc file i the user's home directory must be done manually but ```!pip install twine``` and ```!make release``` work normally from Colab notebooks with nbdev installed. 




## Quirks and tips for using nbdev with Colab and Google Drive



*   To use nbdev/Github/pypi functionality it is necessary to ```%cd``` into the local project repo on Google Drive. 

*   Use ```%cd``` for changing directory but ```!cmd``` for other command line actions.

*   Google Colab can't edit text files so editing text files (for example 'settings.init' or '__init__.py') requires either linking a text editor to your Google Drive or simply downloading the text file from Google Drive to your local machine, editing it there with your chosen text editor, followed by re-uploading it to Google Drive when done.

*   ```show_doc(class.method)``` doesn't give the expected notebook output in Colab notebook cells. However, it works fine when the documentation is built with ```!nbdev_build_docs``` so do continue to use it as per the nbdev docs/tutorial (https://nbdev.fast.ai/) 

*   Exceptions (errors) arising during execution of command line actions from Colab notebooks, sometimes results in a runtime reset and return to the Google drive root diectory '/content'. Check the current directory after exceptions with ```!pwd``` and cd back to the repo if needed to continue working. 

*   Running ```!nbdev_test_nbs``` runs tests on all notebooks in the project. As well as passing all specific tests, project notebooks must also be able to run from start to finish independently to pass. For example, if a notebook contains code to connect to Google Drive (e.g. ```drive.mount("/content/drive")```,  but is not connected to Google Drive at the time of the test, it may fail because notebook execution will stall at this point pending user input. 

*   Notebook cells relying on installs specifically within the Colab environment will cause Github tests to fail during a github push. The push and githubpages build still succeed, but the push is marked as a fail with a red cross because testing failed. A common culprit is ```from google.colab import drive```. Comment this out if you want the github tests to succeed during a push

*   There are probably others - I'll add to the list as I become aware of them!

