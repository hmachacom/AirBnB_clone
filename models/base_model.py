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
        if len(kwargs) >= 1 and kwargs is not None:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
                if key == "created_at" or key == "updated_at":
                    format_string = "%Y-%m-%dT%H:%M:%S.%f"
                    value = datetime.strptime(value, format_string)
                    setattr(self, key, value)
        else:
            self.updated_at = datetime.now()
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
        format_string = "%Y-%m-%dT%H:%M:%S.%f"
        dic = dict(**self.__dict__)
        dic["__class__"] = type(self).__name__
        
        dic["created_at"] = datetime.strptime(self.created_at, format_string).isoformat() if type(self.created_at) == str else self.created_at.isoformat()
        dic["updated_at"] = datetime.strptime(self.updated_at, format_string).isoformat() if type(self.updated_at) == str else self.updated_at.isoformat()
        ''' dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat() '''
        return dic

