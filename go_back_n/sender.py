import time
from typing import List, Optional
from models import Frame, Ack


class Sender:
    def __init__(self, messages: List[str], window_size: int, timeout: float):
        self.messages = messages
        self.window_size = window_size
        self.timeout = timeout
        self.base = 0
        self.next_seq = 0
        self.timer_deadline: Optional[float] = None

    def can_send_next(self) -> bool:
        return (
            self.next_seq < len(self.messages)
            and self.next_seq < self.base + self.window_size
        )

    def next_frame(self) -> Frame:
        frame = Frame(self.next_seq, self.messages[self.next_seq])
        if self.base == self.next_seq:
            self.timer_deadline = time.time() + self.timeout
        print(f"Sender: sending frame {frame.seq} -> '{frame.data}'")
        self.next_seq += 1
        return frame

    def process_ack(self, ack: Optional[Ack]) -> None:
        if ack is None:
            return

        if ack.seq < self.base or ack.seq >= self.next_seq:
            print(f"Sender: ACK {ack.seq} ignored")
            return

        print(f"Sender: ACK {ack.seq} received")
        self.base = ack.seq + 1
        if self.base < self.next_seq:
            self.timer_deadline = time.time() + self.timeout
        else:
            self.timer_deadline = None

    def get_retransmissions(self) -> List[Frame]:
        now = time.time()
        if self.timer_deadline is None or now < self.timer_deadline:
            return []

        print(
            f"Sender: timeout expired, retransmitting window from {self.base} to {self.next_seq - 1}"
        )
        self.timer_deadline = now + self.timeout
        return [
            Frame(seq, self.messages[seq]) for seq in range(self.base, self.next_seq)
        ]

    def all_acked(self) -> bool:
        return self.base >= len(self.messages)
