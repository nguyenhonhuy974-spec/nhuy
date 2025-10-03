import re

# Canonical command matching order (longest-first)
_COMMANDS = ["cuối", "cuoi", "dc", "lô", "lo", "đ", "d", "c"]

def _match_command_at(s: str, pos: int):
    """
    Try to match a command at s[pos:]. Returns (cmd_str, length) or (None, 0).
    Matching is case-insensitive and supports both 'cuoi' and accented 'cuối', 'lô', 'đ'.
    """
    substr = s[pos:]
    low = substr.lower()
    for cmd in _COMMANDS:
        if low.startswith(cmd):
            return substr[:len(cmd)], len(cmd)  # return the original-case slice and length
    return None, 0

def apply_rules(text: str) -> str:
    """
    Apply the user's rules (final agreed version) to the input text.
    - Numbers of 1..3 digits are recognized and processed sequentially.
    - Commands recognized immediately after a number are converted per rules.
    - Commands supported: lo, lô, d/đ, c, dc, cuoi/Cuối (accented variants accepted).
    - dc --> ALWAYS becomes 'dd' regardless of digit count.
    - For d/c/cuoi: 3-digit number => 'd' or 'cang'; otherwise (1-2 digits) => 'dau' or 'duoi'.
    - All other characters (spaces, punctuation, letters not part of commands) are preserved exactly.
    """
    i = 0
    out = []
    n = len(text)
    while i < n:
        ch = text[i]
        # If current char starts a digit, capture up to 3 consecutive digits (1..3)
        if ch.isdigit():
            m = re.match(r'\d{1,3}', text[i:])
            if not m:
                # shouldn't happen, but append the char and move on
                out.append(ch)
                i += 1
                continue
            num = m.group(0)
            j = i + len(num)
            # Try to match a command immediately after the number
            cmd_raw, cmd_len = _match_command_at(text, j)
            if cmd_raw:
                # Normalize command for decision (use lowercase, strip accents preserved in cmd_raw)
                cmd_norm = cmd_raw.lower()
                # Decide replacement based on rules
                if cmd_norm in ("lo", "lô"):
                    replacement = "lo"
                elif cmd_norm == "dc":
                    replacement = "dd"   # always dd
                elif cmd_norm in ("d", "đ"):
                    replacement = "d" if len(num) == 3 else "dau"
                elif cmd_norm == "c":
                    replacement = "cang" if len(num) == 3 else "duoi"
                elif cmd_norm in ("cuoi", "cuối"):
                    replacement = "cang" if len(num) == 3 else "duoi"
                else:
                    # fallback - shouldn't occur
                    replacement = cmd_raw
                out.append(num + replacement)
                i = j + cmd_len
            else:
                # No command after this number -> keep the number as-is
                out.append(num)
                i = j
        else:
            # Not a digit: just copy the char
            out.append(ch)
            i += 1
    return "".join(out)
