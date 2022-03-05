#!/usr/bin/python3
""" HBNBCommand """
import cmd
from types import new_class
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ Class command interpreter """

    prompt = "(hbnb) "
    class_inherit = ["BaseModel", "User", "State", "City",
                     "Amenity", "Place", "Review"]

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
            if line not in self.class_inherit:
                print("** class doesn't exist **")
            else:
                if line == self.class_inherit[0]:
                    new_class = BaseModel()
                elif line == self.class_inherit[1]:
                    new_class = User()
                elif line == self.class_inherit[2]:
                    new_class = State()
                elif line == self.class_inherit[3]:
                    new_class = City()
                elif line == self.class_inherit[4]:
                    new_class = Amenity()
                elif line == self.class_inherit[5]:
                    new_class = Place()
                elif line == self.class_inherit[6]:
                    new_class = Review()
                new_class.save()
                print(new_class.id)
        else:
            print("** class name missing  **")

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

    def do_update(self, line):
        """_summary_

        Args:
            line (_type_): _description_
        """
        storage.reload()
        to_update = line.split()
        if len(to_update) >= 1:
            if len(to_update) == 1:
                print("** instance id missing **")
            elif len(to_update) == 2:
                print("** attribute name missing **")
            elif len(to_update) == 3:
                print("** value missing **")

            elif len(to_update) >= 4:
                if to_update[0] in self.all_class(storage.all()):
                    this_dict = storage.all()
                    this_key = str(to_update[0] + "." + to_update[1])
                    if this_key in this_dict.keys():
                        this_obj = this_dict[this_key]
                        new_dict = this_obj.to_dict()
                        key_attr = to_update[2]
                        value_attr = to_update[3]
                        new_dict[key_attr] = value_attr
                        new_instans = eval(to_update[0])(**new_dict)
                        storage.new(new_instans)
                        storage.save()
                    else:
                        print("** no instance found **")

                else:
                    print("** class doesn't exist **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
