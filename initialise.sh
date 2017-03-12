#!/usr/bin/env bash
# Requirements:
# A. virtualenv # $ pip install virtualenv
# B. python3    # add to apt-get repository then install

# If we specify
#if [[ -z $1 ]]
#then
#    VIRTUAL_ENV_DIRECTORY='virtualenv'
#else
#    VIRTUAL_ENV_DIRECTORY=$1
#fi
venv='venv'

# Create the virtual_env directory if it doesn't exist already
if [[ ! -e $venv ]]
then
    echo Creating directory $venv
    mkdir $venv

    python3 -m virtualenv $venv
fi

echo Activating Virtual environment at $venv/bin/activate
. $venv/bin/activate

echo Installing All Requirements
pip install -r requirements.txt

