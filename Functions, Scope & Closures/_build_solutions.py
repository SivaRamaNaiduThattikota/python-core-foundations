# Builder for Session 5, solutions.ipynb (answer key).
# Runnable, verified solutions for all 12 Exercises and 8 Code Challenges.
import nbformat as nbf
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell

cells = []
def md(t):   cells.append(new_markdown_cell(t))
def code(t): cells.append(new_code_cell(t))

md('<div style="background:#1e1e2e; padding:16px 20px; border-radius:8px; font-family:monospace; '
   'color:#cdd6f4; line-height:1.8">'
   '<p style="margin:0 0 8px 0; color:#cba6f7; font-weight:bold; font-size:1.05em;">✅ Session 5 — Functions, Scope &amp; Closures · Solutions</p>'
   '<p style="margin:0;">Worked, runnable solutions for the 12 <strong>Exercises</strong> and 8 '
   '<strong>Code Challenges</strong>. Run top to bottom to verify. Try them in '
   '<code>01_functions.ipynb</code> first.</p></div>')

md("### Exercises — Solutions")

code('# E1 (Easy) — build_url(base, **params)\n'
    'def build_url(base, **params):\n'
    '    return base + "?" + "&".join(f"{k}={v}" for k, v in params.items())\n\n'
    'print(build_url("api", page=1, size=10))   # api?page=1&size=10')
code('# E2 (Easy) — fix BOTH bugs: mutable default AND the `or []` false-empty pitfall\n'
    'def add(item, acc=None):\n'
    '    if acc is None:          # NOT `acc or []` (would discard a passed empty list)\n'
    '        acc = []\n'
    '    acc.append(item)\n'
    '    return acc\n\n'
    'print(add(1), add(2))                  # [1] [2] - no accumulation\n'
    'passed = []\n'
    'print(add(9, passed) is passed, passed)  # True [9] - passed empty list IS filled')
code('# E3 (Medium) — make_counter(start=0, step=1)\n'
    'def make_counter(start=0, step=1):\n'
    '    n = start - step\n'
    '    def inc():\n'
    '        nonlocal n\n'
    '        n += step\n'
    '        return n\n'
    '    return inc\n\n'
    'c = make_counter(10, 5)\n'
    'print(c(), c(), c())                   # 10 15 20')
code('# E4 (Medium) — apply_n(f, x, n)\n'
    'def apply_n(f, x, n):\n'
    '    for _ in range(n):\n'
    '        x = f(x)\n'
    '    return x\n\n'
    'print(apply_n(lambda v: v*2, 1, 3))    # 8')
code('# E5 (Medium) — calc(a, b, /, *, op)\n'
    'def calc(a, b, /, *, op):\n'
    '    return op(a, b)\n\n'
    'print(calc(3, 4, op=max))              # 4')
code('# E6 (Medium) — trace(fn): wrapper factory (decorator shape)\n'
    'def trace(fn):\n'
    '    def wrapper(*args, **kwargs):\n'
    '        print(f"call {fn.__name__}{args}")\n'
    '        return fn(*args, **kwargs)\n'
    '    return wrapper\n\n'
    'add = lambda a, b: a + b\n'
    'print(trace(add)(2, 3))                # prints "call <lambda>(2, 3)", returns 5')
code('# E7 (Medium) — running_stats() -> (count, mean)\n'
    'def running_stats():\n'
    '    total = n = 0\n'
    '    def add(x):\n'
    '        nonlocal total, n\n'
    '        total += x; n += 1\n'
    '        return (n, total / n)\n'
    '    return add\n\n'
    's = running_stats()\n'
    'print(s(10), s(20))                    # (1, 10.0) (2, 15.0)')
code('# E8 (Hard) — memoize(fn) keyed by *args\n'
    'def memoize(fn):\n'
    '    cache = {}\n'
    '    def wrapper(*args):\n'
    '        if args not in cache:          # args tuple is hashable (2B)\n'
    '            cache[args] = fn(*args)\n'
    '        return cache[args]\n'
    '    return wrapper\n\n'
    'm = memoize(lambda a, b: a + b)\n'
    'print(m(1, 2), m(1, 2))                # 3 3 (2nd from cache)')
code('# E9 (Hard) — compose(*funcs) left-to-right\n'
    'def compose(*funcs):\n'
    '    def inner(x):\n'
    '        for f in funcs:\n'
    '            x = f(x)\n'
    '        return x\n'
    '    return inner\n\n'
    'print(compose(lambda x: x+1, lambda x: x*2)(3))   # 8')
code('# E10 (Hard) — partial(fn, *fixed)\n'
    'def partial(fn, *fixed):\n'
    '    def inner(*rest):\n'
    '        return fn(*fixed, *rest)\n'
    '    return inner\n\n'
    'add3 = lambda a, b, c: a + b + c\n'
    'print(partial(add3, 1)(2, 3), partial(add3, 1, 2)(3))   # 6 6')
code('# E11 (Hard) — beat late binding, and explain why\n'
    '# Naive: [lambda: i for i in range(3)] -> all return 2 (they share one i, read at call time).\n'
    'funcs = [lambda i=i: i for i in range(3)]   # default arg captures the value NOW\n'
    'print([f() for f in funcs])            # [0, 1, 2]')
code('# E12 (Hard) — once(fn): run first time only, cache result forever\n'
    'def once(fn):\n'
    '    done = False\n'
    '    result = None\n'
    '    def wrapper(*args, **kwargs):\n'
    '        nonlocal done, result\n'
    '        if not done:\n'
    '            result = fn(*args, **kwargs)\n'
    '            done = True\n'
    '        return result\n'
    '    return wrapper\n\n'
    'calls = []\n'
    'def work(x):\n'
    '    calls.append(x)\n'
    '    return x * 10\n'
    'w = once(work)\n'
    'print(w(5), w(6), calls)               # 50 50 [5] - work ran exactly once')

md("### Code Challenges — Solutions")

code('# C1 (Easy) — flip(fn)\n'
    'def flip(fn):\n'
    '    return lambda a, b: fn(b, a)\n\n'
    'print(flip(pow)(2, 3))                 # 9')
code('# C2 (Easy) — negate(pred)\n'
    'def negate(pred):\n'
    '    return lambda *a, **k: not pred(*a, **k)\n\n'
    'print(negate(str.isdigit)("a"), negate(str.isdigit)("5"))   # True False')
code('# C3 (Medium) — count_calls(fn)\n'
    'def count_calls(fn):\n'
    '    def wrapper(*a, **k):\n'
    '        wrapper.calls += 1\n'
    '        return fn(*a, **k)\n'
    '    wrapper.calls = 0\n'
    '    return wrapper\n\n'
    'w = count_calls(len); w("ab"); w("cde")\n'
    'print(w.calls)                         # 2')
code('# C4 (Medium) — group_by(items, key_fn)\n'
    'from collections import defaultdict\n'
    'def group_by(items, key_fn):\n'
    '    g = defaultdict(list)\n'
    '    for it in items:\n'
    '        g[key_fn(it)].append(it)\n'
    '    return dict(g)\n\n'
    'print(group_by([1, 2, 3, 4, 5], lambda x: x % 2))   # {1:[1,3,5], 0:[2,4]}')
code('# C5 (Medium) — with_retry(fn, times)\n'
    'def with_retry(fn, times):\n'
    '    def wrapper(*a, **k):\n'
    '        last = None\n'
    '        for _ in range(times):\n'
    '            try:\n'
    '                return fn(*a, **k)\n'
    '            except Exception as e:\n'
    '                last = e\n'
    '        raise last\n'
    '    return wrapper\n\n'
    'state = {"n": 0}\n'
    'def flaky():\n'
    '    state["n"] += 1\n'
    '    if state["n"] < 3:\n'
    '        raise ValueError("boom")\n'
    '    return "ok"\n'
    'print(with_retry(flaky, 5)(), "after", state["n"], "tries")   # ok after 3 tries')
code('# C6 (Medium) — pipe(x, *funcs)\n'
    'def pipe(x, *funcs):\n'
    '    for f in funcs:\n'
    '        x = f(x)\n'
    '    return x\n\n'
    'print(pipe(3, lambda x: x+1, lambda x: x*2))   # 8')
code('# C7 (Hard) — curry3(fn)\n'
    'def curry3(fn):\n'
    '    return lambda a: lambda b: lambda c: fn(a, b, c)\n\n'
    'print(curry3(lambda a, b, c: a + b + c)(1)(2)(3))   # 6')
code('# C8 (Hard) — make_stack() -> (push, pop) sharing one hidden list\n'
    'def make_stack():\n'
    '    items = []\n'
    '    def push(x):\n'
    '        items.append(x)\n'
    '    def pop():\n'
    '        return items.pop()\n'
    '    return push, pop\n\n'
    'push, pop = make_stack()\n'
    'push(1); push(2)\n'
    'print(pop(), pop())                    # 2 1')

nb = new_notebook(cells=cells)
nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
nb.metadata["language_info"] = {"name": "python"}
nbf.write(nb, "solutions.ipynb")
print("wrote solutions.ipynb with", len(cells), "cells")
