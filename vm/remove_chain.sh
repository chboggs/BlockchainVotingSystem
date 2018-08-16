#!/bin/bash

DATA_DIR="/home/eecs591/multichain-1.0.4/server_data"

killall multichaind
sleep 2s
rm -r $DATA_DIR
