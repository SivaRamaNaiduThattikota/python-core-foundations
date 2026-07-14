# Builder for Session 5, 01_functions.ipynb (hands-on practice scaffold).
import nbformat as nbf
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell

cells = []
def md(t):   cells.append(new_markdown_cell(t))
def code(t): cells.append(new_code_cell(t))

md('<div style="background:#1e1e2e; padding:16px 20px; border-radius:8px; font-family:monospace; '
   'color:#cdd6f4; line-height:1.8">'
   '<p style="margin:0 0 8px 0; color:#cba6f7; font-weight:bold; font-size:1.05em;">📎 Session 5 — Functions, Scope &amp; Closures · Hands-on</p>'
   '<p style="margin:0;">Attempt space for the 12 <strong>Exercises</strong> and 8 <strong>Code Challenges</strong>. '
   'Hints in <code>theory.ipynb</code>; worked solutions in <code>solutions.ipynb</code> — try each yourself first.</p></div>')

md("### Exercises (Part 2 · §6) — 12 problems (leaning hard)")
EX = [
 ('E1 (Easy)', 'build_url(base, **params) -> "base?k=v&k2=v2"', '"&".join(f"{k}={v}" for k,v in params.items())'),
 ('E2 (Easy)', 'Fix BOTH bugs in def add(item, acc=[])', 'acc=None; if acc is None (NOT acc or []); prove passed empty list is filled'),
 ('E3 (Med)',  'make_counter(start=0, step=1) closure', 'nonlocal n; first call returns start, then += step'),
 ('E4 (Med)',  'apply_n(f, x, n) -> apply f n times', 'loop n times, x = f(x)'),
 ('E5 (Med)',  'calc(a, b, /, *, op) keyword-only callable op', 'return op(a, b); test op=max'),
 ('E6 (Med)',  'trace(fn) -> wrapper factory (decorator shape)', 'return inner wrapper(*args,**kwargs) that prints then forwards'),
 ('E7 (Med)',  'running_stats() -> each call returns (count, mean)', 'closure over total & n; nonlocal both'),
 ('E8 (Hard)', 'memoize(fn) -> cache keyed by *args', 'cache dict; key = args tuple; recompute on miss'),
 ('E9 (Hard)', 'compose(*funcs) -> apply left-to-right', 'inner threads x through each func'),
 ('E10 (Hard)','partial(fn, *fixed) -> pre-fill leading args', 'inner(*rest): return fn(*fixed, *rest)'),
 ('E11 (Hard)','[f0,f1,f2] where fi() returns i; explain the naive failure', 'lambda i=i: i  (beats late binding)'),
 ('E12 (Hard)','once(fn) -> run first time only, cache result forever', 'nonlocal done, result flag'),
]
for tag, prob, hint in EX:
    code(f"# {tag} — {prob}\n# Hint: {hint}\n\n")

md("### Code Challenges (Part 3 · §8b) — 8 problems")
CC = [
 ('C1 (Easy)', 'flip(fn) -> call fn with its two args swapped: flip(pow)(2,3)==9'),
 ('C2 (Easy)', 'negate(pred) -> logical NOT of a predicate'),
 ('C3 (Med)',  'count_calls(fn) -> wrapper tracking .calls'),
 ('C4 (Med)',  'group_by(items, key_fn) -> dict of lists'),
 ('C5 (Med)',  'with_retry(fn, times) -> retry on exception, else re-raise last'),
 ('C6 (Med)',  'pipe(x, *funcs) -> thread value through funcs left-to-right'),
 ('C7 (Hard)', 'curry3(fn) -> f(a)(b)(c)'),
 ('C8 (Hard)', 'make_stack() -> return (push, pop) sharing one hidden list'),
]
for tag, prob in CC:
    code(f"# {tag} — {prob}\n\n")

nb = new_notebook(cells=cells)
nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
nb.metadata["language_info"] = {"name": "python"}
nbf.write(nb, "01_functions.ipynb")
print("wrote 01_functions.ipynb with", len(cells), "cells")
