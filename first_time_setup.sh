#!/bin/bash

python3.7 setup.py install;
echo ". .lzconfigrc" >> ~/.bashrc;
scatter -v now -r;
echo "Please run the command 'source ~/.bashrc' now";