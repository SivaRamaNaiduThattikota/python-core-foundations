# Builder for Session 7D, 01_properties.ipynb (hands-on practice scaffold).
import nbformat as nbf
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell

cells = []
def md(t):   cells.append(new_markdown_cell(t))
def code(t): cells.append(new_code_cell(t))

md('<div style="background:#1e1e2e; padding:16px 20px; border-radius:8px; font-family:monospace; '
   'color:#cdd6f4; line-height:1.8">'
   '<p style="margin:0 0 8px 0; color:#cba6f7; font-weight:bold; font-size:1.05em;">📎 Session 7D — Properties &amp; Methods · Hands-on</p>'
   '<p style="margin:0;">Attempt space for the 12 <strong>Exercises</strong> and 8 <strong>Code Challenges</strong>. '
   'Hints in <code>theory.ipynb</code>; worked solutions in <code>solutions.ipynb</code> — try each yourself first.</p></div>')

md("### Exercises (Part 2 · §6) — 12 problems")
EX = [
 ('E1 (Easy)', 'Rectangle(w,h) with read-only @property area', 'getter returns w*h; no setter'),
 ('E2 (Easy)', 'Person(first,last) with full_name property', 'f-string over self.first/self.last'),
 ('E3 (Easy)', 'Circle(radius) with read-only diameter property', 'return self.radius * 2'),
 ('E4 (Med)',  'Age with a validated setter (reject negatives)', '@years.setter raises ValueError if v<0; store self._years'),
 ('E5 (Med)',  'Grade with score setter validated 0-100', 'if not 0<=v<=100: raise ValueError'),
 ('E6 (Med)',  'Money(cents) with read-only dollars property', 'return self.cents / 100'),
 ('E7 (Med)',  'Point.from_tuple((x,y)) classmethod constructor', 'return cls(t[0], t[1])'),
 ('E8 (Med)',  'Color.from_hex("#ff0080") classmethod', 'h.lstrip("#"); int(h[0:2],16) ...; return cls(r,g,b)'),
 ('E9 (Med)',  'TextUtils.word_count(s) @staticmethod', 'return len(s.split())'),
 ('E10 (Hard)','BankAccount: validated balance property + deposit/withdraw + from_dict', 'validating setter + guarded methods + classmethod'),
 ('E11 (Hard)','Vector2D with __slots__ = ("x","y")', 'hasattr(v,"__dict__") is False; v.z=3 raises'),
 ('E12 (Hard)','Temperature: two linked read-write properties (celsius<->fahrenheit)', 'store _celsius; fahrenheit setter writes (v-32)*5/9'),
]
for tag, prob, hint in EX:
    code(f"# {tag} — {prob}\n# Hint: {hint}\n\n")

md("### Code Challenges (Part 3 · §8b) — 8 problems")
CC = [
 ('C1 (Easy)', 'Employee(monthly): read-only annual property (monthly*12)'),
 ('C2 (Easy)', 'Duration.from_minutes(m) classmethod -> stores seconds'),
 ('C3 (Med)',  'Email with a setter validating "@"'),
 ('C4 (Med)',  'Password: @staticmethod is_strong used by the setter'),
 ('C5 (Med)',  'Widget instance counter (class attr + @classmethod total)'),
 ('C6 (Med)',  'Angle: two linked read-write properties (degrees<->radians)'),
 ('C7 (Hard)', 'Vec: __slots__ + magnitude property + from_tuple + __repr__'),
 ('C8 (Hard)', 'functools.cached_property: compute an expensive value once'),
]
for tag, prob in CC:
    code(f"# {tag} — {prob}\n\n")

nb = new_notebook(cells=cells)
nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
nb.metadata["language_info"] = {"name": "python"}
nbf.write(nb, "01_properties.ipynb")
print("wrote 01_properties.ipynb with", len(cells), "cells")
