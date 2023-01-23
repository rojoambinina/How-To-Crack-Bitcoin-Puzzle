import bit
import random
x=int(input("'start range Min 1-115792089237316195423570985008687907852837564279074904382605163141518161494335 -> "))
y=int(input("stop range Max 115792089237316195423570985008687907852837564279074904382605163141518161494336 -> "))
k = 1
while True:
    key = bit.Key.from_int(random.randint(x,y))
    ran = 0
    print(key.address + ' : ' + key.to_hex() + ' : ' + key.get_balance('mbtc')) # btc mbtc usd
    if key.get_balance('mbtc') > str(ran)  :
        print("Matching Key ==== Found!!!\n PrivateKey: " + key.to_wif())
        f=open(u"winner.txt","a")
        f.write('\nBitcoin Address: ' + key.address)
        f.write('\nPrivateKey (hex): ' + key.to_hex())
        f.write('\nPrivateKey (wif): ' + key.to_wif())
        f.write('\n==================================')
        f.close()
    k += 1