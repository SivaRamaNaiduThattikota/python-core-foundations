# Builder for Session 8, solutions.ipynb (answer key).
# Runnable, verified solutions for all 12 Exercises and 8 Code Challenges.
import nbformat as nbf
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell

cells = []
def md(t):   cells.append(new_markdown_cell(t))
def code(t): cells.append(new_code_cell(t))

md('<div style="background:#1e1e2e; padding:16px 20px; border-radius:8px; font-family:monospace; '
   'color:#cdd6f4; line-height:1.8">'
   '<p style="margin:0 0 8px 0; color:#cba6f7; font-weight:bold; font-size:1.05em;">✅ Session 8 — Iterators &amp; Context Managers · Solutions</p>'
   '<p style="margin:0;">Worked, runnable solutions for the 12 <strong>Exercises</strong> and 8 '
   '<strong>Code Challenges</strong>. Run top to bottom to verify. Try them in '
   '<code>01_iterators.ipynb</code> first.</p></div>')

md("### Exercises — Solutions")
code('import itertools, time, io\n'
    'from contextlib import contextmanager, redirect_stdout, ExitStack\n'
    'from collections import deque')
code('# E1 — iter()/next()\n'
    'it = iter([10, 20, 30])\n'
    'print(next(it), next(it))            # 10 20')
code('# E2 — evens(n)\n'
    'def evens(n):\n'
    '    for i in range(n):\n'
    '        yield i * 2\n\n'
    'print(list(evens(4)))                # [0, 2, 4, 6]')
code('# E3 — Repeat (re-iterable via __iter__ generator method)\n'
    'class Repeat:\n'
    '    def __init__(self, v, t): self.v = v; self.t = t\n'
    '    def __iter__(self):\n'
    '        for _ in range(self.t):\n'
    '            yield self.v\n\n'
    'r = Repeat("x", 3)\n'
    'print(list(r), list(r))              # [\'x\',\'x\',\'x\'] both times')
code('# E4 — CountUp custom iterator class\n'
    'class CountUp:\n'
    '    def __init__(self, start, stop): self.cur = start; self.stop = stop\n'
    '    def __iter__(self): return self\n'
    '    def __next__(self):\n'
    '        if self.cur >= self.stop: raise StopIteration\n'
    '        v = self.cur; self.cur += 1; return v\n\n'
    'print(list(CountUp(2, 5)))           # [2, 3, 4]')
code('# E5 — infinite generator + islice\n'
    'def naturals():\n'
    '    n = 0\n'
    '    while True:\n'
    '        yield n; n += 1\n\n'
    'print(list(itertools.islice(naturals(), 5)))   # [0, 1, 2, 3, 4]')
code('# E6 — first matching (or default)\n'
    'def first(iterable, pred, default=None):\n'
    '    return next((x for x in iterable if pred(x)), default)\n\n'
    'print(first([1,3,4,6], lambda x: x%2==0), first([1,3], lambda x: x%2==0, -1))   # 4 -1')
code('# E7 — batched(iterable, n)\n'
    'def batched(iterable, n):\n'
    '    batch = []\n'
    '    for x in iterable:\n'
    '        batch.append(x)\n'
    '        if len(batch) == n:\n'
    '            yield batch; batch = []\n'
    '    if batch:\n'
    '        yield batch\n\n'
    'print(list(batched(range(7), 3)))    # [[0,1,2],[3,4,5],[6]]')
code('# E8 — Tag context manager\n'
    'class Tag:\n'
    '    def __init__(self, name): self.name = name\n'
    '    def __enter__(self): print(f"<{self.name}>"); return self\n'
    '    def __exit__(self, *a): print(f"</{self.name}>")\n\n'
    'with Tag("b"):\n'
    '    print("hi")                      # <b> / hi / </b>')
code('# E9 — @contextmanager timer capturing elapsed\n'
    '@contextmanager\n'
    'def timer(out):\n'
    '    t0 = time.perf_counter()\n'
    '    try:\n'
    '        yield\n'
    '    finally:\n'
    '        out.append(time.perf_counter() - t0)\n\n'
    'holder = []\n'
    'with timer(holder):\n'
    '    sum(range(1000))\n'
    'print("captured:", len(holder) == 1)   # True')
code('# E10 — @contextmanager setattr_temp (set & restore)\n'
    '@contextmanager\n'
    'def setattr_temp(obj, attr, value):\n'
    '    old = getattr(obj, attr)\n'
    '    setattr(obj, attr, value)\n'
    '    try:\n'
    '        yield obj\n'
    '    finally:\n'
    '        setattr(obj, attr, old)\n\n'
    'class C: pass\n'
    'c = C(); c.x = 1\n'
    'with setattr_temp(c, "x", 99):\n'
    '    print("inside:", c.x)            # 99\n'
    'print("restored:", c.x)              # 1')
code('# E11 — reimplement suppress(*excs)\n'
    'class suppress_exc:\n'
    '    def __init__(self, *excs): self.excs = excs\n'
    '    def __enter__(self): return self\n'
    '    def __exit__(self, et, ev, tb):\n'
    '        return et is not None and issubclass(et, self.excs)\n\n'
    'with suppress_exc(ValueError):\n'
    '    raise ValueError("x")\n'
    'print("suppressed, continued")')
code('# E12 — pairwise(iterable)\n'
    'def pairwise(iterable):\n'
    '    it = iter(iterable)\n'
    '    prev = next(it, None)\n'
    '    if prev is None:\n'
    '        return\n'
    '    for cur in it:\n'
    '        yield (prev, cur); prev = cur\n\n'
    'print(list(pairwise([1, 2, 3, 4])))  # [(1,2),(2,3),(3,4)]')

md("### Code Challenges — Solutions")
code('# C1 — take(iterable, n)\n'
    'def take(it, n): return list(itertools.islice(it, n))\n'
    'print(take(range(100), 3))           # [0, 1, 2]')
code('# C2 — ilen(iterable)\n'
    'def ilen(it): return sum(1 for _ in it)\n'
    'print(ilen(iter([1, 2, 3, 4])))      # 4')
code('# C3 — unique(iterable), order-preserving\n'
    'def unique(it):\n'
    '    seen = set()\n'
    '    for x in it:\n'
    '        if x not in seen:\n'
    '            seen.add(x); yield x\n\n'
    'print(list(unique([1, 2, 1, 3, 2, 4])))   # [1, 2, 3, 4]')
code('# C4 — sliding_window(iterable, k)\n'
    'def sliding_window(it, k):\n'
    '    it = iter(it)\n'
    '    win = deque(itertools.islice(it, k), maxlen=k)\n'
    '    if len(win) == k:\n'
    '        yield tuple(win)\n'
    '    for x in it:\n'
    '        win.append(x); yield tuple(win)\n\n'
    'print(list(sliding_window([1, 2, 3, 4], 2)))   # [(1,2),(2,3),(3,4)]')
code('# C5 — reimplement enumerate\n'
    'def enumerate_from(it, start=0):\n'
    '    i = start\n'
    '    for x in it:\n'
    '        yield (i, x); i += 1\n\n'
    'print(list(enumerate_from(["a", "b"], 1)))   # [(1,\'a\'), (2,\'b\')]')
code('# C6 — @contextmanager capture_stdout\n'
    '@contextmanager\n'
    'def capture_stdout():\n'
    '    buf = io.StringIO()\n'
    '    with redirect_stdout(buf):\n'
    '        yield buf\n\n'
    'with capture_stdout() as buf:\n'
    '    print("hello")\n'
    'print(repr(buf.getvalue()))          # \'hello\\n\'')
code('# C7 — both an iterator AND a context manager (like a file object)\n'
    'class LineSource:\n'
    '    def __init__(self, lines): self.lines = lines; self.closed = False\n'
    '    def __enter__(self): return self\n'
    '    def __exit__(self, *a): self.closed = True\n'
    '    def __iter__(self): return iter(self.lines)\n\n'
    'with LineSource(["a", "b", "c"]) as src:\n'
    '    got = list(src)\n'
    'print(got, "| closed:", src.closed)  # [\'a\',\'b\',\'c\'] | closed: True')
code('# C8 — dynamic context managers with ExitStack\n'
    'log = []\n'
    '@contextmanager\n'
    'def res(name):\n'
    '    log.append(f"open {name}")\n'
    '    try:\n'
    '        yield name\n'
    '    finally:\n'
    '        log.append(f"close {name}")\n\n'
    'with ExitStack() as stack:\n'
    '    for n in ["a", "b", "c"]:\n'
    '        stack.enter_context(res(n))\n'
    'print(log)   # open a,b,c then close c,b,a (reverse order)')

nb = new_notebook(cells=cells)
nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
nb.metadata["language_info"] = {"name": "python"}
nbf.write(nb, "solutions.ipynb")
print("wrote solutions.ipynb with", len(cells), "cells")
