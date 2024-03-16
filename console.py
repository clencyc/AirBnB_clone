#!/usr/bin python3
from models.base_model import BaseModel
import cmd
from models.engine.file_storage import FileStorage
from models import storage



class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the commandline"""
        return True

    def do_EOF(self, arg):
        """Handles CTRL+D signal"""
        return True
    
    def emptyline(self):
        """An empty commandline + ENTER shouldn’t execute anything"""
        pass

    def do_create(self, arg):

        model = {"BaseModel":BaseModel}
        """Creates a new instance of BaseModel, saves it, and prints the id."""
        if not arg:
            print("** class name missing **")
        elif arg not in model:
            print("** class doesn't exist **")
        else:
            new_instance = model[arg]()
            new_instance.save()
            print(new_instance.id)

        

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in storage.all():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            try:
                obj = storage.get(args[0], args[1])
                print(obj)
            except KeyError:
                print("** no instance found **")


    # ... implementation for do_show (provided earlier) ...

    def do_destroy(self, arg):
        """Destroys an instance based on the class name and id."""
        args = arg.split()
        # ... same argument parsing and error handling as in do_show ...
        try:
            obj = storage.get(arg, id)
            storage.delete(obj)
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all instances, or instances of a specific class."""
        args = arg.split()
        if len(args) == 0:
            for obj in storage.all().values():
                print(obj)
        elif args[0] in storage.all():
            for obj in storage.all(args[0]).values():
                print(obj)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        args = arg.split()
        # ... same argument parsing as in do_destroy ...
        if len(args) < 4:
            if len(args) == 3:
                print("** value missing **")
            else:
                print("** attribute name missing **")
        else:
            try:
                obj = storage.get(arg, id)
                attr_name = args[3]
                attr_value = args[4].strip('"')
                try:
                    setattr(obj, attr_name, int(attr_value))
                except ValueError:
                    try:
                        setattr(obj, attr_name, float(attr_value))
                    except ValueError:
                        setattr(obj, attr_name, attr_value)
                storage.save()
            except KeyError:
                print("** no instance found **")

    pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()