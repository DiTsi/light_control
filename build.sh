#!/bin/bash

docker build -t smart_light:latest .
docker save smart_light:latest -o ansible/smart_light_latest.dckr
cd ansible && ansible-playbook -i hosts smart_light.yml
