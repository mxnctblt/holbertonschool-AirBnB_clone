#!/usr/bin/python3
"""
Console module
"""
import cmd
import models
from models.base_model import BaseModel



class HBNBCommand(cmd.Cmd):
    """
    the main class for the HBNBCommand
    """
    prompt = "(hbnb)"

    def do_quit(self, line):
        """
        quit : command to quit the programm
        """
        return True

    def do_EOF(self, line):
        """
        EOF : command to quit the programm
        kind of same as do_quit
        """
        return True

    def emptyline(self):
        """
        An empty line + ENTER shouldn’t execute anything
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
