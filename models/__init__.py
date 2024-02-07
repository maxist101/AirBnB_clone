#!/usr/bin/python3
"""
This script initializes a FileStorage instance and reloads data from a JSON file into the storage.
"""

from models.engine.file_storage import FileStorage

if __name__ == "__main__":
    storage = FileStorage()
    storage.reload()

