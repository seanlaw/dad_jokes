#!/usr/bin/env python

import requests
import os
import json
from datetime import datetime
import re

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = os.environ.get("BEARER_TOKEN")


def create_url():
    # Replace with user ID below
    user_id = 905028905026846720
    return "https://api.twitter.com/2/users/{}/tweets".format(user_id)


def get_params():
    # Tweet fields are adjustable.
    # Options include:
    # attachments, author_id, context_annotations,
    # conversation_id, created_at, entities, geo, id,
    # in_reply_to_user_id, lang, non_public_metrics, organic_metrics,
    # possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets,
    # source, text, and withheld
    return {"tweet.fields": "created_at"}


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2UserTweetsPython"
    return r


def connect_to_endpoint(url, params):
    response = requests.request("GET", url, auth=bearer_oauth, params=params)
    # print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()


def print_tweet(tweet):
    print("___")
    text = tweet["text"]
    # text = text.replace("'", '')
    text = text.replace('"', "")
    text = re.sub("\u201c", "", text)
    text = re.sub("\u201d", "", text)
    print(text)
    print("___")
    print()


def main():
    url = create_url()
    params = get_params()
    json_response = connect_to_endpoint(url, params)
    # print(json.dumps(json_response, indent=4, sort_keys=True))

    today = datetime.today()
    yesterday = today - timedelta(days=1)
    two_days_ago = yesterday = today - timedelta(days=2)
    print(f"Date: {today.date()}")
    print("___")
    for tweet in json_response["data"]:
        created_at = datetime.strptime(tweet["created_at"], "%Y-%m-%dT%H:%M:%S.%fZ")
        if today.weekday == 0:  # Monday
            if (
                created_at.date() == today.date()
                or created_at.date() == yesterday.date()
                or created_at.date() == two_days_ago.date()
            ):
                print_tweet(tweet)
        else:
            if (
                created_at.date() == today.date()
                or created_at.date() == yesterday.date()
            ):
                print_tweet(tweet)


if __name__ == "__main__":
    main()
