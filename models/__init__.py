#!/usr/bin/python3
"""
Instantiate a FileStorage object.

Retrieve and load data from the JSON file into the storage.
"""


from models.engine import file_storage


storage = file_storage.FileStorage()
storage.reload()
