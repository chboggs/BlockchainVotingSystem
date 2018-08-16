#!/usr/bin/env python
import argparse
import json
import subprocess

KEY_FILE = 'all_keys_list.json'

parser = argparse.ArgumentParser(description='Run the counting application for the voting system')
parser.add_argument('-m','--multichain', help='path to the multichain CLI',
                    default='../multichain-1.0.4/multichain-cli')
parser.add_argument('-d','--datadir', help='path to the multichain data directory',
                    default='../multichain-1.0.4/server_data')
parser.add_argument('-c','--chain', help='name of the blockchain',
                    default='vote_chain')
parser.add_argument('-s','--stream', help='name of the blockchain stream',
                    default='voting_stream')
commandArgs = parser.parse_args()

listKeyArgs = (commandArgs.multichain, commandArgs.chain, '-datadir={}'.format(commandArgs.datadir),
               'liststreamkeys', commandArgs.stream)
with open(KEY_FILE, 'w') as fd:
    listKeyProc = subprocess.Popen(listKeyArgs, stdout=fd)
    listKeyProc.wait()

allKeys = []
with open(KEY_FILE, 'r') as fd:
    keysDict = json.load(fd)
for element in keysDict:
    allKeys.append(element['key'])

print('{} unique keys have been collected'.format(len(allKeys)))

allVotes = {}

for key in allKeys:
    listItemArgs = (commandArgs.multichain, commandArgs.chain, '-datadir={}'.format(commandArgs.datadir),
                    'liststreamkeyitems', commandArgs.stream, key)
    listItemProc = subprocess.Popen(listItemArgs, stdout=subprocess.PIPE)
    results = listItemProc.communicate()
    itemDict = json.loads(results[0])
    dataHex = itemDict[0]['data']
    dataJson = bytes.fromhex(dataHex).decode('utf-8')
    data = json.loads(dataJson)
    for category, vote in data.items():
        if category not in allVotes:
            allVotes[category] = {}
        if vote not in allVotes[category]:
            allVotes[category][vote] = 0
        allVotes[category][vote] += 1

print(allVotes)
