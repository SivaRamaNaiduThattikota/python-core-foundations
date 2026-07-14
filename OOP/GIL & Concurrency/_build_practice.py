# Builder for Session 7E, 01_concurrency.ipynb (hands-on practice scaffold).
import nbformat as nbf
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell

cells = []
def md(t):   cells.append(new_markdown_cell(t))
def code(t): cells.append(new_code_cell(t))

md('<div style="background:#1e1e2e; padding:16px 20px; border-radius:8px; font-family:monospace; '
   'color:#cdd6f4; line-height:1.8">'
   '<p style="margin:0 0 8px 0; color:#cba6f7; font-weight:bold; font-size:1.05em;">📎 Session 7E — GIL &amp; Concurrency · Hands-on</p>'
   '<p style="margin:0;">Attempt space for the 12 <strong>Exercises</strong> and 8 <strong>Code Challenges</strong>. '
   'Hints in <code>theory.ipynb</code>; worked solutions in <code>solutions.ipynb</code>. '
   'Timings vary per run; multiprocessing (E10 / C7) must run as a <strong>script</strong> with the '
   '<code>if __name__ == "__main__"</code> guard.</p></div>')

md("### Exercises (Part 2 · §6) — 12 problems")
EX = [
 ('E1 (Easy)', 'Run two functions concurrently with threading.Thread', 'target=/args=, start() each, join() each'),
 ('E2 (Easy)', 'Map a function over inputs with ThreadPoolExecutor', 'with ThreadPoolExecutor() as ex: list(ex.map(fn, items))'),
 ('E3 (Easy)', 'pick_tool(kind): "multiprocessing" for cpu else "threads/asyncio"', 'CPU -> processes; I/O -> threads/async'),
 ('E4 (Med)',  'Show I/O overlap: serial vs 2 threads over time.sleep tasks', 'threaded ~ half; sleep releases the GIL'),
 ('E5 (Med)',  'Fix a race on a shared counter with threading.Lock', 'with lock: counter += 1; 2x50k -> 100000'),
 ('E6 (Med)',  'Producer/consumer with queue.Queue (+ sentinel)', 'producer puts items then None; consumer loops until None'),
 ('E7 (Med)',  'Collect results as they finish with as_completed', 'submit futures; iterate as_completed; f.result()'),
 ('E8 (Med)',  'Run two coroutines concurrently with asyncio.gather', 'async def + await asyncio.sleep; asyncio.run(gather(a,b))'),
 ('E9 (Hard)', 'gather over N fetches -> total ~= slowest, not sum', 'asyncio.gather(*[fetch(i) for i in range(N)])'),
 ('E10 (Hard)','CPU-bound speedup with ProcessPoolExecutor (guard __main__)', 'top-level worker; run under if __name__ == "__main__"'),
 ('E11 (Hard)','A thread-safe memoize cache (dict + Lock)', 'guard check-compute-store with a lock -> computes once'),
 ('E12 (Hard)','Worker pool draining a queue with N sentinels to stop', 'start N workers; after items, put N Nones'),
]
for tag, prob, hint in EX:
    code(f"# {tag} — {prob}\n# Hint: {hint}\n\n")

md("### Code Challenges (Part 3 · §8b) — 8 problems")
CC = [
 ('C1 (Easy)', 'Parallel map over 3 items with ThreadPoolExecutor'),
 ('C2 (Easy)', 'Concurrent "fetches" returned in order (map preserves order)'),
 ('C3 (Med)',  'Thread-safe Counter class (Lock) -> correct total'),
 ('C4 (Med)',  'asyncio.gather returning results in order'),
 ('C5 (Med)',  'Time out a slow coroutine with asyncio.wait_for'),
 ('C6 (Med)',  'Cap concurrency with a threading.Semaphore (<=2 at once)'),
 ('C7 (Hard)', 'CPU-bound parallel map with ProcessPoolExecutor (guard __main__)'),
 ('C8 (Hard)', 'Async producer/consumer with asyncio.Queue'),
]
for tag, prob in CC:
    code(f"# {tag} — {prob}\n\n")

nb = new_notebook(cells=cells)
nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
nb.metadata["language_info"] = {"name": "python"}
nbf.write(nb, "01_concurrency.ipynb")
print("wrote 01_concurrency.ipynb with", len(cells), "cells")
