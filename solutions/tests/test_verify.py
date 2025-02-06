#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for verify function.
Includes 12 tests, with deliberately faulty tests for debugging practice.

Test categories:
    - Edge Cases: Matching and non-matching data with simple keys.
    - Standard Cases: Various combinations of sender, receiver, and key.
    - Defensive Tests: Wrong input types, assertions.

@author: AL-HASSEN SABEEH
"""

import unittest

from ..verify import verify


class TestVerify(unittest.TestCase):
    """Test the verify function"""

    # Test Edge Cases
    def test_matching_data(self):
        """It should return 0 when sender and receiver data match"""
        self.assertEqual(verify("1010", "1010", "1111"), 0)

    def test_non_matching_data(self):
        """It should return a non-zero value when sender and receiver data do not match"""
        self.assertEqual(verify("1010", "1000", "1111"), 2)

    # Test Standard Cases
    def test_different_key(self):
        """It should return 0 when sender and receiver data match, even with a different key"""
        self.assertEqual(verify("1010", "1010", "0000"), 0)

    def test_empty_data(self):
        """It should return 0 when sender and receiver data are empty"""
        self.assertEqual(verify("", "", "1111"), 0)

    def test_large_binary_strings(self):
        """It should handle large binary strings correctly"""
        self.assertEqual(verify("1010101010101010101010", "1010101010101010101010", "1111111111111111111111"), 0)

    # Test Defensive Assertions
    def test_defensive_check_sender_is_not_string(self):
        """It should raise an error if the sender is not a string"""
        with self.assertRaises(AssertionError):
            verify(1010, "1010", "1111")

    def test_defensive_check_receiver_is_not_string(self):
        """It should raise an error if the receiver is not a string"""
        with self.assertRaises(AssertionError):
            verify("1010", 1000, "1111")

    def test_defensive_check_key_is_not_string(self):
        """It should raise an error if the key is not a string"""
        with self.assertRaises(AssertionError):
            verify("1010", "1010", 1111)

    def test_defensive_check_sender_has_invalid_chars(self):
        """It should raise an error if the sender string contains invalid characters"""
        with self.assertRaises(AssertionError):
            verify("1020", "1010", "1111")

    def test_defensive_check_receiver_has_invalid_chars(self):
        """It should raise an error if the receiver string contains invalid characters"""
        with self.assertRaises(AssertionError):
            verify("1010", "1002", "1111")

    # Deliberately Faulty Tests (for debugging practice)
    def test_faulty_matching_data(self):
        """Deliberately faulty test: expects non-zero value for matching data"""
        self.assertNotEqual(verify("1010", "1010", "1111"), 0)  # Faulty expectation

    def test_faulty_non_matching_data(self):
        """Deliberately faulty test: expects 0 for non-matching data"""
        self.assertEqual(verify("1010", "1000", "1111"), 0)  # Faulty expectation


if __name__ == "__main__":
    unittest.main()