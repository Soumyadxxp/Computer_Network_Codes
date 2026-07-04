import random
import time

FRAME_LOSS = 0.2
ACK_LOSS = 0.1


def send_frame(seq, payload):
    """Simulate sending a frame across the channel."""
    print(f"Sender: send seq={seq}, data={payload!r}")
    if random.random() < FRAME_LOSS:
        print(f"Channel: frame {seq} lost")
        return None
    time.sleep(0.1)
    return seq, payload


def send_ack(ack_seq):
    """Simulate sending an acknowledgment across the channel."""
    if random.random() < ACK_LOSS:
        print(f"Channel: ACK({ack_seq}) lost")
        return None
    time.sleep(0.05)
    return ack_seq
