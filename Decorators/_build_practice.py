# Builder for Session 6, 01_decorators.ipynb (hands-on practice scaffold).
import nbformat as nbf
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell

cells = []
def md(t):   cells.append(new_markdown_cell(t))
def code(t): cells.append(new_code_cell(t))

md('<div style="background:#1e1e2e; padding:16px 20px; border-radius:8px; font-family:monospace; '
   'color:#cdd6f4; line-height:1.8">'
   '<p style="margin:0 0 8px 0; color:#cba6f7; font-weight:bold; font-size:1.05em;">📎 Session 6 — Decorators · Hands-on</p>'
   '<p style="margin:0;">Attempt space for the 12 <strong>Exercises</strong> and 8 <strong>Code Challenges</strong>. '
   'Hints in <code>theory.ipynb</code>; worked solutions in <code>solutions.ipynb</code> — try each yourself first.</p></div>')

md("### Exercises (Part 2 · §6) — 12 problems")
EX = [
 ('E1 (Easy)', 'logged: print "calling <name>" then return the result', 'wrapper prints fn.__name__, return fn(*a,**k); @wraps'),
 ('E2 (Easy)', 'Add @functools.wraps so __name__/__doc__ survive', '@functools.wraps(fn) on the wrapper'),
 ('E3 (Easy)', 'debug: print the call args and the result', 'print fn.__name__ + args, compute, print, return'),
 ('E4 (Med)',  'timer: print elapsed ms around the call', 'time.perf_counter() before/after; return result (timing varies)'),
 ('E5 (Med)',  'collect(n): call n times, return the LIST of all results', '3-layer factory; [fn(*a,**k) for _ in range(n)]'),
 ('E6 (Med)',  'default_on_error(default): return default if fn raises', 'parameterized; try/except Exception -> return default'),
 ('E7 (Med)',  'memoize: cache by args (@wraps); then compare functools.lru_cache', 'closure cache dict; key = args tuple'),
 ('E8 (Med)',  'require_nonneg: raise ValueError if any numeric arg < 0', 'scan args; raise on negative, else forward'),
 ('E9 (Hard)', 'count_calls: expose the count as fn.calls', 'hang wrapper.calls attribute; increment each call'),
 ('E10 (Hard)','Memoize: CLASS-based caching decorator with inspectable .cache', '__init__(fn)+cache dict; __call__ caches by args; update_wrapper'),
 ('E11 (Hard)','tag(*labels): attach fn.tags = labels, return fn unchanged', 'factory over *labels; set attribute, return fn (no wrapper)'),
 ('E12 (Hard)','validate_types: enforce parameter annotations at call time', 'inspect.signature(fn).bind(...); fn.__annotations__; raise TypeError'),
]
for tag, prob, hint in EX:
    code(f"# {tag} — {prob}\n# Hint: {hint}\n\n")

md("### Code Challenges (Part 3 · §8b) — 8 problems")
CC = [
 ('C1 (Easy)', 'uppercase(fn): uppercase a string result'),
 ('C2 (Easy)', 'add_prefix(prefix): parameterized; prefix a string result'),
 ('C3 (Med)',  'call_limit(n): allow n calls, then raise RuntimeError'),
 ('C4 (Med)',  'audit(fn): record each (args, result) into fn.log'),
 ('C5 (Med)',  'enforce_return_type(t): raise TypeError if result is not type t'),
 ('C6 (Med)',  'ignore_exceptions(*excs): swallow the given types, return None'),
 ('C7 (Hard)', 'memoize_full(fn): cache keyed by args AND kwargs'),
 ('C8 (Hard)', 'smart(fn=None, *, prefix=">>"): works as @smart AND @smart(prefix=...)'),
]
for tag, prob in CC:
    code(f"# {tag} — {prob}\n\n")

nb = new_notebook(cells=cells)
nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
nb.metadata["language_info"] = {"name": "python"}
nbf.write(nb, "01_decorators.ipynb")
print("wrote 01_decorators.ipynb with", len(cells), "cells")
