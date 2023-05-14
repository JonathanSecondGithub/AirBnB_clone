#!/usr/bin/python3
<<<<<<< HEAD
"""Defines the HBnB console."""
=======
"""This is the class for the interactive console where the user enters commands"""
>>>>>>> 98c7bde7a7b1a60e2c23e6188d3aacbf520fa035
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
<<<<<<< HEAD
from models.place import Place
from models.amenity import Amenity
from models.review import Review


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
    """Defines the HolbertonBnB command interpreter.
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

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit command to exit the program."""
=======
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
import json
import shlex


class HBNBCommand(cmd.Cmd):
    """This is the class for the interactive console where the user enters commands"""
    prompt = '(hbnb) '
    valid_classes = ["BaseModel" , "User", "State", "City", "Amenity", "Place", "Review"]
    types = {   'number_rooms': int, 
                'number_bathrooms': int,
                'max_guest': int, 
                'price_by_night': int,
                'latitude': float, 
                'longitude': float
            }
    def do_quit(self, line):
        """When the quit command is pressed the terminal is closed and the program is terminated"""
>>>>>>> 98c7bde7a7b1a60e2c23e6188d3aacbf520fa035
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

<<<<<<< HEAD
    def do_create(self, arg):
        """Usage: create <class>
        Create a new class instance and print its id.
        """
        argl = parse(arg)
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(argl[0])().id)
            storage.save()

    def do_show(self, arg):
        """Usage: show <class> <id> or <class>.show(<id>)
        """
        argl = parse(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(argl[0], argl[1])])

    def do_destroy(self, arg):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        """
        argl = parse(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(argl[0], argl[1])]
            storage.save()

    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        """
        argl = parse(arg)
        if len(argl) > 0 and argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(argl) > 0 and argl[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(argl) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        """
        argl = parse(arg)
        count = 0
        for obj in storage.all().values():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        argl = parse(arg)
        objdict = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argl) == 4:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            for k, v in eval(argl[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
=======
    def emptyline(self):
        """Don't do anything when an empty line + enter is pressed"""
        pass
    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id. Ex: $ create BaseModel"""
        args = line.split()

        if len(args) == 0:
            print ("** class name missing **")
            return False
        if args[0] not in __class__.valid_classes:
            print ("** class doesn't exist **")
        else:
            if args[0] == "BaseModel":
                new_instance = BaseModel()
                new_instance.save()
                print (new_instance.id)
            elif args[0] == "User":
                new_user = User()
                new_user.save()
                print (new_user.id)
            elif args[0] == "State":
                new_state = State()
                new_state.save()
                print (new_state.id)
            elif args[0] == "City":
                new_city = City()
                new_city.save()
                print (new_city.id)
            elif args[0] == "Amenity":
                new_amenity = Amenity()
                new_amenity.save()
                print (new_amenity.id)
            elif args[0] == "Place":
                new_place = Place()
                new_place.save()
                print (new_place.save())
            elif args[0] == "Review":
                new_review = Review()
                new_review.save()
                print (new_review.id)
                

    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and id. Ex: $ show BaseModel 1234-1234-1234."""
        args = line.split()
        
        if len(args) == 0:
            print ("** class name missing **")
            return False
        if args[0] in __class__.valid_classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in storage.all():
                    print(storage.all()[key])
                else: 
                    print("** no instance found **")
            else:
                print ("** instance id missing **")
        else:
            print ("** class doesn't exist **")
        

    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id (save the change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234."""
        args = line.split()

        if len(args) == 0:
            print ("** class name missing **")
            return False
        if args[0] in __class__.valid_classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in storage.all():
                    storage.all().pop(key)
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                    print ("** instance id missing **")
        else:
            print ("** class doesn't exist **")

        

    def do_all(self, line):
        """Prints all string representation of all instances based or not on the class name. Ex: $ all BaseModel or $ all"""
        args = line.split()
        if len(args) > 0:
            if args[0] not in __class__.valid_classes:
                print ("** class doesn't exist **")
                return False
            else:
                str_list = [str(obj) for key, obj in storage.all().items()if type(obj).__name__ == args[0]]
                print (str_list)
        else:
            new_list = [str(obj) for key, obj in storage.all().items()]
            print(new_list)
            
    def do_update(self, line):
        """ Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"."""
        args = shlex.split(line)
        integers = ["number_rooms", "number_bathrooms", "max_guest","price_by_night"]
        floats = ["latitude", "longitude"]
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in __class__.valid_classes:
            if len(args) > 1:
                k = args[0] + "." + args[1]
                if k in storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            if args[0] == "Place":
                                if args[2] in integers:
                                    try:
                                        args[3] = int(args[3])
                                    except:
                                        args[3] = 0
                                elif args[2] in floats:
                                    try:
                                        args[3] = float(args[3])
                                    except:
                                        args[3] = 0.0
                            setattr(storage.all()[k], args[2], args[3])
                            storage.all()[k].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")
"""Code should not be executed when imported."""    
if __name__ == '__main__':
        HBNBCommand().cmdloop()
>>>>>>> 98c7bde7a7b1a60e2c23e6188d3aacbf520fa035
