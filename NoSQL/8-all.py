#!/usr/bin/env python3
""" List all documents in a collection """

def list_all(mongo_collection):
    """Return all documents in the collection or empty list if none"""
    if mongo_collection is None:
        return []

    return list(mongo_collection.find())