import argparse
import zipfile
import requests
import subprocess
import os
import pprint
import re
from pymongo import MongoClient
from io import BytesIO


def import_data_from_csv():
    result = requests.get("http://cs.stanford.edu/people/alecmgo/trainingandtestdata.zip")
    zip_file = zipfile.ZipFile(BytesIO(result.content))
    zip_file.extractall()

    cwd = os.getcwd()
    path_to_file = os.path.join(
        cwd, "training.1600000.processed.noemoticon.csv")

    subprocess.run(["mongoimport", "--drop", "--db", "social_net", "--collection",
                    "tweets", "--type", "csv", "--file", path_to_file, 
                    "--fields", "polarity,id,date,query,user,text"])


def unique_users(tweets):
    return len(tweets.distinct("user"))


def links_to_users_the_most(tweets):
    regex = re.compile("@\w+", re.IGNORECASE)

    return tweets.aggregate([
        {
            "$match": {
                "text": {
                    "$regex": regex
                }
            }
        },
        {
            "$group": {
                "_id": "$user",
                "count": {
                    "$sum": 1
                }
            }
        },
        {
            "$sort": {
                "count": -1
            }
        },
        {
            "$limit": 10
        }
    ])


def most_mentioned_users(tweets):
    regex = re.compile("@\w+", re.IGNORECASE)

    results = tweets.aggregate([
        {
            "$match": {
                "text": {
                    "$regex": regex
                }
            }
        }
    ])

    mentioned_users = dict()
    for document in results:
        mention = re.match(regex, document["text"])
        if mention:
            username = mention.group(0)
            mentioned_users.setdefault(username, 0)
            mentioned_users[username] += 1

    return sorted(mentioned_users.items(), key=lambda item: item[1])[-1:-6:-1]


def most_active_users(tweets):
    return tweets.aggregate([
        {
            "$group": {
                "_id": "$user",
                "count": {
                    "$sum": 1
                }
            }
        },
        {
            "$sort": {
                "count": -1
            }
        },
        {
            "$limit": 10
        }
    ])


def most_polarizing_users(tweets):
    return tweets.aggregate([
        {
            "$facet": {
                "grumpy": [
                    {
                        "$match": {
                            "polarity": 0
                        }
                    },
                    {
                        "$group": {
                            "_id": "$user",
                            "count": {
                                "$sum": 1
                            }
                        }
                    },
                    {
                        "$sort": {
                            "count": -1
                        }
                    },
                    {
                        "$limit": 5
                    }
                ],
                "happy": [
                    {
                        "$match": {
                            "polarity": 4
                        }
                    },
                    {
                        "$group": {
                            "_id": "$user",
                            "count": {
                                "$sum": 1
                            }
                        }
                    },
                    {
                        "$sort": {
                            "count": -1
                        }
                    },
                    {
                        "$limit": 5
                    }
                ]
            }
        }
    ])


def main():
    if not os.path.isfile("training.1600000.processed.noemoticon.csv"):
        import_data_from_csv()
    client = MongoClient()
    db = client["social_net"]
    tweets = db["tweets"]

    print("\nThe number of unique users is " + str(unique_users(tweets)) + "\n")
    print("The top ten users who link the most to other users are:" + "\n")
    for user in links_to_users_the_most(tweets):
        print(f"{user['_id']} — {user['count']}")
    print("\nThe top five most mentioned users are:" + "\n")
    for user in most_mentioned_users(tweets):
        print(f"{user[0]} — {user[1]}")
    print("\nThe top ten most active users are:" + "\n")
    for user in most_active_users(tweets):
        print(f"{user['_id']} — {user['count']}")
    print("\nThe five most grumpy and five most happy users are: " + "\n")
    for user in most_polarizing_users(tweets):
        pprint.pprint(user)
    print("\n")

    

if __name__ == "__main__":
    main()
