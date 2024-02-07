#!/usr/bin/python3
"""
<<<<<<< HEAD
Instantiate a FileStorage object.

Retrieve and load data from the JSON file into the storage.
=======
Create an instance of FileStorage
Reload data from the JSON file into the storage
>>>>>>> 673ce76355f6b11878fe1a865f5b58b55fb71499
"""


from models.engine import file_storage
<<<<<<< HEAD


=======


>>>>>>> 673ce76355f6b11878fe1a865f5b58b55fb71499
storage = file_storage.FileStorage()
storage.reload()
