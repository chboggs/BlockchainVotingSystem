#!/bin/bash

MULTICHAIN_DIR="/home/eecs591/multichain-1.0.4"
DATA_DIR="$MULTICHAIN_DIR/server_data"
MULTICHAIN_CLI="$MULTICHAIN_DIR/multichain-cli"

$MULTICHAIN_CLI vote_chain -datadir=$DATA_DIR subscribe voting_stream
