#!/usr/bin/python3
from cgitb import strong
from datetime import datetime
from uuid import uuid4
from models import storage


class BaseModel:
    """ that defines all common attributes/methods for other classes
	"""

    def __init__(self, *args, **kwargs):
        """_summary_
		"""
        self.updated_at = datetime.now()
        if len(kwargs) >= 1 and kwargs is not None:
            for key, value in kwargs.items():
                if key == "my_number":
                    self.my_number = value
                if key == "name":
                    self.name = value
                if key == "id":
                    self.id = str(uuid4())
                if key == "created_at":
                    self.created_at = datetime.now()
                if key == "updated_at":
                    self.updated_at = datetime.now()
        else:
            self.created_at = datetime.now()
            self.id = str(uuid4())
            """self.my_number = 0
            self.name = """
            storage.new(self)

    def __str__(self):
        """_summary_

		Returns:
			_type_: _description_
		"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """_summary_
		"""
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """_summary_
		"""
        dic = self.__dict__
        dic['__class__'] = type(self).__name__
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
        return dic
            

