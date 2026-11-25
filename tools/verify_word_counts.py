#!/usr/bin/env python3
"""Verify every lecture file meets the 5,000-word minimum requirement."""
import os as _os
_HERE = _os.path.dirname(_os.path.abspath(__file__))
_ROOT = _os.path.dirname(_HERE)
if _os.getcwd() != _ROOT and not _os.path.isdir("PhD_Marriage_and_Family_Therapy_Lectures"):
    _os.chdir(_ROOT)
import os, glob, re, sys

BASE = "PhD_Marriage_and_Family_Therapy_Lectures"
MIN_WORDS = 5000

expected = {
    "MFLT.901", "MFLT.902", "MFLT.903", "MFLT.904", "MFLT.905", "MFLT.906",
    "MFLT.907", "MFLT.908", "MFLT.909", "MFLT.910", "MFLT.911", "MFLT.912",
    "MFLT.913", "MFLT.914", "MFLT.915", "MFLT.916", "MFLT.917", "MFLT.918",
    "MFLT.919", "MFLT.920", "MFLT.921", "MFLT.922", "MFLT.923", "MFLT.960",
    "MFLT.924", "MFLT.925", "MFLT.926", "MFLT.927", "MFLT.928", "MFLT.929",
    "MFLT.930", "MFLT.931",
}

REQUIRED_SECTIONS = [
    "WELCOME, MY DEAR STUDENTS",
    "Learning Objectives",
    "PART ONE: CORE CONCEPTS",
    "PART TWO: REAL LIFE PRACTICALS",
    "PART THREE: CASE STUDIES",
    "PART THREE-B: DEEPER TEACHING NOTES",
    "PART FOUR: KEY TECHNIQUES",
    "PART FIVE: SUMMARY",
    "Self-Test Questions",
    "Assignment",
]

found = {}
problems = []

for path in sorted(glob.glob(os.path.join(BASE, "*", "*.txt"))):
    name = os.path.basename(path)
    m = re.match(r"MFLT(\d+)_", name)
    if not m:
        continue
    code = f"MFLT.{m.group(1)}"
    text = open(path, encoding="utf-8").read()
    words = len(text.split())
    found[code] = words

    if words < MIN_WORDS:
        problems.append(f"{code}: only {words:,} words (need {MIN_WORDS:,})")
    missing = [s for s in REQUIRED_SECTIONS if s not in text]
    if missing:
        problems.append(f"{code}: missing sections -> {', '.join(missing)}")
    if "REAL LIFE PRACTICAL" not in text:
        problems.append(f"{code}: no real life practicals found")

missing_courses = expected - set(found)
extra_courses = set(found) - expected
if missing_courses:
    problems.append(f"Missing course files: {sorted(missing_courses)}")
if extra_courses:
    problems.append(f"Unexpected course files: {sorted(extra_courses)}")

print("=" * 74)
print("WORD COUNT VERIFICATION - PhD MARRIAGE AND FAMILY LIFE THERAPY")
print("=" * 74)
for code in sorted(found, key=lambda c: (int(c.split(".")[1]) < 900, c)):
    w = found[code]
    flag = "PASS" if w >= MIN_WORDS else "FAIL"
    print(f"{code:<10} {w:>8,} words   {flag}")
print("-" * 74)
total = sum(found.values())
print(f"{'FILES':<10} {len(found):>8}")
print(f"{'TOTAL':<10} {total:>8,} words")
print(f"{'MINIMUM':<10} {min(found.values()):>8,} words")
print(f"{'AVERAGE':<10} {total // len(found):>8,} words")
print("=" * 74)

if problems:
    print("\nPROBLEMS FOUND:")
    for p in problems:
        print(" -", p)
    sys.exit(1)

print("\nRESULT: ALL 32 COURSES PASS. Every lecture is 5,000+ words,")
print("contains real life practicals, all required sections, and is ready")
print("for spoken narration.")
