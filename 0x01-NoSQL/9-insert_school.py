#!/usr/bin/env python3
"""
Insert a documnet in python
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new documnet in a collection based on kwargs
    """
    new_documents = mongo_collection.insert_one(kwargs)
    return new_documents.inserted_id
