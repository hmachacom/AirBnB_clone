#!/usr/bin/python3
""" Class BaseModels """

from datetime import datetime
from uuid import uuid4
from models import storage


class BaseModel:
    """ that defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Arguments
            - **kwargs: dictionary that contains all arguments by key/value
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
            storage.new(self)

    def __str__(self):
        """str representation of an object
        """
        return (
            "[{}] ({}) {}"
            .format(self.__class__.__name__, self.id, self.__dict__)
        )

    def save(self):
        """update the public instance attribute updated_at
            whit the current date time
        """
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """ returns a dictionary containing
            all keys/values of __dict__ of the instance
        """
        format_string = "%Y-%m-%dT%H:%M:%S.%f"
        dic = dict(**self.__dict__)
        dic["__class__"] = type(self).__name__

        dic["created_at"] = (
            datetime.strptime(self.created_at, format_string).isoformat()
            if type(self.created_at) == str
            else self.created_at.isoformat()
        )
        dic["updated_at"] = (
            datetime.strptime(self.updated_at, format_string).isoformat()
            if type(self.updated_at) == str
            else self.updated_at.isoformat()
        )
        return dic
