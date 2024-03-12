# models/storage_instance.py

from models.engine.file_storage import FileStorage

storage = FileStorage.get_instance()