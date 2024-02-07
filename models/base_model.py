#!/usr/bin/python3
"""BaseModel that defines all the common attributes/methods for other classes for the project"""

import uuid
from datetime import datetime
import models

class BaseModel:
    """A model defining common attributes and methods for other classes.
        Attributes: Date format used for date string conversion"""

    def _init_(self, *args, **kwargs):
        """Initializing a new instance of BaseModel
           Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        DATE_FMT = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4()
                self.created_at = datetime.now()
                self.updated_at = datetime.now()
                """ Above, we assigned a unquie identifier, set creation date and update date"""

                if len(kwargs) != 0:
                for key, value in kwargs.items():
                if key in ['created_at', 'updated_at']:
                self._dict_[key] = datetime.strptime(value, DATE_FMT)
                else:
                self._dict_[key] = value
                else:
                """Code to create new instance in storage"""
                models.storage.new(self)

                def _str_(self):
                """Fuction to Returns a string representation of the BaseModel instance"""
                class_nam = self._class.name_
                return "[{}] ({}) {}".format(class_nam, self.id, self._dict_)

                def save(self):
                """Updates the update save the instance storeage"""
                self.updated_at = datetime.today()
                models.storage.save()

                def to_dict(self):
                """fuction that add class information, formate create date and format update date"""
                result_dic = self._dict_.copy()
                result_dic['_class'] = type(self).name_
                result_dic['created_at'] = self.created_at.isoformat()
                result_dic['updated_at'] = self.updated_at.isoformat()
                return result_dic
