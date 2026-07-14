# Builder for Session 7E, solutions.ipynb (answer key).
# Runnable, verified solutions. Timings vary per run.
# Async cells use asyncio.run() (in Jupyter, use top-level `await main()` instead).
# Multiprocessing cells (E10/C7) need the __main__ guard + top-level workers -> run as a script.
import nbformat as nbf
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell

cells = []
def md(t):   cells.append(new_markdown_cell(t))
def code(t): cells.append(new_code_cell(t))

md('<div style="background:#1e1e2e; padding:16px 20px; border-radius:8px; font-family:monospace; '
   'color:#cdd6f4; line-height:1.8">'
   '<p style="margin:0 0 8px 0; color:#cba6f7; font-weight:bold; font-size:1.05em;">✅ Session 7E — GIL &amp; Concurrency · Solutions</p>'
   '<p style="margin:0;">Worked, runnable solutions for the 12 <strong>Exercises</strong> and 8 '
   '<strong>Code Challenges</strong>. <strong>Notes:</strong> timings vary per run; async cells use '
   '<code>asyncio.run()</code> (in Jupyter use top-level <code>await main()</code> instead); '
   'multiprocessing cells (E10 / C7) must run as a <strong>.py script</strong> with the '
   '<code>if __name__ == "__main__"</code> guard.</p></div>')

md("### Exercises — Solutions")
code('import threading, queue, asyncio, time\n'
    'from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed')
code('# E1 — two functions concurrently\n'
    'res = []\n'
    'def work(x, out): out.append(x * x)\n'
    'ts = [threading.Thread(target=work, args=(n, res)) for n in [1, 2, 3]]\n'
    'for t in ts: t.start()\n'
    'for t in ts: t.join()\n'
    'print(sorted(res))                    # [1, 4, 9]')
code('# E2 — ThreadPoolExecutor.map (order preserved)\n'
    'with ThreadPoolExecutor() as ex:\n'
    '    print(list(ex.map(lambda x: x * 2, [1, 2, 3])))   # [2, 4, 6]')
code('# E3 — pick the tool\n'
    'def pick_tool(kind):\n'
    '    return "multiprocessing" if kind == "cpu" else "threads/asyncio"\n\n'
    'print(pick_tool("cpu"), "|", pick_tool("io"))')
code('# E4 — I/O overlap (timing varies)\n'
    'def io(): time.sleep(0.05)\n'
    't0 = time.perf_counter(); io(); io(); ser = time.perf_counter() - t0\n'
    't0 = time.perf_counter()\n'
    'ts = [threading.Thread(target=io) for _ in range(2)]\n'
    'for t in ts: t.start()\n'
    'for t in ts: t.join()\n'
    'thr = time.perf_counter() - t0\n'
    'print(f"serial={ser*1000:.0f}ms  threaded={thr*1000:.0f}ms  (threads overlap the sleeps)")')
code('# E5 — fix a race with a Lock\n'
    'counter = 0\n'
    'lock = threading.Lock()\n'
    'def inc():\n'
    '    global counter\n'
    '    for _ in range(50000):\n'
    '        with lock:\n'
    '            counter += 1\n'
    'ts = [threading.Thread(target=inc) for _ in range(2)]\n'
    'for t in ts: t.start()\n'
    'for t in ts: t.join()\n'
    'print(counter)                        # 100000 (exact, thanks to the lock)')
code('# E6 — producer/consumer with a queue + sentinel\n'
    'q = queue.Queue(); out = []\n'
    'def producer():\n'
    '    for i in range(5): q.put(i)\n'
    '    q.put(None)\n'
    'def consumer():\n'
    '    while True:\n'
    '        item = q.get()\n'
    '        if item is None: break\n'
    '        out.append(item * 10)\n'
    'p = threading.Thread(target=producer); c = threading.Thread(target=consumer)\n'
    'p.start(); c.start(); p.join(); c.join()\n'
    'print(out)                            # [0, 10, 20, 30, 40]')
code('# E7 — collect results as they finish\n'
    'with ThreadPoolExecutor() as ex:\n'
    '    futs = [ex.submit(lambda x: x * x, n) for n in [1, 2, 3]]\n'
    '    print(sorted(f.result() for f in as_completed(futs)))   # [1, 4, 9]')
code('# E8 — asyncio.gather two coroutines\n'
    'async def task(n):\n'
    '    await asyncio.sleep(0.01)\n'
    '    return n * n\n'
    'async def main():\n'
    '    return await asyncio.gather(task(1), task(2), task(3))\n'
    'print(asyncio.run(main()))            # [1, 4, 9]   (in Jupyter: await main())')
code('# E9 — gather over N fetches (total ~= slowest, not sum)\n'
    'async def fetch(i):\n'
    '    await asyncio.sleep(0.03)\n'
    '    return i\n'
    'async def main():\n'
    '    return await asyncio.gather(*[fetch(i) for i in range(5)])\n'
    't0 = time.perf_counter(); r = asyncio.run(main()); dt = time.perf_counter() - t0\n'
    'print(r, f"| ~{dt*1000:.0f}ms (not 150ms)")')
code('# E10 — CPU-bound speedup with ProcessPoolExecutor (RUN AS A SCRIPT)\n'
    'def cpu_sum(n):\n'
    '    s = 0\n'
    '    for i in range(n): s += i\n'
    '    return s\n\n'
    'if __name__ == "__main__":            # required: spawn re-imports the module\n'
    '    with ProcessPoolExecutor() as ex:\n'
    '        print(list(ex.map(cpu_sum, [1000, 2000, 3000])))   # [499500, 1999000, 4498500]')
code('# E11 — thread-safe memoize (computes once)\n'
    'def make_cache():\n'
    '    cache, lock, calls = {}, threading.Lock(), [0]\n'
    '    def get(k, compute):\n'
    '        with lock:\n'
    '            if k not in cache:\n'
    '                calls[0] += 1\n'
    '                cache[k] = compute(k)\n'
    '            return cache[k]\n'
    '    return get, calls\n\n'
    'get, calls = make_cache()\n'
    'print(get(4, lambda x: x*x), get(4, lambda x: x*x), "| computed", calls[0])   # 16 16 | computed 1')
code('# E12 — worker pool draining a queue with N sentinels\n'
    'q = queue.Queue(); out = []; olock = threading.Lock()\n'
    'def worker():\n'
    '    while True:\n'
    '        item = q.get()\n'
    '        if item is None: break\n'
    '        with olock: out.append(item * item)\n'
    'N = 3\n'
    'workers = [threading.Thread(target=worker) for _ in range(N)]\n'
    'for w in workers: w.start()\n'
    'for i in range(6): q.put(i)\n'
    'for _ in range(N): q.put(None)        # one sentinel per worker\n'
    'for w in workers: w.join()\n'
    'print(sorted(out))                    # [0, 1, 4, 9, 16, 25]')

md("### Code Challenges — Solutions")
code('# C1 — parallel map with a thread pool\n'
    'def square(x): return x * x\n'
    'with ThreadPoolExecutor(max_workers=3) as ex:\n'
    '    print(list(ex.map(square, range(3))))   # [0, 1, 4]')
code('# C2 — concurrent fetches returned in order\n'
    'def fetch(u): time.sleep(0.01); return f"data:{u}"\n'
    'with ThreadPoolExecutor() as ex:\n'
    '    print(list(ex.map(fetch, ["a", "b", "c"])))   # [\'data:a\', \'data:b\', \'data:c\']')
code('# C3 — thread-safe Counter (Lock)\n'
    'class Counter:\n'
    '    def __init__(self): self._v = 0; self._lock = threading.Lock()\n'
    '    def inc(self):\n'
    '        with self._lock: self._v += 1\n'
    '    @property\n'
    '    def value(self): return self._v\n\n'
    'c = Counter()\n'
    'ts = [threading.Thread(target=lambda: [c.inc() for _ in range(10000)]) for _ in range(4)]\n'
    'for t in ts: t.start()\n'
    'for t in ts: t.join()\n'
    'print(c.value)                        # 40000')
code('# C4 — asyncio.gather in order\n'
    'async def dbl(n):\n'
    '    await asyncio.sleep(0.01)\n'
    '    return n * 2\n'
    'async def main():\n'
    '    return await asyncio.gather(*[dbl(i) for i in range(4)])\n'
    'print(asyncio.run(main()))            # [0, 2, 4, 6]')
code('# C5 — timeout a slow coroutine\n'
    'async def slow():\n'
    '    await asyncio.sleep(1)\n'
    '    return "done"\n'
    'async def main():\n'
    '    try:\n'
    '        return await asyncio.wait_for(slow(), timeout=0.05)\n'
    '    except asyncio.TimeoutError:\n'
    '        return "timeout"\n'
    'print(asyncio.run(main()))            # timeout')
code('# C6 — cap concurrency with a Semaphore (never more than 2 active)\n'
    'sem = threading.Semaphore(2)\n'
    'active, mx, lk = [], [0], threading.Lock()\n'
    'def task():\n'
    '    with sem:\n'
    '        with lk:\n'
    '            active.append(1); mx[0] = max(mx[0], sum(active))\n'
    '        time.sleep(0.02)\n'
    '        with lk: active.pop()\n'
    'ts = [threading.Thread(target=task) for _ in range(6)]\n'
    'for t in ts: t.start()\n'
    'for t in ts: t.join()\n'
    'print("max concurrent:", mx[0], "(<= 2)")')
code('# C7 — CPU-bound parallel map with ProcessPoolExecutor (RUN AS A SCRIPT)\n'
    'def sq(x): return x * x            # top-level, picklable\n\n'
    'if __name__ == "__main__":\n'
    '    with ProcessPoolExecutor(max_workers=4) as ex:\n'
    '        print(list(ex.map(sq, range(6))))   # [0, 1, 4, 9, 16, 25]')
code('# C8 — async producer/consumer with asyncio.Queue\n'
    'async def main():\n'
    '    q = asyncio.Queue(); out = []\n'
    '    async def prod():\n'
    '        for i in range(5): await q.put(i)\n'
    '        await q.put(None)\n'
    '    async def cons():\n'
    '        while True:\n'
    '            item = await q.get()\n'
    '            if item is None: break\n'
    '            out.append(item * 10)\n'
    '    await asyncio.gather(prod(), cons())\n'
    '    return out\n'
    'print(asyncio.run(main()))            # [0, 10, 20, 30, 40]')

nb = new_notebook(cells=cells)
nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
nb.metadata["language_info"] = {"name": "python"}
nbf.write(nb, "solutions.ipynb")
print("wrote solutions.ipynb with", len(cells), "cells")
