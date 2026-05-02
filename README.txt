================================================================
  ⊕  CAESAR CIPHER  —  ROT-N SUBSTITUTION ENGINE
  Python GUI Application
================================================================

----------------------------------------------------------------
1.  OVERVIEW
----------------------------------------------------------------
Caesar Cipher is a classic substitution cipher that shifts each
letter of the plaintext by a fixed number of positions in the
alphabet. This Python application provides a polished graphical
interface for encrypting and decrypting text using the Caesar
Cipher algorithm with any shift value from 1 to 25.

The GUI is built entirely with Python's built-in tkinter library
— no third-party packages are required.


----------------------------------------------------------------
2.  FEATURES
----------------------------------------------------------------
  Feature               Details
  ---------------       ----------------------------------------
  Encrypt               Shifts each letter forward by shift value
  Decrypt               Shifts each letter backward (reverses)
  Shift Slider          Drag to select any shift from 1 to 25
  Alphabet Strip        Flashes gold/indigo to show letter mapping
  Copy Result           One-click clipboard copy of the output
  Clear All             Resets message, shift, and result
  Symbol passthrough    Digits, spaces & punctuation unchanged


----------------------------------------------------------------
3.  REQUIREMENTS
----------------------------------------------------------------
  Dependency    Version     Notes
  ----------    -------     ------------------------------------
  Python        3.8+        Standard library only — no pip needed
  tkinter       Built-in    Included with all Python distributions
  OS            Any         Windows · macOS · Linux

  On some Linux distros, tkinter must be installed separately:

    # Debian / Ubuntu
    sudo apt-get install python3-tk

    # Fedora / RHEL
    sudo dnf install python3-tkinter


----------------------------------------------------------------
4.  INSTALLATION & USAGE
----------------------------------------------------------------

  4.1  Clone or download
  ----------------------
    git clone https://github.com/your-username/caesar-cipher.git
    cd caesar-cipher

  4.2  Run the application
  ------------------------
    python caesar_cipher.py

  4.3  Using the GUI
  ------------------
    1. Type or paste your message into the Input Message box.
    2. Drag the Shift Value slider to choose a shift (1–25).
    3. Click ENCRYPT to cipher or DECRYPT to reverse.
    4. The result appears in the Output panel below.
    5. Use Copy Result to place the output on the clipboard.
    6. Use Clear All to reset every field back to defaults.


----------------------------------------------------------------
5.  HOW THE ALGORITHM WORKS
----------------------------------------------------------------
The Caesar Cipher replaces each letter with the letter that is
'shift' positions ahead (encrypt) or behind (decrypt) it in the
alphabet. The shift wraps around at Z back to A using modular
arithmetic.

  5.1  Formula
  ------------
    # Encrypt
    encrypted_char = chr((ord(char) - base + shift) % 26 + base)

    # Decrypt  (negative shift)
    decrypted_char = chr((ord(char) - base - shift) % 26 + base)

    # where  base = ord('A')  for uppercase letters
    #        base = ord('a')  for lowercase letters

  5.2  Example  (shift = 3)
  -------------------------
    Step      Encrypt               Decrypt
    ------    --------------------  --------------------
    Input     H  E  L  L  O        K  H  O  O  R
    Shift     +3 +3 +3 +3 +3       -3 -3 -3 -3 -3
    Output    K  H  O  O  R        H  E  L  L  O

  Non-alphabetic characters (spaces, digits, punctuation) are
  passed through unchanged.


----------------------------------------------------------------
6.  PROJECT STRUCTURE
----------------------------------------------------------------
    caesar-cipher/
      caesar_cipher.py      # Main application (single file)
      README.txt            # This document


----------------------------------------------------------------
7.  CUSTOMISATION
----------------------------------------------------------------
All colour constants are defined at the top of the
CaesarCipherApp class and can be changed freely:

    BG        = '#0d0d14'   # window background
    ACCENT    = '#e8c87a'   # gold  — encrypt highlights
    ACCENT2   = '#7a8de8'   # indigo — decrypt highlights
    TEXT_MAIN = '#f0eadc'   # primary text colour


----------------------------------------------------------------
8.  LIMITATIONS & SECURITY NOTE
----------------------------------------------------------------
  - The Caesar Cipher is a toy cipher — NOT cryptographically
    secure.
  - With only 25 possible keys, brute-force is trivial.
  - Only the 26 Latin letters (A-Z, a-z) are encrypted; all
    other characters pass through unchanged.
  - This application is intended for educational purposes and
    should NOT be used to protect sensitive data.


----------------------------------------------------------------
9.  LICENCE
----------------------------------------------------------------
MIT Licence — free to use, modify, and distribute with
attribution.

Copyright © 2026. See LICENCE file for full terms.

================================================================
  Caesar Cipher  ·  Python GUI  ·  Built with tkinter
================================================================
