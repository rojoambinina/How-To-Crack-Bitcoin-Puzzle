import random
from random import SystemRandom
import secrets
from bit import *
from bit.format import bytes_to_wif
from binascii import hexlify
import multiprocessing
from multiprocessing import Pool
import atexit
from time import time
from datetime import timedelta, datetime


def seconds_to_str(elapsed=None):
    if elapsed is None:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    else:
        return str(timedelta(seconds=elapsed))


def log(txt, elapsed=None):
    colour_cyan = '\033[36m'
    colour_reset = '\033[0;0;39m'
    colour_red = '\033[31m'
    print('\n ' + colour_cyan + '  [TIMING]> [' + seconds_to_str() + '] ----> ' + txt + '\n' + colour_reset)
    if elapsed:
        print("\n " + colour_red + " [TIMING]> Elapsed time ==> " + elapsed + "\n" + colour_reset)


def end_log():
    end = time()
    elapsed = end-start
    log("End Program", seconds_to_str(elapsed))


start = time()
atexit.register(end_log)
log("Start Program")

print("Loading Puzzle TXT Please Wait and Good Luck...")
with open("puzzle.txt","r") as m: #List of Puzzle Addresses 1-160
    add = m.read().split()
add= set(add)
  
r = 0
cores=1 #CPU Control Set Cores

def seek(r):
        while True:
            ran = secrets.SystemRandom().randrange(1,1023)     #TestScan # Already found  #Use Examples 
            key1 = Key.from_int(ran)
            wif = bytes_to_wif(key1.to_bytes(), compressed=False) #Uncompressed WIF
            wif2 = bytes_to_wif(key1.to_bytes(), compressed=True) #compressed WIF
            key2 = Key(wif)
            caddr = key1.address #Legacy compressed address
            uaddr = key2.address #Legacy uncompressed address
            myhex = "%064x" % ran
            private_key = myhex[:64]
            if caddr in add:
                print ("Nice One Found!!!",ran, caddr, wif2, private_key) #Legacy compressed address
                s1 = str(ran)
                s2 = caddr
                s3 = wif2
                s4 = private_key
                f=open(u"CompressedWinner.txt","a") #Output File of Legacy compressed Wallet Found
                f.write(s1+":"+s2+":"+s3+":"+s4)
                f.write("\n")
                f.close()
                continue #break or continue
            if uaddr in add:
                print ("Nice One Found!!!",ran, uaddr, wif, private_key) #Legacy uncompressed address
                s1 = str(ran)
                s2 = uaddr
                s3 = wif
                s4 = private_key
                f=open(u"UncompressedWinner.txt","a") #Output File of Legacy uncompressed Wallet Found
                f.write(s1+":"+s2+":"+s3+":"+s4)
                f.write("\n")
                f.close()
                continue #break or continue
            else:
                colour_cyan = '\033[36m'
                colour_reset = '\033[0;0;39m'
                colour_red = '\033[31m'
                print ("\n " + colour_cyan + " RandomSearchPuzzle -----" + colour_red + " Random Search for Bitcoin Puzzle Wallets " + colour_cyan + "-----RandomSearchPuzzle "  + colour_reset) # Running Display Output
                print (myhex)
                print (wif2)
                print (caddr)
                print (wif)
                print (uaddr)
                print(colour_cyan + seconds_to_str())

#CPU Control Command
if __name__ == '__main__':
        jobs = []
        for r in range(cores):
                p = multiprocessing.Process(target=seek, args=(r,))
                jobs.append(p)
                p.start()