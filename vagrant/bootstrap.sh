#!/usr/bin/env bash

apt-get update -y
apt-get install build-essential -y

cd /opt/wwc/tulalens-survey-web
mkdir /opt/tulalens

pip install virtualenv
/usr/local/bin/virtualenv /opt/tulalens --distribute --python=/usr/bin/python3

/opt/tulalens/bin/pip install -r requirements/requirements.txt