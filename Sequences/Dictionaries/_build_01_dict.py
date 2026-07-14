# Builder for the hands-on 01_dict.ipynb notebook.
import nbformat as nbf
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell

cells = []
def md(t): cells.append(new_markdown_cell(t.strip("\n")))
def code(t): cells.append(new_code_cell(t.strip("\n")))

CARD = ('<div style="background:#1e1e2e; padding:16px 20px; border-radius:8px; '
        'font-family:monospace; color:#cdd6f4; line-height:1.8">\n{body}\n</div>')

def card(body): md(CARD.format(body=body))

# ── Title ─────────────────────────────────────────────────────────────
card(
'  <p style="margin:0 0 10px 0; color:#cba6f7; font-weight:bold; font-size:1.05em;">'
'📎 Session 2D — Dict (Deep) · Hands-on</p>\n'
'  <p style="margin:0;">The runnable playground for the dict theory — construction, the method '
'surface, comprehensions, <code>Counter</code>/<code>defaultdict</code>, the seven edge cases, and '
'the ML patterns. A dict is a <strong style="color:#89b4fa">hash table mapping hashable keys to '
'arbitrary values</strong> — O(1) access plus insertion order.</p>'
)

# ── 1. O(1) access ────────────────────────────────────────────────────
md("### 1. O(1) key access")
code(
"big = {i: i for i in range(1_000_000)}\n"
"big[999999]        # one hash lookup - O(1), no scan"
)
code(
"# vs scanning a list of (key, value) pairs for the same key - O(n)\n"
"pairs = list(big.items())\n"
"def scan_lookup(pairs, key):\n"
"    for k, v in pairs:\n"
"        if k == key:\n"
"            return v\n"
"scan_lookup(pairs, 999999)"
)
code(
"import time\n"
"start = time.perf_counter(); big[999999];            t_dict = time.perf_counter() - start\n"
"start = time.perf_counter(); scan_lookup(pairs, 999999); t_scan = time.perf_counter() - start\n"
"print(f'dict lookup: {t_dict*1e6:8.2f} us')\n"
"print(f'list scan:   {t_scan*1e6:8.2f} us')"
)
card(
'  <p style="margin:0;">A dict hashes the key, jumps straight to the bucket, and returns the value — '
'constant time no matter how big the dict is. Scanning a list of pairs is O(n). '
'<strong style="color:#cba6f7">SQL anchor:</strong> a dict is a lookup table with a primary-key index; '
'<code>d[key]</code> is an indexed seek, the scan is a full table scan.</p>'
)

# ── 2. Construction ───────────────────────────────────────────────────
md("### 2. Construction — the ways to build a dict")
code('{"a": 1, "b": 2}                      # literal')
code('dict(a=1, b=2)                        # keyword args (string keys only)')
code('dict([("a", 1), ("b", 2)])            # from an iterable of pairs')
code('dict(zip(["a", "b", "c"], [1, 2, 3])) # zip two parallel lists')
code('dict.fromkeys(["x", "y", "z"], 0)     # same value for every key')
code('{x: x * x for x in range(5)}          # comprehension')

# ── 3. [] vs .get() ───────────────────────────────────────────────────
md("### 3. Access — `[]` vs `.get()`")
code(
'd = {"a": 1, "b": 2}\n'
'd["a"]                # 1'
)
code(
'try:\n'
'    d["z"]            # KeyError - the key must exist\n'
'except KeyError as e:\n'
'    print("KeyError:", e)'
)
code(
'print(d.get("z"))         # None - safe, no crash\n'
'print(d.get("z", 0))      # 0   - with a fallback default'
)
card(
'  <p style="margin:0;">Use <code>d[key]</code> when the key <strong style="color:#89b4fa">must exist</strong> '
'(fail loud on a bug). Use <code>d.get(key, default)</code> when absence is a '
'<strong style="color:#a6e3a1">normal, expected case</strong> with a sensible fallback.</p>'
)

# ── 4. Method surface ─────────────────────────────────────────────────
md("### 4. The method surface")
code(
'd = {"a": 1, "b": 2}\n'
'd.setdefault("c", 3)      # inserts c=3 (missing) and returns 3'
)
code('d.setdefault("a", 99)     # a exists -> returns existing 1, no overwrite')
code('d')
code('list(d.keys()), list(d.values()), list(d.items())')
code(
'd.update({"b": 20, "d": 4})   # merge / overwrite in place\n'
'd'
)
code('d.pop("d")                # removes "d", RETURNS its value 4')
code('d.popitem()               # removes & RETURNS the last-inserted (key, value)')
code('d')
code(
'del d["a"]                # delete by key (returns nothing)\n'
'd'
)
code('"b" in d, "zzz" in d      # membership tests KEYS')
card(
'  <p style="margin:0 0 12px 0;">Which methods hand you a value vs only mutate:</p>\n'
'  <ul style="margin:0; padding-left:20px; line-height:2.2">\n'
'    <li><strong style="color:#a6e3a1">Return something useful</strong> — <code>get</code>, '
'<code>pop</code>, <code>popitem</code>, <code>setdefault</code></li>\n'
'    <li><strong style="color:#f38ba8">Mutate, return None</strong> — <code>update</code>, '
'<code>clear</code>; <code>del</code> is a statement</li>\n'
'  </ul>'
)

# ── 5. Iteration ──────────────────────────────────────────────────────
md("### 5. Iteration — keys by default, `.items()` for pairs")
code(
'd = {"a": 1, "b": 2, "c": 3}\n'
'for k in d:               # iterating a dict yields KEYS\n'
'    print(k, end=" ")'
)
code(
'for v in d.values():\n'
'    print(v, end=" ")'
)
code(
'for k, v in d.items():    # (key, value) pairs - the common loop\n'
'    print(f"{k}={v}", end="  ")'
)
code(
'try:\n'
'    for k, v in d:        # ValueError - unpacking a single key into two names\n'
'        pass\n'
'except ValueError as e:\n'
'    print("ValueError:", e)'
)

# ── 6. Comprehensions ─────────────────────────────────────────────────
md("### 6. Comprehensions — build / filter / invert")
code('{x: x * x for x in range(5)}                     # build')
code(
'prices = {"apple": 3, "banana": 1, "cherry": 5}\n'
'{k: v for k, v in prices.items() if v > 2}       # filter  (WHERE v > 2)'
)
code('{v: k for k, v in prices.items()}               # invert (values must be unique)')
card(
'  <p style="margin:0;">Inverting is handy for reverse lookups, but it is '
'<strong style="color:#f38ba8">lossy when values are not unique</strong> — duplicate values collapse '
'because keys must be unique (last one wins).</p>'
)

# ── 7. Counter ────────────────────────────────────────────────────────
md("### 7. Counter — counting made trivial")
code(
'words = "the cat the dog the cat".split()\n'
'# the mechanism first, with .get(k, 0) + 1\n'
'f = {}\n'
'for w in words:\n'
'    f[w] = f.get(w, 0) + 1\n'
'f'
)
code(
'from collections import Counter\n'
'c = Counter(words)        # the one-liner\n'
'c'
)
code('c.most_common(2)          # top 2 by count')
code('Counter("mississippi")    # counts characters')
code('Counter("aab") + Counter("bcc")   # Counter arithmetic')

# ── 8. defaultdict ────────────────────────────────────────────────────
md("### 8. defaultdict — auto-create the missing value")
code(
'from collections import defaultdict\n'
'people = [("eng", "Alice"), ("sales", "Bob"), ("eng", "Cara"), ("sales", "Dan")]\n'
'groups = defaultdict(list)\n'
'for dept, name in people:\n'
'    groups[dept].append(name)     # no KeyError on first touch\n'
'dict(groups)'
)
code(
'counts = defaultdict(int)\n'
'for w in words:\n'
'    counts[w] += 1                # missing key auto-starts at 0\n'
'dict(counts)'
)

# ── 9. Merging ────────────────────────────────────────────────────────
md("### 9. Merging dicts — right side wins")
code(
'DEFAULTS = {"lr": 0.01, "epochs": 100, "batch": 32}\n'
'user = {"lr": 0.001, "batch": 64}\n'
'DEFAULTS | user                     # 3.9+  -> user overrides, epochs falls back'
)
code('{**DEFAULTS, **user}                # older syntax, same result')
code(
'merged = DEFAULTS.copy()\n'
'merged.update(user)                 # mutate a copy in place\n'
'merged'
)

# ── Edge cases ────────────────────────────────────────────────────────
md("### Edge Cases (the seven from Chunk C)")
code('{"a": 1, "a": 2, "a": 3}            # Edge 3: duplicate keys collapse -> {\'a\': 3}')
code('dict([("x", 1), ("x", 2)])          # first value lost silently -> {\'x\': 2}')
code(
'# Edge 4: dict.fromkeys with a mutable default shares ONE object\n'
'd = dict.fromkeys(["a", "b", "c"], [])\n'
'd["a"].append(1)\n'
'print(d)                                  # {\'a\': [1], \'b\': [1], \'c\': [1]}  -- all changed!'
)
code(
'd2 = {k: [] for k in ["a", "b", "c"]}     # comprehension -> distinct lists\n'
'd2["a"].append(1)\n'
'print(d2)                                 # {\'a\': [1], \'b\': [], \'c\': []}  -- correct'
)
code(
'# Edge 5: modifying a dict during iteration raises\n'
'd = {"a": 1, "b": 2, "c": 3}\n'
'try:\n'
'    for k in d:\n'
'        if d[k] == 2:\n'
'            del d[k]        # RuntimeError: dictionary changed size during iteration\n'
'except RuntimeError as e:\n'
'    print("RuntimeError:", e)'
)
code(
'# fix: build a new dict with a comprehension (or iterate list(d))\n'
'd = {"a": 1, "b": 2, "c": 3}\n'
'{k: v for k, v in d.items() if v != 2}'
)
code(
'# Edge 6: 1 and 1.0 are the SAME key (equal, same hash); the string "1" is distinct\n'
'{1: "a", "1": "b", 1.0: "c"}            # -> {1: \'c\', \'1\': \'b\'}'
)
code(
'd = {1: "a", "1": "b", 1.0: "c"}\n'
'"a" in d          # False -- "in" checks KEYS, not values'
)
code(
'# Edge 7: .get() with a default does NOT store; setdefault does\n'
'd = {}\n'
'd.get("k", [])            # returns [] but leaves d unchanged\n'
'd'
)
code(
'd = {}\n'
'd.setdefault("k", []).append(1)   # stores [] AND returns it -> mutation sticks\n'
'd'
)
code(
'# bonus: unhashable keys are rejected\n'
'try:\n'
'    {[1, 2]: "x"}         # a list cannot be a key\n'
'except TypeError as e:\n'
'    print("TypeError:", e)'
)

# ── ML uses ───────────────────────────────────────────────────────────
md("### ML Real-World Uses")
code(
'# A feature vector / data row is a dict\n'
'sample = {"age": 34, "income": 55000, "region": "south", "score": 0.87}\n'
'print(sample["age"])\n'
'print(sample.get("missing_feat", 0))    # safe default for an absent feature'
)
code(
'# Class distribution - step zero before training\n'
'labels = ["spam", "ham", "spam", "spam", "ham", "spam"]\n'
'dist = Counter(labels)\n'
'total = sum(dist.values())\n'
'balance = {k: round(v / total, 2) for k, v in dist.items()}\n'
'print(dist)\n'
'print(balance)'
)
code(
'# Vocabulary encoding - the tokenizer core\n'
'corpus = ["deploy docker", "docker build", "deploy kubernetes"]\n'
'vocab = {}\n'
'for doc in corpus:\n'
'    for tok in doc.split():\n'
'        if tok not in vocab:\n'
'            vocab[tok] = len(vocab)     # next token gets the next integer id\n'
'def encode(doc):\n'
'    return [vocab[t] for t in doc.split()]\n'
'print(vocab)\n'
'print(encode("deploy docker"))'
)
code(
'# Memoization - a dict cache turns exponential into linear\n'
'cache = {}\n'
'def fib(n):\n'
'    if n < 2:\n'
'        return n\n'
'    if n in cache:\n'
'        return cache[n]\n'
'    cache[n] = fib(n - 1) + fib(n - 2)\n'
'    return cache[n]\n'
'print(fib(30))\n'
'print(len(cache), "cached entries")'
)
code(
'# Config merged over defaults - reproducible and immutable-friendly\n'
'DEFAULTS = {"lr": 0.01, "epochs": 100, "optimizer": "adam"}\n'
'run_config = DEFAULTS | {"lr": 0.001, "epochs": 50}\n'
'run_config'
)

# ── Worked challenges ─────────────────────────────────────────────────
md("### Worked Challenges")
code(
'# C1 - invert a dict with NON-unique values (lossless, via defaultdict)\n'
'grades = {"Alice": 88, "Bob": 92, "Cara": 88}\n'
'inv = defaultdict(list)\n'
'for name, score in grades.items():\n'
'    inv[score].append(name)\n'
'dict(inv)                     # {88: [\'Alice\', \'Cara\'], 92: [\'Bob\']}'
)
code(
'# C2 - group anagrams by their sorted-letter signature\n'
'def group_anagrams(words):\n'
'    groups = defaultdict(list)\n'
'    for w in words:\n'
'        key = "".join(sorted(w))    # canonical signature\n'
'        groups[key].append(w)\n'
'    return list(groups.values())\n'
'group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])'
)
code(
'# C3 - two-sum in O(n) with a dict for O(1) complement lookup\n'
'def two_sum(nums, target):\n'
'    seen = {}\n'
'    for i, n in enumerate(nums):\n'
'        if target - n in seen:\n'
'            return [seen[target - n], i]\n'
'        seen[n] = i\n'
'    return None\n'
'two_sum([2, 7, 11, 15], 9)'
)
code(
'# C4 - top-k frequent elements via Counter.most_common\n'
'def top_k_frequent(items, k):\n'
'    return [x for x, _ in Counter(items).most_common(k)]\n'
'top_k_frequent([1, 1, 1, 2, 2, 3], 2)'
)
code(
'# C5 - first non-repeating element (the 2C set -> dict bridge)\n'
'def first_unique(seq):\n'
'    counts = Counter(seq)\n'
'    for x in seq:            # scan in ORIGINAL order\n'
'        if counts[x] == 1:\n'
'            return x\n'
'    return None\n'
'first_unique([2, 3, 2, 4, 3, 5])'
)
card(
'  <p style="margin:0;">C5 is the seam where sets stop and dicts begin: a set knows only '
'<strong style="color:#89b4fa">present/absent</strong>, but this needs <strong style="color:#a6e3a1">'
'counts</strong> (how many times) <em>and</em> <strong style="color:#a6e3a1">order</strong> (which came '
'first) — a <code>Counter</code> gives both. That is exactly why Dict follows Set in the track.</p>'
)

# ── Key takeaways ─────────────────────────────────────────────────────
card(
'  <p style="margin:0 0 10px 0; color:#cba6f7; font-weight:bold;">🔑 Key Takeaways</p>\n'
'  <ul style="margin:0; padding-left:20px; line-height:2.2">\n'
'    <li>A dict is a hash table mapping <strong style="color:#89b4fa">hashable keys</strong> → arbitrary '
'values; <code>d[key]</code> is O(1)</li>\n'
'    <li><code>[]</code> fails loud, <code>.get()</code> is safe</li>\n'
'    <li><code>Counter</code> to count, <code>defaultdict</code> to group</li>\n'
'    <li><code>fromkeys</code> with a mutable default aliases one object — use a comprehension</li>\n'
'    <li>Iterate <code>.items()</code> for pairs; never change a dict\'s size mid-iteration</li>\n'
'  </ul>'
)

nb = new_notebook(cells=cells)
nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
nb.metadata["language_info"] = {"name": "python"}

path = "01_dict.ipynb"
nbf.write(nb, path)
print("wrote", path, "with", len(cells), "cells")
