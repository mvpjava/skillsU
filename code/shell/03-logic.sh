#!/bin/sh

echo "My $0 is starting ..."

# Check required parameters
if [ -z "$1" ]; then
    echo "Error: Missing Directory parameter!"
    exit 1
fi

DIRECTORY_NAME=$1

# Check if directory exists
if [ -d "$DIRECTORY_NAME" ]; then
    echo "Directory exist. Will list files from directory $DIRECTORY_NAME ..."
else
    echo "Directory does not exist. Exiting..."
    exit 1
fi

ls -l $DIRECTORY_NAME

# What happens if we do not pass in anything?

echo "$0 finished"

# Where did the exit go?