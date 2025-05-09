#---------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# Python: 3.11.9
# Author: Killian Nallet
# Date: 07/05/2025
#---------------------------------------------------------------------------------


# ------------------- env_tool.py v1.0 -------------------
#
# This script is used to backup and extract the virtual environment for python projects.
# It must be launched from the python virtual environnement (for get the python venv version)
# and creates a zip file of the virtual environment and extracts it when needed.
#
# This script can be launched from dev/, src/ directory or from the root of the project.
#
# args:
# --backup : backup the virtual environment (in the directory of the script)
# --extract : extract the virtual environment (at the root of the project)
#
# --------------------------------------------------------


# imports
import os
import sys
import zipfile


# change current dir
current_dir = os.path.dirname(__file__)
os.chdir(os.path.dirname(current_dir)) # change working directory to the script's directory

# check file location
if os.path.basename(current_dir) == "dev":
    project_path = os.path.dirname(current_dir)
else:
    project_path = current_dir


# constants
venv_src_path = os.path.join(project_path, ".venv")

python_location = os.path.join(current_dir, venv_src_path, "Scripts", "python.exe")
txtpython_version = "-".join([str(i) for i in sys.version_info[:3]]) # like "3-11-9"
term_size = os.get_terminal_size()[0]# get terminal width size

venv_zip_path = os.path.join(current_dir, f"python{txtpython_version}_venv.zip")
config_file_path = os.path.join(current_dir, "envtool_config.json")


# functions
def progress(txt):
    """Prints progress a text in the terminal."""
    print(f"- {txt}{' '*(term_size-len(txt)-2)}", end="\r", flush=True)

# check args
if len(sys.argv) > 1:
    if sys.argv[1] == "--backup":
        action, mode = "bac", "w"
    elif sys.argv[1] == "--extract":
        action, mode = "ext", "r"
    else:
        print("Invalid argument. Use --backup or --extract.")
        sys.exit(1)
else:
    print("No argument provided. Use --backup or --extract.")
    sys.exit(1)

# zip actual venv (for developpement and tests)
if action == "bac" and os.path.exists(venv_zip_path):
    print("Removing old zip venv ...")
    os.remove(venv_zip_path)
    print("Old zip env removed.")
elif action == "ext" and not os.path.exists(venv_zip_path):
    print(f"Error: '{venv_zip_path}' folder not found !")
    sys.exit(1)

# do action (bacup or extract)
with zipfile.ZipFile(venv_zip_path, mode, zipfile.ZIP_DEFLATED) as bacup_env:

    if action == "bac":
        print("Backup actual venv ...\n", end="")
        try:
            for path_dir, _dirs, list_files in os.walk(venv_src_path): # warning: recursive method
                for file in list_files:         
                    if file.endswith(".pyc"): # skip pyc files
                        continue
                    path_file = os.path.join(path_dir, file)
                    arcpath = path_file.split(venv_src_path)[1]
                    progress(arcpath)
                    bacup_env.write(path_file, arcpath)
        except KeyboardInterrupt:
            pass
        except:
            print(f"Error: {os.path.basename(path_file)} not added to the zip file !")
        else:
            print("Actual venv backuped.")

    elif action == "ext":
        print("Extracting default venv (this can make some time) ...\n", end="")
        if not os.path.exists(venv_src_path):
            os.mkdir(venv_src_path)
        for member in bacup_env.namelist():
            progress(member)
            bacup_env.extract(member, venv_src_path)
        print("Actual venv extracted.")
