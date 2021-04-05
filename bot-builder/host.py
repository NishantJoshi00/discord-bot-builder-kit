import os
import shutil, pathlib
from sys import path

def host_command(argv):
    if len(argv) == 0:
        os.system("heroku create")
        os.system("git add .")
        os.system("git commit -m \"Hosting this version\"")
        os.system("git push heroku master")
    if len(argv) == 1:
        os.system(f"heroku create {argv[0]}")
        os.system("git add .")
        os.system("git commit -m \"Hosting this version\"")
        os.system("git push heroku master")

def rehost_command(argv):
    if len(argv) == 0:

        os.system("git add .")
        os.system("git commit -m \"Hosting this version\"")
        os.system("git push heroku master")