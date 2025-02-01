#!/bin/sh

DIRECTORY_NAME=$1

echo "My $0 is starting and will list files from directory $DIRECTORY_NAME ..."

ls -l $DIRECTORY_NAME

# What happens if we do not pass in anything?

echo "$0 finished"

# Where did the exit go?