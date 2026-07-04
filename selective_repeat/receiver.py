from typing import Dict, List, Optional
from models import Frame, Ack


class Receiver:
    def __init__(self, window_size: int):
        self.window_size = window_size
        self.base = 0
        self.buffer: Dict[int, str] = {}
        self.delivered: List[str] = []

    def receive(self, frame: Optional[Frame]) -> Optional[Ack]:
        if frame is None:
            return None

        if frame.data == "<CORRUPTED>":
            print(f"Receiver: frame {frame.seq} corrupted, discarding")
            return None

        if frame.seq < self.base:
            print(f"Receiver: duplicate frame {frame.seq} received, ACKing again")
            return Ack(frame.seq)

        if frame.seq >= self.base + self.window_size:
            print(f"Receiver: frame {frame.seq} outside receiver window, dropped")
            return None

        if frame.seq in self.buffer:
            print(f"Receiver: duplicate buffered frame {frame.seq}, ACKing")
            return Ack(frame.seq)

        print(f"Receiver: buffering frame {frame.seq}")
        self.buffer[frame.seq] = frame.data

        while self.base in self.buffer:
            message = self.buffer.pop(self.base)
            self.delivered.append(message)
            print(f"Receiver: delivered frame {self.base} -> '{message}'")
            self.base += 1

        return Ack(frame.seq)
