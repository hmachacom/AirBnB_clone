#!/usr/bin/python3
import json


class FileStorage:
    """_summary_
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """_summary_
        """
        return FileStorage.__objects

    def new(self, obj):
        """_summary_

        Args:
            obj (_type_): _description_
        """
        """Creo que asi es """
        FileStorage.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """_summary_
        """
        """Nose como hacerlo"""
        with open(FileStorage.__file_path, mode="w") as my_file:
            # my_file.write(json.dumps(FileStorage.__objects))
            for cl in FileStorage.__objects.values():
                json.dump(cl.to_dict(), my_file)

    def reload(self):
        """_summary_
        """
        try:
            with open(FileStorage.__file_path, mode="r") as my_file:
                return json.load(my_file.read())
        except:
            pass

