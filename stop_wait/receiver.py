def receive_frame(frame, expected_seq):
    """Simulate receiving a frame and sending acknowledgment."""
    seq, payload = frame
    print(f"Receiver: got seq={seq}, data={payload!r}")
    if seq == expected_seq:
        print(f"Receiver: accepted payload {payload!r}")
        return seq, payload, expected_seq ^ 1
    print(f"Receiver: duplicate frame, resend ACK for seq={1 - expected_seq}")
    return 1 - expected_seq, None, expected_seq
