def verify(sender, receiver, key):
    """
    Verify the integrity of data transmission between sender and receiver using a key.

    This function performs a checksum verification by XORing the sender's data, receiver's data,
    and a shared key. It ensures that the data transmitted matches between the sender and receiver.

    Args:
        sender (str): Binary string representing the sender's data.
        receiver (str): Binary string representing the receiver's data.
        key (str): Binary string representing the shared key.

    Returns:
        int: Result of the checksum verification. Returns 0 if the data matches, otherwise a non-zero value.

    Example:
        >>> verify("1010", "1010", "1111")
        0
        >>> verify("1010", "1000", "1111")
        2
    """
    # Convert binary strings to integers
    sender = int(sender, 2)
    receiver = int(receiver, 2)
    key = int(key, 2)

    # Calculate checksums
    sender_checksum = sender ^ key
    receiver_checksum = receiver ^ key

    # Return the result of the final XOR operation
    return sender_checksum ^ receiver_checksum