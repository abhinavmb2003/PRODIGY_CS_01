import tkinter as tk
from tkinter import messagebox, ttk
import tkinter.font as tkFont


# ─────────────────────────────────────────────
#  Caesar Cipher Logic
# ─────────────────────────────────────────────

def caesar_encrypt(text: str, shift: int) -> str:
    result = []
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return "".join(result)


def caesar_decrypt(text: str, shift: int) -> str:
    return caesar_encrypt(text, -shift)


# ─────────────────────────────────────────────
#  GUI Application
# ─────────────────────────────────────────────

class CaesarCipherApp(tk.Tk):
    # Palette
    BG        = "#0d0d14"
    PANEL     = "#13131f"
    ACCENT    = "#e8c87a"       # warm gold
    ACCENT2   = "#7a8de8"       # cool indigo
    TEXT_MAIN = "#f0eadc"
    TEXT_DIM  = "#6b6980"
    BORDER    = "#2a2a3d"
    ENCRYPT_C = "#1a2e1a"
    DECRYPT_C = "#1a1a2e"
    RESULT_BG = "#0a0a12"

    def __init__(self):
        super().__init__()
        self.title("Caesar Cipher")
        self.resizable(False, False)
        self.configure(bg=self.BG)

        self._build_fonts()
        self._build_ui()
        self._center_window(760, 640)

    # ── fonts ──────────────────────────────────

    def _build_fonts(self):
        self.f_title   = tkFont.Font(family="Courier New", size=22, weight="bold")
        self.f_sub     = tkFont.Font(family="Courier New", size=9)
        self.f_label   = tkFont.Font(family="Courier New", size=10, weight="bold")
        self.f_mono    = tkFont.Font(family="Courier New", size=11)
        self.f_btn     = tkFont.Font(family="Courier New", size=11, weight="bold")
        self.f_result  = tkFont.Font(family="Courier New", size=12, weight="bold")
        self.f_small   = tkFont.Font(family="Courier New", size=8)

    # ── layout ─────────────────────────────────

    def _build_ui(self):
        outer = tk.Frame(self, bg=self.BG, padx=28, pady=24)
        outer.pack(fill="both", expand=True)

        # ── header ──
        hdr = tk.Frame(outer, bg=self.BG)
        hdr.pack(fill="x", pady=(0, 18))

        tk.Label(hdr, text="⊕  CAESAR CIPHER", font=self.f_title,
                 fg=self.ACCENT, bg=self.BG).pack(side="left")

        tk.Label(hdr, text="ROT-N SUBSTITUTION ENGINE",
                 font=self.f_sub, fg=self.TEXT_DIM, bg=self.BG).pack(
                     side="right", anchor="s", pady=(0, 4))

        self._divider(outer)

        # ── input message ──
        self._section_label(outer, "01  INPUT MESSAGE")

        self.msg_text = tk.Text(outer, height=5, font=self.f_mono,
                                bg=self.PANEL, fg=self.TEXT_MAIN,
                                insertbackground=self.ACCENT,
                                relief="flat", bd=0,
                                wrap="word",
                                selectbackground=self.ACCENT,
                                selectforeground=self.BG,
                                padx=10, pady=8)
        self.msg_text.pack(fill="x", pady=(4, 0))
        self._border_frame(outer, self.msg_text)

        tk.Label(outer, text="Letters only are shifted; digits, spaces & symbols pass through unchanged.",
                 font=self.f_small, fg=self.TEXT_DIM, bg=self.BG,
                 anchor="w").pack(fill="x", pady=(3, 12))

        # ── shift row ──
        self._section_label(outer, "02  SHIFT VALUE  (1 – 25)")

        shift_row = tk.Frame(outer, bg=self.BG)
        shift_row.pack(fill="x", pady=(4, 12))

        self.shift_var = tk.IntVar(value=3)

        self.shift_scale = tk.Scale(
            shift_row, from_=1, to=25,
            orient="horizontal", variable=self.shift_var,
            bg=self.BG, fg=self.ACCENT, troughcolor=self.BORDER,
            activebackground=self.ACCENT,
            highlightthickness=0, bd=0,
            font=self.f_small, showvalue=False,
            command=lambda _: self.shift_display.config(text=str(self.shift_var.get()))
        )
        self.shift_scale.pack(side="left", fill="x", expand=True, padx=(0, 14))

        badge = tk.Frame(shift_row, bg=self.ACCENT, padx=10, pady=4)
        badge.pack(side="left")
        self.shift_display = tk.Label(badge, text="3", font=self.f_btn,
                                      fg=self.BG, bg=self.ACCENT, width=3)
        self.shift_display.pack()

        # ── buttons ──
        self._section_label(outer, "03  OPERATION")

        btn_row = tk.Frame(outer, bg=self.BG)
        btn_row.pack(fill="x", pady=(4, 16))

        self._btn(btn_row, "▲  ENCRYPT", self.ACCENT,  self.BG, self._encrypt).pack(
            side="left", fill="x", expand=True, padx=(0, 6))
        self._btn(btn_row, "▼  DECRYPT", self.ACCENT2, self.BG, self._decrypt).pack(
            side="left", fill="x", expand=True, padx=(6, 0))

        self._divider(outer)

        # ── output ──
        self._section_label(outer, "04  OUTPUT")

        out_frame = tk.Frame(outer, bg=self.RESULT_BG, padx=14, pady=12,
                             highlightbackground=self.BORDER,
                             highlightthickness=1)
        out_frame.pack(fill="x", pady=(4, 10))

        self.mode_label = tk.Label(out_frame, text="—",
                                   font=self.f_small, fg=self.TEXT_DIM,
                                   bg=self.RESULT_BG, anchor="w")
        self.mode_label.pack(fill="x")

        self.result_var = tk.StringVar(value="")
        self.result_label = tk.Label(out_frame, textvariable=self.result_var,
                                     font=self.f_result, fg=self.ACCENT,
                                     bg=self.RESULT_BG,
                                     wraplength=680, justify="left", anchor="w")
        self.result_label.pack(fill="x", pady=(6, 4))

        # ── copy / clear row ──
        act_row = tk.Frame(outer, bg=self.BG)
        act_row.pack(fill="x", pady=(0, 2))

        self._ghost_btn(act_row, "⊡  COPY RESULT", self._copy).pack(side="left")
        self._ghost_btn(act_row, "✕  CLEAR ALL",   self._clear).pack(side="left", padx=(10, 0))

        # ── alphabet strip ──
        self._divider(outer)
        self._build_alphabet_strip(outer)

    # ── helpers ────────────────────────────────

    def _divider(self, parent):
        tk.Frame(parent, bg=self.BORDER, height=1).pack(fill="x", pady=(0, 14))

    def _section_label(self, parent, text):
        tk.Label(parent, text=text, font=self.f_label,
                 fg=self.TEXT_DIM, bg=self.BG, anchor="w").pack(fill="x")

    def _border_frame(self, parent, widget):
        """Drawn after widget so it appears over it as a border effect using highlight."""
        widget.config(highlightbackground=self.BORDER,
                      highlightcolor=self.ACCENT, highlightthickness=1)

    def _btn(self, parent, text, bg, fg, cmd):
        b = tk.Button(parent, text=text, font=self.f_btn,
                      bg=bg, fg=fg, activebackground=fg,
                      activeforeground=bg, relief="flat", bd=0,
                      cursor="hand2", pady=10, command=cmd)
        self._hover(b, bg, fg)
        return b

    def _ghost_btn(self, parent, text, cmd):
        b = tk.Button(parent, text=text, font=self.f_small,
                      bg=self.BG, fg=self.TEXT_DIM,
                      activebackground=self.PANEL,
                      activeforeground=self.TEXT_MAIN,
                      relief="flat", bd=0, cursor="hand2",
                      pady=4, padx=6, command=cmd)
        return b

    def _hover(self, widget, normal_bg, normal_fg):
        def on_enter(_): widget.config(bg=normal_fg, fg=normal_bg)
        def on_leave(_): widget.config(bg=normal_bg, fg=normal_fg)
        widget.bind("<Enter>", on_enter)
        widget.bind("<Leave>", on_leave)

    def _build_alphabet_strip(self, parent):
        strip_frame = tk.Frame(parent, bg=self.BG)
        strip_frame.pack(fill="x", pady=(6, 0))

        self.alpha_labels = {}
        row = tk.Frame(strip_frame, bg=self.BG)
        row.pack()

        for i, ch in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            lbl = tk.Label(row, text=ch, font=self.f_small,
                           fg=self.TEXT_DIM, bg=self.BG, width=2)
            lbl.grid(row=0, column=i)
            self.alpha_labels[ch] = lbl

    def _flash_alphabet(self, shift):
        """Highlight shifted pairs briefly."""
        for lbl in self.alpha_labels.values():
            lbl.config(fg=self.TEXT_DIM)

        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i, ch in enumerate(alphabet):
            mapped = alphabet[(i + shift) % 26]
            self.alpha_labels[ch].config(fg=self.ACCENT)
            self.alpha_labels[mapped].config(fg=self.ACCENT2)

        self.after(2000, lambda: [lbl.config(fg=self.TEXT_DIM)
                                   for lbl in self.alpha_labels.values()])

    # ── actions ────────────────────────────────

    def _get_input(self):
        return self.msg_text.get("1.0", "end-1c").strip()

    def _encrypt(self):
        msg = self._get_input()
        if not msg:
            messagebox.showwarning("Empty Input", "Please enter a message to encrypt.")
            return
        shift = self.shift_var.get()
        out = caesar_encrypt(msg, shift)
        self.result_var.set(out)
        self.result_label.config(fg=self.ACCENT)
        self.mode_label.config(
            text=f"ENCRYPTED  ·  shift +{shift}  ·  {len(msg)} chars → {len(out)} chars")
        self._flash_alphabet(shift)

    def _decrypt(self):
        msg = self._get_input()
        if not msg:
            messagebox.showwarning("Empty Input", "Please enter a message to decrypt.")
            return
        shift = self.shift_var.get()
        out = caesar_decrypt(msg, shift)
        self.result_var.set(out)
        self.result_label.config(fg=self.ACCENT2)
        self.mode_label.config(
            text=f"DECRYPTED  ·  shift -{shift}  ·  {len(msg)} chars → {len(out)} chars")
        self._flash_alphabet(-shift % 26)

    def _copy(self):
        result = self.result_var.get()
        if not result:
            messagebox.showinfo("Nothing to Copy", "Run an operation first.")
            return
        self.clipboard_clear()
        self.clipboard_append(result)
        messagebox.showinfo("Copied", "Result copied to clipboard!")

    def _clear(self):
        self.msg_text.delete("1.0", "end")
        self.result_var.set("")
        self.mode_label.config(text="—")
        self.shift_var.set(3)
        self.shift_display.config(text="3")
        for lbl in self.alpha_labels.values():
            lbl.config(fg=self.TEXT_DIM)

    # ── window centering ───────────────────────

    def _center_window(self, w, h):
        self.update_idletasks()
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x = (sw - w) // 2
        y = (sh - h) // 2
        self.geometry(f"{w}x{h}+{x}+{y}")


# ─────────────────────────────────────────────
if __name__ == "__main__":
    app = CaesarCipherApp()
    app.mainloop()
