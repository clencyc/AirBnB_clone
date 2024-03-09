import cmd
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in storage.classes:  # Change to correct attribute
            print("** class doesn't exist **")
        else:
            new_obj = storage.classes[args[0]]()
            storage.save()
            print(new_obj.id)


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
        elif args[0] in storage.classes:
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

if __name__ == "__main__":
    HBNBCommand().cmdloop()