#!/usr/bin/env python3
""" Return list of schools with a specific topic """

def schools_by_topic(mongo_collection, topic):
    """Find all schools that contain the given topic"""
    return list(mongo_collection.find({"topics": topic}))