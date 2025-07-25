# Python IDE Installation – Lecture Notes

## Introduction

In this session, we will learn how to install and configure a Python development environment. Rather than just showing how to install Python, the goal is to teach you how to independently explore and set up the right tools, like IDEs (Integrated Development Environments), based on your needs.

---

## IDEs and Development Tools – A Quick Background

Over the years, developers have used a variety of editors and IDEs:

- **Turbo C** (old, blue-screen based, keyboard only)
- **VI Editor** (terminal based)
- **Visual Studio**
- **Eclipse**
- **VS Code**
- **PyCharm**
- **Xcode**

### Learning Philosophy
> "Instead of giving a man a fish, teach him how to fish."

We are focusing on learning **how to learn** – so you can install and use any tool on your own.

---

## Step-by-Step: How to Search and Choose Python IDEs

### Start with a search:
- Ask Google or ChatGPT: *“Which are the best IDEs for Python?”*

### Common IDEs Recommended:
- **PyCharm**
- **VS Code (Visual Studio Code)**
- **IDLE** (comes with Python)
- **Spyder**, **Eclipse**, **Jupyter Notebooks**

Use trusted sources like blogs from official websites, GeeksForGeeks, and JetBrains.

---

## Recommended IDE 1: Visual Studio Code (VS Code)

### Why Choose VS Code?
- Lightweight and fast.
- Works with many languages, not just Python.
- Highly customizable with extensions.

### Installation Steps:
1. Go to [https://code.visualstudio.com](https://code.visualstudio.com)
2. Download and install VS Code for your OS.
3. Install Python extension from the **Extensions Marketplace**:
   - Search for `Python`.
   - Install the one with IntelliSense, debugging, and formatting.

### First Python Program in VS Code

1. Open VS Code
2. Create a new file: `hello.py`
3. Add the following code:

```python
print("Namaskara")
num1 = 10
num2 = 20
print("Sum:", num1 + num2)
```

4. Click the **Run** arrow ▶️ or use Terminal > Run Python File
5. If you get an error like "Invalid Python Interpreter":
   - Go to **Command Palette** → Select Interpreter
   - Choose your Python path (e.g., `C:\Program Files\Python\python.exe`)

### Debugging in VS Code
- Set a **breakpoint** (red dot left of a line).
- Click the debug ▶️ icon and select “Debug Python File”.
- Use **Step Over**, **Step Into**, and other debug controls to walk through your code.

---

## Recommended IDE 2: PyCharm (Community Edition)

### Why Choose PyCharm?
- Feature-rich environment for professional development.
- Designed specifically for Python.

### Installation Steps:
1. Go to [https://www.jetbrains.com/pycharm](https://www.jetbrains.com/pycharm)
2. Download **Community Edition** (free)
3. Install it (approx. 700MB download, 1.7GB space required)

### First Python Program in PyCharm
1. Create a new project (e.g., `my_first_project`)
2. It will auto-detect Python if it’s in system PATH
3. Right-click → New → Python File → Name it `hello.py`
4. Paste the same code:

```python
print("Namaskara")
num1 = 10
num2 = 20
print("Sum:", num1 + num2)
```

5. Right-click the file and click **Run**.

### Debugging in PyCharm
- Set a breakpoint.
- Right-click → Debug
- Use debug panel to inspect variables, step through lines, etc.

---

## Optional: Installing Python (If Not Already Installed)

### Steps:
1. Go to [https://www.python.org](https://www.python.org)
2. Download the latest version
3. Run the installer
   - Check **Add Python to PATH**
   - Use **Customize Installation** if needed
   - Enable options like pip, test suite, and documentation
4. Python is installed to a default location like `C:\Program Files\Python 3.x`

### Verifying Installation
```bash
python --version
```
Or
```bash
py
```
Will launch the interactive Python shell.

---

## What Are Extensions (in VS Code)?

- Extensions are like **apps** or **add-ons**.
- Add functionality such as formatting, code completion, and debugging.
- Install via the Extensions tab (🔌 icon) in VS Code.

### Analogy:
Think of extensions like accessories in a car — not needed to drive, but make your experience smoother and better.

---

## Summary

- IDEs like VS Code and PyCharm make Python coding easier.
- Use search engines, official docs, and platforms like ChatGPT to explore options.
- Learn how to install, configure, and debug — this skill applies to any language or tool.
- Python setup requires interpreter + editor or IDE.
- Use breakpoints and debug tools to learn coding logic better.

---

**End of Lecture Notes**
