# Introduction to Coding and Evolution of Programming Languages

## Introduction
Welcome to this session on coding – the most exciting part of our skill development program. In earlier sessions, we covered the software industry, roles, and basics like operating systems and computers. Now, let's get started with how to **code**, and understand the **evolution of programming languages**.

---

## Why Students Struggle with Coding
Many students complete courses and projects but still don’t feel confident in their coding skills. After interacting with 50+ students and mentoring 8–10 interns, we found that:

- Many focus too much on one language.
- Courses don’t teach **why** something works — just **how** to write it.
- Hands-on practice is missing.

### Our Approach
- Learn **multiple languages** (C, Python, Java) side by side.
- Focus on **concepts** that are shared across languages.
- Practice **hands-on coding and environment setup**.

---

## Introduction to Programming Languages

Programming languages allow us to write instructions that a computer can understand. Here's a simplified hierarchy of how they evolved:

1. **Binary (Machine Language)**: 1s and 0s
2. **Assembly Language**: Symbolic representation (e.g., `MOV AX, BX`)
3. **High-Level Languages**: Human-readable (e.g., C, Python, Java)

---

## Learning 3 Key Languages

### 1. C Language
- **Used for**: System software (e.g., database servers, Memcached).
- **Compiled Language**: Converts to binary before execution.
- **Machine Dependent**: Runs only on the platform it was compiled for.
- **No Object-Oriented Support**: For that, use C++.

```c
#include <stdio.h>
int main() {
    printf("Namaste from India\n");
    return 0;
}
```

### 2. Python
- **Used for**: Frontend, backend, data science, AI, automation.
- **Interpreted Language**: Source code is read and executed directly.
- **Machine Independent / Portable**: Works across platforms via interpreter.
- **Open Source & Upgradable**: Regular updates and community libraries.

```python
print("Namaste from Bharat")
```

### 3. Java
- **Used for**: Backend, enterprise apps, Android.
- **Compiled + Portable**: Compiled into bytecode, then run on Java Virtual Machine (JVM).
- **Hybrid**: Combines advantages of compiled and interpreted models.

```java
class Hello {
    public static void main(String[] args) {
        System.out.println("Namaste from Java");
    }
}
```

---

## Compiled vs Interpreted Languages

| Feature                | C (Compiled) | Python (Interpreted) | Java (Hybrid)       |
|------------------------|--------------|-----------------------|----------------------|
| Speed                  | Fast         | Slower                | Moderate             |
| Portability            | Low          | High                  | High (via JVM)       |
| Requires Compilation   | Yes          | No                    | Yes (to bytecode)    |
| Output File Type       | .exe/.out    | N/A                   | .class               |

---

## How Compilation Works (C Example)

1. You write code in a text file (`.c`).
2. Compiler converts it into an **object file** (`.obj`).
3. Linker creates an **executable file** (`.exe`).

### Demo:
```bash
cl namaste.c  # Compiles using Microsoft C Compiler
namaste.exe   # Run the compiled program
```

Even a simple `printf()` creates an executable with hundreds of lines of binary code. This is because standard libraries and OS-level instructions are included during compilation.

---

## Platform Dependence

Programs compiled on one OS (e.g., Windows) cannot run on another (e.g., Android or Linux) due to:

- **Different OS APIs**
- **Different CPU architectures (x86 vs ARM)**
- **32-bit vs 64-bit support**

### Analogy:
Trying to run a Windows `.exe` file on an Android phone is like inserting a square peg into a round hole — it just won’t fit.

To solve this, developers must use platform-specific compilers for each OS and processor type.

---

## Code Portability: Challenges and Solutions

### Problem:
- Platform-dependent software needs **16+ compiler versions** for various combinations of OS and CPU architectures.

### Example:
- Android, Windows, Linux, Mac (each with 32/64-bit and x86/ARM).
- Each needs its own binary package.

### Industry Solution:
- Use **interface layers** or **abstractions** that isolate OS-specific code.
- Example: In 2005, mobile browser code used one interface layer to support Symbian, Windows, and other platforms.

---

## Binary Files & Compilation Output

Even simple programs generate:
- `.obj` (object files)
- `.exe` (executables)

These are **binary files**, unreadable by humans but understood by CPUs.

### Example:
Open a compiled `.exe` and it shows garbage text. But this binary contains:
- Code
- Library references
- Metadata for the OS

---

## Python: Interpreted Language

Python avoids many headaches of C:
- No need to compile for every OS.
- Just install a **Python interpreter** for your platform.
- Write once, run anywhere (with Python installed).

```bash
# Example
python hello.py
```

Python interpreters are available for:
- Windows (x86/ARM, 32/64-bit)
- Linux, Mac, Android, etc.

---

## Summary

- Learn coding concepts, not just syntax.
- Study C, Python, and Java in parallel for a broader understanding.
- Understand compilation vs interpretation.
- Know how OS and CPU affect portability.
- Python simplifies portability using interpreters.

By understanding these fundamentals, you'll build a strong foundation for advanced programming topics.

---

**End of Lecture Notes**
