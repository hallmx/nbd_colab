# Welcome to nbd_colab
> nbd_colab is a thin wrapper of functions around nbdev to aid integration of nbdev with Google drive and Google Colab. 


## Install

`pip install nbd_colab`

## Overview

See the nbdev documentstion formore details of nbdev, a powerful system for exploratory programming, and why you may want to use it. These docs will simply focus on using nbd_colab as an aid to integrating nbded with Google drive and Google Colab.  

## Create new project

Clone a new nbdev template repo from your github to Google Drive.

`clone_new_repo()`

## Navigating your project

Change directory to your home directory while it is linked to Colab.

`home_dir()`


## Module setup

Each new module requires its own Colab notebook. Create a new python 3 notebook in Colab and name it according to the nbdev convention of incremental numbering followed by an underscore and a name describing its contents. For example, if this is the third notebook added to the project, and it contains syncing functions and code a conforming name might be '03_sync.ipynb'. 

Then add the following code snippets in order to set up the notebook for nbdev integration.

`# default_exp <module>`

Where <module> is the name of the .py file that the notebook will create. IN the case of the 03_sync.ipynb notebook, the module name should be 'sync'. Submodules can be specified with <module.submodule'.



## Publishing your project on Pypi
