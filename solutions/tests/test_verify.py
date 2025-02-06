#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for verify function.
Includes deliberately faulty tests for debugging practice.

Test categories:
    - Edge Cases: Matching and non-matching data with simple keys.
    - Standard Cases: Various combinations of sender, receiver, and key.
    - Defensive Tests: Wrong input types, assertions.

Created on Dec 28, 2024.
Team Number: 28
Team Name: MIT Alpha
@author: AL-HASSEN SABEEH
"""

import unittest

from ..verify import verify


class TestVerifyFunction(unittest.TestCase):
    def test_matching_data(self):
        """
        Test case where sender and receiver data match.
        Expected result: 0
        """
        result = verify("1010", "1010", "1111")
        self.assertEqual(result, 0)

    def test_non_matching_data(self):
        """
        Test case where sender and receiver data do not match.
        Expected result: Non-zero value.
        """
        result = verify("1010", "1000", "1111")
        self.assertEqual(result, 2)

    def test_different_key(self):
        """
        Test case with a different key.
        Expected result: Non-zero value.
        """
        result = verify("1010", "1010", "0000")
        self.assertEqual(result, 0)  # Key does not affect matching data

    def test_empty_data(self):
        """
        Test case with empty binary strings.
        Expected result: 0 (since empty data is treated as 0).
        """
        result = verify("", "", "1111")
        self.assertEqual(result, 0)

    def test_invalid_binary_input(self):
        """
        Test case with invalid binary input.
        Expected result: ValueError.
        """
        with self.assertRaises(ValueError):
            verify("1020", "1010", "1111")


if __name__ == "__main__":
    unittest.main()

