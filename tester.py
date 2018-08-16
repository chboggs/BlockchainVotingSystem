#!/usr/bin/env python
import argparse
import json
import time
import uniqueid as uid
import voter


parser = argparse.ArgumentParser(description='Run the testing application for the voting system')
parser.add_argument('-t','--template', help='path to the ballot template',
                    default='data/paper_ballot.json')
parser.add_argument('-m','--multichain', help='path to the multichain CLI',
                    default='../multichain-1.0.4/multichain-cli')
parser.add_argument('-d','--datadir', help='path to the multichain data directory',
                    default='../multichain-1.0.4/server_data')
parser.add_argument('-c','--chain', help='name of the blockchain',
                    default='vote_chain')
parser.add_argument('-s','--stream', help='name of the blockchain stream',
                    default='voting_stream')
parser.add_argument('-p','--publickey', help='path to the public key',
                    default='data/publickey.der')
parser.add_argument('-r','--privatekey', help='path to the private key',
                    default='data/privatekey.p8')
parser.add_argument('-v', '--votes', type=int, help='number of votes to cast',
                    default=100)
parser.add_argument('-o', '--outcounts', help='path to output voting count file',
                    default='local_counts.json')
parser.add_argument('-i', '--interval', type=float, help='interval of how often to write a vote',
                    default=1.0)
args = parser.parse_args()

vInstance = voter.Voter(args.template, args.multichain, args.datadir, args.chain, args.stream, args.publickey, args.interval)
voteCount = {}
startTime = time.time()

for i in range(args.votes):
    print('Iteration {}'.format(i))
    # Create a random ballot and add it to the blockchain
    newID = uid.generateID(args.privatekey)
    ballot = vInstance.autoFillBallot()
    vInstance.processBallot(ballot, newID)
    # Save the results of the ballot locally
    for position, vote in ballot.items():
        if position not in voteCount:
            voteCount[position] = {}
        if vote not in voteCount[position]:
            voteCount[position][vote] = 0
        voteCount[position][vote] += 1
    time.sleep(args.interval)

while not vInstance.isFinished():
    time.sleep(args.interval)

duration = time.time() - startTime
print('{} seconds elapsed'.format(duration))
with open(args.outcounts, 'w') as fd:
    json.dump(voteCount, fd)
print('Wrote local vote counts to {}'.format(args.outcounts))
