# Builder for Session 3 - Strings, 01_string.ipynb (hands-on practice scaffold).
# Problems as comments + empty attempt space. Solutions live in solutions.ipynb.
import nbformat as nbf
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell

cells = []
def md(t):   cells.append(new_markdown_cell(t))
def code(t): cells.append(new_code_cell(t))

md('<div style="background:#1e1e2e; padding:16px 20px; border-radius:8px; font-family:monospace; '
   'color:#cdd6f4; line-height:1.8">'
   '<p style="margin:0 0 8px 0; color:#cba6f7; font-weight:bold; font-size:1.05em;">📎 Session 3 — Strings · Hands-on</p>'
   '<p style="margin:0;">Your attempt space for the Part 2 <strong>Exercises</strong> (12) and Part 3 '
   '<strong>Code Challenges</strong> (8). Hints are in <code>theory.ipynb</code>; worked solutions in '
   '<code>solutions.ipynb</code> — try each yourself first.</p></div>')

md("### Exercises (Part 2 · §6) — 12 problems")
EX = [
 ('E1 (Easy)', 'Reverse word order: "the cat sat" -> "sat cat the"', 'split() -> reverse [::-1] -> " ".join(...)'),
 ('E2 (Easy)', 'Count vowels, case-insensitive: "Education" -> 5', '.lower(), sum(1 for c in s if c in "aeiou")'),
 ('E3 (Easy)', 'Title-case a name: "siva rama naidu" -> "Siva Rama Naidu"', 'split(), .capitalize() each, " ".join(...)'),
 ('E4 (Easy)', 'File extension: "report.final.csv" -> "csv"', 'rsplit(".",1)[-1] or rpartition(".")[2]'),
 ('E5 (Med)',  'Clean CSV fields: "a, b ,c , d" -> [\'a\',\'b\',\'c\',\'d\']', 'split(","), .strip() each in a comprehension'),
 ('E6 (Med)',  'Valid palindrome (alnum, case-insensitive): "A man, a plan, a canal: Panama" -> True', 'keep .isalnum(), lower, compare to reverse'),
 ('E7 (Med)',  'Most frequent character: "mississippi" -> \'i\' (tie -> first-seen)', 'Counter(s).most_common(1)[0][0]'),
 ('E8 (Med)',  'Aligned report row: ("precision", 0.8734) -> \'precision  87.3%\'', 'f"{name:<10}{score:>6.1%}"'),
 ('E9 (Med)',  'Caesar cipher: caesar("xyz", 3) -> "abc" (wrap, keep case, leave non-letters)', 'base=ord(\'a\'/\'A\'); chr((ord(ch)-base+k)%26+base)'),
 ('E10 (Hard)','Run-length encode: "aaabbc" -> "a3b2c1"', 'track char+count, append on change, join; handle ""'),
 ('E11 (Hard)','Longest repeated-char run: "aaabbbbcc" -> (\'b\', 4)', 'RLE accumulator, keep best (char,count)'),
 ('E12 (Hard)','Reverse only the vowels: "leetcode" -> "leotcede"', 'two pointers; swap when both point at vowels'),
]
for tag, prob, hint in EX:
    code(f"# {tag} — {prob}\n# Hint: {hint}\n\n")

md("### Code Challenges (Part 3 · §8b) — 8 problems")
CC = [
 ('C1 (Easy)', 'Reverse a string: reverse("hello") -> "olleh"'),
 ('C2 (Easy)', 'Anagram check: is_anagram("listen","silent") -> True'),
 ('C3 (Med)',  'First non-repeating char: "leetcode" -> "l", "aabb" -> None'),
 ('C4 (Med)',  'Word frequency: "the cat the dog the" -> {the:3, cat:1, dog:1}'),
 ('C5 (Med)',  'Valid palindrome: "A man, a plan, a canal: Panama" -> True'),
 ('C6 (Med)',  'Run-length encode: "aaabbc" -> "a3b2c1"'),
 ('C7 (Hard)', 'Longest substring w/o repeating chars: "abcabcbb" -> 3, "pwwkew" -> 3'),
 ('C8 (Hard)', 'Group anagrams: ["eat","tea","tan","ate","nat","bat"] -> grouped'),
]
for tag, prob in CC:
    code(f"# {tag} — {prob}\n\n")

nb = new_notebook(cells=cells)
nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
nb.metadata["language_info"] = {"name": "python"}
nbf.write(nb, "01_string.ipynb")
print("wrote 01_string.ipynb with", len(cells), "cells")
