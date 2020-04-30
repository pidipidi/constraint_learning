#!/bin/sh

if [ ! -e .venv-honda ]
then
    # install python3
    sudo apt update
    sudo apt install software-properties-common
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt update
    sudo apt install python3.7

    sudo apt-get install python-virtualenv

    # generate virtual environment
    virtualenv --python=python3.7 .venv
    #.venv/bin/pip install -r requirements.txt
    .venv/bin/python -m pip install --upgrade pip
    
fi    

# for pybullet-gym
.venv/bin/pip install -e ./pybullet-gym

# for spinningup
sudo apt-get install libopenmpi-dev
.venv/bin/pip install -e ./spinningup

