#!/bin/sh

echo Inputs:
echo URL: $URL
echo GREETING: $GREETING

export FLASK_APP=web.py
export PORT="8090"

cd py-world-git

pip install -r dependency

flask run --port=$PORT &

curl -sSf "$URL:$PORT" | grep "$GREETING"

echo $GREETING

if [ $? != 0 ] 
then 
    echo fail 
    exit 22
else
    echo found
    exit 0
fi
