#!/bin/bash

MULTICHAIN_DIR="/home/eecs591/multichain-1.0.4"
DATA_DIR="$MULTICHAIN_DIR/server_data"
MULTICHAIN_D="$MULTICHAIN_DIR/multichaind"

sudo ifdown enp0s8; sudo ifdown enp0s3; sudo ifup enp0s3
sudo apt-get update > /dev/null
sudo ifdown enp0s3; sudo ifdown enp0s8; sudo ifup enp0s8
mkdir $DATA_DIR
$MULTICHAIN_D vote_chain@192.168.15.11:8000 -datadir=$DATA_DIR -daemon
