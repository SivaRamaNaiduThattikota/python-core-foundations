# Builder for Session 7B, solutions.ipynb (answer key).
# Runnable, verified solutions for all 12 Exercises and 8 Code Challenges.
import nbformat as nbf
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell

cells = []
def md(t):   cells.append(new_markdown_cell(t))
def code(t): cells.append(new_code_cell(t))

md('<div style="background:#1e1e2e; padding:16px 20px; border-radius:8px; font-family:monospace; '
   'color:#cdd6f4; line-height:1.8">'
   '<p style="margin:0 0 8px 0; color:#cba6f7; font-weight:bold; font-size:1.05em;">✅ Session 7B — Dunder Methods · Solutions</p>'
   '<p style="margin:0;">Worked, runnable solutions for the 12 <strong>Exercises</strong> and 8 '
   '<strong>Code Challenges</strong>. Run top to bottom to verify. Try them in '
   '<code>01_dunders.ipynb</code> first.</p></div>')

md("### Exercises — Solutions")

code('from functools import total_ordering')
code('# E1/E2 — Book: __repr__ (developer) + __str__ (friendly)\n'
    'class Book:\n'
    '    def __init__(self, t, a): self.title = t; self.author = a\n'
    '    def __repr__(self): return f"Book({self.title!r}, {self.author!r})"\n'
    '    def __str__(self): return f"{self.title} by {self.author}"\n\n'
    'b = Book("Dune", "Herbert")\n'
    'print(repr(b))                        # Book(\'Dune\', \'Herbert\')\n'
    'print(str(b))                         # Dune by Herbert')
code('# E3 — Temperature: __repr__ + value __eq__\n'
    'class Temperature:\n'
    '    def __init__(self, c): self.c = c\n'
    '    def __repr__(self): return f"Temperature({self.c})"\n'
    '    def __eq__(self, o): return isinstance(o, Temperature) and self.c == o.c\n\n'
    'print(Temperature(20) == Temperature(20), Temperature(20) == Temperature(21))   # True False')
code('# E4 — Color hashable\n'
    'class Color:\n'
    '    def __init__(self, r, g, b): self.rgb = (r, g, b)\n'
    '    def __eq__(self, o): return isinstance(o, Color) and self.rgb == o.rgb\n'
    '    def __hash__(self): return hash(self.rgb)\n\n'
    'print(len({Color(255,0,0), Color(255,0,0), Color(0,0,0)}))   # 2')
code('# E5 — fix an unhashable class (add __hash__)\n'
    'class Tag:\n'
    '    def __init__(self, name): self.name = name\n'
    '    def __eq__(self, o): return self.name == o.name\n'
    '    def __hash__(self): return hash(self.name)   # <- the fix\n\n'
    'print(len({Tag("a"), Tag("a")}), Tag.__hash__ is None)   # 1 False')
code('# E6 — Card sorts via @total_ordering\n'
    '@total_ordering\n'
    'class Card:\n'
    '    def __init__(self, rank): self.rank = rank\n'
    '    def __repr__(self): return f"Card({self.rank})"\n'
    '    def __eq__(self, o): return self.rank == o.rank\n'
    '    def __lt__(self, o): return self.rank < o.rank\n\n'
    'print(sorted([Card(5), Card(2), Card(9)]))   # [Card(2), Card(5), Card(9)]')
code('# E7 — Fraction: __add__, __eq__, __repr__\n'
    'class Fraction:\n'
    '    def __init__(self, n, d): self.n = n; self.d = d\n'
    '    def __add__(self, o): return Fraction(self.n*o.d + o.n*self.d, self.d*o.d)\n'
    '    def __eq__(self, o): return self.n * o.d == o.n * self.d\n'
    '    def __repr__(self): return f"{self.n}/{self.d}"\n\n'
    'print(Fraction(1,2) + Fraction(1,3), Fraction(1,2) == Fraction(2,4))   # 5/6 True')
code('# E8 — Duration: __add__ + "Hh Mm Ss" __repr__\n'
    'class Duration:\n'
    '    def __init__(self, seconds): self.seconds = seconds\n'
    '    def __add__(self, o): return Duration(self.seconds + o.seconds)\n'
    '    def __repr__(self):\n'
    '        s = self.seconds\n'
    '        return f"{s//3600}h {(s%3600)//60}m {s%60}s"\n\n'
    'print(Duration(3661) + Duration(60))   # 1h 2m 1s')
code('# E9 — Playlist: container protocol\n'
    'class Playlist:\n'
    '    def __init__(self, songs): self.songs = list(songs)\n'
    '    def __len__(self): return len(self.songs)\n'
    '    def __getitem__(self, i): return self.songs[i]\n'
    '    def __contains__(self, s): return s in self.songs\n\n'
    'pl = Playlist(["a", "b", "c"])\n'
    'print(len(pl), pl[0], "b" in pl, list(pl))   # 3 a True [\'a\', \'b\', \'c\']')
code('# E10 — Adder: callable instance\n'
    'class Adder:\n'
    '    def __init__(self, n): self.n = n\n'
    '    def __call__(self, x): return x + self.n\n\n'
    'print(Adder(10)(5))                   # 15')
code('# E11 — n-dim Vector: container + operator protocols\n'
    'class Vector:\n'
    '    def __init__(self, *comps): self.comps = list(comps)\n'
    '    def __len__(self): return len(self.comps)\n'
    '    def __getitem__(self, i): return self.comps[i]\n'
    '    def __eq__(self, o): return self.comps == o.comps\n'
    '    def __add__(self, o): return Vector(*[a+b for a, b in zip(self.comps, o.comps)])\n'
    '    def __repr__(self): return f"Vector{tuple(self.comps)}"\n\n'
    'print(Vector(1,2,3) + Vector(4,5,6), len(Vector(1,2,3)), Vector(1,2,3)[0])   # Vector(5, 7, 9) 3 1')
code('# E12 — Coordinate: full value object, usable as a dict key\n'
    'class Coordinate:\n'
    '    def __init__(self, x, y): self.x = x; self.y = y\n'
    '    def __repr__(self): return f"Coordinate({self.x}, {self.y})"\n'
    '    def __eq__(self, o):\n'
    '        if not isinstance(o, Coordinate): return NotImplemented\n'
    '        return (self.x, self.y) == (o.x, o.y)\n'
    '    def __hash__(self): return hash((self.x, self.y))\n'
    '    def __add__(self, o): return Coordinate(self.x + o.x, self.y + o.y)\n\n'
    'print({Coordinate(1,2): "home"}[Coordinate(1,2)])   # home\n'
    'print(Coordinate(1,2) + Coordinate(3,4))            # Coordinate(4, 6)\n'
    'print(Coordinate(1,2) == "x")                       # False')

md("### Code Challenges — Solutions")

code('# C1 — RGBColor hex repr\n'
    'class RGBColor:\n'
    '    def __init__(self, r, g, b): self.r = r; self.g = g; self.b = b\n'
    '    def __repr__(self): return f"#{self.r:02x}{self.g:02x}{self.b:02x}"\n\n'
    'print(RGBColor(255, 0, 128))          # #ff0080')
code('# C2 — Time repr + eq\n'
    'class Time:\n'
    '    def __init__(self, h, m): self.h = h; self.m = m\n'
    '    def __repr__(self): return f"{self.h:02d}:{self.m:02d}"\n'
    '    def __eq__(self, o): return (self.h, self.m) == (o.h, o.m)\n\n'
    'print(Time(9, 5), Time(9,5) == Time(9,5))   # 09:05 True')
code('# C3 — CIStr: case-insensitive, hashable\n'
    'class CIStr:\n'
    '    def __init__(self, s): self.s = s\n'
    '    def __eq__(self, o): return self.s.lower() == o.s.lower()\n'
    '    def __hash__(self): return hash(self.s.lower())\n'
    '    def __repr__(self): return f"CIStr({self.s!r})"\n\n'
    'print(CIStr("ABC") == CIStr("abc"), len({CIStr("Hi"), CIStr("hi")}))   # True 1')
code('# C4 — Vector3D: __sub__ + __abs__ (magnitude)\n'
    'class Vector3D:\n'
    '    def __init__(self, x, y, z): self.x = x; self.y = y; self.z = z\n'
    '    def __sub__(self, o): return Vector3D(self.x-o.x, self.y-o.y, self.z-o.z)\n'
    '    def __abs__(self): return (self.x**2 + self.y**2 + self.z**2) ** 0.5\n'
    '    def __repr__(self): return f"Vector3D({self.x}, {self.y}, {self.z})"\n\n'
    'print(abs(Vector3D(3,4,0)), Vector3D(5,5,5) - Vector3D(1,2,3))   # 5.0 Vector3D(4, 3, 2)')
code('# C5 — Matrix2x2: element-wise __add__ + __eq__\n'
    'class Matrix2x2:\n'
    '    def __init__(self, a, b, c, d): self.a=a; self.b=b; self.c=c; self.d=d\n'
    '    def __add__(self, o): return Matrix2x2(self.a+o.a, self.b+o.b, self.c+o.c, self.d+o.d)\n'
    '    def __eq__(self, o): return (self.a,self.b,self.c,self.d) == (o.a,o.b,o.c,o.d)\n'
    '    def __repr__(self): return f"[[{self.a}, {self.b}], [{self.c}, {self.d}]]"\n\n'
    'print(Matrix2x2(1,2,3,4) + Matrix2x2(1,1,1,1))   # [[2, 3], [4, 5]]')
code('# C6 — NumberRange: __contains__ + __len__ (half-open)\n'
    'class NumberRange:\n'
    '    def __init__(self, start, stop): self.start = start; self.stop = stop\n'
    '    def __contains__(self, x): return self.start <= x < self.stop\n'
    '    def __len__(self): return max(0, self.stop - self.start)\n\n'
    'r = NumberRange(2, 7)\n'
    'print(5 in r, 7 in r, len(r))         # True False 5')
code('# C7 — Bag (multiset)\n'
    'class Bag:\n'
    '    def __init__(self, items=()):\n'
    '        self.counts = {}\n'
    '        for it in items: self.counts[it] = self.counts.get(it, 0) + 1\n'
    '    def __add__(self, o):\n'
    '        m = dict(self.counts)\n'
    '        for k, v in o.counts.items(): m[k] = m.get(k, 0) + v\n'
    '        b = Bag(); b.counts = m; return b\n'
    '    def __len__(self): return sum(self.counts.values())\n'
    '    def __contains__(self, x): return x in self.counts\n'
    '    def __eq__(self, o): return self.counts == o.counts\n'
    '    def __repr__(self): return f"Bag({self.counts})"\n\n'
    'big = Bag("aab") + Bag("bc")\n'
    'print(big, len(big), "a" in big)      # Bag({\'a\': 2, \'b\': 2, \'c\': 1}) 5 True')
code('# C8 — Vec: __matmul__ (@ dot product) + __mul__ (scalar)\n'
    'class Vec:\n'
    '    def __init__(self, *c): self.c = list(c)\n'
    '    def __matmul__(self, o): return sum(a*b for a, b in zip(self.c, o.c))\n'
    '    def __mul__(self, k): return Vec(*[a*k for a in self.c])\n'
    '    def __eq__(self, o): return self.c == o.c\n'
    '    def __repr__(self): return f"Vec{tuple(self.c)}"\n\n'
    'print(Vec(1,2,3) @ Vec(4,5,6), Vec(1,2) * 3)   # 32 Vec(3, 6)')

nb = new_notebook(cells=cells)
nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
nb.metadata["language_info"] = {"name": "python"}
nbf.write(nb, "solutions.ipynb")
print("wrote solutions.ipynb with", len(cells), "cells")
