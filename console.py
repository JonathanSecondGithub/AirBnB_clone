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
        c_name = c_id = att_name = att_val = kwargs = ''

        # isolate cls from id/args, ex: (<cls>, delim, <id/args>)
        args = args.partition(" ")
        if args[0]:
            c_name = args[0]
        else:  
            # class name not present
            print("** class name missing **")
            return

        if c_name not in __class__.valid_classes:  # class name invalid
            print("** class doesn't exist **")
            return
            
            # isolate id from args
            args = args[2].partition(" ")
            if args[0]:
                c_id = args[0]
            else:
                print("** instance id missing **")
                return

            # generate key from class and id
            key = c_name + "." + c_id

            if key not in storage.all():
                 print("** no instance found **")
                 return

            if '{' in args[2] and '}' in args[2] and type(eval(args[2])) is dict:
                kwargs = eval(args[2])
                args = []
                for k, v in kwargs.items():
                    args.append(k)
                    args.append(v)
            else:
                args = args[2]
                if args and args[0] is '\"':
                    second_quote = args.find('\"', 1)
                    att_name = args[1:second_quote]
                    args = args[second_quote + 1:]
                args = args.partition(' ')

                if not att_name and args[0] is not ' ':
                    att_name = args[0]

                if args[2] and args[2][0] is '\"':
                    att_val = args[2][1:args[2].find('\"', 1)]

                if not att_val and args[2]:
                    att_val = args[2].partition(' ')[0]

                args = [att_name, att_val]

            new_dict = storage.all()[key]

            for i, att_name in enumerate(args):
                if (i % 2 == 0):
                    att_val = args[i + 1]
                    if not att_name:  # check for att_name
                        print("** attribute name missing **")
                        return
                    if not att_val:  # check for att_value
                        print("** value missing **")
                        return
                    if att_name in HBNBCommand.types:
                        att_val = HBNBCommand.types[att_name](att_val)

                    new_dict.__dict__.update({att_name: att_val})
            new_dict.save()  # save updates to file
"""Code should not be executed when imported."""    
if __name__ == '__main__':
        HBNBCommand().cmdloop()
