#!/bin/sh

echo Inputs:
echo URL: $URL
echo GREETING: $GREETING

apk add --no-cache curl

which python
pwd

ls -la

curl -sSf "$URL" | grep "$GREETING"

if [ $? != 0 ] 
then 
    echo fail 
    exit 22
else
    echo found
    exit 0
fi
