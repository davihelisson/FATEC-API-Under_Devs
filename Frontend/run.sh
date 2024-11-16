#!/bin/bash

# script de automatização de criação do ambiente virtual e instalação do flask

if [ -d "venv" ]; then
    echo "Activating virtual environment"
    source venv/bin/activate
else
    echo "Creating virtual environment"
    python3 -m venv venv
    source venv/bin/activate
    echo "Installing Flask"
    pip install flask
fi

echo "Starting Flask server on port 80"
flask run --debug --host=0.0.0.0 --port=80

clear
echo "Deactivating virtual environment"
deactivate