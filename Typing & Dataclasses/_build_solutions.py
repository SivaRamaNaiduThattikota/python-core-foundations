# Builder for Session 10, solutions.ipynb (answer key).
# Runnable, verified solutions for all 12 Exercises and 8 Code Challenges.
import nbformat as nbf
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell

cells = []
def md(t):   cells.append(new_markdown_cell(t))
def code(t): cells.append(new_code_cell(t))

md('<div style="background:#1e1e2e; padding:16px 20px; border-radius:8px; font-family:monospace; '
   'color:#cdd6f4; line-height:1.8">'
   '<p style="margin:0 0 8px 0; color:#cba6f7; font-weight:bold; font-size:1.05em;">✅ Session 10 — Typing &amp; Dataclasses · Solutions</p>'
   '<p style="margin:0;">Worked, runnable solutions for the 12 <strong>Exercises</strong> and 8 '
   '<strong>Code Challenges</strong>. Run top to bottom to verify. Try them in '
   '<code>01_typing.ipynb</code> first.</p></div>')

code('from dataclasses import dataclass, field, asdict, replace\n'
     'from typing import Optional, Callable, TypeVar, TypedDict, Protocol, Literal, Generic\n'
     'from collections import Counter')

md("### Exercises — Solutions")
code('# E1 — annotate a function\n'
    'def greet(name: str) -> str:\n'
    '    return f"hi {name}"\n\n'
    'print(greet("Ada"))                     # hi Ada')
code('# E2 — annotate a container param\n'
    'def mean(xs: list[float]) -> float:\n'
    '    return sum(xs) / len(xs)\n\n'
    'print(mean([2.0, 4.0]))                 # 3.0')
code('# E3 — return int | None\n'
    'def first_positive(xs: list[int]) -> int | None:\n'
    '    for x in xs:\n'
    '        if x > 0:\n'
    '            return x\n'
    '    return None\n\n'
    'print(first_positive([-1, -2, 5]), first_positive([-1]))   # 5 None')
code('# E4 — Union parameter\n'
    'def to_int(x: int | str) -> int:\n'
    '    return int(x)\n\n'
    'print(to_int(3), to_int("7"))           # 3 7')
code('# E5 — typed Callable parameter\n'
    'def repeat_apply(f: Callable[[int], int], x: int, n: int) -> int:\n'
    '    for _ in range(n):\n'
    '        x = f(x)\n'
    '    return x\n\n'
    'print(repeat_apply(lambda v: v + 1, 0, 5))   # 5')
code('# E6 — generic with TypeVar\n'
    'T = TypeVar("T")\n'
    'def last(xs: list[T]) -> T:\n'
    '    return xs[-1]\n\n'
    'print(last([1, 2, 3]), last(["a", "b"]))     # 3 b')
code('# E7 — basic dataclass (free __repr__ / __eq__)\n'
    '@dataclass\n'
    'class Book:\n'
    '    title: str\n'
    '    author: str\n'
    '    year: int\n\n'
    'b = Book("Dune", "Herbert", 1965)\n'
    'print(b)                                # Book(title=\'Dune\', author=\'Herbert\', year=1965)\n'
    'print(b == Book("Dune", "Herbert", 1965))   # True')
code('# E8 — mutable field via default_factory\n'
    '@dataclass\n'
    'class Cart:\n'
    '    items: list[str] = field(default_factory=list)\n\n'
    'c1, c2 = Cart(), Cart()\n'
    'c1.items.append("apple")\n'
    'print(c1.items, c2.items)               # [\'apple\'] []  (independent)')
code('# E9 — frozen dataclass as a counter key\n'
    '@dataclass(frozen=True)\n'
    'class GridCell:\n'
    '    x: int\n'
    '    y: int\n\n'
    'cells = [GridCell(0, 0), GridCell(1, 1), GridCell(0, 0)]\n'
    'print(Counter(cells)[GridCell(0, 0)])   # 2')
code('# E10 — sort with order=True\n'
    '@dataclass(order=True)\n'
    'class Student:\n'
    '    gpa: float\n'
    '    name: str\n\n'
    'ranked = sorted([Student(3.2, "A"), Student(3.9, "B"), Student(3.5, "C")], reverse=True)\n'
    'print([s.name for s in ranked])         # [\'B\', \'C\', \'A\']')
code('# E11 — TypedDict payload + reader\n'
    'class Payload(TypedDict):\n'
    '    user_id: int\n'
    '    active: bool\n\n'
    'def is_active(p: Payload) -> bool:\n'
    '    return p["active"]\n\n'
    'print(is_active({"user_id": 1, "active": True}))   # True')
code('# E12 — structural typing with Protocol\n'
    'class HasName(Protocol):\n'
    '    name: str\n\n'
    'def describe(obj: HasName) -> str:\n'
    '    return f"name={obj.name}"\n\n'
    '@dataclass\n'
    'class Dog:\n'
    '    name: str\n\n'
    'print(describe(Dog("Rex")))             # name=Rex')

md("### Code Challenges — Solutions")
code('# C1 — frozen + hashable de-dup\n'
    '@dataclass(frozen=True)\n'
    'class Money:\n'
    '    amount: int\n'
    '    currency: str\n\n'
    'coins = {Money(10, "USD"), Money(10, "USD"), Money(5, "EUR")}\n'
    'print(len(coins))                       # 2  (duplicate collapsed)')
code('# C2 — type alias + function\n'
    'JSONNum = list[float]\n'
    'def normalize(v: JSONNum) -> JSONNum:\n'
    '    s = sum(v)\n'
    '    return [x / s for x in v]\n\n'
    'print(normalize([1.0, 3.0]))            # [0.25, 0.75]')
code('# C3 — sort ignoring a field via compare=False\n'
    '@dataclass(order=True)\n'
    'class Task:\n'
    '    priority: int\n'
    '    label: str = field(compare=False)\n\n'
    'print(sorted([Task(2, "b"), Task(1, "a")])[0].label)   # a\n'
    'print(Task(1, "x") == Task(1, "y"))     # True  (label ignored)')
code('# C4 — validate in __post_init__\n'
    '@dataclass\n'
    'class Percentage:\n'
    '    value: float\n'
    '    def __post_init__(self):\n'
    '        if not 0 <= self.value <= 100:\n'
    '            raise ValueError("0..100")\n\n'
    'print(Percentage(50).value)             # 50\n'
    'try: Percentage(150)\n'
    'except ValueError as e: print("guard:", e)   # guard: 0..100')
code('# C5 — generic Stack[T]\n'
    'class Stack(Generic[T]):\n'
    '    def __init__(self) -> None:\n'
    '        self._items: list[T] = []\n'
    '    def push(self, x: T) -> None:\n'
    '        self._items.append(x)\n'
    '    def pop(self) -> T:\n'
    '        return self._items.pop()\n\n'
    's: Stack[int] = Stack()\n'
    's.push(1); s.push(2)\n'
    'print(s.pop(), s.pop())                 # 2 1')
code('# C6 — Protocol over unrelated model classes\n'
    'class SupportsPredict(Protocol):\n'
    '    def predict(self, x: float) -> float: ...\n\n'
    'class Const:\n'
    '    def __init__(self, c): self.c = c\n'
    '    def predict(self, x): return self.c\n'
    'class Double:\n'
    '    def predict(self, x): return x * 2\n\n'
    'def score(models: list[SupportsPredict], x: float) -> list[float]:\n'
    '    return [m.predict(x) for m in models]\n\n'
    'print(score([Const(5), Double()], 3))   # [5, 6]')
code('# C7 — immutable update with replace\n'
    '@dataclass(frozen=True)\n'
    'class HyperParams:\n'
    '    lr: float = 0.01\n'
    '    epochs: int = 10\n\n'
    'def with_lr(cfg: HyperParams, lr: float) -> HyperParams:\n'
    '    return replace(cfg, lr=lr)\n\n'
    'base = HyperParams()\n'
    'tuned = with_lr(base, 0.1)\n'
    'print(base.lr, tuned.lr, base is tuned) # 0.01 0.1 False')
code('# C8 — hand-rolled schema validation (Pydantic-lite)\n'
    'class UserT(TypedDict):\n'
    '    name: str\n'
    '    age: int\n\n'
    'def validate(d: dict, schema: type) -> bool:\n'
    '    hints = schema.__annotations__\n'
    '    return all(k in d and isinstance(d[k], t) for k, t in hints.items())\n\n'
    'print(validate({"name": "Ada", "age": 30}, UserT))   # True\n'
    'print(validate({"name": "Ada"}, UserT))              # False  (missing age)')

nb = new_notebook(cells=cells)
nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
nb.metadata["language_info"] = {"name": "python"}
nbf.write(nb, "solutions.ipynb")
print("wrote solutions.ipynb with", len(cells), "cells")
