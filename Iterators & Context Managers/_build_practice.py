# Builder for Session 8, 01_iterators.ipynb (hands-on practice scaffold).
import nbformat as nbf
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell

cells = []
def md(t):   cells.append(new_markdown_cell(t))
def code(t): cells.append(new_code_cell(t))

md('<div style="background:#1e1e2e; padding:16px 20px; border-radius:8px; font-family:monospace; '
   'color:#cdd6f4; line-height:1.8">'
   '<p style="margin:0 0 8px 0; color:#cba6f7; font-weight:bold; font-size:1.05em;">📎 Session 8 — Iterators &amp; Context Managers · Hands-on</p>'
   '<p style="margin:0;">Attempt space for the 12 <strong>Exercises</strong> and 8 <strong>Code Challenges</strong>. '
   'Hints in <code>theory.ipynb</code>; worked solutions in <code>solutions.ipynb</code> — try each yourself first.</p></div>')

md("### Exercises (Part 2 · §6) — 12 problems")
EX = [
 ('E1 (Easy)', 'Pull first two values from a list with iter()/next()', 'it = iter(xs); next(it); next(it)'),
 ('E2 (Easy)', 'Generator evens(n) yielding first n even numbers', 'for i in range(n): yield i*2'),
 ('E3 (Easy)', 'Repeat(value, times) - re-iterable (loops twice)', '__iter__ as generator method'),
 ('E4 (Med)',  'CountUp(start, stop) custom iterator class', '__iter__ returns self; __next__ raises StopIteration at stop'),
 ('E5 (Med)',  'naturals() infinite generator + islice for first N', 'while True: yield n; n+=1; itertools.islice'),
 ('E6 (Med)',  'first(iterable, pred, default=None) - first match or default', 'next((x for x in it if pred(x)), default)'),
 ('E7 (Med)',  'batched(iterable, n) generator yielding chunks of size n', 'accumulate; yield+reset at n; flush remainder'),
 ('E8 (Med)',  'Tag(name) context manager: prints <name> / </name>', '__enter__ open tag; __exit__ close tag'),
 ('E9 (Med)',  '@contextmanager timer(out) capturing elapsed time', 'record start; try: yield / finally: out.append(elapsed)'),
 ('E10 (Hard)','@contextmanager setattr_temp(obj, attr, value) - set & restore', 'save old; set new; try: yield / finally: restore'),
 ('E11 (Hard)','Reimplement suppress(*excs) as a context-manager class', '__exit__ returns True when exc_type subclasses one of excs'),
 ('E12 (Hard)','pairwise(iterable) -> (a,b),(b,c),...', 'keep prev; iterate rest yielding (prev,cur); advance prev'),
]
for tag, prob, hint in EX:
    code(f"# {tag} — {prob}\n# Hint: {hint}\n\n")

md("### Code Challenges (Part 3 · §8b) — 8 problems")
CC = [
 ('C1 (Easy)', 'take(iterable, n): first n items as a list (islice)'),
 ('C2 (Easy)', 'ilen(iterable): count by consuming (one-shot iterators)'),
 ('C3 (Med)',  'unique(iterable): dedup, preserving first-seen order'),
 ('C4 (Med)',  'sliding_window(iterable, k): tuples of k consecutive items'),
 ('C5 (Med)',  'Reimplement enumerate(iterable, start)'),
 ('C6 (Med)',  '@contextmanager capture_stdout(): capture printed output'),
 ('C7 (Hard)', 'A class that is BOTH an iterator and a context manager'),
 ('C8 (Hard)', 'Manage a dynamic number of context managers with ExitStack'),
]
for tag, prob in CC:
    code(f"# {tag} — {prob}\n\n")

nb = new_notebook(cells=cells)
nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
nb.metadata["language_info"] = {"name": "python"}
nbf.write(nb, "01_iterators.ipynb")
print("wrote 01_iterators.ipynb with", len(cells), "cells")
