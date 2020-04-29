#!/bin/sh

if [ ! -e .venv-honda ]
then
    # install python3
    sudo apt update
    sudo apt install software-properties-common
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt update
    sudo apt install python3.7

    # generate virtual environment
    python3 -m venv .venv
    .venv/bin/pip install -r requirements.txt
    
fi    
