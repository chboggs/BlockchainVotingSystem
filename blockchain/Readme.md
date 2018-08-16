#### Using the Multichain Tool

These are some sample codes which show how the Multichain APIs could be utilized.

The master server is the one that creates the blockchain. Slave servers should join the blockchain.

Here is a sample flow of work:
1. On the master server, run `python create_blockchain.py`
2. On the slave server, run `python join_blockchain.py`. The public key of the slave server should be shown. (Let's call it `SLAVE_KEY`)
3. On the master server, run `python run_blockchain.py SLAVE_KEY`
4. On the slave server, run `python run_blockchain.py`

The `run_blockchain.py` codes are where we want to implement the operations of our blockchain.

By the way, after running these sample codes, you may want to manually kill the `multichaind` daemon.
