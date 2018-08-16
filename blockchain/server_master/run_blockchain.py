import subprocess
import sys

MULTICHAIN_CLI = '../multichain-cli'
CHAIN_NAME = 'election_chain'
DATA_DIR = 'server_data'

# Grant 'connect' permission to the server with the given public key
args = (MULTICHAIN_CLI, CHAIN_NAME, '-datadir=' + DATA_DIR, 'grant', sys.argv[1], 'connect')
popen = subprocess.Popen(args)
popen.wait()

# Next, we can do other blockchain operations in a similar way...
