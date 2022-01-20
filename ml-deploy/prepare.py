import imp
from os.path import exists
import subprocess, sys


class Error(Exception):
    """base error class"""
    pass

class RequirementsNotExistsException(Error):
    """raised if the requirements.txt file is not included in the base directory"""
    pass

class NoModelFileException(Error):
    """raised if a serialized model file is not found in the base directory"""
    pass

class EntryFileNotFoundException(Error):
    """raised if the entry file, with name of 'score.py', is not found in the base directory"""
    pass

def prepare():
    """this is the module that will prepare the assets for building"""
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pigar"])
    if not exists("requirements.txt"):
        raise RequirementsNotExistsException("There is no file named 'requirements.txt'")
    if not exists("*.pkl"):
        raise NoModelFileException("You must have a serialized model file.")
    if not exists("score.py"):
        raise EntryFileNotFoundException("An entry file named 'score.py' must be included in the base directory.")