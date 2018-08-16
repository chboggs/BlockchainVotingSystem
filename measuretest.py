#!/usr/bin/env python
import argparse
import datetime
import json
import os
import subprocess
import time


OUTPUT_FILE = 'time_counts.txt'
KEY_FILE = 'all_keys_list_measurement.json'

parser = argparse.ArgumentParser(description='Run the measurement program to see the size of the blockchain')
parser.add_argument('-m','--multichain', help='path to the multichain CLI',
                    default='../multichain-1.0.4/multichain-cli')
parser.add_argument('-d','--datadir', help='path to the multichain data directory',
                    default='../multichain-1.0.4/server_data')
parser.add_argument('-c','--chain', help='name of the blockchain',
                    default='vote_chain')
parser.add_argument('-s','--stream', help='name of the blockchain stream',
                    default='voting_stream')
parser.add_argument('-l','--limit', type=int, help='limit of when to stop measuring',
                    default=100)
parser.add_argument('-i','--interval', type=int, help='interval of how often to take measurement',
                    default=60)
commandArgs = parser.parse_args()


lastCount = 0
countList = []
listKeyArgs = (commandArgs.multichain, commandArgs.chain, '-datadir={}'.format(commandArgs.datadir),
               'liststreamkeys', commandArgs.stream)

while lastCount < commandArgs.limit - 1:
    time.sleep(commandArgs.interval)
    currentTime = datetime.datetime.utcnow()
    filepath = '{}-{}'.format(lastCount, KEY_FILE)
    with open(filepath, 'w') as fd:
        listKeyProc = subprocess.Popen(listKeyArgs, stdout=fd)
        listKeyProc.wait()
    with open(filepath, 'r') as fd:
        keysDict = json.load(fd)
    lastCount = len(keysDict)
    print('Counted {} keys'.format(lastCount))
    os.remove(filepath)
    formattedTime = currentTime.strftime("%H:%M:%S")
    countList.append((formattedTime, lastCount))

with open(OUTPUT_FILE, 'w') as fd:
    for entry in countList:
        fd.write('{}\t{}\n'.format(entry[0], entry[1]))
