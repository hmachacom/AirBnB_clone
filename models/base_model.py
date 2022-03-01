#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4
from models import storage


class BaseModel:
    """ that defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """_summary_
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.my_number = 0
        self.updated_at = datetime.now()
        self.name = ""
        if kwargs:
            for key, value in kwargs.items():
                if key == "my_number":
                    self.my_number = value
                if key == "name":
                    self.name = value

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
        return {
            "my_number": self.my_number,
            "__class__": self.__class__.__name__,
            "updated_at": self.updated_at.isoformat(),
            "created_at": self.created_at.isoformat(),
            "name": self.name,
            "id": self.id,
        }

