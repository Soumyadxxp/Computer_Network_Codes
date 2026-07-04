from typing import List, Optional
from models import Frame, Ack


class Receiver:
    def __init__(self):
        self.expected_seq = 0
        self.delivered: List[str] = []

    def receive(self, frame: Optional[Frame]) -> Optional[Ack]:
        if frame is None:
            return None

        if frame.data == "<CORRUPTED>":
            print(f"Receiver: frame {frame.seq} corrupted, discarding")
            return None

        if frame.seq == self.expected_seq:
            print(f"Receiver: accepted frame {frame.seq} -> '{frame.data}'")
            self.delivered.append(frame.data)
            self.expected_seq += 1
            return Ack(frame.seq)

        if frame.seq < self.expected_seq:
            print(
                f"Receiver: duplicate frame {frame.seq} received, sending ACK {frame.seq}"
            )
            return Ack(frame.seq)

        print(
            f"Receiver: out-of-order frame {frame.seq} discarded, expected {self.expected_seq}"
        )
        if self.expected_seq > 0:
            return Ack(self.expected_seq - 1)
        return None
