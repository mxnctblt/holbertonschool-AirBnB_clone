#!/usr/bin/python3
"""
Console module
"""
import cmd
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    the main class for the HBNBCommand
    """
    prompt = "(hbnb) "
    __classes = {
        'BaseModel',
        'User',
        'Place',
        'State',
        'City',
        'Amenity',
        'Review'
        }

    def do_quit(self, line):
        """Quit command to exit the programm
        """
        return True

    def do_EOF(self, line):
        """EOF command to exit the programm """
        return True

    def emptyline(self):
        """
        An empty line + ENTER shouldn’t execute anything
        """
        pass

    def do_create(self, line):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id
        """
        if not line:
            print("** class name missing **")
        elif line not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            d = {
                'BaseModel': BaseModel,
                'User': User,
                'Place': Place,
                'State': State,
                'City': City,
                'Amenity': Amenity,
                'Review': Review
                }
            new = d[line]()
            new.save()
            print('{}'.format(new.id))
            storage.save()

    def do_show(self, line):
        """
        Prints the string representation of an instance based on the class name
        and id.
        """
        l = line.split()
        d = storage.all()
        if len(l) == 0:
            print("** class name missing **")
        elif l[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(l) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(l[0], l[1]) not in d:
            print("** no instance found **")
        else:
            print(d["{}.{}".format(l[0], l[1])])

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """
        l = line.split()
        d = storage.all()
        if len(l) == 0:
            print("** class name missing **")
        elif l[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(l) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(l[0], l[1]) not in d:
            print("** no instance found **")
        else:
            del (d["{}.{}".format(l[0], l[1])])
            storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all instances based or
        not on the class name.
        """
        n = 0
        o = [str(v) for v in storage.all().values()]
        if not line:
            n = 1
            print('{}'.format(o))
        elif line:
            l = line.split()
        if line and l[0] in HBNBCommand.__classes:
            n = 1
            o = storage.all()
            name = l[0]
            o = ([str(v) for k, v in o.items()
                  if name == v.__class__.__name__])
        print(o)
        if n == 0:
            print("** class doesn't exist **")

    def do_update(self, line):
        """
        Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        """
        l = line.split()
        n = ["id", "created_at", "updated_at"]
        d = storage.all()
        if not line:
            print("** class name missing **")
        elif l[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(l) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(l[0], l[1]) not in d:
            print("** no instance found **")
        elif len(l) < 3:
            print("** attribute name missing **")
        elif len(l) < 4:
            print("** value missing **")
        elif l[2] not in n:
            obj = d["{}.{}".format(l[0], l[1])]
            obj.__dict__[l[2]] = l[3]
            obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
