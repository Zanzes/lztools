#!/bin/bash

set -e

if [ $# != 1 ];then
    exit
fi

target=$1

ssh $target "test -e ~/.ssh/id_rsa.pub"

if [ ! $? -eq 0 ]; then
    ssh $target "ssh-keygen -t rsa"
fi

test -e ~/.ssh/id_rsa.pub

if [ ! $? -eq 0 ]; then
    ssh-keygen -t rsa
fi

cat ~/.ssh/id_rsa.pub | ssh $target 'cat >> .ssh/authorized_keys'

