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
		"""se exyrae directamente el dicionario aparti de la funcion to_dict() """
		FileStorage.__objects[str(obj.__class__.__name__) + "." + str(obj.id)] = obj.to_dict()

	def save(self):
		"""_summary_
		"""
		"""con la correccion de la funcion new() se pasa directamente el dicionario y no presenta problemas """
		with open(FileStorage.__file_path, mode="a") as my_file:
			json.dump(FileStorage.__objects, my_file, indent=0)

	def reload(self):
		"""_summary_
		"""
		try:
			with open(FileStorage.__file_path, mode="r") as my_file:
				var = json.load(my_file)
				FileStorage.__objects = var
		except :
			pass
		

