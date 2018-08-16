import subprocess

MULTICHAIN_D = '../multichaind'
CHAIN_NAME = 'election_chain'
DATA_DIR = 'server_data'
MASTER_IP = '141.212.111.216'
MASTER_PORT = '8000'

# Connect to the master server
args = (MULTICHAIN_D, CHAIN_NAME + '@' + MASTER_IP + ':' + MASTER_PORT, '-datadir=' + DATA_DIR, '-daemon')
popen = subprocess.Popen(args)
popen.wait()

# Public key should be displayed
