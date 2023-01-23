# BITCOIN PUZZLE

When I was looking for my private key online, I came across the result of my search on this website www.privatekeys.pw and what is funny, when I typed my private key on the search form, the platform returned 6 private keys found including mine, ai ai ai, they have everything.

Many also use the online scanner tool and scan billions and billions of keys using the database at https://privatekeys.pw/scanner and no one still finds the correct private key hex of the puzzle #66, the solution may be to specify a minimum start number with 10,000,000,000,000,000,000 and stop at the maximum number with 100,000,000,000,000,000,000,000,000 to get the 17 and 18 last characters of the Hex private key.

## What is a Bitcoin puzzle?

In 2015, in order to show the hugeness of the private key space (or maybe just for fun), someone created a “puzzle” where he chose keys in a certain smaller space and sent increasing amounts to each of those keys like this:

20 ≤ random key < 21 — 0.001 BTC
21 ≤ random key < 22 — 0.002 BTC
23 ≤ random key < 23 — 0.003 BTC
…
2255 ≤ random key < 2256 — 0.256 BTC
(total 32.896 BTC)

As of June 2020, first 63 and #65, #70, #75, #80, #85, #90, #95, #100, #105, #110, #115 addresses have been cracked. People are still trying to crack #64 address, which requires scanning 9,223,372,036,854,775,808 keys.

Check for yourself on the website https://privatekeys.pw/puzzles/bitcoin-puzzle-tx and some private keys have already been found, but others have yet to be calculated. But you wonder how do we calculate this bitcoin puzzle to obtain the private key and be able to transfer the balance.

To answer your question, we are going to use codes made with python, and there are 6 differents ways to calculate bitcoin addresse puzzle:

### Random Search Puzzle
Random Search for Bitcoin Puzzle Wallets
Because I am a nice guy, I have already prepared the list of puzzle bitcoin addresses that are not yet found in the puzzle.txt file.

And when you run the code in your terminal, you need to type these commands below:

**py RandomSearchPuzzle.py**




### Sequential Search Puzzle
Sequential Search for Bitcoin Puzzle Wallets
When you run SequentialSearchPuzzle.py, you must specify a minimum start number and a maximum stop number to have a good calculation and then the program generates the bitcoin addresses and private key.

To run the code in your terminal, you need to type these commands below:

**py SequentialSearchPuzzle.py**





### Random Search Bitcoin and ETH
Random Search for Bitcoin and ETH Puzzle Wallets
Because I am still generous, I have already prepared a mix file of Bitcoin and Ethereum addresses for you, you only have to download the BtcEthList.txt file

And to run the code in your terminal, you need to type these commands below:

**py RandomSearchBitcoinETH.py**





### Sequential Search Bitcoin and ETH
Sequential Search for Bitcoin and ETH Puzzle Wallets
To use the code, you must specify a minimum start number and a maximum stop number to have a good calculation and then the program generates the bitcoin addresses and private key.

And to run the code in your terminal, you need to type these commands below:

**py SequentialSearchBitcoinETH.py**





### Random Search Bitcoin Balance
Random Search for Bitcoin With Balance Checker
When you run RandomSearchBitcoinBalance.py you must specify a minimum start number and a maximum stop number to have a good calculation and then the program generates the bitcoin addresses and private key.

And to run the code in your terminal, you need to type these commands below:

**py RandomSearchBitcoinBalance.py**




### Sequential Search Bitcoin Balance
Sequential search for Bitcoin Wallet With Balance Checker
When you run SequentialSearchBitcoinBalance.py you must also specify a minimum start number and a maximum stop number to have a good calculation and then the program generates the bitcoin addresses and private key.

And to run the code in your terminal, you need to type these commands below:

**py SequentialSearchBitcoinBalance.py**




## Use:
To be able to use these codes, you must install all the modules just by typing in your terminal the command below:

### pip3 install bit chainside-btcpy 
or 
### pip3 install bit chainside-btcpy eth_keys eth-hash[pycryptodome]
