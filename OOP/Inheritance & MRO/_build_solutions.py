# Builder for Session 7C, solutions.ipynb (answer key).
# Runnable, verified solutions for all 12 Exercises and 8 Code Challenges.
import nbformat as nbf
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell

cells = []
def md(t):   cells.append(new_markdown_cell(t))
def code(t): cells.append(new_code_cell(t))

md('<div style="background:#1e1e2e; padding:16px 20px; border-radius:8px; font-family:monospace; '
   'color:#cdd6f4; line-height:1.8">'
   '<p style="margin:0 0 8px 0; color:#cba6f7; font-weight:bold; font-size:1.05em;">✅ Session 7C — Inheritance &amp; MRO · Solutions</p>'
   '<p style="margin:0;">Worked, runnable solutions for the 12 <strong>Exercises</strong> and 8 '
   '<strong>Code Challenges</strong>. Run top to bottom to verify. Try them in '
   '<code>01_inheritance.ipynb</code> first.</p></div>')

md("### Exercises — Solutions")
code('from abc import ABC, abstractmethod\n'
    'from typing import Protocol, runtime_checkable')
code('# E1 — Vehicle base + subclasses\n'
    'class Vehicle:\n'
    '    def __init__(self, wheels): self.wheels = wheels\n'
    '    def describe(self): return f"{type(self).__name__} with {self.wheels} wheels"\n'
    'class Car(Vehicle):\n'
    '    def __init__(self): super().__init__(4)\n'
    'class Motorcycle(Vehicle):\n'
    '    def __init__(self): super().__init__(2)\n\n'
    'print(Car().describe(), "|", Motorcycle().describe())')
code('# E2 — Shape polymorphic sum\n'
    'class Shape:\n'
    '    def area(self): raise NotImplementedError\n'
    'class Circle(Shape):\n'
    '    def __init__(self, r): self.r = r\n'
    '    def area(self): return 3.14159 * self.r ** 2\n'
    'class Square(Shape):\n'
    '    def __init__(self, s): self.s = s\n'
    '    def area(self): return self.s ** 2\n\n'
    'print(round(sum(s.area() for s in [Circle(1), Square(2)]), 5))   # 7.14159')
code('# E3 — Student via super().__init__\n'
    'class Person:\n'
    '    def __init__(self, name): self.name = name\n'
    'class Student(Person):\n'
    '    def __init__(self, name, school):\n'
    '        super().__init__(name)\n'
    '        self.school = school\n\n'
    's = Student("Siva", "MIT")\n'
    'print(s.name, s.school)               # Siva MIT')
code('# E4 — extend a method with super()\n'
    'class Greeter:\n'
    '    def greet(self): return "Hello"\n'
    'class PoliteGreeter(Greeter):\n'
    '    def greet(self): return super().greet() + ", please"\n\n'
    'print(PoliteGreeter().greet())        # Hello, please')
code('# E5 — DictReprMixin\n'
    'class DictReprMixin:\n'
    '    def __repr__(self): return f"{type(self).__name__}({self.__dict__})"\n'
    'class Item(DictReprMixin):\n'
    '    def __init__(self, name, price): self.name = name; self.price = price\n\n'
    'print(repr(Item("x", 5)))             # Item({\'name\': \'x\', \'price\': 5})')
code('# E6 — Storage ABC + DictStorage\n'
    'class Storage(ABC):\n'
    '    @abstractmethod\n'
    '    def save(self, k, v): ...\n'
    '    @abstractmethod\n'
    '    def load(self, k): ...\n'
    'class DictStorage(Storage):\n'
    '    def __init__(self): self.d = {}\n'
    '    def save(self, k, v): self.d[k] = v\n'
    '    def load(self, k): return self.d.get(k)\n\n'
    'ds = DictStorage(); ds.save("a", 1)\n'
    'print(ds.load("a"))                   # 1\n'
    'try: Storage()\n'
    'except TypeError: print("Storage() -> TypeError")')
code('# E7 — Wallet via composition\n'
    'class Wallet:\n'
    '    def __init__(self): self.amounts = []\n'
    '    def deposit(self, x): self.amounts.append(x)\n'
    '    def total(self): return sum(self.amounts)\n\n'
    'w = Wallet(); w.deposit(10); w.deposit(5)\n'
    'print(w.total())                      # 15')
code('# E8 — hierarchy checks\n'
    'class A: pass\n'
    'class B(A): pass\n'
    'class C(B): pass\n\n'
    'print(issubclass(C, A), isinstance(C(), A), isinstance(A(), C))   # True True False')
code('# E9 — diamond MRO cooperative super()\n'
    'class X:\n'
    '    def m(self): return ["X"]\n'
    'class Y(X):\n'
    '    def m(self): return ["Y"] + super().m()\n'
    'class Z(X):\n'
    '    def m(self): return ["Z"] + super().m()\n'
    'class W(Y, Z):\n'
    '    def m(self): return ["W"] + super().m()\n\n'
    'print(W().m())                        # [\'W\', \'Y\', \'Z\', \'X\']\n'
    'print([c.__name__ for c in W.__mro__])')
code('# E10 — HasArea Protocol\n'
    '@runtime_checkable\n'
    'class HasArea(Protocol):\n'
    '    def area(self) -> float: ...\n\n'
    'print(isinstance(Circle(1), HasArea), isinstance("x", HasArea))   # True False')
code('# E11 — template-method Pipeline ABC\n'
    'class Pipeline(ABC):\n'
    '    def run(self):\n'
    '        return self.load(self.transform(self.extract()))\n'
    '    @abstractmethod\n'
    '    def extract(self): ...\n'
    '    @abstractmethod\n'
    '    def transform(self, d): ...\n'
    '    @abstractmethod\n'
    '    def load(self, d): ...\n'
    'class Demo(Pipeline):\n'
    '    def extract(self): return [1, 2, 3]\n'
    '    def transform(self, d): return [x*2 for x in d]\n'
    '    def load(self, d): return sum(d)\n\n'
    'print(Demo().run())                   # 12')
code('# E12 — duck-typed dispatch\n'
    'def render(items): return [it.draw() for it in items]\n'
    'class Btn:\n'
    '    def draw(self): return "[Button]"\n'
    'class Txt:\n'
    '    def draw(self): return "Text"\n\n'
    'print(render([Btn(), Txt()]))         # [\'[Button]\', \'Text\']')

md("### Code Challenges — Solutions")
code('# C1 — SavingsAccount\n'
    'class Account:\n'
    '    def __init__(self, balance=0): self.balance = balance\n'
    'class SavingsAccount(Account):\n'
    '    def __init__(self, balance=0, rate=0.05):\n'
    '        super().__init__(balance); self.rate = rate\n'
    '    def add_interest(self): self.balance += self.balance * self.rate; return self.balance\n\n'
    'print(SavingsAccount(100).add_interest())   # 105.0')
code('# C2 — Media polymorphic\n'
    'class Media:\n'
    '    def play(self): raise NotImplementedError\n'
    'class Song(Media):\n'
    '    def play(self): return "playing song"\n'
    'class Video(Media):\n'
    '    def play(self): return "playing video"\n\n'
    'print([m.play() for m in [Song(), Video()]])')
code('# C3 — OrderedByKeyMixin\n'
    'class OrderedByKeyMixin:\n'
    '    def sort_key(self): raise NotImplementedError\n'
    '    def __eq__(self, o): return self.sort_key() == o.sort_key()\n'
    '    def __lt__(self, o): return self.sort_key() < o.sort_key()\n'
    'class Product(OrderedByKeyMixin):\n'
    '    def __init__(self, name, price): self.name = name; self.price = price\n'
    '    def sort_key(self): return self.price\n\n'
    'print([p.name for p in sorted([Product("a",30), Product("b",10), Product("c",20)])])   # [\'b\', \'c\', \'a\']')
code('# C4 — Serializer ABC + implementations\n'
    'import json\n'
    'class Serializer(ABC):\n'
    '    @abstractmethod\n'
    '    def serialize(self, data): ...\n'
    'class JsonSerializer(Serializer):\n'
    '    def serialize(self, data): return json.dumps(data)\n'
    'class CsvSerializer(Serializer):\n'
    '    def serialize(self, data): return ",".join(map(str, data.values()))\n\n'
    'd = {"a": 1, "b": 2}\n'
    'print(JsonSerializer().serialize(d), "|", CsvSerializer().serialize(d))')
code('# C5 — dependency injection via composition\n'
    'class Logger:\n'
    '    def __init__(self): self.messages = []\n'
    '    def log(self, msg): self.messages.append(msg)\n'
    'class Service:\n'
    '    def __init__(self, logger): self.logger = logger\n'
    '    def run(self): self.logger.log("ran"); return "done"\n\n'
    'log = Logger(); Service(log).run()\n'
    'print(log.messages)                   # [\'ran\']')
code('# C6 — 3-level super() chain\n'
    'class A:\n'
    '    def setup(self): return ["A"]\n'
    'class B(A):\n'
    '    def setup(self): return super().setup() + ["B"]\n'
    'class C(B):\n'
    '    def setup(self): return super().setup() + ["C"]\n\n'
    'print(C().setup())                    # [\'A\', \'B\', \'C\']')
code('# C7 — SupportsLen Protocol over unrelated types\n'
    '@runtime_checkable\n'
    'class SupportsLen(Protocol):\n'
    '    def __len__(self) -> int: ...\n'
    'def describe_size(x): return len(x) if isinstance(x, SupportsLen) else None\n'
    'class Box:\n'
    '    def __init__(self, n): self.n = n\n'
    '    def __len__(self): return self.n\n\n'
    'print(describe_size([1,2,3]), describe_size("hi"), describe_size(Box(5)), describe_size(42))   # 3 2 5 None')
code('# C8 — auto-registering plugins via __init_subclass__\n'
    'class Plugin:\n'
    '    registry = {}\n'
    '    def __init_subclass__(cls, **kwargs):\n'
    '        super().__init_subclass__(**kwargs)\n'
    '        Plugin.registry[cls.__name__] = cls\n\n'
    'class Foo(Plugin): pass\n'
    'class Bar(Plugin): pass\n'
    'print(list(Plugin.registry))          # [\'Foo\', \'Bar\']')

nb = new_notebook(cells=cells)
nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
nb.metadata["language_info"] = {"name": "python"}
nbf.write(nb, "solutions.ipynb")
print("wrote solutions.ipynb with", len(cells), "cells")
