#!/bin/bash

# run tshark script
./tshark.sh

# run python script
python project.py .cred

# send prize over ssh
scp .prize hcgong@$1:~/Documents
