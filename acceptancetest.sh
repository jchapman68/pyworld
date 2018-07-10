#!/bin/sh

echo Inputs:
echo URL: $URL
echo GREETING: $GREETING

apk add --no-cache curl

pwd

ls -la

wget "$URL" | grep "$GREETING"

echo $GREETING

if [ $? != 0 ] 
then 
    echo fail 
    exit 22
else
    echo found
    exit 0
fi
