# Welcome to nbd_colab
> Wrapper, resources and documentation around fastai nbdev to streamline literate programming  in Google Colaboratory.  


## Install

`pip install nbd_colab`

## Overview

Nbdev is a system for exploratory programming using Jupyter notebooks developed by Jeremy Howard and Sylvain Gugger of fastai aimed at helping python developers and software engineers practice literate programming. Many of these use Google Colaboratory (Colab) to develop and run GPU accelerated code, and while nbdev works perfectly well with Colab's Jupyter notebooks, there are few tricks and twists to creating a smooth workflow with nbdev, GitHub, Google Colab and Drive. 

Here we describe an approach to using nbdev with Google Colab and Google Drive, provide some useful tools for GitHub integration and add some nbdev-colab specific documentation including troubleshooting and testing advice. Further information on nbdev itself can be found in the nbdev [documentation](https://nbdev.fast.ai/) and [tutorial](https://nbdev.fast.ai/tutorial/).

## Approach to using nbdev with Colaboratory's Jupyter notebooks

Normally, project code is written in a Jupyter notebook and the project managed from the command line. Developing in Colab we don't have a separate command line as such and instead access command line functionality from notebook cells using the os module and ! or % prefixes.
While it is quite possible to manage an nbdev project entirely from within development notebooks, having code for two different purposes - project code and command line code - in the same notebook quickly becomes cumbersome and a source of confusion. An alternative approach is to set up a Colab notebook outside of the project itself to use exclusively exclusively as the command line - a 'command line notebook` if you like. All that is required is to make sure that the current working directory of the command line notebook is within the project directory on Google Drive and any commands and scripts run in the command line notebook will execute in respect to the project files. We can use the project management notebook for running tests, nbdev and GitHub integration, making PyPi releases and pretty much anything else you would normally use the command line for.

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

1.  Follow the nbdev [documentation](https://nbdev.fast.ai/) and [tutorial](https://nbdev.fast.ai/tutorial/) to generate a new Github repository from the [nbdev template repository](https://github.com/fastai/nbdev_template/generate) (you must be logged in to your Github account for this to work) and edit the settings.ini file of the new repository as instructed. Don't forget also to set up GitHub Pages for your new repository, selecting the 'master branch/docs folder' option.

2. If your project needs to install other libraries add these, separated by a spaces, to the requirements line in settings.ini.

3. From your project management notebook (created above) clone the new remote GitHub repository to your Google Drive by typing the following code and following the instructions to enter the required information. Successfully cloned repositories are automatically configured for integration with the remote repository and `nbdev_git_hooks` is installed  (`nbdev_git_hooks` gives smoother Github integration by cleaning up notebook metadata). Entering sensitive user information into a form, avoids hardcoding it into the notebook (as a function arguement or class attibute,  for example) where there is then a risk of accidental upload to GitHub if the user forgets to delete it before a push. 
```
clone_new_repo()
```
> **CAUTION.** The users GitHub username and password are stored (unencrypted) in the cloned repository's `.git/config` file to allow automatic authentication when Colab interacts with GitHub during git pushes. They need to be stored in advance because Colab has no facility for prompting users for authentication details from within Colab notebooks. This is far from ideal but there appears no way around it and so users must be careful NOT to share the cloned repository folder or files from Google Drive as this risks exposing their GitHub credentials. By default the `.git/config` file is '.gitignored' and not pushed to GitHub.

4.  Change directory into the newly cloned repository on Google Drive.
```
change_dir('path_to_repo') 
```
or
```
 %cd path_to_repo
```
Check cloning was successful by printing out the contents of the settings.ini file. Take this oppurtunity to make sure you have made all the necessary changes to settings.ini. 
```
! cat settings.ini
```

From here, follow the instructions in the nbdev [documentation](https: //nbdev.fast.ai/) and [tutorial](https://nbdev.fast.ai/tutorial/) to make an initial build of the project library and documentation (i.e. run `!nbdev_build_lib` then `!nb_build_docs` in the command line notebook).

## Navigating your project

Change directory to your Google Drive/Colab home directory `/content/drive/My Drive`

`home_dir()`


Change directory to ```path```

```change_dir(path)```


## Adding a new notebook/module to your project

See the 'Notebooks' page of the nbd_colab documentation [here](https://hallmx.github.io/nbd_colab/tutorial/).

## Working with nbdev and Colab notebooks

### Automatic documentation syntax (nbdev):
*   #export - include cell content and cell output in module `.py` files and docs. 

*   #exports - include cell content, cell output and source code in module and docs

*   #hide - do not include cell in module or docs

*   none - include in documenttaion only

*   _ (underscore) before a function or class will include it in the module but hide it from the docs

*   A thick blue line is added above the documentation for a class. To include a thick blue line divider elsewhere, start a text cell with ## (two hashes).

* Only functions and classes are included in the documentation of cells flagged with `#export` or `#exports`. Other code is converted to script but not included in the docs. 

*   Tests are best placed in a separate cell without any flags. There, they will always be run with `nbdev_test_nbs` and be included in the documentation but excluded from the script `.py` file. `#hide` cells with tests you don't want including in the docs. 

*   The "Docstring" of classes and functions is automatically formatted as the class or function description in the documentation 

*   Class methods are not automatically included in the documentation. Include those you want manually using `#show_doc(class.method)` in a cell after the cell containing the class or function. The method "Docstring" becomes the method description in the docs. 


See the nbdev [documentation](https://nbdev.fast.ai/) for the full guide.

### Markdown references. 

* [Colab markdown guide](https://colab.research.google.com/notebooks/markdown_guide.ipynb#scrollTo=70pYkR9LiOV0)

* [GitHub markdown](https://help.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax)

* [Guide to Latex](https://en.wikibooks.org/wiki/LaTeX/Mathematics)

## Dependencies and imports

* Use the `requirements` setting in `settings.ini` to install any dependencies required by your project. Multiple library names should be separated by a single space only, e.g. `requirements = fastcore nbdev xyz_lib`. Note that `!` generates an error when building the docs so `#hide` code such as `!install xyz` or put it into a text cell to show to users. 

* Edit `init.py` with the name of modules to import with just `*`. For example, add `from .core import *` to `init.py` to allow `core` (and all other modules specified in this way) to be imported into notebooks with just `from nbdev import *`

### Tests

Nbdev has a great test integration in the form of `nbdev_test_nbs` and test_flags.

Note that tests are run locally at the programmer's discretion but `nbdev_test-nbs` is also run automatically as a GitHub Action when code is pushed. Thus, given the Colaboratory and GitHub python virtual environments are likely to differ, tests may pass when `nbdev_test_nbs` is run locally on Colab, but fail during a GitHub push (or vice versa!).
Read more about testing and test_flags on the nbdev [documentation](https://nbdev.fast.ai/tests), about using test_flags with Colab on the 'Notebooks' page [here](https://hallmx.github.io/nbd_colab/tutorial/) and if your tests aren't passing, the 'Troubleshooting' page [here](https://hallmx.github.io/nbd_colab/troubleshooting/) 

## Building, pushing and releasing your project

In the command line notebook, change directory to the root directory of the project/local repository on Google Drive ```change_dir('path_to_repo')``` or ```%cd path_to_repo```. From here, all nbdev and GitHub commands should work as expected:

*    Build the library (.py modules), build the docs (.html files) and check for diffs between notebook and scripts with ```!nbdev_build_lib```, ```!nbdev_build_docs```, and ```!nbdev_diff_nbs``` respectively (and in that order). See the nbdev [documentation](https://nbdev.fast.ai/) for all available commands . 

*    Push to github with  ```!git.status```, ```!git add -A```, ```!git commit -am "message"```, and ```!git push```. All other Github commands (prefixed by !) should also work normally.

*    Publish to [PyPi](https://pypi.org/) by following the instructions in the [nbdev tutorial](https://nbdev.fast.ai/tutorial/). Creating a _pypirc file in the user's home directory must be done manually with a text editor but ```!pip install twine``` and ```!make release``` work normally from Colab notebooks with nbdev installed. 

The command line notebook can be adapted and customized to your particular workflow. 


## Templates

We provide a minimal project code template notebook (03_nbtemplayte.ipynb) and command line template (04_cltemplate.ipynb) to get you started. These can be viewed in the docs and downloaded from GitHub for use. Customize them to your particular project or workflow. 

## Docs

This project, it's github repo, and documentation were all built using [nbdev](https://github.com/fastai/nbdev).

## Contributing

After you clone this repository, please run `nbdev_install_git_hooks` in your terminal. This sets up git hooks, which clean up the notebooks to remove the extraneous stuff stored in the notebooks (e.g. which cells you ran) which causes unnecessary merge conflicts.

Before submitting a PR, check that the local library and notebooks match. The script `nbdev_diff_nbs` can let you know if there is a difference between the local library and the notebooks.

## Copyright


Copyright 2020 onwards, Mathew Hall, Licensed under the Apache License, Version 2.0 (the "License"); you may not use this project's files except in compliance with the License. A copy of the License is provided in the LICENSE file in this repository
