#!/bin/bash

path="$( cd "$(dirname "$0")" ; pwd -P )"

GIT_DIR=$(git rev-parse --git-dir)

echo "Starting to install dependencies"
pip install -r $path/../requirements.txt

echo "Registering pre-commit hook"

# Create the hook if it doesnt exists
filename=$GIT_DIR/hooks/pre-commit
rm -f $filename

# Copy pre-commit from source
ln -s $path/pre-commit.sh $filename