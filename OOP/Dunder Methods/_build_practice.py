# Builder for Session 7B, 01_dunders.ipynb (hands-on practice scaffold).
import nbformat as nbf
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell

cells = []
def md(t):   cells.append(new_markdown_cell(t))
def code(t): cells.append(new_code_cell(t))

md('<div style="background:#1e1e2e; padding:16px 20px; border-radius:8px; font-family:monospace; '
   'color:#cdd6f4; line-height:1.8">'
   '<p style="margin:0 0 8px 0; color:#cba6f7; font-weight:bold; font-size:1.05em;">📎 Session 7B — Dunder Methods · Hands-on</p>'
   '<p style="margin:0;">Attempt space for the 12 <strong>Exercises</strong> and 8 <strong>Code Challenges</strong>. '
   'Hints in <code>theory.ipynb</code>; worked solutions in <code>solutions.ipynb</code> — try each yourself first.</p></div>')

md("### Exercises (Part 2 · §6) — 12 problems")
EX = [
 ('E1 (Easy)', 'Book(title, author) with a recreatable __repr__', 'f"Book({self.title!r}, {self.author!r})"'),
 ('E2 (Easy)', 'Add __str__ to Book: "title by author"', '__str__ friendly; __repr__ stays developer form'),
 ('E3 (Easy)', 'Temperature(celsius): __repr__ + value __eq__', 'isinstance check then compare self.c'),
 ('E4 (Med)',  'Color(r,g,b) hashable -> dedups in a set', '__eq__ + __hash__ over the (r,g,b) tuple'),
 ('E5 (Med)',  'Fix an unhashable class (has __eq__, no __hash__)', 'add __hash__ over the same field(s)'),
 ('E6 (Med)',  'Card(rank) that sorts, via @total_ordering', '@total_ordering + __eq__ + __lt__'),
 ('E7 (Med)',  'Fraction(n,d): __add__, __eq__, __repr__', 'add: (n*o.d + o.n*d, d*o.d); eq: cross-multiply'),
 ('E8 (Med)',  'Duration(seconds): __add__ + "Hh Mm Ss" __repr__', 'sum seconds; //3600, (%3600)//60, %60'),
 ('E9 (Hard)', 'Playlist(songs): __len__ + __getitem__ + __contains__', 'back with a list; __getitem__ also gives iteration/slicing'),
 ('E10 (Hard)','Adder(n): callable instance that adds n', '__call__(self, x): return x + self.n'),
 ('E11 (Hard)','Vector(*components): __len__/__getitem__/__eq__/__add__', 'store *comps as list; add via zip'),
 ('E12 (Hard)','Coordinate(x,y): full value object (repr/eq+NotImplemented/hash/add), dict key', 'eq returns NotImplemented for foreign; hash the (x,y) tuple'),
]
for tag, prob, hint in EX:
    code(f"# {tag} — {prob}\n# Hint: {hint}\n\n")

md("### Code Challenges (Part 3 · §8b) — 8 problems")
CC = [
 ('C1 (Easy)', 'RGBColor(r,g,b): __repr__ as hex #rrggbb'),
 ('C2 (Easy)', 'Time(h,m): __repr__ "HH:MM" + __eq__'),
 ('C3 (Med)',  'CIStr(s): case-insensitive, hashable (__eq__/__hash__ on lowercased)'),
 ('C4 (Med)',  'Vector3D: __sub__ and __abs__ (magnitude)'),
 ('C5 (Med)',  'Matrix2x2: __add__ (element-wise) + __eq__ + __repr__'),
 ('C6 (Med)',  'NumberRange(start, stop): __contains__ + __len__ (half-open)'),
 ('C7 (Hard)', 'Bag (multiset): __add__ / __len__ / __contains__ / __eq__'),
 ('C8 (Hard)', 'Vec: __matmul__ (@ dot product) + __mul__ (scalar) + __eq__'),
]
for tag, prob in CC:
    code(f"# {tag} — {prob}\n\n")

nb = new_notebook(cells=cells)
nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
nb.metadata["language_info"] = {"name": "python"}
nbf.write(nb, "01_dunders.ipynb")
print("wrote 01_dunders.ipynb with", len(cells), "cells")
