from bit import *
from bit.format import bytes_to_wif
from binascii import hexlify
import eth_keys
from eth_keys import keys
from btcpy.structs.crypto import PublicKey
from btcpy.structs.address import P2wpkhAddress
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
filename ='puzzle.txt' #List of Address starting1 3 bc1 and ETH

with open(filename) as f:
    add = f.read().split()
add = set(add)
       

x=int(input("'start range Min 1-115792089237316195423570985008687907852837564279074904382605163141518161494335 -> "))
y=int(input("stop range Max 115792089237316195423570985008687907852837564279074904382605163141518161494336 -> "))

r = 0
cores=1 #CPU Control Set Cores

def seek(r):
    F = []
    P = x
    while P<y:
            P+=1
            ran = P 
            key1 = Key.from_int(ran)
            wif = bytes_to_wif(key1.to_bytes(), compressed=False) #Uncompressed WIF
            wif2 = bytes_to_wif(key1.to_bytes(), compressed=True) #compressed WIF
            key2 = Key(wif)
            caddr = key1.address											#Legacy compressed address
            uaddr = key2.address											#Legacy uncompressed address
            saddr = key1.segwit_address										#Segwit address
            pub1 = hexlify(key1.public_key).decode()
            pub2 = hexlify(key2.public_key).decode()
            pubk1 = PublicKey.unhexlify(pub1)
            pubk2 = PublicKey.unhexlify(pub2)
            bcaddr = P2wpkhAddress(pubk1.hash(), version=0, mainnet=True)	#Segwit (bech32) compressed address
            buaddr = P2wpkhAddress(pubk2.hash(), version=0, mainnet=True)	#Segwit (bech32) uncompressed address
            myhex = "%064x" % ran
            private_key = myhex[:64]
            private_key_bytes = bytes.fromhex(private_key)
            public_key_hex = keys.PrivateKey(private_key_bytes).public_key
            public_key_bytes = bytes.fromhex(str(public_key_hex)[2:])
            eaddr = keys.PublicKey(public_key_bytes).to_address()			#Eth address
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
            if saddr in add:
                print ("Nice One Found!!!",ran, saddr, wif, private_key) #Segwit address
                s1 = str(ran)
                s2 = saddr
                s3 = wif
                s4 = private_key
                f=open(u"Winner3.txt","a") #Output File of Segwit Wallet Found
                f.write(s1+":"+s2+":"+s3+":"+s4)
                f.write("\n")                
                f.close()
                continue #break or continue
            if str(bcaddr) in add:
                print ("Nice One Found!!!",ran, str(bcaddr)) #Segwit (bech32) compressed address
                s1 = str(ran)
                s2 = str(bcaddr)
                s3 = wif
                s4 = private_key
                f=open(u"bech32CompressedWinner.txt","a") #Output File of Segwit (bech32) compressed Wallet Found
                f.write(s1+":"+s2+":"+s3+":"+s4) 
                f.write("\n")                
                f.close()
                continue #break or continue
            if str(buaddr) in add:
                print ("Nice One Found!!!",ran, str(buaddr)) #Segwit (bech32) uncompressed address
                s1 = str(ran)
                s2 = str(buaddr)
                s3 = wif
                s4 = private_key
                f=open(u"bechUncompressedWinner.txt","a") #Output File of Segwit (bech32) uncompressed Wallet Found
                f.write(s1+":"+s2+":"+s3+":"+s4) 
                f.write("\n")
                f.close()
                continue #break or continue
            if eaddr in add:
                print ("Nice One Found!!!",ran, private_key, eaddr) #Eth address
                s1 = str(ran)
                s2 = eaddr
                s3 = wif
                s4 = private_key
                f=open(u"EthWinner.txt","a") #Output File of Eth Wallet Found
                f.write(s1+":"+s2+":"+s3+":"+s4) 
                f.write("\n")
                f.close()
                continue #break or continue
            else:
                colour_cyan = '\033[36m'
                colour_reset = '\033[0;0;39m'
                colour_red = '\033[31m'
                print (colour_cyan + seconds_to_str() + colour_red + "----- Sequential Search for Bitcoin and ETH Puzzle Wallets -----" + colour_cyan + myhex, end='\r'  + colour_reset) # Running Display Output
#CPU Control Command
if __name__ == '__main__':
        jobs = []
        for r in range(cores):
                p = multiprocessing.Process(target=seek, args=(r,))
                jobs.append(p)
                p.start()