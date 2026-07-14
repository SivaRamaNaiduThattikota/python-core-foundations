# Builder for Session 4, 01_comprehensions.ipynb (hands-on practice scaffold).
import nbformat as nbf
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell

cells = []
def md(t):   cells.append(new_markdown_cell(t))
def code(t): cells.append(new_code_cell(t))

md('<div style="background:#1e1e2e; padding:16px 20px; border-radius:8px; font-family:monospace; '
   'color:#cdd6f4; line-height:1.8">'
   '<p style="margin:0 0 8px 0; color:#cba6f7; font-weight:bold; font-size:1.05em;">📎 Session 4 — Comprehensions &amp; Generators · Hands-on</p>'
   '<p style="margin:0;">Attempt space for the 12 <strong>Exercises</strong> and 8 <strong>Code Challenges</strong>. '
   'Hints in <code>theory.ipynb</code>; worked solutions in <code>solutions.ipynb</code> — try each yourself first.</p></div>')

md("### Exercises (Part 2 · §6) — 12 problems")
EX = [
 ('E1 (Easy)', 'Squares of even numbers 0-20 (list comp)', '[x*x for x in range(21) if x%2==0]'),
 ('E2 (Easy)', 'Dict comp n -> n**2 for 1..5', '{n: n**2 for n in range(1,6)}'),
 ('E3 (Easy)', 'Set of unique word lengths', '{len(w) for w in words}'),
 ('E4 (Easy)', 'Flatten a 2D list', '[x for row in m for x in row]  (outer for first)'),
 ('E5 (Med)',  'Filter dict comp: keep scores >= 50', '{name: s for name, s in pairs if s >= 50}'),
 ('E6 (Med)',  'Invert a dict (unique values)', '{v: k for k, v in d.items()}  (lossy if values repeat)'),
 ('E7 (Med)',  'Transpose a matrix (nested comp)', '[[row[i] for row in m] for i in range(cols)]'),
 ('E8 (Med)',  'Sum of squares of odd numbers 1-100 (genexpr)', 'sum(x*x for x in range(1,101) if x%2)'),
 ('E9 (Med)',  'Any word longer than 10 chars? (short-circuit)', 'any(len(w) > 10 for w in words)'),
 ('E10 (Hard)','Fibonacci generator (first 10)', 'yield a; a,b=b,a+b in while True; itertools.islice'),
 ('E11 (Hard)','Streaming: total length of non-empty lines', 'sum(len(ln.strip()) for ln in lines if ln.strip())'),
 ('E12 (Hard)','Recursively flatten arbitrary nesting (generator)', 'yield from flatten(x) if isinstance(x,list) else yield x'),
]
for tag, prob, hint in EX:
    code(f"# {tag} — {prob}\n# Hint: {hint}\n\n")

md("### Code Challenges (Part 3 · §8b) — 8 problems")
CC = [
 ('C1 (Easy)', 'List of the first n squares'),
 ('C2 (Easy)', 'Sum of even numbers (genexpr)'),
 ('C3 (Med)',  'Invert a dict'),
 ('C4 (Med)',  'Batch a sequence into chunks of size n: chunk([1..7],3) -> [1,2,3],[4,5,6],[7]'),
 ('C5 (Med)',  'Fibonacci generator'),
 ('C6 (Med)',  'Cumulative sum generator: [1,2,3,4] -> [1,3,6,10]'),
 ('C7 (Hard)', 'Sliding-window generator: windows("abcde",3) -> abc,bcd,cde'),
 ('C8 (Hard)', 'Infinite prime generator + first N via islice'),
]
for tag, prob in CC:
    code(f"# {tag} — {prob}\n\n")

nb = new_notebook(cells=cells)
nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
nb.metadata["language_info"] = {"name": "python"}
nbf.write(nb, "01_comprehensions.ipynb")
print("wrote 01_comprehensions.ipynb with", len(cells), "cells")
