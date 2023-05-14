#!/usr/bin/python3
"""This is the class for the interactive console where the user enters commands"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
import json


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
        return True
    
    def do_EOF(self, line):
        """The EOF command is a special command that is executed when you press CTRL-D on your keyboard."""
        return True

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
        args = line.split()
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
