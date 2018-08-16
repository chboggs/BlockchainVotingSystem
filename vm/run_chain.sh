#!/bin/bash

MULTICHAIN_DIR="/home/eecs591/multichain-1.0.4"
DATA_DIR="$MULTICHAIN_DIR/server_data"
MULTICHAIN_D="$MULTICHAIN_DIR/multichaind"

sudo ifdown enp0s8; sudo ifdown enp0s3; sudo ifup enp0s3
sudo apt-get update > /dev/null
sudo ifdown enp0s3; sudo ifdown enp0s8; sudo ifup enp0s8

$MULTICHAIN_D vote_chain -datadir=$DATA_DIR -daemon
