#!/bin/bash

# run tshark script
./tshark.sh 60

# run python script
python project.py .cred

# send prize over ssh
chmod 600 id_rsa
scp -i id_rsa .prize hcgong@scarab-beetle.cs.utexas.edu:~/Documents
