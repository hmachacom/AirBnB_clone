#!/usr/bin/python3
import cmd
from types import new_class
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Class command interpreter """

    prompt = " (hbnb) "
    class_inherit = ["BaseModel", "User"]

    def do_EOF(self, line):
        """ exit the program """
        return True

    def do_quit(self, line):
        """ Quit command to exit the program"""
        return True

    def do_create(self, line):
        """_summary_

        Args:
            line (_type_): _description_
        """

        if line:
            if line == self.class_inherit[0]:
                new_class = BaseModel()
            elif line == self.class_inherit[1]:
                new_class = User() 
            new_class.save()          
            print(new_class.id)  
        else:
            if not self.class_inherit:
                print("** class name missing **")
            else:
                print("** class doesn't exist **")

    def emptyline(self):
        """ an empty line + ENTER shouldn’t execute anything"""
        pass

    def do_show(self, line):
        """_summary_

        Args:
            line (_type_): _description_
        """
        storage.reload()
        to_show = line.split()
        if len(to_show) >= 1:
            if to_show[0] not in self.class_inherit:
                print("** class doesn't exist **")
            elif len(to_show) < 2:
                print("** instance id missing **")
            elif (
                str(to_show[0] + "." + to_show[1])
                not in storage.all().keys()
            ):
                print("** no instance found **")
            else:
                share_class = str(to_show[0] + "." + to_show[1])
                new_dict = storage.all()
                print(new_dict[share_class])
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        """_summary_

        Args:
            line (_type_): _description_
            _class (str, optional): _description_. Defaults to "".
            id (str, optional): _description_. Defaults to "".
        """
        storage.reload()
        to_destroy = line.split()
        if len(to_destroy) >= 1:
            if to_destroy[0] not in self.class_inherit:
                print("** class doesn't exist **")
            elif len(to_destroy) < 2:
                print("** instance id missing **")
            elif (
                str(to_destroy[0] + "." + to_destroy[1])
                not in storage.all().keys()
            ):
                print("** no instance found **")
            else:
                del_class = str(to_destroy[0] + "." + to_destroy[1])
                storage.dic_del(del_class)
                storage.reload()
        else:
            print("** class name missing **")

    def do_all(self, line):
        """_summary_

        Args:
            line (_type_): _description_
        """
        storage.reload()
        to_all = line.split()
        new_list = []
        if len(to_all) >= 1:
            all_class = self.all_class(storage.all())
            if to_all[0] in all_class:
                for key, value in storage.all().items():
                    cls = key.split(".", 1)
                    if to_all[0] == cls[0]:
                        new_list.append(str(value))
                print(new_list)
            else:
                print("** class doesn't exist **")
        else:
            for key, value in storage.all().items():
                new_list.append(str(value))
            print(new_list)

    def all_class(self, dit):
        """_summary_

        Args:
            dit (_type_): _description_
        """
        new_class = []
        for key, value in dit.items():
            tmp = key.split(".", 1)
            new_class.append(tmp[0])
        return new_class


if __name__ == "__main__":
    HBNBCommand().cmdloop()
