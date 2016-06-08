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
        
    def test_symmetric_byte_hex_conversion(self):
        sequence = crypto.randbytes(32)
        tohex = crypto.b2hex(sequence)
        tob = crypto.hex2b(tohex)
        self.assertEqual(sequence, tob)
        
        tobtohex = crypto.b2hex(tob)
        self.assertEqual(tohex, tobtohex)
        
if __name__ == '__main__':
    unittest.main()