# Builder for Session 7C, 01_inheritance.ipynb (hands-on practice scaffold).
import nbformat as nbf
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell

cells = []
def md(t):   cells.append(new_markdown_cell(t))
def code(t): cells.append(new_code_cell(t))

md('<div style="background:#1e1e2e; padding:16px 20px; border-radius:8px; font-family:monospace; '
   'color:#cdd6f4; line-height:1.8">'
   '<p style="margin:0 0 8px 0; color:#cba6f7; font-weight:bold; font-size:1.05em;">📎 Session 7C — Inheritance &amp; MRO · Hands-on</p>'
   '<p style="margin:0;">Attempt space for the 12 <strong>Exercises</strong> and 8 <strong>Code Challenges</strong>. '
   'Hints in <code>theory.ipynb</code>; worked solutions in <code>solutions.ipynb</code> — try each yourself first.</p></div>')

md("### Exercises (Part 2 · §6) — 12 problems")
EX = [
 ('E1 (Easy)', 'Vehicle(wheels) base + describe(); Car/Motorcycle set wheels', 'subclass __init__ calls super().__init__(4)/(2)'),
 ('E2 (Easy)', 'Shape base (area raises); Circle/Square override; polymorphic sum', 'sum(s.area() for s in shapes)'),
 ('E3 (Easy)', 'Student(Person) adds school via super().__init__', 'super().__init__(name); self.school = school'),
 ('E4 (Med)',  'PoliteGreeter extends Greeter.greet() with super()', 'return super().greet() + ", please"'),
 ('E5 (Med)',  'DictReprMixin: __repr__ from self.__dict__, mixed into a class', 'f"{type(self).__name__}({self.__dict__})"'),
 ('E6 (Med)',  'Storage ABC (abstract save/load) + DictStorage', 'abc.ABC + @abstractmethod; Storage() should raise'),
 ('E7 (Med)',  'Wallet via composition: holds amounts, deposit/total', 'self.amounts=[] in __init__; delegate to the list'),
 ('E8 (Med)',  'Hierarchy checks: issubclass/isinstance on a 3-level chain', 'A<-B<-C; isinstance(C(),A) True, isinstance(A(),C) False'),
 ('E9 (Hard)', 'Diamond MRO: cooperative super() -> return the call order', 'each m prepends its name + super().m(); check D.__mro__'),
 ('E10 (Hard)','HasArea Protocol: isinstance works on any class with area()', '@runtime_checkable class HasArea(Protocol): def area(self)->float: ...'),
 ('E11 (Hard)','Template-method Pipeline ABC: run() = extract->transform->load', 'concrete run calls 3 abstract methods; subclass fills them'),
 ('E12 (Hard)','Duck-typed dispatch: render(items) calls .draw() on each', 'works for any object with draw(), no shared base'),
]
for tag, prob, hint in EX:
    code(f"# {tag} — {prob}\n# Hint: {hint}\n\n")

md("### Code Challenges (Part 3 · §8b) — 8 problems")
CC = [
 ('C1 (Easy)', 'SavingsAccount(Account): add_interest() via super().__init__'),
 ('C2 (Easy)', 'Media base + Song/Video override play(); polymorphic loop'),
 ('C3 (Med)',  'OrderedByKeyMixin: __eq__/__lt__ from a subclass sort_key()'),
 ('C4 (Med)',  'Serializer ABC + JsonSerializer/CsvSerializer'),
 ('C5 (Med)',  'Dependency injection via composition: Service(logger)'),
 ('C6 (Med)',  '3-level super() chain: A -> B -> C setup()'),
 ('C7 (Hard)', 'SupportsLen Protocol: works on list, str, and a custom class'),
 ('C8 (Hard)', 'Auto-registering plugins via __init_subclass__'),
]
for tag, prob in CC:
    code(f"# {tag} — {prob}\n\n")

nb = new_notebook(cells=cells)
nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
nb.metadata["language_info"] = {"name": "python"}
nbf.write(nb, "01_inheritance.ipynb")
print("wrote 01_inheritance.ipynb with", len(cells), "cells")
