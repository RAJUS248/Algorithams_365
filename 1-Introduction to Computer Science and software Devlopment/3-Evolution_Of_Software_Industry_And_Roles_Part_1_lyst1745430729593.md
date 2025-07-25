# Evolution of Software Industry and Roles – Part 1

## Introduction

Welcome! In this session, we'll explore the fascinating journey of the software industry: from its origin to where it stands today. We’ll also discuss different roles, types of software, and how industry dynamics have shaped its growth.

Understanding this big picture is essential — it’s like having a GPS for your tech career.

---

## How Software Started

- The term **"software"** was coined around **1950** by a mathematician named **John**.
- In early computers, programs were tightly coupled with the machines — mostly mechanical.
- Around the 1950s, the idea emerged that software could be separated from hardware.

### The Binary Language
- Computers operate using **binary (1s and 0s)**.
- Whether it's a **photo, video, text, or number**, it’s stored and processed as binary.

#### Example
```bash
# In Python, converting decimal 10 to binary
bin(10)  # Output: '0b1010'
```

---

## Evolution of Programming Languages

### Assembly Language
- Replaced binary programming.
- Used simple instruction sets like:
  ```asm
  MOV AX, SUM
  ADD AX, BX
  ```
- Required an **assembler** to convert to machine code.

### High-Level Languages (1960s–70s)
- **Fortran**, **COBOL**, and **BASIC** were developed.
- Languages became more readable and easier to use.
- This made programming accessible to more people.

---

## Rise of Operating Systems

### Why Operating Systems Were Needed
- Originally, programmers had to manage all device interactions (input/output, printing, etc.).
- Example: 5000+ lines of code were needed to print a file.
- With OS and APIs, the same task takes only 4–5 lines.

### Architecture
```
[ Applications ]
     ↓
[ Operating System (APIs) ]
     ↓
[ BIOS + Hardware Drivers ]
     ↓
[ Computer Hardware ]
```

- **BIOS** has basic instructions.
- **OS** bridges between hardware and software.
- **APIs** handle file I/O, networking, rendering, etc.

---

## System Software vs. Application Software

### System Software
- Operating systems like **Windows**, **Linux**, **Unix**, **macOS**.
- Developed by Microsoft, Apple, IBM, and open-source communities.

### Application Software
- Runs on top of OS using provided APIs.
- Two types:
  1. **Enterprise Software** – Salesforce, SAP, Walmart systems (B2B).
  2. **Consumer Software** – Ola, Uber, Swiggy, Amazon (B2C).

---

## Developer Tools and Open Source

- **Microsoft** and others created OS + Developer Tools.
- Tools made it easier to build applications.
- **Open-source** libraries accelerated development.

#### Example
Earlier, database operations required 30+ lines of code. Now:
```python
import sqlite3
conn = sqlite3.connect('data.db')
```

This simplification was made possible by open-source libraries and reusable client code.

---

## Industry Trends: No-Code & Low-Code

- **Low-code**: Minimal coding needed to customize software.
- **No-code**: Drag-and-drop interface, no programming required.
- Common in enterprise workflows where custom solutions are expensive and time-consuming.

---

## Software Architectures

### Standalone Software
- Installed and run locally.
- Doesn’t communicate with other systems.

### Client-Server Model (1980s–1990s)
- Software runs on centralized servers.
- Clients (user devices) connect over a network.
- Enabled by the rise of the internet.

### Peer-to-Peer and Distributed Systems
- Software and resources are decentralized.
- More scalable and resilient.

---

## Software Development Models

### 1. **Product-Based Companies**
- Build and sell their own software products.
- Example: Google, Microsoft, Facebook, Apple, etc.

### 2. **Service-Based Companies**
- Build custom software for other businesses.
- Example: Infosys, TCS, Wipro, HCL

#### Services Model
- Client provides requirements.
- IT service company builds, deploys, and maintains the software.
- Most code is proprietary and client-specific.

---

## Software in Business

Software is now essential across industries:
- **Banking**: In-house teams with 5000+ software engineers.
- **Manufacturing**: Asian Paints uses software for supply chain and distribution.
- **Automotive**: Tesla is as much a software company as a car company.

---

## Global Impact of Software

- In 2023, the global IT industry reached nearly **$1 trillion**.
- Tech companies dominate the list of top 10 companies globally.
- Software increases **human productivity**:
  - Automates low-skill jobs.
  - Frees up time for creative and strategic work.

---

## The Future of Software

- We're still in the **early stages** of this revolution.
- **AI, ML, robotics, automation** will further increase productivity.
- **Government and public sector** are embracing IT for efficiency.

### Example
- Bangalore uses AI to detect traffic violations in real-time.

---

## Summary

- Software evolved from binary and mechanical systems to highly abstracted, API-driven models.
- Operating systems and developer tools reduced development time.
- Open-source tools and no-code/low-code platforms accelerate innovation.
- Software industry spans both consumer and enterprise domains.
- Product vs. Service-based models define company structures.
- Global adoption of IT continues to increase human productivity and transform industries.

Stay curious — the best is yet to come!

---

**End of Lecture Notes – Part 1**
