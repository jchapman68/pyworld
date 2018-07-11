#!/bin/sh

echo Inputs:
echo HOST: $HOST
echo URL: $URL
echo NAME: $NAME

export FLASK_APP=web.py
export PORT="8090"

cd py-world-git

pip install -r requirements

nohup flask run --port=$PORT & > /dev/null 2>&1
sleep 5

curl -sSf "$HOST:$PORT/$URL/$NAME" | grep "$NAME"

echo $NAME

set -eu

if [ $? != 0 ] 
then 
    echo fail 
    exit 22
else
    echo found
    exit 0
fi
