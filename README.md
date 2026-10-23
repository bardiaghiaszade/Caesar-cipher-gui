# Encrypted Windows GUI

A small Python desktop application that demonstrates a Caesar cipher through a two-window Tkinter interface. Users type text in an input window and see the transformed text in a separate output window. Encryption can be enabled or disabled, and the shift value can be changed.

> **Security note:** This project implements the classical Caesar cipher for educational purposes. It is not secure encryption and must not be used to protect passwords, personal information, or other sensitive data.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies](#technologies)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Run the Application](#run-the-application)
- [How to Use](#how-to-use)
- [How It Works](#how-it-works)
- [Limitations](#limitations)

## Overview

The application demonstrates how a simple substitution cipher works. The user enters text in the first window. When the **Encrypt text** checkbox is selected, the program applies a Caesar shift before displaying the result in the second window.

The application updates the output as the user types, making it easy to observe how the shift changes the text.

## Features

- **Two-window interface:** Keeps the input and output in separate Tkinter windows.
- **Live text transfer:** Updates the output when the user types in the input field.
- **Optional encryption:** Toggle the **Encrypt text** checkbox to apply the Caesar cipher or display the original text.
- **Configurable shift:** Enter an integer shift value. The default shift is `3`.
- **Preserves non-letter characters:** Spaces, punctuation, digits, and other characters that are not treated as letters are passed through unchanged by the cipher logic.
- **Separate cipher module:** Keeps the Caesar cipher function in `crypto.py`, apart from the GUI in `crypto_gui.py`.

## Technologies

- **Python 3**
- **Tkinter** for the graphical user interface
- Python standard library only; no third-party packages are required by the current source code.

Tkinter is usually included with Python on Windows. On some Linux installations, it may need to be installed separately.

## Project Structure

| File | Purpose |
|---|---|
| `crypto_gui.py` | Creates both windows, reads user input, handles the checkbox and shift field, and displays the output. |
| `crypto.py` | Implements the Caesar cipher in the `caesar_encrypt()` function. |
| `.gitignore` | Excludes Python bytecode and cache files from Git. |

## Requirements

- Python 3
- Tkinter support
- A desktop environment that can open GUI windows

## Installation

Clone the repository:

```bash
git clone https://github.com/bardiaghiaszade/encrypted-windows-gui.git
cd encrypted-windows-gui
```

Check that Python is installed:

```powershell
python --version
```

If your system uses `python3`, run:

```bash
python3 --version
```

## Run the Application

From the project directory, run:

```powershell
python crypto_gui.py
```

Or:

```bash
python3 crypto_gui.py
```

The input window and output window should open.

## How to Use

1. Type or paste text into the **Input Window**.
2. Adjust the **Verschiebung** (shift) field if needed. Its default value is `3`.
3. Select **Encrypt text** to apply the Caesar cipher.
4. Watch the result appear in the **Output Window**.
5. Clear the checkbox to show the input text without applying the cipher.

The shift field is expected to contain an integer. If its value cannot be converted to an integer, the current application falls back to a shift of `3`.

## How It Works

### Caesar cipher

The `caesar_encrypt(text, shift=3)` function processes the input one character at a time.

For ASCII letters, it shifts each letter through the alphabet by the requested amount, wrapping around at the end. Uppercase and lowercase letters retain their case. Characters that are not considered letters are copied unchanged.

For example, with a shift of `3`:

```text
Input:  Hello, World!
Output: Khoor, Zruog!
```

A shift larger than the alphabet length wraps around modulo 26. Negative shifts are also accepted by the arithmetic.

### GUI update flow

- Typing in the input text box triggers `transfer_text()`.
- Changing the shift field also triggers `transfer_text()`.
- The checkbox calls `transfer_text()` when toggled.
- `transfer_text()` reads the input, optionally encrypts it, clears the output box, and inserts the resulting text.

## Limitations

- **Not secure for real-world protection:** Caesar cipher is easily broken and is included only as a learning demonstration.
