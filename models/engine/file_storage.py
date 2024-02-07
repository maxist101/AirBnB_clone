#!/usr/bin/python3
import json
from models.base_model import BaseModel


class FileStorage:
    """
    This class offers functionalities for serializing instances to a JSON file and deserializing a JSON file back to instances.

Attributes:

__file_path (str): The path to the JSON file.
__objects (dict): A dictionary used to store all objects indexed by <class name>.id.
    """
    __file_path = "file.json"
    __objects = {}

    @classmethod
    def _import_all_model_classes(cls):
        """
        Import model classes dynamically.
        """
        from models.user import User
        from models.city import City
        from models.state import State
        from models.place import Place
        from models.amenity import Amenity
        from models.review import Review

    def all(self):
        """
        Returns a dictionary containing all objects.

        Returns:

        dict: A dictionary of all objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        object to the __objects dictionary.

        Args:
        the obj (BaseModel): The object to be added.
        """
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """
        Serialize the __objects dictionary to the JSON file specified by __file_path.
        """
        ob_dict = FileStorage.__objects
        obdict = {obj: ob_dict[obj].to_dict() for obj in ob_dict.keys()}
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(obdict, file)

    def reload(self):
        """
        Deserializes the JSON file into __objects.
        If the JSON file (__file_path) exists, it loads the data and creates
        instances of the corresponding classes; otherwise, it takes no action.
        """
        self._import_all_model_classes()
        try:
            with open(FileStorage.__file_path) as file:
                obdict = json.load(file)
                for obj_id, obj_data in obj_dict.items():
                    class_name = obj_data["__class__"]
                    del obj_data["__class__"]
                    if class_name not in globals():
                        self._import_all_model_classes()
                    model_class = globals()[class_name]
                    self.new(model_class(**obj_data))
        except FileNotFoundError:
            return
