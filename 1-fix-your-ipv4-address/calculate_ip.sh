#!/bin/bash

MY_CURRENT_IP=$(curl -s http://checkip.amazonaws.com/)
IFS='.'  
read -r -a IP_ARR <<<"$MY_CURRENT_IP" 
echo "My current IP-address is ${MY_CURRENT_IP}My fixed IP-address is $((IP_ARR[0] + 1)).$((IP_ARR[1] + 1)).$((IP_ARR[2] + 1)).$((IP_ARR[3] + 1))"
