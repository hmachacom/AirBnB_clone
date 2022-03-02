#!/usr/bin/python3
import json
from types import new_class


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
        """se guarda el objeto directamente en el diccionario al momento de codificar el JSON se extare con la funcion to_dict"""
        FileStorage.__objects[type(obj).__name__ + "." + obj.id] = obj

    def save(self):
        """_summary_
		"""
        """se crea un dicionario vacio para guardar los datos de los objetos con la funcion to_dict()"""
        new_dict = {}
        with open(FileStorage.__file_path, mode="w") as my_file:
            for key, value in FileStorage.__objects.items():
                new_dict[key] = value.to_dict()
            json.dump(new_dict, my_file)

    def reload(self):
        """_summary_
		"""
        from models.base_model import BaseModel
        from datetime import datetime

        """Se importa la clase aqui para evitar errores de importacion
			ademas se crean nuevamente las instancias apartir del los datos JSON"""
        try:

            with open(FileStorage.__file_path, mode="r") as my_file:
                var = json.load(my_file)
                for key, value in var.items():
                    """este new_class esta pendiente creo que servira mas adelante al igual que key"""
                    new_class = value["__class__"]
                    new_obj = BaseModel(**value)
                    self.new(new_obj)
        except:
            pass

