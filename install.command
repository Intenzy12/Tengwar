#!/bin/bash

if [ -z $(command -v python3) ]
then
	printf '\033[38;2;200;20;20mError \033[39mPlease install python3 before using'
else
	python3 -m venv venv
	source ./venv/bin/activate
	pip install -r ./requirements.txt
fi
#h