# ENV-TOOL
This repository store a useful tool : env_tool.py. Why this tool exists ? Because when you work on a python project (or using python), you might be use virtual environnements. It can is the cause of a principal problem : the python source version (of the virtual env) is generally not the same for everyone ...

## Features :
- [x] Don't need an Archive Manager on your computer
- [x] Backup a python venv (in .zip)
- [x] Extract a backuped venv (from .zip)
- [ ] Use other compress algorithms and extensions
- [ ] Can use mdp to protect the venv

## What is a Python Virtual-ENVironnement and what is used for ?
A python virtual env is a specific version of python with his specifics modules in a directory (like ".env" or ".venv"). What is used for ? For example if you use the same python (version and modules) for all, it sometimes make problems because some packages (with different versions) may not perfect work together, in a program. Moreover, if you use a specific version of a python module in a project and other version in other project, this can make problems if you use only a python global version.

## Install/Extract the default (.zip) venv (or skip and create yourself venv) :
***Note : Le fichier .gitignore est configuré pour ne pas synchroniser le venv (mais une version est zippée dans ce dossier).***
``` shell
python env_tool.py --extract
```

## Backup the default (.zip) env : (after modificate this env)
``` shell
python env_tool.py --backup
```

## Activate python env :
***In a powershell terminal (if OS is Windows) :***
``` shell
.venv/Scripts/Activate.ps1
```

## Use PIP for install modules (in this env) :
***After you have activate the python venv, you can use the folow command :***
``` shell
pip install module
```

## Run a python file :
***After you have activate the python venv, you can use the folow command :***
``` shell
python main.py
```

## Deactivate python env :
***Note : you also can close the terminal without cause problems.***
``` shell
deactivate
```
