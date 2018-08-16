# Blockchain Voting System

This research project proposes voting in polling stations using machines that use a blockchain (via MultiChain) to safely store immutable ballot records and allow for quick parallel counting.

There are six parts: the program that generates a unique one-time ID (a ticket for voting, essentially) for a registered voter at the polling station; the library that cryptographically generated the ID; the program that takes in votes for the actual ballots then enters the record on the blockchain; the program that reads the blockchain and counts all votes; the program that is used for testing all parts of the project together; the program for measuring the test and counting the time votes observed on the chain at each interval.

The code is written for Python 3.6.

Original repo: https://github.com/tiberiuvs/eecs591research

## ID Library
`uniqueid.py` is a library that can be imported by the other programs to support creating unique IDs and validating unique IDs. It can create a unique ID using a timestamp and private key then returns the hexdump. It can also verify a unique ID is valid by the hexdump. Uses the C++ execultables that must be compiled in the `cpp` directory.

## ID Generator Program
`generator.py` is a very simple standalone program that uses the ID libary to generate and print the contents of a new unique ID upon hitting enter.

## Voter Program
`voter.py` is the program that does the grunt work. At initialization, it reads in the paper ballot to know what and how to ask the user polling questions then later construct the ballot record data structure that is used on the blockchain.

It supports being run as a standalone program and also being imported by the tester, therefore the core functionality is implemented in a Class that stores ballot data and is able to run functions to get/enter ballots.

## Counter Program
`counter.py` is the program that iterates over every block in the blockchain, ballot record in the block, and aggregates votes for each item voted on. It outputs one single file that has a count for every item voted on by the entire state, with regional prefixes intact.

## Tester Program
`tester.py` is a program that is used to test for correctness and throughput in the system. It repeatedly generates a new ID, fills in a sample ballot randomly, then adds that ballot to the blockchain at a certain interval for a certain number of iterations.

## Measurement program
`measuretest.py` is the program that is to be run on a separate machine that also has access to the blockchain. It queries the blockchain to see the number of accepted votes, then sleeps for a given interval of time.

## Other necessary data

### Public/private keys
The machine used to generate IDs at each individual polling station must create a public/private key pair. The private key is stored on that machine and the public key is distributed to and stored on each voting machine in that polling station.

### Paper ballot format
The templated ballot is saved in a JSON format and is published prior to the election. It allows for statewide/national elections, regional elections, and yes/no votes on reginal propositions. This paper ballot template is used by the voter program to ask the user the correct questions and assemble a ballot record. Regional questions are prefixed by `REGIONID//` where each district or region within the state has its own unique ID.
A sample paper ballot is stored in `data/paper_ballot.json`.
The template is as follows:
```
{
    "elections":
    [
        {
            "position": "REGIONID//POSITION_TITLE",
            "options": [{"1": "NAME"}, {"2": "NAME"}],
            "writein": true
        },
        {
            "position": "REGIONID//POSITION_TITLE2",
            "options": [{"1": "NAME"}, {"2": "NAME"}],
            "writein": false
        }
    ],
    "propositions":
    [
        {
            "proposition": "REGIONID//PROP_TITLE",
            "description": "Description of what it means"
        },
        {
            "proposition": "REGIONID//PROP_TITLE",
            "description": "Description of what it means"
        }
    ]
}
```

### Ballot record data structure
This data structure is stored by the voter program in memory and later is exported to JSON to write to the blockchain. It aggregates all votes the user cast together, where values may be names or true/false values.
The template is as follows:
```
{
    "votes":
    [
        {"REGIONID//title": "value"},
        {"title": "value"},
        {"title": "value"}
    ]
}
```

### Counting record format
This format is output by the counter at the very end. The template is as follows:
```
{
    "votes":
    [
        {"REGIONID//title": 1},
        {"title": 1},
        {"title": 1}
    ]
}
```

### Multichain parameters
After experimentation, the agreed on parameters for the blockchain data stream are
```
-target-block-time=2
-mining-turnover=0.0
-mining-diversity=1.0
```
