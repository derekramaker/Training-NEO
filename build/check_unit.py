#!/usr/bin/env python3
"""Check one flashcard unit and write its contact sheet, without touching dist/.

    python3 build/check_unit.py 3

Validates data/anki/core/unit-03.csv and every diagram it uses, renders the images, and writes
build/.cache/card-preview/unit-03.png (front and back of every card at phone width).
"""

import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import anki_deck  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        sys.exit("usage: check_unit.py UNIT_NUMBER")
    n = int(sys.argv[1])
    with tempfile.TemporaryDirectory() as tmp:
        try:
            print(anki_deck.build_deck(ROOT, Path(tmp), preview=True, only_units={n}))
        except anki_deck.DeckError as e:
            sys.exit(f"FAIL\n{e}")
    print(f"preview: build/.cache/card-preview/unit-{n:02d}.png")
