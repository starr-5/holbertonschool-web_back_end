#!/usr/bin/env python3
""" Update all topics of a school document based on name """

def update_topics(mongo_collection, name, topics):
    """Update the topics field of matching school documents"""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )