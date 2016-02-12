import unittest
from jkspy.modules.words import Generator

class WordTests(unittest.TestCase):
    
    def test_generator_seed_consistency(self):
        gen = Generator(1)
        wordlist = [ gen.randWord() for i in range(0, 10) ]
        gen2 = Generator(1)
        wordlist_reseed = [ gen2.randWord() for i in range(0, 10) ]
        
        self.assertEqual(wordlist, wordlist_reseed)
        
    def test_word_conversion_consistency(self):
        gen = Generator(1)
        test_words = ['Happy', 'happy', 'Hello', 'World']
        converted_words = [gen.convertWord(word) for word in test_words]
        gen.randWord() #move(waste) random generator's pointer
        gen.randWord() #move(waste) random generator's pointer
        converted_again = [gen.convertWord(word) for word in test_words]
        
        self.assertEqual(converted_words, converted_again)
        
    def test_generator_uniqueness(self):
        gen_A = Generator(1)
        gen_B = Generator(2)
        test_words = ['Happy', 'happy', 'Hello', 'World']
        converted_A = [gen_A.convertWord(word) for word in test_words]
        converted_B = [gen_B.convertWord(word) for word in test_words]
        match = False
        for i, word_A in enumerate(converted_A):
            if word_A == converted_B[i]:
                match = True
        self.assertEqual(match, False)
        
    def test_seed_collision(self):
        gen = Generator(1)
        first = gen.convertWord('happ')
        second = gen.convertWord('happy')
        self.assertNotEqual(first, second)
        
if __name__ == '__main__':
    unittest.main()