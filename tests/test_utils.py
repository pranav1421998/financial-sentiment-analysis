import unittest
from scripts.utils import is_english, clean_text

class TestUtils(unittest.TestCase):
    def test_is_english(self):
        self.assertTrue(is_english("This is an English sentence."))
        self.assertFalse(is_english("这是一个中文句子。"))

    def test_clean_text(self):
        text = "Check out https://example.com @user #hashtag"
        cleaned = clean_text(text)
        expected = "check out"
        self.assertEqual(cleaned, expected)

if __name__ == '__main__':
    unittest.main()
