#!/bin/bash

# run tshark script
./tshark.sh

# run python script
python project.py .cred

# send prize over ssh
scp -i id_rsa .prize hcgong@$1:~/Documents
