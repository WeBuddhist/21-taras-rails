"""Make ``src/`` importable without an install step.

The repo has no ``pyproject.toml`` yet, so there is no editable install to rely
on.  Putting the shim here rather than in each test module keeps every test
file a plain ``import kangyur_wiki...`` and means the suite runs from a clean
checkout with nothing but pytest available.  Harmless once packaging lands: an
installed copy already on ``sys.path`` wins over this appended entry only if we
insert at the end, so we insert at the front deliberately — during development
the working tree is the copy under test.
"""

from __future__ import annotations

import sys
from pathlib import Path

_SRC = Path(__file__).resolve().parents[1] / "src"

if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))
