#!/bin/sh

set -eu

echo Inputs:
echo HOST: $HOST
echo URL: $URL
echo NAME: $NAME

NAME=$(curl -sSf "$HOST/$URL/$NAME" | grep "$NAME")

echo $NAME

if [ $? != 0 ] 
then 
    echo fail 
    exit 22
else
    echo found
    exit 0
fi
