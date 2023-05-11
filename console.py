#!/usr/bin/python3
import cmd
from models.base_model import BaseModel

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
        new_instance = BaseModel()
        new_instance.save()

        if line == "":
            print ("** class name missing **")

    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and id. Ex: $ show BaseModel 1234-1234-1234."""
        pass    
    def do_destroy(self, line):
        """ Deletes an instance based on the class name and id (save the change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234."""
        pass

    def do_all(self, line):
        """Prints all string representation of all instances based or not on the class name. Ex: $ all BaseModel or $ all"""
        pass

    def do_update(self, line):
        """ Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"."""
        pass




"""Code should not be executed when imported."""    
if __name__ == '__main__':
        HBNBCommand().cmdloop()
