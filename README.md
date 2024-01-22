# HOW TO CRACK BITCOIN PUZZLE

When I was looking for my private key online, I came across the result of my research on this website www.privatekeys.pw and what was funny, when I typed my private key on the search form, the platform returned 6 privates keys found including mine, WoW, they have everything.

In the tools menu, many people desperately use the online scanner tool and scan billions and billions of keys using the database at https://privatekeys.pw/scanner and no one still finds the correct private key hex of **#66 puzzle address**, while 9,223,372,036,854,775,808 keys required to crack #64 address, to solve this riddle is may be to specify a minimum start number of 10,000,000,000,000,000,000 and a maximum stop number of 100,000,000,000,000,000,000,000,000 to get the 17 or 18 last characters of the Hex private key.

## What is a Bitcoin Puzzle?

In 2015, in order to show the hugeness of the private key space (or maybe just for fun), someone created a “puzzle” where he chose keys in a certain smaller space and sent increasing amounts to each of those keys like this:

20 ≤ random key < 21 — 0.001 BTC      
21 ≤ random key < 22 — 0.002 BTC      
23 ≤ random key < 23 — 0.003 BTC        
…           
2255 ≤ random key < 2256 — 0.256 BTC         
(total 32.896 BTC)        

As of June 2020, first 63 and #65, #70, #75, #80, #85, #90, #95, #100, #105, #110, #115 addresses have been cracked.

Check for yourself on the website https://privatekeys.pw/puzzles/bitcoin-puzzle-tx and some private keys have already been found, but others have yet to be calculated. But you wonder how do we calculate this bitcoin puzzle to obtain the private key and be able to transfer the balance.

To answer to this question, we are going to use codes made with python, and there are 6 differents ways to calculate bitcoin address puzzle:

## Random Search for Bitcoin Puzzle Wallets
![RandomSearchPuzzle](https://user-images.githubusercontent.com/89576432/214027314-3370a890-054f-4997-b19e-c80cb633e93d.png)

Because I am a nice guy, I have already prepared the list of puzzle bitcoin addresses that are not yet found in the **puzzle.txt** file.

And when you run the code in your terminal, you need to type these commands below:

**py RandomSearchPuzzle.py**

## Sequential Search for Bitcoin Puzzle Wallets
![SequentialSearchPuzzle](https://user-images.githubusercontent.com/89576432/214027761-a9a7eebf-0d5c-467f-aca4-532dc6d611bf.png)

When you run SequentialSearchPuzzle.py, you must specify a minimum start number and a maximum stop number to have a good calculation and then the program generates the bitcoin addresses and private key.

To run the code in your terminal, you need to type these commands below:

**py SequentialSearchPuzzle.py**

## Random Search for Bitcoin and ETH Puzzle Wallets
![RandomSearchBitcoinETH](https://user-images.githubusercontent.com/89576432/214027114-a51c3f80-802c-41af-810e-7f1d1d1be269.png)

Because I am still generous, I have already prepared a mix file of Bitcoin and Ethereum addresses for you, you only have to download the **BtcEthList.txt** file.

And to run the code in your terminal, you need to type these commands below:

**py RandomSearchBitcoinETH.py**

## Sequential Search for Bitcoin and ETH Puzzle Wallets
![SequentialSearchBitcoinETH](https://user-images.githubusercontent.com/89576432/214027626-22821319-427b-42cd-b270-93b43ad746c2.png)

To use the code, you must specify a minimum start number and a maximum stop number to have a good calculation and then the program generates the bitcoin addresses and private key.

And to run the code in your terminal, you need to type these commands below:

**py SequentialSearchBitcoinETH.py**

## Random Search for Bitcoin with Balance Checker
![RandomSearchBitcoinBalance](https://user-images.githubusercontent.com/89576432/214026909-f929d469-c37b-4e82-93b9-ceedbf73a798.png)

When you run RandomSearchBitcoinBalance.py you must specify a minimum start number and a maximum stop number to have a good calculation and then the program generates the bitcoin addresses and private key.

And to run the code in your terminal, you need to type these commands below:

**py RandomSearchBitcoinBalance.py**

## Sequential search for Bitcoin Wallet with Balance Checker
![SequentialSearchBitcoinBalance](https://user-images.githubusercontent.com/89576432/214027464-ecbf7ac5-58f9-416f-8112-0dba2325e4c0.png)

When you run SequentialSearchBitcoinBalance.py you must also specify a minimum start number and a maximum stop number to have a good calculation and then the program generates the bitcoin addresses and private key.

And to run the code in your terminal, you need to type these commands below:

**py SequentialSearchBitcoinBalance.py**


## Install dependencies
To be able to use these codes, you must install all the modules just by typing in your terminal the command below:

**pip3 install bit chainside-btcpy** 

or 

**pip3 install bit chainside-btcpy eth_keys eth-hash[pycryptodome]**
