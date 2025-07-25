# Know Your Operating System and Computer

## Introduction

In this session, we explore the basics of the **Operating System (OS)**. While Computer Science students study OS in depth, non-IT students often don’t get the same exposure. This lecture offers a clear and simple overview, helpful for all engineering students.

If you wish to go deeper, consider watching a dedicated one-hour video on OS or refer to operating system textbooks.

---

## What is an Operating System?

An **Operating System** is the *boss* of the computer. It controls everything that happens inside the system:

- It manages processes and hardware.
- It decides which applications run, when, and how.
- It ensures that resources (CPU, memory, input/output devices) are shared efficiently.

### Common Operating Systems
- **Phones**: Android, iOS
- **Laptops/Desktops**: Windows, Linux, macOS
- **Servers**: Linux Server, Windows Server, Unix

### Analogy: Traffic Police & Law Enforcer
- Like a **traffic police**, it controls traffic between different applications.
- Like a **law enforcer**, it stops misbehaving programs and handles permissions.

---

## Structure of a Computer System

Think of a computer system in layered architecture:

1. **Hardware** – The physical machine.
2. **Device Drivers** – Translate between OS and hardware (e.g., for keyboard, mouse, storage).
3. **System Processes/Services** – Inner workings of the OS.
4. **Operating System Core** – Controls everything.
5. **Applications** – Outer layer, like browsers, word processors, or mobile apps.

This layered model shows how everything builds upon the OS.

---

## Key Functions of the OS

### 1. Process Scheduling
Manages running applications and assigns CPU time.

#### Example: Round Robin Algorithm
A scheduling method where each process gets a fixed time slice in turn.

```text
[Process A] → [Process B] → [Process C] → [Process A] → ...
```
Each switch happens so fast (in milliseconds) that it feels like all programs are running simultaneously.

### 2. Memory Management
- Allocates memory to programs.
- Ensures one app doesn’t interfere with another.

### 3. Permission Handling
When an app needs access (e.g., contacts, camera, location), the OS asks you to approve it.

### 4. Device Management
Handles input/output devices through drivers.

### 5. Resource Sharing
Shares resources like CPU, memory, network, and storage across all programs.

---

## Why is an OS Necessary?
Without an OS:
- You’d have to manually write code to manage memory, devices, and process execution.
- Running a modern computer would be nearly impossible.

---

## Real-Life Story: Building an OS in College

The speaker recalls an attempt to build a simple OS in their third year of engineering:

- Started with understanding **boot loaders**.
- Earlier computers booted from floppy disks (1.44 MB) or CDs.
- BIOS (Basic Input/Output System) checks hardware and then looks for the boot loader.

### Boot Process Flow:
1. Power ON → BIOS runs.
2. BIOS checks hardware (beep sound confirms success).
3. BIOS looks for **boot loader** (usually 512 bytes) in the boot device.
4. Boot loader loads OS into RAM.
5. A simple **command-line interface** starts.

At the time, they wrote a basic input/output system that accepted commands like `date`, `time`, or basic calculations.

Though they thought it was a full OS, they later realized real OSes are far more complex.

---

## Types of Operating Systems

### 1. **Open Source Operating Systems**
- Examples: Linux, Android, Unix
- Source code is available online (e.g., GitHub).
- Usually written in **C or C++**.

### 2. **Proprietary Operating Systems**
- Examples: Microsoft Windows, macOS, iOS
- Owned by companies like Microsoft or Apple.
- Source code is not publicly available.

---

## Summary

- The Operating System is essential to every computer and mobile device.
- It handles memory, permissions, device access, and process scheduling.
- Without it, using a computer would require writing low-level code.
- OSes like Linux are open-source and customizable, while others like Windows or macOS are closed-source.
- Even a simple boot loader is a fundamental step toward understanding OS internals.

Understanding the OS helps you become a better programmer, system designer, or tech-savvy engineer.

---

**End of Lecture Notes**
