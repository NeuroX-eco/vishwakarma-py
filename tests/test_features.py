"""
Vishwakarma AI - Features Tests
© 2025 Vishwakarma Industries
"""
import unittest
from unittest.mock import patch
import sys

# Mock the pyautogui and pywhatkit modules before they're imported by engine.features
sys.modules['pyautogui'] = unittest.mock.MagicMock()
sys.modules['pywhatkit'] = unittest.mock.MagicMock()
sys.modules['playsound'] = unittest.mock.MagicMock()

from engine.features import extract_yt_term, remove_words

class TestFeatures(unittest.TestCase):
    """Unit tests for the features module."""

    def test_extract_yt_term(self):
        """Test extracting the YouTube search term."""
        self.assertEqual(extract_yt_term("play despacito on youtube"), "despacito")
        self.assertEqual(extract_yt_term("play some music on youtube"), "some music")
        self.assertIsNone(extract_yt_term("play some music"))

    def test_remove_words(self):
        """Test removing words from a string."""
        words_to_remove = ["assistant", "please", "can", "you"]
        self.assertEqual(remove_words("assistant please can you open chrome", words_to_remove), "open chrome")
        self.assertEqual(remove_words("open chrome", words_to_remove), "open chrome")

if __name__ == '__main__':
    unittest.main()
