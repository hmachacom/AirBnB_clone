#!/usr/bin/python3
""" Filestorage Class """
import json
from types import new_class


class FileStorage:
    """ Filestorage Class
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns dictionary
        """
        return FileStorage.__objects

    def dic_del(self, key):
        """_summary_

        Args:
            key (_type_): _description_
        """
        if key in self.__objects.keys():
            del self.__objects[key]
        self.save()

    def new(self, obj):
        """ Sets in __objects the obj with
            key <obj class name>.id
        """
        FileStorage.__objects[type(obj).__name__ + "." + obj.id] = obj

    def save(self):
        """ Serializes __objects to the JSON file
        """
        new_dict = {}
        with open(FileStorage.__file_path, mode="w") as my_file:
            for key, value in FileStorage.__objects.items():
                new_dict[key] = value.to_dict()
            json.dump(new_dict, my_file)

    def reload(self):
        """ Deserializes the JSON file to __objects
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        try:

            with open(FileStorage.__file_path, mode="r") as my_file:
                var = json.load(my_file)
                for key, value in var.items():
                    new_class = value["__class__"]
                    new_obj = eval(new_class)(**value)
                    self.new(new_obj)
        except Exception:
            pass
