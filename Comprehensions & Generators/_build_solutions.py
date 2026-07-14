# Builder for Session 4, solutions.ipynb (answer key).
# Runnable, verified solutions for all 12 Exercises and 8 Code Challenges.
import nbformat as nbf
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell

cells = []
def md(t):   cells.append(new_markdown_cell(t))
def code(t): cells.append(new_code_cell(t))

md('<div style="background:#1e1e2e; padding:16px 20px; border-radius:8px; font-family:monospace; '
   'color:#cdd6f4; line-height:1.8">'
   '<p style="margin:0 0 8px 0; color:#cba6f7; font-weight:bold; font-size:1.05em;">✅ Session 4 — Comprehensions &amp; Generators · Solutions</p>'
   '<p style="margin:0;">Worked, runnable solutions for the 12 <strong>Exercises</strong> and 8 '
   '<strong>Code Challenges</strong>. Run top to bottom to verify. Try them in '
   '<code>01_comprehensions.ipynb</code> first.</p></div>')

md("### Exercises — Solutions")

code('# E1 (Easy) — Squares of even numbers 0-20\n'
    'print([x*x for x in range(21) if x % 2 == 0])')
code('# E2 (Easy) — Dict comp n -> n**2 for 1..5\n'
    'print({n: n**2 for n in range(1, 6)})')
code('# E3 (Easy) — Set of unique word lengths\n'
    'words = ["a", "bb", "cc", "ddd"]\n'
    'print({len(w) for w in words})')
code('# E4 (Easy) — Flatten a 2D list (outer for first)\n'
    'm = [[1, 2], [3, 4], [5]]\n'
    'print([x for row in m for x in row])')
code('# E5 (Medium) — Filter dict comp: keep scores >= 50\n'
    'pairs = [("Alice", 88), ("Bob", 40), ("Cara", 50)]\n'
    'print({name: s for name, s in pairs if s >= 50})')
code('# E6 (Medium) — Invert a dict (unique values)\n'
    'd = {"a": 1, "b": 2}\n'
    'print({v: k for k, v in d.items()})   # lossy if values repeat')
code('# E7 (Medium) — Transpose a matrix (nested comprehension)\n'
    'm = [[1, 2, 3], [4, 5, 6]]\n'
    'cols = len(m[0])\n'
    'print([[row[i] for row in m] for i in range(cols)])')
code('# E8 (Medium) — Sum of squares of odd numbers 1-100 (genexpr, no list built)\n'
    'print(sum(x*x for x in range(1, 101) if x % 2))')
code('# E9 (Medium) — Any word longer than 10 chars? (short-circuits)\n'
    'words = ["short", "a_very_long_word", "ok"]\n'
    'print(any(len(w) > 10 for w in words))')
code('# E10 (Hard) — Fibonacci generator\n'
    'from itertools import islice\n'
    'def fib():\n'
    '    a, b = 0, 1\n'
    '    while True:\n'
    '        yield a\n'
    '        a, b = b, a + b\n\n'
    'print(list(islice(fib(), 10)))')
code('# E11 (Hard) — Streaming pipeline: total length of non-empty lines\n'
    'lines = ["  hi ", "", "  bye"]\n'
    'print(sum(len(ln.strip()) for ln in lines if ln.strip()))')
code('# E12 (Hard) — Recursively flatten arbitrary nesting (generator)\n'
    'def flatten(nested):\n'
    '    for x in nested:\n'
    '        if isinstance(x, list):\n'
    '            yield from flatten(x)\n'
    '        else:\n'
    '            yield x\n\n'
    'print(list(flatten([1, [2, [3, [4, 5]]], 6])))')

md("### Code Challenges — Solutions")

code('# C1 (Easy) — List of the first n squares\n'
    'def squares(n):\n'
    '    return [x*x for x in range(n)]\n\n'
    'print(squares(5))')
code('# C2 (Easy) — Sum of even numbers (genexpr)\n'
    'def sum_evens(nums):\n'
    '    return sum(x for x in nums if x % 2 == 0)\n\n'
    'print(sum_evens([1, 2, 3, 4, 5, 6]))')
code('# C3 (Medium) — Invert a dict\n'
    'def invert(d):\n'
    '    return {v: k for k, v in d.items()}\n\n'
    'print(invert({"a": 1, "b": 2, "c": 3}))')
code('# C4 (Medium) — Batch a sequence into chunks of size n (ML batching / DataLoader)\n'
    'def chunk(seq, n):\n'
    '    for i in range(0, len(seq), n):\n'
    '        yield seq[i:i+n]\n\n'
    'print(list(chunk([1, 2, 3, 4, 5, 6, 7], 3)))   # [[1,2,3],[4,5,6],[7]]')
code('# C5 (Medium) — Fibonacci generator\n'
    'from itertools import islice\n'
    'def fib():\n'
    '    a, b = 0, 1\n'
    '    while True:\n'
    '        yield a\n'
    '        a, b = b, a + b\n\n'
    'print(list(islice(fib(), 8)))')
code('# C6 (Medium) — Cumulative sum generator (itertools.accumulate)\n'
    'def cumsum(nums):\n'
    '    total = 0\n'
    '    for n in nums:\n'
    '        total += n\n'
    '        yield total\n\n'
    'print(list(cumsum([1, 2, 3, 4])))')
code('# C7 (Hard) — Sliding-window generator\n'
    'def windows(seq, k):\n'
    '    for i in range(len(seq) - k + 1):\n'
    '        yield seq[i:i+k]\n\n'
    'print(list(windows("abcde", 3)))')
code('# C8 (Hard) — Infinite prime generator + first N\n'
    'from itertools import islice\n'
    'def primes():\n'
    '    found, n = [], 2\n'
    '    while True:\n'
    '        if all(n % p for p in found):   # short-circuiting genexpr\n'
    '            found.append(n)\n'
    '            yield n\n'
    '        n += 1\n\n'
    'print(list(islice(primes(), 6)))')

nb = new_notebook(cells=cells)
nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
nb.metadata["language_info"] = {"name": "python"}
nbf.write(nb, "solutions.ipynb")
print("wrote solutions.ipynb with", len(cells), "cells")
