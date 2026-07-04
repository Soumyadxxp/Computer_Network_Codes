import time
from typing import Dict, List, Optional
from models import Frame, Ack


class Sender:
    def __init__(self, messages: List[str], window_size: int, timeout: float):
        self.messages = messages
        self.window_size = window_size
        self.timeout = timeout
        self.base = 0
        self.next_seq = 0
        self.acked: Dict[int, bool] = {i: False for i in range(len(messages))}
        self.timers: Dict[int, float] = {}

    def can_send_next(self) -> bool:
        return (
            self.next_seq < len(self.messages)
            and self.next_seq < self.base + self.window_size
        )

    def next_frame(self) -> Frame:
        frame = Frame(self.next_seq, self.messages[self.next_seq])
        self.timers[self.next_seq] = time.time() + self.timeout
        print(f"Sender: sending frame {frame.seq} -> '{frame.data}'")
        self.next_seq += 1
        return frame

    def process_ack(self, ack: Optional[Ack]) -> None:
        if ack is None:
            return

        if ack.seq < self.base or ack.seq >= self.base + self.window_size:
            print(f"Sender: received ACK {ack.seq} outside sender window, ignored")
            return

        if self.acked.get(ack.seq, False):
            print(f"Sender: duplicate ACK {ack.seq} ignored")
            return

        print(f"Sender: ACK {ack.seq} received")
        self.acked[ack.seq] = True
        self.timers.pop(ack.seq, None)

        while self.base < len(self.messages) and self.acked.get(self.base, False):
            print(
                f"Sender: sliding window, base moves from {self.base} to {self.base + 1}"
            )
            self.base += 1

    def get_retransmissions(self) -> List[Frame]:
        now = time.time()
        retransmissions = []
        for seq in range(
            self.base, min(self.base + self.window_size, len(self.messages))
        ):
            if not self.acked[seq] and self.timers.get(seq, 0) <= now:
                print(f"Sender: timeout for frame {seq}, retransmitting")
                self.timers[seq] = now + self.timeout
                retransmissions.append(Frame(seq, self.messages[seq]))
        return retransmissions

    def all_acked(self) -> bool:
        return self.base >= len(self.messages)
