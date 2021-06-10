# Creating Virtual Environments.
- python3 -m venv tutorial-env (name whichever you want)

## activate virtual environment.
- Unix or MaxOS run:
  - source tutorial-env/bin/activate

- Windows run:
  - tutorial-env/Scripts/activate.bat

**print in python sys.path to check if the path of venv is inside**

# Managing Packages pip
## Install
To install the latest version of package just write the package withouth ==
- python -m pip install pandas.

To install a specific version write the package followed of == [version of package]
- python -m pip install requests==2.6.0

## Upgrade an existing package.
If you have a package which is not up to date you can upgrade it to the latest version.
- python -m pip install --upgrade requests.

## Uninstalling a package.
- pip uninstall pandas.

## Display package info.
### Single Package.
Show the info of a single package.
- pip show requests.

### Display a list of all the packages installed.
- pip list.
Will display a list of packages installed on the venv.

### Generate requirements.txt
When installed all the packages and app already tested, you can run:
- pip freeze > requirements.txt
To see the requirements.txt content run:
- cat requirements.txt

This document can be sent to a repository and cloned to another device, then packages can be installed through requirements doc.

# Install requirements.txt:
When app in another environment, you can run:
- python -m pip install -r requirements.txt

In order to install all the packages used by the project.
