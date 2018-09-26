#!/bin/bash

path="$( cd "$(dirname "$0")" ; pwd -P )"

echo "Saving project requirements"
pip freeze > $path/../requirements.txt