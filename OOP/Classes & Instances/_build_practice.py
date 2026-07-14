# Builder for Session 7A, 01_classes.ipynb (hands-on practice scaffold).
import nbformat as nbf
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell

cells = []
def md(t):   cells.append(new_markdown_cell(t))
def code(t): cells.append(new_code_cell(t))

md('<div style="background:#1e1e2e; padding:16px 20px; border-radius:8px; font-family:monospace; '
   'color:#cdd6f4; line-height:1.8">'
   '<p style="margin:0 0 8px 0; color:#cba6f7; font-weight:bold; font-size:1.05em;">📎 Session 7A — Classes &amp; Instances · Hands-on</p>'
   '<p style="margin:0;">Attempt space for the 12 <strong>Exercises</strong> and 8 <strong>Code Challenges</strong>. '
   'Hints in <code>theory.ipynb</code>; worked solutions in <code>solutions.ipynb</code> — try each yourself first.</p></div>')

md("### Exercises (Part 2 · §6) — 12 problems")
EX = [
 ('E1 (Easy)', 'Rectangle(w, h) with area() and perimeter()', 'store w/h in __init__; methods use self'),
 ('E2 (Easy)', 'Circle(radius) with class constant PI and area()', 'PI is a class attribute; area() reads self.PI'),
 ('E3 (Easy)', 'Person(name, age) with greet()', 'f-string using self.name/self.age'),
 ('E4 (Med)',  'Fix a mutable-class-attribute bug in Team', 'move members=[] into __init__; prove two teams independent'),
 ('E5 (Med)',  'Stack: push/pop/peek/is_empty', 'list created in __init__; is_empty -> not self._items'),
 ('E6 (Med)',  'Temperature(celsius): to_fahrenheit(), to_kelvin()', 'compute from self.celsius'),
 ('E7 (Med)',  'Instance counter: track how many objects created', 'class attr count; ClassName.count += 1 in __init__'),
 ('E8 (Med)',  'to_dict(): return instance attributes as a dict', 'dict(vars(self)) i.e. copy of __dict__'),
 ('E9 (Hard)', 'Vector2D(x,y) with add(other) returning a NEW vector', 'return Vector2D(self.x+other.x, self.y+other.y) - pure'),
 ('E10 (Hard)','Grid(rows, cols) with get(r,c)/set(r,c,v)', '[[0]*cols for _ in range(rows)] - NOT [[0]*cols]*rows'),
 ('E11 (Hard)','Config: class-attr defaults + instance overrides, get(key)', 'getattr(self, key, self.defaults.get(key))'),
 ('E12 (Hard)','Subject/Observer: register(obs) + notify(event)', 'notify calls obs.update(event) on each - duck typing'),
]
for tag, prob, hint in EX:
    code(f"# {tag} — {prob}\n# Hint: {hint}\n\n")

md("### Code Challenges (Part 3 · §8b) — 8 problems")
CC = [
 ('C1 (Easy)', 'Toggle: flip() flips a boolean, is_on() reads it'),
 ('C2 (Easy)', 'Queue (FIFO): enqueue/dequeue/is_empty'),
 ('C3 (Med)',  'RunningMean: add(x), mean() (metric accumulator)'),
 ('C4 (Med)',  'Histogram: add(v), counts() -> dict of value->count'),
 ('C5 (Med)',  'Inventory: add/remove (guard) / total'),
 ('C6 (Med)',  'Player: health clamped to [0, max_health]'),
 ('C7 (Hard)', 'MovingAverage(window): average of the last `window` values'),
 ('C8 (Hard)', 'MiniDataset(data): size()/get(i)/batches(n) (ML Dataset shape)'),
]
for tag, prob in CC:
    code(f"# {tag} — {prob}\n\n")

nb = new_notebook(cells=cells)
nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
nb.metadata["language_info"] = {"name": "python"}
nbf.write(nb, "01_classes.ipynb")
print("wrote 01_classes.ipynb with", len(cells), "cells")
