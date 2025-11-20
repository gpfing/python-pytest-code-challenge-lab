# Test suite for longest_palindromic_substring function
import pytest
from palindrome import longest_palindromic_substring


def test_basic_palindrome():
    """Test with a simple palindrome example"""
    result = longest_palindromic_substring("babad")
    assert result in ["bab", "aba"]


def test_even_palindrome():
    """Test with an even-length palindrome"""
    result = longest_palindromic_substring("cbbd")
    assert result == "bb"


def test_single_character():
    """Test with a single character"""
    result = longest_palindromic_substring("a")
    assert result == "a"

def test_whole_string_palindrome():
    """Test with the whole string being a palindrome"""
    result = longest_palindromic_substring("racecar")
    assert result == "racecar"
