#!/bin/sh

echo Inputs:
echo URL: $URL
echo GREETING: $GREETING


export PORT=8090

py-world-git/web.py &

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
