import unittest
from jkspy.modules import crypto

class CryptoTests(unittest.TestCase):
    
    def test_symmetric_encryption(self):
        passphrase = 'Password!!!'
        plaintext = 'Hello World'
        ciphertext = crypto.sencrypt(passphrase, plaintext)
        deciphered = crypto.sdecrypt(passphrase, ciphertext)
        self.assertEqual(plaintext, deciphered)
        
    def test_symmetric_encryption_loop(self):
        passphrase = 'Password!!!'
        plaintext = 'Hello World'
        ciphertext = crypto.sencrypt(passphrase, plaintext)
        deciphered = crypto.sdecrypt(passphrase, ciphertext)
        for i in range(0, 25):
            ciphertext = crypto.sencrypt(passphrase, deciphered)
            deciphered = crypto.sdecrypt(passphrase, ciphertext)
        self.assertEqual(plaintext, deciphered)
        
if __name__ == '__main__':
    unittest.main()