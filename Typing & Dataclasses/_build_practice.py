# Builder for Session 10, 01_typing.ipynb (hands-on practice scaffold).
import nbformat as nbf
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell

cells = []
def md(t):   cells.append(new_markdown_cell(t))
def code(t): cells.append(new_code_cell(t))

md('<div style="background:#1e1e2e; padding:16px 20px; border-radius:8px; font-family:monospace; '
   'color:#cdd6f4; line-height:1.8">'
   '<p style="margin:0 0 8px 0; color:#cba6f7; font-weight:bold; font-size:1.05em;">📎 Session 10 — Typing &amp; Dataclasses · Hands-on</p>'
   '<p style="margin:0;">Attempt space for the 12 <strong>Exercises</strong> and 8 <strong>Code Challenges</strong>. '
   'Hints in <code>theory.ipynb</code>; worked solutions in <code>solutions.ipynb</code> — try each yourself first.</p></div>')

md("### Exercises (Part 2 · §6) — 12 problems")
EX = [
 ('E1 (Easy)', 'Annotate greet(name) -> str', 'params after `:`, return after `->`'),
 ('E2 (Easy)', 'Annotate mean(xs) -> float on a list', 'xs: list[float]'),
 ('E3 (Easy)', 'first_positive(xs) -> int | None', 'return None if none found'),
 ('E4 (Med)',  'to_int(x: int | str) -> int', 'int(x) handles both'),
 ('E5 (Med)',  'repeat_apply(f, x, n): apply f n times, typed', 'f: Callable[[int], int]'),
 ('E6 (Med)',  'Generic last(xs: list[T]) -> T', 'T = TypeVar("T")'),
 ('E7 (Med)',  'Book dataclass (title, author, year); check repr/eq', '@dataclass; compare two equal Books'),
 ('E8 (Med)',  'Cart with items list via default_factory', 'field(default_factory=list); two carts independent'),
 ('E9 (Hard)', 'Frozen GridCell(x, y) counted with Counter', '@dataclass(frozen=True); Counter(cells)'),
 ('E10 (Hard)','order=True Student(gpa, name); rank with sorted', 'sorted(..., reverse=True); mind field order'),
 ('E11 (Hard)','TypedDict Payload(user_id, active) + reader fn', 'class Payload(TypedDict): ...'),
 ('E12 (Hard)','Protocol HasName; describe(obj: HasName)', 'class HasName(Protocol): name: str'),
]
for tag, prob, hint in EX:
    code(f"# {tag} — {prob}\n# Hint: {hint}\n\n")

md("### Code Challenges (Part 3 · §8b) — 8 problems")
CC = [
 ('C1 (Easy)', 'Money(amount, currency) frozen; de-dup in a set'),
 ('C2 (Easy)', 'Alias JSONNum = list[float]; normalize(v) -> JSONNum'),
 ('C3 (Med)',  'Task(priority, label) order=True with label compare=False'),
 ('C4 (Med)',  'Percentage(value): __post_init__ enforces 0..100'),
 ('C5 (Med)',  'Generic Stack[T] with push/pop typed'),
 ('C6 (Med)',  'SupportsPredict Protocol; score(models, x)'),
 ('C7 (Hard)', 'Frozen HyperParams; with_lr(cfg, lr) via replace'),
 ('C8 (Hard)', 'validate(d, schema) checks TypedDict keys + isinstance types'),
]
for tag, prob in CC:
    code(f"# {tag} — {prob}\n\n")

nb = new_notebook(cells=cells)
nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
nb.metadata["language_info"] = {"name": "python"}
nbf.write(nb, "01_typing.ipynb")
print("wrote 01_typing.ipynb with", len(cells), "cells")
