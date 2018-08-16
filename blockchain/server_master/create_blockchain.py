import subprocess

MULTICHAIN_UTIL = '../multichain-util'
MULTICHAIN_D = '../multichaind'
CHAIN_NAME = 'election_chain'
DATA_DIR = 'server_data'
PORT = '8000'

# Setting up the blockchain
args = (MULTICHAIN_UTIL, 'create', CHAIN_NAME, '-datadir=' + DATA_DIR, '-default-network-port=' + PORT)
popen = subprocess.Popen(args)
popen.wait()

# Running the daemon
args = (MULTICHAIN_D, CHAIN_NAME, '-datadir=' + DATA_DIR, '-daemon')
popen = subprocess.Popen(args)
popen.wait()
