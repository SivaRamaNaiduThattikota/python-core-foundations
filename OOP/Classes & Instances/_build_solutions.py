# Builder for Session 7A, solutions.ipynb (answer key).
# Runnable, verified solutions for all 12 Exercises and 8 Code Challenges.
import nbformat as nbf
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell

cells = []
def md(t):   cells.append(new_markdown_cell(t))
def code(t): cells.append(new_code_cell(t))

md('<div style="background:#1e1e2e; padding:16px 20px; border-radius:8px; font-family:monospace; '
   'color:#cdd6f4; line-height:1.8">'
   '<p style="margin:0 0 8px 0; color:#cba6f7; font-weight:bold; font-size:1.05em;">✅ Session 7A — Classes &amp; Instances · Solutions</p>'
   '<p style="margin:0;">Worked, runnable solutions for the 12 <strong>Exercises</strong> and 8 '
   '<strong>Code Challenges</strong>. Run top to bottom to verify. Try them in '
   '<code>01_classes.ipynb</code> first.</p></div>')

md("### Exercises — Solutions")

code('# E1 — Rectangle\n'
    'class Rectangle:\n'
    '    def __init__(self, w, h): self.w = w; self.h = h\n'
    '    def area(self): return self.w * self.h\n'
    '    def perimeter(self): return 2 * (self.w + self.h)\n\n'
    'r = Rectangle(3, 4)\n'
    'print(r.area(), r.perimeter())        # 12 14')
code('# E2 — Circle with class constant PI\n'
    'class Circle:\n'
    '    PI = 3.14159\n'
    '    def __init__(self, radius): self.radius = radius\n'
    '    def area(self): return self.PI * self.radius ** 2\n\n'
    'print(round(Circle(2).area(), 4))     # 12.5664')
code('# E3 — Person\n'
    'class Person:\n'
    '    def __init__(self, name, age): self.name = name; self.age = age\n'
    '    def greet(self): return f"Hi, I\'m {self.name} ({self.age})"\n\n'
    'print(Person("Siva", 27).greet())')
code('# E4 — fix the mutable class attribute bug\n'
    'class Team:\n'
    '    def __init__(self): self.members = []   # per-instance, NOT a class attr\n'
    '    def add(self, m): self.members.append(m)\n\n'
    'a, b = Team(), Team(); a.add("x")\n'
    'print(a.members, b.members)           # [\'x\'] []  - independent')
code('# E5 — Stack\n'
    'class Stack:\n'
    '    def __init__(self): self._items = []\n'
    '    def push(self, x): self._items.append(x)\n'
    '    def pop(self): return self._items.pop()\n'
    '    def peek(self): return self._items[-1]\n'
    '    def is_empty(self): return not self._items\n\n'
    's = Stack(); s.push(1); s.push(2)\n'
    'print(s.peek(), s.pop(), s.is_empty())   # 2 2 False')
code('# E6 — Temperature\n'
    'class Temperature:\n'
    '    def __init__(self, celsius): self.celsius = celsius\n'
    '    def to_fahrenheit(self): return self.celsius * 9/5 + 32\n'
    '    def to_kelvin(self): return self.celsius + 273.15\n\n'
    't = Temperature(100)\n'
    'print(t.to_fahrenheit(), t.to_kelvin())  # 212.0 373.15')
code('# E7 — instance counter\n'
    'class Widget:\n'
    '    count = 0\n'
    '    def __init__(self): Widget.count += 1\n\n'
    'Widget(); Widget(); Widget()\n'
    'print(Widget.count)                   # 3')
code('# E8 — to_dict()\n'
    'class Record:\n'
    '    def __init__(self, **kw):\n'
    '        for k, v in kw.items(): setattr(self, k, v)\n'
    '    def to_dict(self): return dict(vars(self))\n\n'
    'print(Record(a=1, b=2).to_dict())     # {\'a\': 1, \'b\': 2}')
code('# E9 — Vector2D.add returns a NEW vector (pure)\n'
    'class Vector2D:\n'
    '    def __init__(self, x, y): self.x = x; self.y = y\n'
    '    def add(self, other): return Vector2D(self.x + other.x, self.y + other.y)\n\n'
    'v = Vector2D(1, 2).add(Vector2D(3, 4))\n'
    'print((v.x, v.y))                     # (4, 6)')
code('# E10 — Grid built with a comprehension (no aliasing)\n'
    'class Grid:\n'
    '    def __init__(self, rows, cols): self.cells = [[0]*cols for _ in range(rows)]\n'
    '    def set(self, r, c, v): self.cells[r][c] = v\n'
    '    def get(self, r, c): return self.cells[r][c]\n\n'
    'g = Grid(2, 3); g.set(0, 0, 9)\n'
    'print(g.cells)                        # [[9, 0, 0], [0, 0, 0]]')
code('# E11 — Config: defaults (class attr) + overrides (instance)\n'
    'class Config:\n'
    '    defaults = {"lr": 0.01, "epochs": 100}\n'
    '    def __init__(self, **overrides):\n'
    '        for k, v in overrides.items(): setattr(self, k, v)\n'
    '    def get(self, key): return getattr(self, key, self.defaults.get(key))\n\n'
    'cfg = Config(lr=0.001)\n'
    'print(cfg.get("lr"), cfg.get("epochs"))   # 0.001 100')
code('# E12 — Subject/Observer (duck typing: any object with .update)\n'
    'class Subject:\n'
    '    def __init__(self): self.observers = []\n'
    '    def register(self, obs): self.observers.append(obs)\n'
    '    def notify(self, event):\n'
    '        for obs in self.observers: obs.update(event)\n'
    'class Logger:\n'
    '    def __init__(self): self.seen = []\n'
    '    def update(self, event): self.seen.append(event)\n\n'
    'subj = Subject(); log = Logger(); subj.register(log)\n'
    'subj.notify("start"); subj.notify("stop")\n'
    'print(log.seen)                       # [\'start\', \'stop\']')

md("### Code Challenges — Solutions")

code('# C1 — Toggle\n'
    'class Toggle:\n'
    '    def __init__(self): self.on = False\n'
    '    def flip(self): self.on = not self.on; return self.on\n'
    '    def is_on(self): return self.on\n\n'
    't = Toggle()\n'
    'print(t.flip(), t.flip(), t.is_on())   # True False False')
code('# C2 — Queue (FIFO)\n'
    'class Queue:\n'
    '    def __init__(self): self._items = []\n'
    '    def enqueue(self, x): self._items.append(x)\n'
    '    def dequeue(self): return self._items.pop(0)   # O(n); deque is O(1)\n'
    '    def is_empty(self): return not self._items\n\n'
    'q = Queue(); q.enqueue(1); q.enqueue(2)\n'
    'print(q.dequeue(), q.dequeue(), q.is_empty())   # 1 2 True')
code('# C3 — RunningMean (metric accumulator)\n'
    'class RunningMean:\n'
    '    def __init__(self): self.total = 0; self.n = 0\n'
    '    def add(self, x): self.total += x; self.n += 1\n'
    '    def mean(self): return self.total / self.n if self.n else 0\n\n'
    'rm = RunningMean(); rm.add(10); rm.add(20)\n'
    'print(rm.mean())                      # 15.0')
code('# C4 — Histogram\n'
    'class Histogram:\n'
    '    def __init__(self): self._c = {}\n'
    '    def add(self, v): self._c[v] = self._c.get(v, 0) + 1\n'
    '    def counts(self): return dict(self._c)\n\n'
    'h = Histogram()\n'
    'for ch in "aabbbc": h.add(ch)\n'
    'print(h.counts())                     # {\'a\': 2, \'b\': 3, \'c\': 1}')
code('# C5 — Inventory (guarded remove)\n'
    'class Inventory:\n'
    '    def __init__(self): self.stock = {}\n'
    '    def add(self, item, qty): self.stock[item] = self.stock.get(item, 0) + qty\n'
    '    def remove(self, item, qty):\n'
    '        if self.stock.get(item, 0) < qty: raise ValueError("not enough")\n'
    '        self.stock[item] -= qty\n'
    '    def total(self): return sum(self.stock.values())\n\n'
    'inv = Inventory(); inv.add("x", 5); inv.remove("x", 2)\n'
    'print(inv.total())                    # 3\n'
    'try: inv.remove("x", 99)\n'
    'except ValueError as e: print("raised:", e)')
code('# C6 — Player (clamped health invariant)\n'
    'class Player:\n'
    '    def __init__(self, max_health=100):\n'
    '        self.max_health = max_health; self.health = max_health\n'
    '    def take_damage(self, d): self.health = max(0, self.health - d)\n'
    '    def heal(self, h): self.health = min(self.max_health, self.health + h)\n\n'
    'p = Player(100); p.take_damage(150)\n'
    'print(p.health)                       # 0\n'
    'p.heal(30)\n'
    'print(p.health)                       # 30')
code('# C7 — MovingAverage (sliding window)\n'
    'from collections import deque\n'
    'class MovingAverage:\n'
    '    def __init__(self, window): self.vals = deque(maxlen=window)\n'
    '    def add(self, x):\n'
    '        self.vals.append(x)\n'
    '        return sum(self.vals) / len(self.vals)\n\n'
    'ma = MovingAverage(3)\n'
    'print(ma.add(1), ma.add(2), ma.add(3), ma.add(4))   # 1.0 1.5 2.0 3.0')
code('# C8 — MiniDataset (ML Dataset/DataLoader shape)\n'
    'class MiniDataset:\n'
    '    def __init__(self, data): self.data = list(data)\n'
    '    def size(self): return len(self.data)\n'
    '    def get(self, i): return self.data[i]\n'
    '    def batches(self, n): return [self.data[i:i+n] for i in range(0, len(self.data), n)]\n\n'
    'ds = MiniDataset(range(7))\n'
    'print(ds.size(), ds.get(0), ds.batches(3))   # 7 0 [[0,1,2],[3,4,5],[6]]')

nb = new_notebook(cells=cells)
nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
nb.metadata["language_info"] = {"name": "python"}
nbf.write(nb, "solutions.ipynb")
print("wrote solutions.ipynb with", len(cells), "cells")
