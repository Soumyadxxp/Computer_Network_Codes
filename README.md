# Computer Networks – ARQ Protocol Simulations

A collection of Computer Networks simulations implemented in Python that demonstrate Automatic Repeat reQuest (ARQ) protocols, Cyclic Redundancy Check (CRC), and IP networking utilities. These projects provide practical implementations of reliable data transmission techniques and networking concepts commonly taught in computer networking courses.

---

## Project Overview

This repository contains multiple networking simulations designed to help students understand error detection, error recovery, reliable data transfer, and IP networking concepts through interactive Python programs.

---

## Projects Included

| Directory | Module | Description |
|-----------|--------|-------------|
| `stop_wait/` | Stop-and-Wait ARQ | Sends one frame at a time and waits for an acknowledgment before sending the next frame. Retransmits frames on timeout or packet loss. |
| `go_back_n/` | Go-Back-N ARQ | Sliding window protocol where multiple frames can be transmitted before acknowledgment. Lost frames cause retransmission of all outstanding frames. |
| `selective_repeat/` | Selective Repeat ARQ | Sliding window protocol that retransmits only the lost or corrupted frames while buffering out-of-order frames. |
| `crc_generator/` | CRC Generator | Generates Cyclic Redundancy Check (CRC) codewords for error detection. |
| `crc_decode/` | CRC Decoder | Verifies received CRC codewords and detects transmission errors. |
| `host_ip/` | Host IP Utility | Displays the host machine's IP address. |
| `ip_config/` | IP Configuration Utility | Retrieves local network configuration information. |
| `ip_info/` | IP Information Utility | Displays detailed information about an IP address. |

---

## Features

### ARQ Protocol Simulations

- Stop-and-Wait ARQ
- Go-Back-N ARQ
- Selective Repeat ARQ
- Sliding Window Implementation
- Timeout Handling
- Frame Retransmission
- ACK Processing
- Packet Loss Simulation
- ACK Loss Simulation
- Frame Corruption Simulation

### CRC Utilities

- CRC Encoding
- CRC Decoding
- Error Detection
- Polynomial Division
- Binary Data Processing

### IP Networking Utilities

- Host IP Detection
- Network Configuration
- IP Information Lookup
- Network Diagnostics

---

## Simulation Parameters

Each ARQ protocol provides configurable parameters through `models.py`.

### Window Size

Number of frames that can be transmitted before waiting for acknowledgments.

### Timeout

Maximum waiting time before retransmitting an unacknowledged frame.

### Packet Loss Probability

Probability that a transmitted frame is dropped during transmission.

### ACK Loss Probability

Probability that an acknowledgment packet is lost.

### Corruption Probability

Probability that a transmitted frame becomes corrupted.

---

## Networking Concepts Covered

### Reliable Data Transfer

- Stop-and-Wait Protocol
- Sliding Window Protocol
- Flow Control
- Error Recovery
- Timeout Mechanism
- Acknowledgment Handling

### Error Detection

- Cyclic Redundancy Check (CRC)
- Generator Polynomial
- Binary Division
- Error Verification

### Internet Protocol

- IPv4 Addressing
- Host Configuration
- Network Interfaces
- IP Lookup

---

## Technologies Used

- Python 3
- Socket Programming
- Object-Oriented Programming
- Networking Libraries
- Random Event Simulation

---

## Learning Objectives

This repository demonstrates:

- Automatic Repeat reQuest (ARQ)
- Sliding Window Protocols
- Reliable Data Transfer
- Error Detection Techniques
- CRC Algorithms
- Packet Transmission
- Flow Control
- Error Control
- Network Simulation
- Socket Programming
- Computer Networking Fundamentals

---

## Applications

- Computer Networks Laboratory
- Networking Coursework
- Academic Projects
- Protocol Analysis
- Network Simulation
- Educational Demonstrations
- Interview Preparation
- Networking Practice

---

## License

This project is intended for educational and academic purposes.

---

## Author

**Soumyadeep Basu**

