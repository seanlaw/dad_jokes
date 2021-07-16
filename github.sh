#!/bin/sh

MS_TEAMS_WEBHOOK="$1"
export 'BEARER_TOKEN'="$2"
HOSTNAME="Github Actions"
#DAD_JOKE=`python3 get_dad_jokes.py 2> /dev/null`
DAD_JOKE=`python3 get_dad_jokes.py`
DAD_JOKE="TEST"

curl -k -X POST -H 'Content-type: application/json' --data "{\"text\":\"Server: $HOSTNAME\n\n$DAD_JOKE\n\n\"}" $MS_TEAMS_WEBHOOK -o /dev/null
