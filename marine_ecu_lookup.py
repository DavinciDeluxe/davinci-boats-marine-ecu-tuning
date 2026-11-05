#!/usr/bin/env python3
"""DaVinci Deluxe Cloud Edition Boats — Marine ECU & Brand Coverage Lookup (https://www.davincideluxe.fr/boats)"""
import json, pathlib, sys

def main():
    p = pathlib.Path(__file__).parent / "data" / "marine_brands_ecus.json"
    data = json.loads(p.read_text(encoding="utf-8"))
    q = (sys.argv[1] if len(sys.argv) > 1 else "").lower()
    for row in data["brands"]:
        if not q or q in row["brand"].lower() or q in row["ecus"].lower():
            print(f"{row['brand']} [{row['segment']}]: {row['ecus']}")

if __name__ == "__main__":
    main()
