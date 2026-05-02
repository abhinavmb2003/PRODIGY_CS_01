# ⊕ Caesar Cipher — ROT-N Substitution Engine

🔐 A Python GUI app for encrypting & decrypting text using the Caesar Cipher algorithm. Built with tkinter — no external dependencies required. Features a shift slider (1–25), live alphabet mapping, one-click clipboard copy, and a sleek retro terminal-style dark interface.

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)
![License](https://img.shields.io/badge/License-MIT-gold?style=flat-square)
![tkinter](https://img.shields.io/badge/GUI-tkinter-darkgreen?style=flat-square)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey?style=flat-square)

---

## 📸 Preview

> A retro terminal-style dark GUI with gold & indigo accents, monospaced typography, and a live alphabet strip.

---

## ✨ Features

| Feature | Details |
|---|---|
| 🔒 Encrypt | Shifts each letter forward by the chosen shift value |
| 🔓 Decrypt | Shifts each letter backward, reversing encryption |
| 🎚️ Shift Slider | Drag to select any shift from 1 to 25 |
| 🔡 Alphabet Strip | Flashes to visualise the letter mapping live |
| 📋 Copy Result | One-click clipboard copy of the output |
| 🗑️ Clear All | Resets message, shift, and result to defaults |
| ✅ Symbol Passthrough | Digits, spaces & punctuation are preserved as-is |

---

## 🛠️ Requirements

| Dependency | Version | Notes |
|---|---|---|
| Python | 3.8+ | Standard library only |
| tkinter | Built-in | Included with all standard Python installs |
| OS | Any | Windows · macOS · Linux |

> **Linux users:** tkinter may need to be installed separately.
> ```bash
> # Debian / Ubuntu
> sudo apt-get install python3-tk
>
> # Fedora / RHEL
> sudo dnf install python3-tkinter
> ```

---

## 🚀 Installation & Usage

**1. Clone the repository**
```bash
git clone https://github.com/your-username/caesar-cipher.git
cd caesar-cipher
```

**2. Run the application**
```bash
python caesar_cipher.py
```

**3. Using the GUI**
1. Type or paste your message into the **Input Message** box.
2. Drag the **Shift Value** slider to choose a shift (1–25).
3. Click **▲ ENCRYPT** to cipher or **▼ DECRYPT** to reverse.
4. The result appears in the **Output** panel below.
5. Use **Copy Result** to place the output on the clipboard.
6. Use **Clear All** to reset every field back to defaults.

---

## 🔢 How the Algorithm Works

The Caesar Cipher replaces each letter with the letter that is `shift` positions ahead (encrypt) or behind (decrypt) it in the alphabet. The shift wraps around at Z back to A using modular arithmetic.

### Formula

```python
# Encrypt
encrypted_char = chr((ord(char) - base + shift) % 26 + base)

# Decrypt
decrypted_char = chr((ord(char) - base - shift) % 26 + base)

# where base = ord('A') for uppercase
#       base = ord('a') for lowercase
```

### Example — Shift = 3

| Step | Encrypt | Decrypt |
|---|---|---|
| Input | `H  E  L  L  O` | `K  H  O  O  R` |
| Shift | `+3 +3 +3 +3 +3` | `-3 -3 -3 -3 -3` |
| Output | `K  H  O  O  R` | `H  E  L  L  O` |

> Non-alphabetic characters (spaces, digits, punctuation) are passed through unchanged.

---

## 📁 Project Structure

```
caesar-cipher/
├── caesar_cipher.py      # Main application (single file)
├── README.md             # This file
├── .gitignore            # Git ignore rules
└── LICENSE               # MIT Licence
```

---

## 🎨 Customisation

All colour constants are defined at the top of the `CaesarCipherApp` class:

```python
BG        = "#0d0d14"   # Window background
ACCENT    = "#e8c87a"   # Gold  — encrypt highlights
ACCENT2   = "#7a8de8"   # Indigo — decrypt highlights
TEXT_MAIN = "#f0eadc"   # Primary text colour
```

---

## ⚠️ Security Note

> The Caesar Cipher is a **toy cipher** — it is **not cryptographically secure**.
> With only 25 possible keys, brute-force is trivial.
> This project is intended for **educational purposes only** and should not be used to protect sensitive data.

---

## 📄 Licence

This project is licensed under the **MIT Licence** — free to use, modify, and distribute with attribution.

See the [LICENSE](LICENSE) file for full terms.

---

## 🙌 Acknowledgements

- Built with Python's built-in `tkinter` library
- Inspired by classic terminal aesthetics and historical cryptography

---

<p align="center">
  Made with ❤️ using Python & tkinter
</p>
