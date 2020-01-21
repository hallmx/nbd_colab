# Welcome to nbd_colab
> nbd_colab is a thin wrapper of functions around nbdev to aid integration of nbdev with Google drive and Google Colab. 


```
from google.colab import drive
drive.mount('/content/drive')
```

    Drive already mounted at /content/drive; to attempt to forcibly remount, call drive.mount("/content/drive", force_remount=True).


```
% cd /content/drive/My\ Drive/nbd_colab
```

    /content/drive/My Drive/nbd_colab


```
#export
from nbd_colab.core import *
```

## Install

`pip install nbd_colab`

## Overview

See the nbdev documentstion formore details of nbdev, a powerful system for exploratory programming, and why you may want to use it. These docs will simply focus on using nbd_colab as an aid to integrating nbded with Google drive and Google Colab.  

There are a number of steps to using nbdev with Google Colab and google Drive



1.   Create an nbdev template repository in your github account (see nbdev tutorial `https://nbdev.fast.ai/tutorial/#Upload-to-pypi`).
2.   Configue the settings.ini file in the nbdev template repo (see nbdev tutorial `https://nbdev.fast.ai/tutorial/#Upload-to-pypi`).
3.   Create a new python 3 instance (notebook) in Google Colab
4.   !pip install nbd_colab from within the new notebook (it will automatically install nbdev itself)
5.   Connect your Colab instance to Google drive with setup_drive()
6.   Run clone_new_repo() to clone the nbdev template repo to your google drive
7.   When you create a new notebook (new project module), install nbd_colab, 
from nbd_colab.core import *, and run setup_nb to ensure the module is connected to the Google drive repo and is ready to go!




