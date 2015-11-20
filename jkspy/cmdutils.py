import sys
from jkspy.modules import hash

def test():
    print(">>> Running jkspy TEST")
    for i in range(0, 10):
        print(i)
    print(">>> TEST Completed")
    
def checksum(filepath, *options):
    try:
        print(hash.get_checksum(filepath, *options))
    except TypeError:
        print("Please provide a filepath.")
        print("  (Example)  >> jkspy checksum test.txt")
        
def keygen(filepath, *options):
    keypair = hash.make_keypair()
    pw = input("Password for the keypair (leave blank if encrypting the keys is unnecessary) >> ")
    if pw:
        prvkey = keypair.exportKey('PEM', pw)
    else:
        prvkey = keypair.exportKey()
    pubkey = keypair.publickey().exportKey()
    print(prvkey)
    print('----------------')
    print(pubkey)