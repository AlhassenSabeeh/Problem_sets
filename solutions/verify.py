#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for verifying the integrity of data transmission between a sender and a receiver.

Module contents:
    - verify: performs a checksum verification using XOR operations on binary strings.

Created on Dec 28, 2024.
@author: AL-HASSEN SABEEH
"""


def verify(sender: str, receiver: str, key: str) -> int:
    """
    Verifies the integrity of data transmission between a sender and a receiver using a shared key.

    This function computes checksums for the sender and receiver data using XOR operations with the key.
    It then compares the checksums to determine if the data matches.

    Parameters:
        sender: str, binary string representing the sender's data (must contain only '0' or '1' characters)
        receiver: str, binary string representing the receiver's data (must contain only '0' or '1' characters)
        key: str, binary string representing the shared key (must contain only '0' or '1' characters)

    Returns:
        int: 0 if the sender and receiver data match, otherwise a non-zero value.

    Raises:
        AssertionError: if any of the inputs are not strings
        AssertionError: if any of the strings are empty
        AssertionError: if any of the strings contain characters other than '0' or '1'

    Examples:
        >>> verify("1010", "1010", "1111")
        0

        >>> verify("1010", "1000", "1111")
        2

        >>> verify("1111", "1111", "0000")
        0

        >>> verify("", "1010", "1111")
        Traceback (most recent call last):
            ...
        AssertionError: Sender string must not be empty

        >>> verify("1020", "1010", "1111")
        Traceback (most recent call last):
            ...
        AssertionError: Sender string contains invalid characters
    """
    # Ensure correct input
    assert isinstance(sender, str), "Sender is not a string"
    assert isinstance(receiver, str), "Receiver is not a string"
    assert isinstance(key, str), "Key is not a string"

    assert sender != "", "Sender string must not be empty"
    assert receiver != "", "Receiver string must not be empty"
    assert key != "", "Key string must not be empty"

    assert set(sender) <= {"0", "1"}, "Sender string contains invalid characters"
    assert set(receiver) <= {"0", "1"}, "Receiver string contains invalid characters"
    assert set(key) <= {"0", "1"}, "Key string contains invalid characters"

    # Convert binary strings to integers
    sender_int = int(sender, 2)
    receiver_int = int(receiver, 2)
    key_int = int(key, 2)

    # Compute checksums
    sender_checksum = sender_int ^ key_int
    receiver_checksum = receiver_int ^ key_int

    # Return the result of the final XOR operation
    return sender_checksum ^ receiver_checksum


if __name__ == "__main__":
    import doctest

    doctest.testmod()
