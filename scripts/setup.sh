#!/bin/bash

path="$( cd "$(dirname "$0")" ; pwd -P )"

echo "Starting to install dependencies"
pip install -r $path/../requirements.txt

echo "Registering pre-commit hook"

# Create the hook if it doesnt exists
filename=$path/../.git/hooks/pre-commit
test -f $filename || touch $filename

# Copy pre-commit from source
cp $path/pre-commit.sh $filename