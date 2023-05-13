#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage

"""This is the class for the interactive console where the user enters commands"""
class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, line):
        """When the quit command is pressed the terminal is closed and the program is terminated"""
        return True
    
    def do_EOF(self, line):
        """The EOF command is a special command that is executed when you press CTRL-D on your keyboard."""
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id. Ex: $ create BaseModel"""
        args = line.split()

        if len(args) == 0:
            print ("** class name missing **")
            return False
        if args[0] != "BaseModel":
            print ("** class doesn't exist **")
        else:
            new_instance = storage.new(BaseModel())
            new_instance.save()
            print (new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and id. Ex: $ show BaseModel 1234-1234-1234."""
        args = line.split()
        
        if len(args) == 0:
            print ("** class name missing **")
            return False
        if args[0] == "BaseModel":
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
        if args[0] == "BaseModel":
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in storage.all():
                    storage.all().pop(key)
                    storage.all.save()
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
            if args[0] != "BaseModel":
                print ("** class doesn't exist **")
                return False
            else:
                obj_dict = json.dumps(storage.all())
        print (obj_dict)

    def do_update(self, line):
        """ Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"."""
        args = line.split()
        if line == "" or line is None:
            print ("** class name missing **")
            return False
        elif args[0] != "BaseModel":
            print ("** class doesn't exist **")
        elif len(args) == 1:
            print ("** instance id missing **")
        elif len(args) > 1:
            key = args[0] + "." + args[1]
            if key in storage.all():
                print ("instance found")
            else:
                print ("** no instance found **")
        elif len(args) == 2:
            print ("** attribute name missing **")
        elif len(args) == 3:
            print ("** value missing **")








"""Code should not be executed when imported."""    
if __name__ == '__main__':
        HBNBCommand().cmdloop()
