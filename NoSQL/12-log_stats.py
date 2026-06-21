#!/usr/bin/env python3
""" Log stats from MongoDB nginx collection """

from pymongo import MongoClient


def print_nginx_stats():
    client = MongoClient("mongodb://127.0.0.1:27017")
    collection = client.logs.nginx

    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for m in methods:
        count = collection.count_documents({"method": m})
        print(f"\tmethod {m}: {count}")

    status_check = collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check} status check")


if __name__ == "__main__":
    print_nginx_stats()