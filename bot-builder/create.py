import os
import shutil, pathlib
from sys import path
def create_command(argv):
    if len(argv) == 0:
        print("For create use this subcommands:\n\tjs, nodejs: for javascript template\n\tpython, py: for python template")
        return
    if argv[0] in ["js", "Js", "JS", "nodejs"]:
        shutil.copytree(pathlib.Path(__file__).parent.joinpath("templates/nodejs"), pathlib.Path(os.getcwd()).joinpath("discord-bot-js"))
        os.chdir(pathlib.Path(os.getcwd()).joinpath("discord-bot-js"))
        os.system("git init .")
        os.system("git add .")
        os.system("git commit -m \"Initial commit!\"")
    elif argv[0] in ["python", "py"]:
        shutil.copytree(pathlib.Path(__file__).parent.joinpath("templates/python"), pathlib.Path(os.getcwd()).joinpath("discord-bot-py"))
        os.chdir(pathlib.Path(os.getcwd()).joinpath("discord-bot-py"))
        os.system("git init .")
        os.system("git add .")
        os.system("git commit -m \"Initial commit!\"")
    else:
        print("For create use this subcommands:\n\tjs, nodejs: for javascript template\n\tpython, py: for python template")
