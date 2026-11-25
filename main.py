#!/usr/bin/env python3
"""One Line of Earned Pride — writes the entry line to /output/entry.txt.

The line is the whole entry: one original line (131 characters) about a
daughter who burned the soup every Sunday for a year, and the Sunday it
didn't burn, her father — who never said a word — asked for seconds. A
quiet, earned moment of pride, landing on the last word.
"""

import os

LINE = "She burned the soup every Sunday for a year, and the Sunday it didn't burn, her father \u2014 who never said a word \u2014 asked for seconds."

assert 1 <= len(LINE) <= 240, "line must be 1-240 characters"
assert len(LINE.encode("utf-8")) <= 240, "line must fit the gate in bytes too"
assert LINE.strip(), "line must not be whitespace only"
assert LINE == LINE.strip(), "line must not have leading/trailing whitespace"
assert "\n" not in LINE, "line must be a single line"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)

print(LINE)
