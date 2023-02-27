import unittest
from translator import frenchToEnglish
from translator import englishToFrench

class TestFrenchToEnglish(unittest.TestCase):
    def test_null_input(self):
        self.assertEqual(frenchToEnglish(None), "Error: input text is null")
        self.assertEqual(frenchToEnglish(''), "Error: input text is null")

    def test_translation(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertEqual(frenchToEnglish('Je suis fatigué'), 'I am tired')
        self.assertEqual(frenchToEnglish('La vie est belle'), 'Life is beautiful')

if __name__ == '__main__':
    unittest.main()
    