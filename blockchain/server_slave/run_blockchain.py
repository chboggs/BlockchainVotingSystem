import subprocess

MULTICHAIN_D = '../multichaind'
CHAIN_NAME = 'election_chain'
DATA_DIR = 'server_data'

# Now that the permission has been granted, connect to the master server again
args = (MULTICHAIN_D, CHAIN_NAME, '-datadir=' + DATA_DIR, '-daemon')
popen = subprocess.Popen(args)
popen.wait()

# Next, we can do other blockchain operations in a similar way...
