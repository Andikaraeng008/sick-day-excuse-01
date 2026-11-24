import os

TEXT = "I got food poisoning from my own meal prep. I followed the recipe exactly, and it still betrayed me."

assert 1 <= len(TEXT) <= 200 and TEXT.strip(), "entry must be 1-200 chars, not whitespace-only"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(TEXT)
