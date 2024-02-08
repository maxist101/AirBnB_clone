#!/usr/bin/python3
"""
Our code module defines a simple HBNB console.
"""

import cmd
from models.place import Place
from models import storage
from shlex import split
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import re


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """
    Our code defines the HBNBC command interpreter.
    """
    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def do_quit(self, arg):
        """Quit command to exit/terminate the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print(" ")
        return True

    def emptyline(self):
        """Do nothing when empty line is received"""
        pass

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        arg_dic = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argx = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", args[1])
            if match is not None:
                command = [argx[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in arg_dic.keys():
                    call = "{} {}".format(argx[0], command[1])
                    return arg_dic[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_create(self, arg):
        """Create a new instance of, save &  print the id."""
        argx = parse(arg)
        if len(argx) == 0:
            print("** class name missing **")
        elif argx[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(argx[0])().id)
            storage.save()

    def do_show(self, arg):
        """Print the string number rep of an instance."""
        argx = parse(arg)
        obdict = storage.all()

        if len(argx) == 0:
            print("** class name missing **")
        elif argx[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argx) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argx[0], argx[1]) not in obdict:
            print("** no instance found **")
        else:
            print(obdict["{}.{}".format(argx[0], argx[1])])

    def do_destroy(self, arg):
        """Delete a given id of a class instance"""
        argx = parse(arg)
        obpdict = storage.all()
        if len(argx) == 0:
            print("** class name missing **")
        elif argx[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argx) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argx[0], argx[1]) not in obpdict.keys():
            print("** no instance found **")
        else:
            del obpdict["{}.{}".format(argx[0], argx[1])]
            storage.save()

    def do_all(self, arg):
        """Display all the string representations of instances of a
        given class, if no specified class,
        display all instantiated objects."""
        argx = parse(arg)
        if len(argx) > 0 and argx[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj1= []
            for obj in storage.all().values():
                if len(argx) > 0 and argx[0] == obj.__class__.__name__:
                    obj1.append(obj.__str__())
                elif len(argx) == 0:
                    obj1.append(obj.__str__())
            print(obj1)

    def do_update(self, arg):
        """Update an instance based on the class name and id."""
        argx = parse(arg)
        obdict = storage.all()

        if len(argx) == 0:
            print("** class name missing **")
            return False
        if argx[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argx) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argx[0], argx[1]) not in obdict.keys():
            print("** no instance found **")
            return False
        if len(argx) == 2:
            print("** attribute name missing **")
            return False
        if len(argx) == 3:
            try:
                type(eval(argx[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argx) == 4:
            obj = obdict["{}.{}".format(argx[0], argx[1])]
            if argx[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argx[2]])
                obj.__dict__[argx[2]] = valtype(argx[3])
            else:
                obj.__dict__[argx[2]] = argx[3]
        elif type(eval(argx[2])) == dict:
            obj = obdict["{}.{}".format(argx[0], argx[1])]
            for k, v in eval(argx[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()

    def do_count(self, arg):
        """Retrieve the number of instances of a given class."""
        argx = parse(arg)
        count = 0
        for obj in storage.all().values():
            if argx[0] == obj.__class__.__name__:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
