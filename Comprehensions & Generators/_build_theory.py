# Builder for Session 4 - Comprehensions & Generators, theory.ipynb.
# Single chunked session. Chunk A = List comprehensions (deep). Catppuccin Mocha UI.
import nbformat as nbf
from nbformat.v4 import new_notebook, new_markdown_cell

cells = []

STYLE = """<style>
  * { box-sizing:border-box; word-wrap:break-word; overflow-wrap:break-word; }
  body, .jp-RenderedHTMLCommon { padding:0 !important; margin:0 !important; overflow-x:hidden !important; }
  h1.main-title { color:#cba6f7; font-family:'Segoe UI',sans-serif; font-size:2em; border-bottom:2px solid #45475a; padding-bottom:10px; margin-bottom:16px; }
  .part-header { background:linear-gradient(90deg,#313244,#1e1e2e); border-left:5px solid #cba6f7; border-radius:10px; padding:14px 22px; margin:24px 0 10px; }
  .part-header h2 { color:#cba6f7; margin:0; font-size:1.3em; font-family:'Segoe UI',sans-serif; }
  .chunk-badge { display:inline-block; background:#2a1e2e; border:1px solid #cba6f7; color:#cba6f7; border-radius:20px; padding:2px 12px; font-size:0.82em; font-family:'Courier New',monospace; margin:6px 0; }
  h3.sub { color:#89dceb; font-family:'Segoe UI',sans-serif; margin:20px 0 8px; font-size:1.02em; }
  .theory-box { background:#2a2a3d; border-left:5px solid #89b4fa; border-radius:10px; padding:16px 22px; margin:14px 0; color:#cdd6f4; font-family:'Segoe UI',sans-serif; line-height:1.8; max-width:100%; }
  .code-block { background:#181825; border:1px solid #313244; border-radius:8px; padding:14px 20px; font-family:'Courier New',monospace; font-size:0.9em; color:#a6e3a1; margin:10px 0; line-height:2; overflow-x:auto; max-width:100%; }
  .output-block { background:#11111b; border:1px solid #313244; border-radius:8px; padding:12px 18px; font-family:'Courier New',monospace; font-size:0.87em; color:#cdd6f4; margin:4px 0 10px; line-height:1.9; overflow-x:auto; max-width:100%; }
  .info-box { background:#1e2030; border-left:4px solid #89b4fa; border-radius:8px; padding:11px 16px; margin:10px 0; color:#89b4fa; font-family:'Segoe UI',sans-serif; font-size:0.92em; line-height:1.7; }
  .note-box { background:#1c1c2e; border-left:4px solid #a6e3a1; border-radius:8px; padding:11px 16px; margin:10px 0; color:#a6e3a1; font-family:'Segoe UI',sans-serif; font-size:0.92em; line-height:1.7; }
  .why-box { background:#2a1e2e; border-left:4px solid #cba6f7; border-radius:0 8px 8px 0; padding:10px 14px; margin:8px 0; color:#cba6f7; font-family:'Segoe UI',sans-serif; font-size:0.9em; line-height:1.7; }
  .warn-box { background:#2a1f00; border-left:4px solid #f9e2af; border-radius:8px; padding:11px 16px; margin:10px 0; color:#f9e2af; font-family:'Segoe UI',sans-serif; font-size:0.92em; line-height:1.7; }
  .theory-box code, .info-box code, .note-box code, .why-box code, .warn-box code { background:#313244; padding:1px 6px; border-radius:4px; color:#a6e3a1; font-family:'Courier New',monospace; font-size:0.88em; }
  .mut-grid { display:block; margin:12px 0; }
  .mut-card { display:inline-block; width:48%; min-width:200px; vertical-align:top; border-radius:10px; padding:14px 16px; margin-right:2%; margin-bottom:10px; font-family:'Segoe UI',sans-serif; font-size:0.88em; line-height:1.85; }
  .mut-card:last-child { margin-right:0; }
  .mc-imm { background:#1e2030; border:1px solid #89b4fa; border-top:3px solid #89b4fa; }
  .mc-mut { background:#1a2e1a; border:1px solid #a6e3a1; border-top:3px solid #a6e3a1; }
  .mc-imm .mc-title { color:#89b4fa; font-weight:bold; margin-bottom:8px; }
  .mc-mut .mc-title { color:#a6e3a1; font-weight:bold; margin-bottom:8px; }
  .mc-body { color:#cdd6f4; font-family:'Courier New',monospace; font-size:0.86em; }
  .ex-header { background:linear-gradient(90deg,#1a2e1a,#1e1e2e); border-left:5px solid #a6e3a1; border-radius:10px; padding:14px 22px; margin:24px 0 10px; }
  .ex-header h2 { color:#a6e3a1; margin:0; font-size:1.3em; font-family:'Segoe UI',sans-serif; }
  .warn-header { background:linear-gradient(90deg,#2a1f00,#1e1e2e); border-left:5px solid #f9e2af; border-radius:10px; padding:14px 22px; margin:24px 0 10px; }
  .warn-header h2 { color:#f9e2af; margin:0; font-size:1.3em; font-family:'Segoe UI',sans-serif; }
  .ex-block { background:#1e1e2e; border:1px solid #313244; border-radius:10px; padding:16px 20px; margin:12px 0; }
  .ex-title { color:#a6e3a1; font-family:'Segoe UI',sans-serif; font-weight:bold; font-size:0.95em; margin-bottom:10px; }
  .ex-badge { display:inline-block; background:#1a2e1a; border:1px solid #a6e3a1; color:#a6e3a1; border-radius:20px; padding:2px 10px; font-size:0.8em; font-family:'Courier New',monospace; margin-right:8px; }
  .edge-block { background:#1e1e2e; border:1px solid #313244; border-radius:10px; padding:16px 20px; margin:12px 0; }
  .edge-title { color:#f9e2af; font-family:'Segoe UI',sans-serif; font-weight:bold; font-size:0.95em; margin-bottom:10px; }
  .edge-badge { display:inline-block; background:#2a1f00; border:1px solid #f9e2af; color:#f9e2af; border-radius:20px; padding:2px 10px; font-size:0.8em; font-family:'Courier New',monospace; margin-right:8px; }
  .rule-block, .trap-block, .ml-block, .exr-block, .cc-block { background:#1e1e2e; border:1px solid #313244; border-radius:10px; padding:14px 18px; margin:10px 0; }
  .rule-title { color:#cba6f7; font-family:'Segoe UI',sans-serif; font-weight:bold; font-size:0.92em; margin-bottom:6px; }
  .rule-badge { display:inline-block; background:#2a1e2e; border:1px solid #cba6f7; color:#cba6f7; border-radius:20px; padding:2px 10px; font-size:0.76em; font-family:'Courier New',monospace; margin-right:8px; }
  .trap-header { background:linear-gradient(90deg,#2e1e1e,#1e1e2e); border-left:5px solid #f38ba8; border-radius:10px; padding:14px 22px; margin:24px 0 10px; }
  .trap-header h2 { color:#f38ba8; margin:0; font-size:1.3em; font-family:'Segoe UI',sans-serif; }
  .trap-title { color:#f38ba8; font-family:'Segoe UI',sans-serif; font-weight:bold; font-size:0.92em; margin-bottom:6px; }
  .trap-badge { display:inline-block; background:#2e1e1e; border:1px solid #f38ba8; color:#f38ba8; border-radius:20px; padding:2px 10px; font-size:0.76em; font-family:'Courier New',monospace; margin-right:8px; }
  .ml-header { background:linear-gradient(90deg,#1a2e1a,#1e1e2e); border-left:5px solid #a6e3a1; border-radius:10px; padding:14px 22px; margin:24px 0 10px; }
  .ml-header h2 { color:#a6e3a1; margin:0; font-size:1.3em; font-family:'Segoe UI',sans-serif; }
  .ml-title { color:#a6e3a1; font-family:'Segoe UI',sans-serif; font-weight:bold; font-size:0.92em; margin-bottom:6px; }
  .ml-badge { display:inline-block; background:#1a2e1a; border:1px solid #a6e3a1; color:#a6e3a1; border-radius:20px; padding:2px 10px; font-size:0.76em; font-family:'Courier New',monospace; margin-right:8px; }
  .body-txt { color:#cdd6f4; font-family:'Segoe UI',sans-serif; font-size:0.9em; line-height:1.7; }
  .body-txt code { background:#313244; padding:1px 5px; border-radius:4px; color:#a6e3a1; font-family:'Courier New',monospace; font-size:0.86em; }
  .interview-header { background:linear-gradient(90deg,#2a1e2e,#1e1e2e); border-left:5px solid #cba6f7; border-radius:10px; padding:14px 22px; margin:24px 0 10px; }
  .interview-header h2 { color:#cba6f7; margin:0; font-size:1.3em; font-family:'Segoe UI',sans-serif; }
  .sub-header { background:linear-gradient(90deg,#1e2030,#1e1e2e); border-left:4px solid #89b4fa; border-radius:8px; padding:8px 16px; margin:16px 0 8px; }
  .sub-header h3 { color:#89b4fa; margin:0; font-size:0.95em; font-family:'Segoe UI',sans-serif; }
  .qa-block { background:#1e1e2e; border:1px solid #313244; border-radius:10px; padding:11px 16px; margin:8px 0; }
  .qa-q { color:#f9e2af; font-family:'Segoe UI',sans-serif; font-weight:bold; font-size:0.89em; margin-bottom:5px; line-height:1.5; }
  .qa-a { color:#cdd6f4; font-family:'Segoe UI',sans-serif; font-size:0.87em; line-height:1.7; }
  .qa-a code, .qa-q code { background:#313244; padding:1px 5px; border-radius:4px; color:#a6e3a1; font-family:'Courier New',monospace; font-size:0.85em; }
  .q-num { display:inline-block; min-width:22px; height:22px; border-radius:50%; background:#2a1e2e; border:2px solid #cba6f7; color:#cba6f7; font-weight:bold; font-size:0.75em; text-align:center; line-height:19px; font-family:'Courier New',monospace; margin-right:8px; }
  .cc-title { color:#89b4fa; font-family:'Segoe UI',sans-serif; font-weight:bold; font-size:0.91em; margin-bottom:8px; }
  .cc-badge { display:inline-block; border-radius:20px; padding:2px 10px; font-size:0.74em; font-family:'Courier New',monospace; margin-right:8px; }
  .badge-easy { background:#1a2e1a; border:1px solid #a6e3a1; color:#a6e3a1; }
  .badge-med { background:#1e2030; border:1px solid #89b4fa; color:#89b4fa; }
  .badge-hard { background:#2e1e1e; border:1px solid #f38ba8; color:#f38ba8; }
  details.sol { background:#181825; border:1px solid #313244; border-radius:8px; padding:8px 14px; margin:8px 0; }
  details.sol summary { color:#a6e3a1; font-family:'Segoe UI',sans-serif; font-size:0.85em; cursor:pointer; font-weight:bold; }
  .hint-box { background:#1c1c2e; border-left:4px solid #89dceb; border-radius:0 8px 8px 0; padding:8px 12px; margin:6px 0; color:#89dceb; font-family:'Segoe UI',sans-serif; font-size:0.85em; line-height:1.6; }
  .hint-box code { background:#313244; padding:1px 5px; border-radius:4px; color:#a6e3a1; font-family:'Courier New',monospace; font-size:0.82em; }
  .exr-title { color:#cdd6f4; font-family:'Segoe UI',sans-serif; font-weight:bold; font-size:0.9em; margin-bottom:6px; }
  .summary-header { background:linear-gradient(90deg,#1e2030,#1e1e2e); border-left:5px solid #89b4fa; border-radius:10px; padding:14px 22px; margin:24px 0 10px; }
  .summary-header h2 { color:#89b4fa; margin:0; font-size:1.3em; font-family:'Segoe UI',sans-serif; }
  table.summary { width:100%; border-collapse:collapse; font-family:'Segoe UI',sans-serif; font-size:0.86em; margin:12px 0; }
  table.summary th { background:#313244; color:#cba6f7; padding:9px 14px; text-align:left; border:1px solid #45475a; }
  table.summary td { background:#1e1e2e; color:#cdd6f4; padding:8px 14px; border:1px solid #313244; vertical-align:top; line-height:1.6; }
  table.summary td:first-child { color:#89dceb; }
  table.summary td:last-child { text-align:center; font-weight:bold; }
  .freq-vh { color:#f38ba8; } .freq-h { color:#f9e2af; } .freq-m { color:#89b4fa; }
  .divider { border:none; border-top:1px solid #313244; margin:22px 0; }
  .cc { color:#6c7086; } .cs { color:#f9e2af; } .ck { color:#cba6f7; } .cm { color:#f38ba8; } .cn { color:#fab387; }
</style>
"""

def md(body):
    cells.append(new_markdown_cell(STYLE + body))

# ── Title ──────────────────────────────────────────────────────────────
md(
'<h1 class="main-title">🐍 Session 4 — Comprehensions &amp; Generators</h1>'
'<div class="info-box"><strong>Part 1:</strong> Theory → Example → Edge Cases &nbsp;·&nbsp; '
'delivered in four chunks (two deep topics in one session).</div>'
'<div class="chunk-badge">Part 1 · Chunk A — List Comprehensions (deep)</div>'
'<div class="theory-box" style="border-left-color:#cba6f7;">'
'This session unifies two ideas. <strong style="color:#89b4fa">Comprehensions</strong> are a declarative '
'way to build a <code>list</code>/<code>dict</code>/<code>set</code> (Session 2) in one readable pass. '
'<strong style="color:#89b4fa">Generators</strong> are the lazy cousin — same syntax, but they yield '
'values on demand instead of building the whole collection. Chunk A starts with the list comprehension, '
'the form you\'ll use most; B extends it to dict/set; C &amp; D turn it lazy.</div>'
)

# ── 1.1 model + map/filter ─────────────────────────────────────────────
md(
'<div class="part-header"><h2>1. Theory</h2></div>'
'<h3 class="sub">🔹 1.1 &nbsp;What a comprehension is — build a list in one declarative pass</h3>'
'<div class="theory-box">'
'<p style="margin:0 0 10px 0">A list comprehension is an expression that produces a new list by '
'<strong>transforming</strong> and/or <strong>filtering</strong> an iterable. The shape:</p>'
'<div class="code-block" style="margin:6px 0">[ <span class="cn">expr</span> <span class="ck">for</span> item <span class="ck">in</span> iterable <span class="ck">if</span> <span class="cn">cond</span> ]</div>'
'<p style="margin:0">Read it as: "collect <code>expr</code> for each <code>item</code>, keeping only those where '
'<code>cond</code> is true." The <code>if</code> is optional.</p></div>'
'<div class="info-box">💡 <strong>SQL / Power BI anchor:</strong> <code>[expr for x in xs if cond]</code> is '
'<code>SELECT expr FROM xs WHERE cond</code>. The expression is a computed column; the <code>if</code> is '
'the <code>WHERE</code>.</div>'
'<div class="code-block">'
'[x*x <span class="ck">for</span> x <span class="ck">in</span> <span class="cm">range</span>(<span class="cn">6</span>)]                 <span class="cc"># map: transform every element</span><br>'
'[x <span class="ck">for</span> x <span class="ck">in</span> <span class="cm">range</span>(<span class="cn">10</span>) <span class="ck">if</span> x % <span class="cn">2</span> == <span class="cn">0</span>]  <span class="cc"># filter: keep some</span><br>'
'[x*x <span class="ck">for</span> x <span class="ck">in</span> <span class="cm">range</span>(<span class="cn">10</span>) <span class="ck">if</span> x % <span class="cn">2</span>]     <span class="cc"># map + filter together</span></div>'
'<div class="output-block">[0, 1, 4, 9, 16, 25]<br>[0, 2, 4, 6, 8]<br>[1, 9, 25, 49, 81]</div>'
'<div class="note-box">💡 Three forms: <strong>map</strong> (transform all), <strong>filter</strong> (keep some), '
'and <strong>map+filter</strong>. The <code>expr</code> can be any expression — a call, a method, a slice, '
'even another comprehension.</div>'
)

# ── 1.2 ternary vs filter ──────────────────────────────────────────────
md(
'<h3 class="sub">🔹 1.2 &nbsp;Conditional <em>expression</em> vs filter — a key distinction</h3>'
'<div class="theory-box">There are two different "if"s, and mixing them up is a classic bug. A '
'<strong>filter</strong> (<code>if</code> after the loop) <em>drops</em> elements. A <strong>conditional '
'expression</strong> (<code>a if cond else b</code>, before the loop) <em>transforms</em> every element and '
'drops nothing.</div>'
'<div class="code-block">'
'[x <span class="ck">if</span> x &gt; <span class="cn">0</span> <span class="ck">else</span> <span class="cn">0</span> <span class="ck">for</span> x <span class="ck">in</span> [-<span class="cn">1</span>, <span class="cn">2</span>, -<span class="cn">3</span>, <span class="cn">4</span>]]   <span class="cc"># ternary in the EXPR -> keeps all, clamps</span><br>'
'[x <span class="ck">for</span> x <span class="ck">in</span> [-<span class="cn">1</span>, <span class="cn">2</span>, -<span class="cn">3</span>, <span class="cn">4</span>] <span class="ck">if</span> x &gt; <span class="cn">0</span>]         <span class="cc"># filter -> DROPS the negatives</span><br>'
'[x <span class="ck">if</span> x &gt; <span class="cn">0</span> <span class="ck">else</span> -x <span class="ck">for</span> x <span class="ck">in</span> [-<span class="cn">1</span>, <span class="cn">2</span>, -<span class="cn">3</span>, <span class="cn">0</span>] <span class="ck">if</span> x != <span class="cn">0</span>]  <span class="cc"># both at once</span></div>'
'<div class="output-block">[0, 2, 0, 4]<br>[2, 4]<br>[1, 2, 3]</div>'
'<div class="why-box"><strong>Why it matters:</strong> position tells you the job. <code>if ... else</code> '
'<em>before</em> <code>for</code> = transform (list length unchanged). Bare <code>if</code> <em>after</em> '
'<code>for</code> = filter (list shrinks). You can use both in one comprehension — the last line clamps sign '
'<em>and</em> drops zeros.</div>'
)

# ── 1.3 why faster than append-loop ────────────────────────────────────
md(
'<h3 class="sub">🔹 1.3 &nbsp;Why a comprehension beats an append-loop</h3>'
'<div class="theory-box">A comprehension isn\'t just prettier — it\'s faster. The equivalent append-loop '
'looks up <code>list.append</code> and makes a Python-level method call on <strong>every iteration</strong>. '
'A comprehension compiles to a specialized <code>LIST_APPEND</code> bytecode that skips that lookup and runs '
'the collect loop at C speed.</div>'
'<div class="code-block">'
'<span class="cc"># same result, two ways</span><br>'
'out = []<br>'
'<span class="ck">for</span> x <span class="ck">in</span> <span class="cm">range</span>(<span class="cn">1_000_000</span>): out.<span class="cm">append</span>(x*x)   <span class="cc"># attribute lookup + call each time</span><br>'
'out = [x*x <span class="ck">for</span> x <span class="ck">in</span> <span class="cm">range</span>(<span class="cn">1_000_000</span>)]        <span class="cc"># specialized bytecode</span></div>'
'<div class="output-block">append-loop  :   627.5 ms<br>comprehension:   518.6 ms   &lt;- faster, and one line</div>'
'<div class="why-box"><strong>Why it matters (2A callback):</strong> this is the flip side of 2A\'s '
'"never <code>result = result + [x]</code> in a loop" rule. The append-loop is already O(n); the '
'comprehension keeps O(n) but shaves the per-iteration overhead (here ~1.2×; often up to ~2× for heavier '
'bodies). The bigger win is <strong>readability</strong> — intent in one line. It is <em>not</em> a reason to '
'cram complex logic in; see 1.7.</div>'
)

# ── 1.4 nested loops / flatten ─────────────────────────────────────────
md(
'<h3 class="sub">🔹 1.4 &nbsp;Multiple <code>for</code> clauses — flattening</h3>'
'<div class="theory-box">A comprehension can have more than one <code>for</code>. They read '
'<strong>left-to-right as nested loops</strong> — the leftmost <code>for</code> is the outer loop.</div>'
'<div class="code-block">'
'matrix = [[<span class="cn">1</span>, <span class="cn">2</span>], [<span class="cn">3</span>, <span class="cn">4</span>]]<br>'
'[x <span class="ck">for</span> row <span class="ck">in</span> matrix <span class="ck">for</span> x <span class="ck">in</span> row]   <span class="cc"># flatten one level -> [1, 2, 3, 4]</span></div>'
'<div class="output-block">[1, 2, 3, 4]</div>'
'<div class="warn-box">⚠ <strong>Order gotcha:</strong> the clauses must be in loop order — outer first. '
'Writing <code>[x for x in row for row in matrix]</code> raises <code>NameError: name \'row\' is not '
'defined</code>, because <code>row</code> is used before its own <code>for</code> introduces it.</div>'
)

# ── 1.5 nested comprehensions / 2D ─────────────────────────────────────
md(
'<h3 class="sub">🔹 1.5 &nbsp;Nested comprehensions — building &amp; transposing 2D</h3>'
'<div class="theory-box">A comprehension whose <em>expression</em> is itself a comprehension builds a 2D '
'structure. This is the <strong>correct</strong> way to make a grid — each row is a fresh list.</div>'
'<div class="code-block">'
'[[<span class="cn">0</span>]*<span class="cn">3</span> <span class="ck">for</span> _ <span class="ck">in</span> <span class="cm">range</span>(<span class="cn">2</span>)]              <span class="cc"># [[0,0,0], [0,0,0]] - distinct rows</span><br>'
'<br>'
'm = [[<span class="cn">1</span>, <span class="cn">2</span>, <span class="cn">3</span>], [<span class="cn">4</span>, <span class="cn">5</span>, <span class="cn">6</span>]]<br>'
'[[row[i] <span class="ck">for</span> row <span class="ck">in</span> m] <span class="ck">for</span> i <span class="ck">in</span> <span class="cm">range</span>(<span class="cn">3</span>)]   <span class="cc"># transpose -> [[1,4],[2,5],[3,6]]</span></div>'
'<div class="output-block">[[0, 0, 0], [0, 0, 0]]<br>[[1, 4], [2, 5], [3, 6]]</div>'
'<div class="why-box"><strong>Why it matters (S1 / 2A callback):</strong> the comprehension form '
'<code>[[0]*3 for _ in range(2)]</code> creates a <strong>new inner list each iteration</strong> — unlike '
'<code>[[0]*3]*2</code>, which aliases one row three times (the matrix trap). Always build grids with a '
'comprehension.</div>'
)

# ── 1.6 scope + 1.7 readability + takeaways ────────────────────────────
md(
'<h3 class="sub">🔹 1.6 &nbsp;The loop variable is scoped to the comprehension (Py3)</h3>'
'<div class="code-block">'
'squares = [i <span class="ck">for</span> i <span class="ck">in</span> <span class="cm">range</span>(<span class="cn">3</span>)]<br>'
'<span class="cm">print</span>(i)   <span class="cc"># NameError: name \'i\' is not defined</span></div>'
'<div class="output-block">NameError: name \'i\' is not defined</div>'
'<div class="why-box"><strong>Why it matters:</strong> in Python 3 the comprehension has its own scope — '
'<code>i</code> does not leak into the surrounding code (it did in Python 2, a notorious bug source). Clean, '
'but don\'t rely on a comprehension variable existing afterward.</div>'
'<h3 class="sub">🔹 1.7 &nbsp;Readability rule — keep them simple</h3>'
'<div class="note-box">💡 A comprehension should read in one breath. One <code>for</code>, maybe one '
'<code>if</code>, a simple expression. The moment you need multiple conditions, deep nesting (&gt;2 levels), '
'or side effects, switch to an explicit loop — clarity beats cleverness. A comprehension you have to decode '
'is worse than the loop it replaced.</div>'
'<hr class="divider">'
'<div style="background:#1e1e2e; border-left:4px solid #cba6f7; padding:16px 20px; border-radius:8px; '
'font-family:monospace; color:#cdd6f4;">'
'<h4 style="color:#cba6f7; margin:0 0 12px 0;">🔑 Chunk A — Key Takeaways</h4>'
'<ul style="margin:0; padding-left:20px; line-height:2.1">'
'<li><code>[expr for x in xs if cond]</code> = map + filter in one declarative pass (SQL <code>SELECT … WHERE</code>)</li>'
'<li><code>a if c else b</code> <strong>before</strong> <code>for</code> = transform; bare <code>if</code> <strong>after</strong> = filter</li>'
'<li>Faster than an append-loop (specialized bytecode) — but readability is the real win</li>'
'<li>Multiple <code>for</code>s read outer-to-inner; nested comprehensions build 2D <strong>without</strong> the aliasing trap</li>'
'<li>The loop variable does not leak (Py3); keep comprehensions simple or use a loop</li>'
'</ul></div>'
)

# ══════════════════════════ CHUNK B ══════════════════════════
md(
'<div class="chunk-badge">Part 1 · Chunk B — Dict &amp; Set Comprehensions</div>'
'<h3 class="sub">🔹 1.8 &nbsp;Dict comprehension — build, filter, invert</h3>'
'<div class="theory-box">Same idea, a <code>key: value</code> pair as the expression: '
'<code>{k: v for ... }</code>. Three staple patterns (2D callback): build a mapping, filter pairs, or '
'invert keys↔values.</div>'
'<div class="code-block">'
'{x: x*x <span class="ck">for</span> x <span class="ck">in</span> <span class="cm">range</span>(<span class="cn">5</span>)}                    <span class="cc"># build:  {0:0, 1:1, 2:4, 3:9, 4:16}</span><br>'
'prices = {<span class="cs">"apple"</span>:<span class="cn">3</span>, <span class="cs">"banana"</span>:<span class="cn">1</span>, <span class="cs">"cherry"</span>:<span class="cn">5</span>}<br>'
'{k: v <span class="ck">for</span> k, v <span class="ck">in</span> prices.<span class="cm">items</span>() <span class="ck">if</span> v &gt; <span class="cn">2</span>}   <span class="cc"># filter: {\'apple\':3, \'cherry\':5}</span><br>'
'{v: k <span class="ck">for</span> k, v <span class="ck">in</span> prices.<span class="cm">items</span>()}          <span class="cc"># invert: {3:\'apple\', 1:\'banana\', 5:\'cherry\'}</span><br>'
'{k: v <span class="ck">for</span> k, v <span class="ck">in</span> <span class="cm">zip</span>([<span class="cs">"a"</span>,<span class="cs">"b"</span>,<span class="cs">"c"</span>], [<span class="cn">1</span>,<span class="cn">2</span>,<span class="cn">3</span>])}  <span class="cc"># from two lists</span></div>'
'<div class="output-block">{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}<br>{\'apple\': 3, \'cherry\': 5}<br>{3: \'apple\', 1: \'banana\', 5: \'cherry\'}<br>{\'a\': 1, \'b\': 2, \'c\': 3}</div>'
'<div class="why-box"><strong>Why it matters (2D callback):</strong> inverting is <em>lossy</em> when values '
'aren\'t unique — duplicate values collapse because keys must be unique (last wins). And use a comprehension, '
'<strong>not</strong> <code>dict.fromkeys(keys, [])</code>, when the value is mutable — <code>fromkeys</code> '
'shares one list across all keys (2D Edge 4).</div>'
'<h3 class="sub">🔹 1.9 &nbsp;Set comprehension — dedup + transform in one pass</h3>'
'<div class="theory-box"><code>{expr for ...}</code> builds a set — duplicates collapse automatically '
'(2C). Great for "unique transformed values."</div>'
'<div class="code-block">'
'{x % <span class="cn">3</span> <span class="ck">for</span> x <span class="ck">in</span> <span class="cm">range</span>(<span class="cn">10</span>)}                 <span class="cc"># {0, 1, 2} - only distinct remainders</span><br>'
'{<span class="cm">len</span>(w) <span class="ck">for</span> w <span class="ck">in</span> [<span class="cs">"a"</span>,<span class="cs">"bb"</span>,<span class="cs">"cc"</span>,<span class="cs">"ddd"</span>]}   <span class="cc"># {1, 2, 3} - unique lengths</span></div>'
'<div class="output-block">{0, 1, 2}<br>{1, 2, 3}</div>'
'<div class="note-box">💡 <strong>The <code>{}</code> disambiguation:</strong> <code>{}</code> is an empty '
'<em>dict</em>; an empty set is <code>set()</code> (2C). But <code>{k: v for …}</code> is a dict comp and '
'<code>{expr for …}</code> is a set comp — the colon decides which.</div>'
'<hr class="divider">'
'<div style="background:#1e1e2e; border-left:4px solid #cba6f7; padding:14px 18px; border-radius:8px; font-family:monospace; color:#cdd6f4;">'
'<h4 style="color:#cba6f7; margin:0 0 10px 0;">🔑 Chunk B — Key Takeaways</h4>'
'<ul style="margin:0; padding-left:20px; line-height:2.0">'
'<li>Dict comp <code>{k: v for …}</code> — build / filter / invert (invert is lossy on duplicate values)</li>'
'<li>Set comp <code>{expr for …}</code> — dedup + transform in one pass</li>'
'<li>Colon distinguishes dict comp from set comp; <code>{}</code> is still an empty dict</li>'
'</ul></div>'
)

# ══════════════════════════ CHUNK C ══════════════════════════
md(
'<div class="chunk-badge">Part 1 · Chunk C — Generator Expressions &amp; Lazy Evaluation</div>'
'<h3 class="sub">🔹 1.11 &nbsp;A genexpr is a comprehension with <code>()</code> — and it\'s lazy</h3>'
'<div class="theory-box">Swap the brackets for parentheses and you get a <strong>generator '
'expression</strong>: same syntax, but it returns a <em>generator object</em> instead of a list. Nothing is '
'computed until you iterate it — values are produced <strong>on demand</strong>.</div>'
'<div class="code-block">'
'g = (x*x <span class="ck">for</span> x <span class="ck">in</span> <span class="cm">range</span>(<span class="cn">5</span>))   <span class="cc"># a generator, NOT a list</span><br>'
'<span class="cm">type</span>(g)                          <span class="cc"># &lt;class \'generator\'&gt;</span><br>'
'<span class="cm">list</span>(g)                          <span class="cc"># [0, 1, 4, 9, 16] - materialize on demand</span></div>'
'<div class="output-block">generator<br>[0, 1, 4, 9, 16]</div>'
'<h3 class="sub">🔹 1.12 &nbsp;Eager vs lazy — the memory story</h3>'
'<div class="mut-grid">'
'<div class="mut-card mc-mut"><div class="mc-title">📦 List comp <code>[ ]</code> — eager</div>'
'<div class="mc-body">builds ALL elements now<br>memory O(n)<br>reusable, indexable, len()</div></div>'
'<div class="mut-card mc-imm"><div class="mc-title">🔁 Genexpr <code>( )</code> — lazy</div>'
'<div class="mc-body">yields one at a time<br>memory O(1)<br>one-shot, no index / len</div></div>'
'</div>'
'<div class="code-block">'
'<span class="ck">import</span> sys<br>'
'sys.<span class="cm">getsizeof</span>([x <span class="ck">for</span> x <span class="ck">in</span> <span class="cm">range</span>(<span class="cn">10000</span>)])   <span class="cc"># ~85,176 bytes</span><br>'
'sys.<span class="cm">getsizeof</span>((x <span class="ck">for</span> x <span class="ck">in</span> <span class="cm">range</span>(<span class="cn">10000</span>)))   <span class="cc"># 192 bytes</span></div>'
'<div class="output-block">size list :  85176 bytes<br>size gen  :    192 bytes   &lt;- constant, regardless of length</div>'
'<div class="why-box"><strong>Why it matters:</strong> a list comp holds every element; a genexpr holds a '
'tiny bit of state and computes each value as asked. For a huge (or infinite) sequence you feed straight into '
'an aggregate, the genexpr uses near-zero memory.</div>'
'<h3 class="sub">🔹 1.13 &nbsp;One-shot exhaustion</h3>'
'<div class="code-block">'
'g = (x <span class="ck">for</span> x <span class="ck">in</span> <span class="cm">range</span>(<span class="cn">3</span>))<br>'
'<span class="cm">list</span>(g)   <span class="cc"># [0, 1, 2]</span><br>'
'<span class="cm">list</span>(g)   <span class="cc"># []  &lt;- already exhausted; generators run ONCE</span></div>'
'<div class="output-block">[0, 1, 2]<br>[]</div>'
'<div class="warn-box">⚠ A generator is consumed as you iterate it. After exhaustion it yields nothing — a '
'silent empty on the second pass. If you need to iterate twice, use a list (or rebuild the generator).</div>'
'<h3 class="sub">🔹 1.14 &nbsp;Genexpr inside a call — no extra parentheses; short-circuiting</h3>'
'<div class="code-block">'
'<span class="cm">sum</span>(x*x <span class="ck">for</span> x <span class="ck">in</span> <span class="cm">range</span>(<span class="cn">1000</span>))   <span class="cc"># 332833500 - no double parens needed</span><br>'
'<span class="cm">any</span>(x &gt; <span class="cn">5</span> <span class="ck">for</span> x <span class="ck">in</span> <span class="cm">range</span>(<span class="cn">100</span>))  <span class="cc"># True - STOPS at 6, doesn\'t scan all 100</span></div>'
'<div class="output-block">332833500<br>True</div>'
'<div class="note-box">💡 When a genexpr is the sole argument to a function, drop the extra parens: '
'<code>sum(x*x for x in xs)</code>. With <code>any</code>/<code>all</code> the laziness gives '
'<strong>short-circuiting</strong> — it stops the moment the answer is known.</div>'
'<h3 class="sub">🔹 1.15 &nbsp;Pipelines — chain generators, materialize nothing in between</h3>'
'<div class="code-block">'
'nums = <span class="cm">range</span>(<span class="cn">1</span>, <span class="cn">11</span>)<br>'
'evens = (x <span class="ck">for</span> x <span class="ck">in</span> nums <span class="ck">if</span> x % <span class="cn">2</span> == <span class="cn">0</span>)   <span class="cc"># lazy stage 1</span><br>'
'squares = (x*x <span class="ck">for</span> x <span class="ck">in</span> evens)          <span class="cc"># lazy stage 2</span><br>'
'<span class="cm">sum</span>(squares)                              <span class="cc"># 220 - work happens only here</span></div>'
'<div class="output-block">220</div>'
'<div class="note-box">💡 Each stage pulls one value from the previous on demand — no intermediate list is '
'ever built. This is how you stream large data (files, logs) through transforms in constant memory.</div>'
'<hr class="divider">'
'<div style="background:#1e1e2e; border-left:4px solid #cba6f7; padding:14px 18px; border-radius:8px; font-family:monospace; color:#cdd6f4;">'
'<h4 style="color:#cba6f7; margin:0 0 10px 0;">🔑 Chunk C — Key Takeaways</h4>'
'<ul style="margin:0; padding-left:20px; line-height:2.0">'
'<li><code>(expr for …)</code> is a lazy generator — O(1) memory vs a list comp\'s O(n)</li>'
'<li>One-shot: a generator is exhausted after one pass (silent empty afterward)</li>'
'<li>Drop extra parens in <code>sum(... for ...)</code>; <code>any</code>/<code>all</code> short-circuit</li>'
'<li>Chained generators form a constant-memory streaming pipeline</li>'
'</ul></div>'
)

# ══════════════════════════ CHUNK D ══════════════════════════
md(
'<div class="chunk-badge">Part 1 · Chunk D — Generator Functions (yield)</div>'
'<h3 class="sub">🔹 1.16 &nbsp;<code>yield</code> — a function that produces a stream</h3>'
'<div class="theory-box">Any function containing <code>yield</code> is a <strong>generator function</strong>. '
'Calling it doesn\'t run the body — it returns a generator. Each <code>next()</code> runs to the next '
'<code>yield</code>, hands back the value, and <strong>suspends</strong>, keeping all local state until '
'resumed.</div>'
'<div class="code-block">'
'<span class="ck">def</span> <span class="cm">countdown</span>(n):<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">while</span> n &gt; <span class="cn">0</span>:<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">yield</span> n      <span class="cc"># emit, then PAUSE here until next()</span><br>'
'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;n -= <span class="cn">1</span><br>'
'<br>'
'<span class="cm">list</span>(<span class="cm">countdown</span>(<span class="cn">3</span>))   <span class="cc"># [3, 2, 1]</span></div>'
'<div class="output-block">[3, 2, 1]</div>'
'<div class="why-box"><strong>Why it matters:</strong> unlike a <code>return</code> (which ends the function), '
'<code>yield</code> pauses it. State (<code>n</code> here) survives between values — that\'s what lets a '
'generator model a stream or an ongoing process without holding everything in memory.</div>'
'<h3 class="sub">🔹 1.17 &nbsp;Infinite generators — lazy makes the impossible cheap</h3>'
'<div class="code-block">'
'<span class="ck">import</span> itertools<br>'
'<span class="ck">def</span> <span class="cm">naturals</span>():<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;n = <span class="cn">0</span><br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">while</span> <span class="ck">True</span>:            <span class="cc"># never ends...</span><br>'
'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">yield</span> n; n += <span class="cn">1</span><br>'
'<br>'
'<span class="cm">list</span>(itertools.<span class="cm">islice</span>(<span class="cm">naturals</span>(), <span class="cn">5</span>))   <span class="cc"># [0, 1, 2, 3, 4] - take just 5</span></div>'
'<div class="output-block">[0, 1, 2, 3, 4]</div>'
'<div class="note-box">💡 An infinite generator is fine because nothing is computed until pulled. '
'<code>itertools.islice</code> takes a finite slice. A list version would never finish.</div>'
'<h3 class="sub">🔹 1.18 &nbsp;<code>yield from</code> — delegate to a sub-iterable</h3>'
'<div class="code-block">'
'<span class="ck">def</span> <span class="cm">chain2</span>(a, b):<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">yield from</span> a      <span class="cc"># re-yield everything from a</span><br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">yield from</span> b<br>'
'<br>'
'<span class="cm">list</span>(<span class="cm">chain2</span>([<span class="cn">1</span>,<span class="cn">2</span>], [<span class="cn">3</span>,<span class="cn">4</span>]))   <span class="cc"># [1, 2, 3, 4]</span></div>'
'<div class="output-block">[1, 2, 3, 4]</div>'
'<div class="note-box">💡 <code>yield from iterable</code> is shorthand for "yield each item of that iterable" — '
'the clean way to flatten or compose generators.</div>'
'<h3 class="sub">🔹 1.19 &nbsp;Generators <em>are</em> iterators (bridge to Session 8)</h3>'
'<div class="theory-box">A generator implements the iterator protocol for free — it works with <code>for</code>, '
'<code>next()</code>, <code>sum()</code>, <code>list()</code>, unpacking, everything that consumes an '
'iterable. Session 8 opens the hood on <code>__iter__</code>/<code>__next__</code>; generators are the '
'ergonomic way to write one without a class.</div>'
'<div class="code-block">'
'<span class="ck">def</span> <span class="cm">gen</span>():<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">yield</span> <span class="cn">1</span>; <span class="ck">yield</span> <span class="cn">2</span><br>'
'g = <span class="cm">gen</span>()<br>'
'<span class="cm">next</span>(g), <span class="cm">next</span>(g)   <span class="cc"># 1, 2 ... then next(g) raises StopIteration</span></div>'
'<div class="output-block">1 2<br>StopIteration after the last yield</div>'
# ── 2. Example ──
'<div class="ex-header"><h2>2. Example</h2></div>'
'<div class="ex-block"><div class="ex-title"><span class="ex-badge">Ex 1</span> Dict comp — word→length map, then filter</div>'
'<div class="code-block">'
'words = [<span class="cs">"hi"</span>, <span class="cs">"bye"</span>, <span class="cs">"ok"</span>]<br>'
'{w: <span class="cm">len</span>(w) <span class="ck">for</span> w <span class="ck">in</span> words}                 <span class="cc"># {\'hi\':2, \'bye\':3, \'ok\':2}</span><br>'
'{w: <span class="cm">len</span>(w) <span class="ck">for</span> w <span class="ck">in</span> words <span class="ck">if</span> <span class="cm">len</span>(w) &gt; <span class="cn">2</span>}   <span class="cc"># {\'bye\':3}</span></div>'
'<div class="output-block">{\'hi\': 2, \'bye\': 3, \'ok\': 2}<br>{\'bye\': 3}</div></div>'
'<div class="ex-block"><div class="ex-title"><span class="ex-badge">Ex 2</span> Set comp — dedup normalized tokens</div>'
'<div class="code-block">{t.<span class="cm">lower</span>() <span class="ck">for</span> t <span class="ck">in</span> [<span class="cs">"Cat"</span>,<span class="cs">"cat"</span>,<span class="cs">"DOG"</span>,<span class="cs">"dog"</span>]}   <span class="cc"># {\'cat\', \'dog\'}</span></div>'
'<div class="output-block">{\'cat\', \'dog\'}</div>'
'<div class="note-box">Normalize (lower) + dedup in one pass — the vocabulary-building step (2C/2D), now a one-liner.</div></div>'
'<div class="ex-block"><div class="ex-title"><span class="ex-badge">Ex 3</span> Lazy pipeline — sum of squares of evens (memory-light)</div>'
'<div class="code-block"><span class="cm">sum</span>(x*x <span class="ck">for</span> x <span class="ck">in</span> <span class="cm">range</span>(<span class="cn">1</span>, <span class="cn">11</span>) <span class="ck">if</span> x % <span class="cn">2</span> == <span class="cn">0</span>)   <span class="cc"># 4+16+36+64+100 = 220</span></div>'
'<div class="output-block">220</div></div>'
'<div class="ex-block"><div class="ex-title"><span class="ex-badge">Ex 4</span> Streaming generator — process lines lazily</div>'
'<div class="code-block">'
'<span class="ck">def</span> <span class="cm">process</span>(lines):<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">for</span> ln <span class="ck">in</span> lines:<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;s = ln.<span class="cm">strip</span>()<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">if</span> s: <span class="ck">yield</span> s.<span class="cm">upper</span>()   <span class="cc"># skip blanks, transform</span><br>'
'<span class="cm">list</span>(<span class="cm">process</span>([<span class="cs">"  a "</span>, <span class="cs">""</span>, <span class="cs">"b"</span>]))            <span class="cc"># [\'A\', \'B\']</span></div>'
'<div class="output-block">[\'A\', \'B\']</div>'
'<div class="note-box">This is the file-processing shape: yield cleaned records one at a time so a huge file never loads fully into memory.</div></div>'
# ── 3. Edge Cases ──
'<div class="warn-header"><h2>3. Edge Cases</h2></div>'
'<p style="color:#cdd6f4;font-family:\'Segoe UI\',sans-serif;font-size:0.92em;margin:0 0 12px 0">All outputs verified by running.</p>'
'<div class="edge-block"><div class="edge-title"><span class="edge-badge">Edge 1</span> A generator is one-shot</div>'
'<div class="code-block">g = (x <span class="ck">for</span> x <span class="ck">in</span> <span class="cm">range</span>(<span class="cn">3</span>))<br><span class="cm">list</span>(g), <span class="cm">list</span>(g)   <span class="cc"># ([0, 1, 2], [])</span></div>'
'<div class="output-block">([0, 1, 2], [])</div>'
'<div class="why-box"><strong>Why it matters:</strong> the second consumption sees an exhausted generator — '
'a silent empty. Passing a generator to two consumers, or looping it twice, drops data. Use a list if you '
'need to reuse.</div></div>'
'<div class="edge-block"><div class="edge-title"><span class="edge-badge">Edge 2</span> <code>{}</code> is a dict, not a set</div>'
'<div class="code-block"><span class="cm">type</span>({}).__name__       <span class="cc"># \'dict\'</span><br><span class="cm">type</span>(<span class="cm">set</span>()).__name__    <span class="cc"># \'set\'  - the only empty-set literal</span><br>{x <span class="ck">for</span> x <span class="ck">in</span> <span class="cm">range</span>(<span class="cn">3</span>)}      <span class="cc"># {0, 1, 2}  - a set comp, though</span></div>'
'<div class="output-block">dict<br>set<br>{0, 1, 2}</div>'
'<div class="why-box"><strong>Why it matters (2C callback):</strong> <code>{}</code> alone is an empty dict; '
'only a comprehension body or elements make <code>{}</code> a set. Empty set is always <code>set()</code>.</div></div>'
'<div class="edge-block"><div class="edge-title"><span class="edge-badge">Edge 3</span> A generator has no <code>len()</code> and no indexing</div>'
'<div class="code-block"><span class="cm">len</span>(x <span class="ck">for</span> x <span class="ck">in</span> <span class="cm">range</span>(<span class="cn">3</span>))   <span class="cc"># TypeError: object of type \'generator\' has no len()</span></div>'
'<div class="output-block">TypeError: object of type \'generator\' has no len()</div>'
'<div class="why-box"><strong>Why it matters:</strong> a generator doesn\'t know its length and can\'t be '
'indexed (<code>g[0]</code> fails) — it hasn\'t produced anything yet. Materialize to a list if you need '
'<code>len</code>/<code>[]</code>.</div></div>'
'<div class="edge-block"><div class="edge-title"><span class="edge-badge">Edge 4</span> Dict comp with duplicate keys — last wins</div>'
'<div class="code-block">{k: v <span class="ck">for</span> k, v <span class="ck">in</span> [(<span class="cs">"a"</span>, <span class="cn">1</span>), (<span class="cs">"a"</span>, <span class="cn">2</span>)]}   <span class="cc"># {\'a\': 2}  - first value lost silently</span></div>'
'<div class="output-block">{\'a\': 2}</div>'
'<div class="why-box"><strong>Why it matters (2D callback):</strong> keys are unique, so a repeated key '
'overwrites — data lost with no warning. Same reason inverting a dict with non-unique values is lossy.</div></div>'
'<div class="edge-block"><div class="edge-title"><span class="edge-badge">Edge 5</span> A genexpr evaluates its outermost iterable eagerly</div>'
'<div class="code-block">'
'<span class="ck">def</span> <span class="cm">side</span>():<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="cm">print</span>(<span class="cs">"outer evaluated NOW"</span>); <span class="ck">return</span> [<span class="cn">1</span>,<span class="cn">2</span>,<span class="cn">3</span>]<br>'
'g = (x <span class="ck">for</span> x <span class="ck">in</span> <span class="cm">side</span>())   <span class="cc"># prints immediately - outer iterable is eager</span><br>'
'<span class="cm">list</span>(g)                        <span class="cc"># [1, 2, 3] - body deferred until now</span></div>'
'<div class="output-block">outer evaluated NOW<br>[1, 2, 3]</div>'
'<div class="why-box"><strong>Why it matters:</strong> only the <em>first</em> <code>for</code>\'s iterable '
'runs when the genexpr is created; everything else is lazy. A subtle source of "why did that run early?" when '
'the outer iterable has side effects.</div></div>'
'<hr class="divider">'
'<div class="info-box">📎 <strong>End of Part 1</strong> (Chunks A–D: list / dict / set comprehensions, '
'generator expressions, lazy evaluation, <code>yield</code> functions, 4 examples, 5 edge cases). '
'<strong>Part 2</strong> — Golden Rules → Common Traps → Exercise. <strong>Part 3</strong> — ML Real-World → '
'Interview Q&amp;A → Summary Table.</div>'
)

# ══════════════════════════ PART 2 ══════════════════════════
md(
'<div class="info-box"><strong>Part 2:</strong> Golden Rules → Common Traps → Exercise</div>'
'<div class="part-header"><h2>4. Golden Rules</h2></div>'
'<div class="rule-block"><div class="rule-title"><span class="rule-badge">Rule 1</span> Prefer a comprehension over an append-loop for building a collection.</div>'
'<div class="body-txt">Cleaner and faster — but keep it to one <code>for</code> and maybe one <code>if</code>.</div></div>'
'<div class="rule-block"><div class="rule-title"><span class="rule-badge">Rule 2</span> Reach for a generator when you iterate once, feed an aggregate, or the data is huge/infinite.</div>'
'<div class="body-txt"><code>sum</code>/<code>any</code>/<code>all</code>/<code>max</code>/<code>join</code> over <code>(… for …)</code> = O(1) memory.</div></div>'
'<div class="rule-block"><div class="rule-title"><span class="rule-badge">Rule 3</span> Use a list comp when you need to reuse, index, <code>len()</code>, or iterate twice.</div>'
'<div class="body-txt">A generator is one-shot; a list is reusable. Pick by access pattern.</div></div>'
'<div class="rule-block"><div class="rule-title"><span class="rule-badge">Rule 4</span> Ternary <em>before</em> <code>for</code> transforms; bare <code>if</code> <em>after</em> filters.</div>'
'<div class="body-txt"><code>[a if c else b for x in xs]</code> keeps length; <code>[x for x in xs if c]</code> shrinks it.</div></div>'
'<div class="rule-block"><div class="rule-title"><span class="rule-badge">Rule 5</span> Keep comprehensions simple — deep nesting or multiple conditions → explicit loop.</div>'
'<div class="body-txt">Clarity beats cleverness; a comprehension you must decode is worse than a loop.</div></div>'
'<div class="rule-block"><div class="rule-title"><span class="rule-badge">Rule 6</span> Build 2D with a comprehension, never <code>[[…]*n]*m</code>.</div>'
'<div class="body-txt"><code>[[0]*3 for _ in range(m)]</code> makes distinct rows; <code>*</code> aliases one row (S1/2A trap).</div></div>'
'<div class="rule-block"><div class="rule-title"><span class="rule-badge">Rule 7</span> A generator is exhausted after one pass — materialize with <code>list()</code> to reuse.</div>'
'<div class="body-txt">Iterating it twice silently yields nothing the second time.</div></div>'
'<div class="rule-block"><div class="rule-title"><span class="rule-badge">Rule 8</span> Drop redundant parens: <code>sum(x for x in xs)</code>, not <code>sum((x for x in xs))</code>.</div>'
'<div class="body-txt">A lone genexpr argument needs no extra parentheses.</div></div>'
)

md(
'<div class="trap-header"><h2>5. Common Traps</h2></div>'
'<div class="trap-block"><div class="trap-title"><span class="trap-badge">Trap 1</span> Reusing an exhausted generator.</div>'
'<div class="body-txt">Second loop/consumer sees nothing. <strong>Fix:</strong> <code>list()</code> it if you need it more than once.</div></div>'
'<div class="trap-block"><div class="trap-title"><span class="trap-badge">Trap 2</span> Ternary-vs-filter confusion.</div>'
'<div class="body-txt">Putting the <code>if</code> in the wrong place either drops elements you meant to keep, or vice versa. Position = job.</div></div>'
'<div class="trap-block"><div class="trap-title"><span class="trap-badge">Trap 3</span> Duplicate keys in a dict comp.</div>'
'<div class="body-txt">Last value silently wins → data lost. Watch inverts and pair-lists with repeats.</div></div>'
'<div class="trap-block"><div class="trap-title"><span class="trap-badge">Trap 4</span> Over-nested comprehension.</div>'
'<div class="body-txt">Two+ nested <code>for</code>s with conditions become unreadable. <strong>Fix:</strong> a plain loop.</div></div>'
'<div class="trap-block"><div class="trap-title"><span class="trap-badge">Trap 5</span> <code>[[0]*3]*3</code> aliasing when you meant distinct rows.</div>'
'<div class="body-txt">Use the nested comprehension form. Setting one cell changes a whole "column" otherwise.</div></div>'
'<div class="trap-block"><div class="trap-title"><span class="trap-badge">Trap 6</span> Expecting <code>len()</code> / indexing on a generator.</div>'
'<div class="body-txt"><code>len(gen)</code> and <code>gen[0]</code> raise <code>TypeError</code>. Materialize first if you need them.</div></div>'
)

md(
'<div class="part-header"><h2>6. Exercise</h2></div>'
'<div class="body-txt" style="margin-bottom:10px">Twelve problems, easy → hard. Attempt each in <code>01_comprehensions.ipynb</code>; hints only here — full solutions in <code>solutions.ipynb</code>.</div>'
'<div class="exr-block"><div class="exr-title"><span class="cc-badge badge-easy">Easy</span> E1 — Squares of even numbers 0–20 (list comp)</div><div class="hint-box">💡 <code>[x*x for x in range(21) if x%2==0]</code>.</div></div>'
'<div class="exr-block"><div class="exr-title"><span class="cc-badge badge-easy">Easy</span> E2 — Dict comp: <code>n → n²</code> for 1–5</div><div class="hint-box">💡 <code>{n: n**2 for n in range(1,6)}</code>.</div></div>'
'<div class="exr-block"><div class="exr-title"><span class="cc-badge badge-easy">Easy</span> E3 — Set of unique word lengths</div><div class="hint-box">💡 <code>{len(w) for w in words}</code>.</div></div>'
'<div class="exr-block"><div class="exr-title"><span class="cc-badge badge-easy">Easy</span> E4 — Flatten a 2D list</div><div class="hint-box">💡 <code>[x for row in m for x in row]</code> — outer <code>for</code> first.</div></div>'
'<div class="exr-block"><div class="exr-title"><span class="cc-badge badge-med">Medium</span> E5 — Filter dict comp: keep scores ≥ 50</div><div class="hint-box">💡 <code>{name: s for name, s in pairs if s >= 50}</code>.</div></div>'
'<div class="exr-block"><div class="exr-title"><span class="cc-badge badge-med">Medium</span> E6 — Invert a dict (unique values)</div><div class="hint-box">💡 <code>{v: k for k, v in d.items()}</code> — remember it\'s lossy if values repeat.</div></div>'
'<div class="exr-block"><div class="exr-title"><span class="cc-badge badge-med">Medium</span> E7 — Transpose a matrix (nested comp)</div><div class="hint-box">💡 <code>[[row[i] for row in m] for i in range(cols)]</code>.</div></div>'
'<div class="exr-block"><div class="exr-title"><span class="cc-badge badge-med">Medium</span> E8 — Sum of squares of odd numbers 1–100 (genexpr, memory-light)</div><div class="hint-box">💡 <code>sum(x*x for x in range(1,101) if x%2)</code> — no list built.</div></div>'
'<div class="exr-block"><div class="exr-title"><span class="cc-badge badge-med">Medium</span> E9 — Any word longer than 10 chars? (short-circuit)</div><div class="hint-box">💡 <code>any(len(w) > 10 for w in words)</code> — stops at the first match.</div></div>'
'<div class="exr-block"><div class="exr-title"><span class="cc-badge badge-hard">Hard</span> E10 — Fibonacci generator</div><div class="hint-box">💡 <code>yield a</code> then <code>a, b = b, a+b</code> in a <code>while True</code>; take with <code>itertools.islice</code>.</div></div>'
'<div class="exr-block"><div class="exr-title"><span class="cc-badge badge-hard">Hard</span> E11 — Streaming pipeline: total length of non-empty lines</div><div class="hint-box">💡 <code>sum(len(ln.strip()) for ln in lines if ln.strip())</code>.</div></div>'
'<div class="exr-block"><div class="exr-title"><span class="cc-badge badge-hard">Hard</span> E12 — Recursively flatten arbitrary nesting (generator)</div><div class="hint-box">💡 Generator + <code>yield from flatten(x)</code> when <code>isinstance(x, list)</code>, else <code>yield x</code>.</div></div>'
)

# ══════════════════════════ PART 3 ══════════════════════════
md(
'<div class="info-box"><strong>Part 3:</strong> ML Real-World → Interview Q&amp;A → Code Challenges → Summary</div>'
'<div class="ml-header"><h2>7. ML Real-World Connection</h2></div>'
'<div class="ml-block"><div class="ml-title"><span class="ml-badge">ML 1</span> Feature transforms &amp; row filtering</div>'
'<div class="body-txt"><code>[normalize(x) for x in features]</code>, <code>[r for r in rows if r["label"] is not None]</code> — comprehensions are the everyday transform/filter of a preprocessing step.</div></div>'
'<div class="ml-block"><div class="ml-title"><span class="ml-badge">ML 2</span> Vocabulary / index maps (dict comp)</div>'
'<div class="body-txt"><code>{tok: i for i, tok in enumerate(vocab)}</code> and its inverse — the tokenizer core (2C/2D), now a one-liner.</div></div>'
'<div class="ml-block"><div class="ml-title"><span class="ml-badge">ML 3</span> Lazy data loading — generators stream batches</div>'
'<div class="body-txt">A generator yields records/batches from a huge file or dataset without loading it all — the essence of a PyTorch <code>DataLoader</code> / streaming ingestion. Constant memory.</div></div>'
'<div class="ml-block"><div class="ml-title"><span class="ml-badge">ML 4</span> Genexprs feeding aggregates</div>'
'<div class="body-txt"><code>sum(loss for loss in batch_losses)</code>, <code>all(x is not None for x in features)</code> — compute a metric or validate a stream lazily, short-circuiting when possible.</div></div>'
'<div class="ml-block"><div class="ml-title"><span class="ml-badge">ML 5</span> Preprocessing pipelines (OpsRAG)</div>'
'<div class="body-txt">read → clean → tokenize → yield, chained generators in constant memory. Exactly the RAG ingestion pattern — documents flow through transforms without materializing intermediates.</div></div>'
)

md(
'<div class="interview-header"><h2>8. Interview Questions</h2></div>'
'<div class="sub-header"><h3>8a — Conceptual Q&amp;A</h3></div>'
'<div class="qa-block"><div class="qa-q"><span class="q-num">1</span> List comprehension vs generator expression?</div><div class="qa-a"><code>[…]</code> builds the whole list eagerly (O(n) memory, reusable); <code>(…)</code> is a lazy generator (O(1) memory, one-shot).</div></div>'
'<div class="qa-block"><div class="qa-q"><span class="q-num">2</span> When choose a generator over a list?</div><div class="qa-a">Iterate once, feed an aggregate, or the data is huge/infinite. Use a list when you need reuse, indexing, or <code>len()</code>.</div></div>'
'<div class="qa-block"><div class="qa-q"><span class="q-num">3</span> Why is a comprehension faster than an append-loop?</div><div class="qa-a">Specialized <code>LIST_APPEND</code> bytecode avoids the per-iteration <code>list.append</code> attribute lookup + Python call; the collect loop runs at C speed.</div></div>'
'<div class="qa-block"><div class="qa-q"><span class="q-num">4</span> Ternary vs filter in a comprehension?</div><div class="qa-a"><code>a if c else b</code> before <code>for</code> transforms every element (length unchanged); bare <code>if</code> after <code>for</code> filters (drops elements).</div></div>'
'<div class="qa-block"><div class="qa-q"><span class="q-num">5</span> What is lazy evaluation and its benefit?</div><div class="qa-a">Values are produced on demand, not upfront. Benefit: constant memory and the ability to handle infinite/huge streams, with short-circuiting.</div></div>'
'<div class="qa-block"><div class="qa-q"><span class="q-num">6</span> What happens if you iterate a generator twice?</div><div class="qa-a">The second pass is empty — generators are one-shot. Materialize to a list to reuse.</div></div>'
'<div class="qa-block"><div class="qa-q"><span class="q-num">7</span> <code>yield</code> vs <code>return</code>?</div><div class="qa-a"><code>return</code> ends the function; <code>yield</code> emits a value and suspends, preserving local state to resume on the next <code>next()</code>.</div></div>'
'<div class="qa-block"><div class="qa-q"><span class="q-num">8</span> What is <code>yield from</code>?</div><div class="qa-a">Delegates to a sub-iterable — re-yields each of its items. The clean way to compose/flatten generators.</div></div>'
'<div class="qa-block"><div class="qa-q"><span class="q-num">9</span> Can you index or <code>len()</code> a generator?</div><div class="qa-a">No — it hasn\'t produced values yet and doesn\'t know its length. Both raise <code>TypeError</code>.</div></div>'
'<div class="qa-block"><div class="qa-q"><span class="q-num">10</span> When is inverting a dict lossy?</div><div class="qa-a">When values aren\'t unique — duplicate values collapse because keys must be unique (last wins).</div></div>'
'<div class="qa-block"><div class="qa-q"><span class="q-num">11</span> Correct way to build a 2D grid with a comprehension?</div><div class="qa-a"><code>[[0]*cols for _ in range(rows)]</code> — a fresh inner list per row, unlike <code>[[0]*cols]*rows</code> which aliases one row.</div></div>'
'<div class="qa-block"><div class="qa-q"><span class="q-num">12</span> Why does a genexpr use so much less memory than a list?</div><div class="qa-a">It stores only iteration state and computes each value on demand — it never holds all n elements at once (192 bytes vs ~85 KB for 10k ints).</div></div>'
)

md(
'<div class="sub-header"><h3>8b — Code Challenges (attempt, then expand the solution)</h3></div>'
'<div class="cc-block"><div class="cc-title"><span class="cc-badge badge-easy">Easy</span> C1 — List of the first n squares</div>'
'<details class="sol"><summary>Solution</summary><div class="code-block"><span class="ck">def</span> <span class="cm">squares</span>(n): <span class="ck">return</span> [x*x <span class="ck">for</span> x <span class="ck">in</span> <span class="cm">range</span>(n)]</div><div class="qa-a">A plain map comprehension. <code>squares(5)</code> → <code>[0, 1, 4, 9, 16]</code>.</div></details></div>'
'<div class="cc-block"><div class="cc-title"><span class="cc-badge badge-easy">Easy</span> C2 — Sum of even numbers (genexpr)</div>'
'<details class="sol"><summary>Solution</summary><div class="code-block"><span class="ck">def</span> <span class="cm">sum_evens</span>(nums): <span class="ck">return</span> <span class="cm">sum</span>(x <span class="ck">for</span> x <span class="ck">in</span> nums <span class="ck">if</span> x % <span class="cn">2</span> == <span class="cn">0</span>)</div><div class="qa-a">Genexpr into <code>sum</code> — no list built. <code>[1..6]</code> → <code>12</code>.</div></details></div>'
'<div class="cc-block"><div class="cc-title"><span class="cc-badge badge-med">Med</span> C3 — Invert a dict</div>'
'<details class="sol"><summary>Solution</summary><div class="code-block"><span class="ck">def</span> <span class="cm">invert</span>(d): <span class="ck">return</span> {v: k <span class="ck">for</span> k, v <span class="ck">in</span> d.<span class="cm">items</span>()}</div><div class="qa-a">Dict comp swapping key/value. Lossy if values repeat — group with <code>defaultdict(list)</code> then.</div></details></div>'
'<div class="cc-block"><div class="cc-title"><span class="cc-badge badge-med">Med</span> C4 — Batch a sequence into chunks of size n</div>'
'<div class="body-txt"><code>chunk([1,2,3,4,5,6,7], 3)</code> → <code>[1,2,3], [4,5,6], [7]</code> (last chunk partial).</div>'
'<details class="sol"><summary>Solution</summary><div class="code-block">'
'<span class="ck">def</span> <span class="cm">chunk</span>(seq, n):<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">for</span> i <span class="ck">in</span> <span class="cm">range</span>(<span class="cn">0</span>, <span class="cm">len</span>(seq), n):<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">yield</span> seq[i:i+n]</div>'
'<div class="qa-a">Strided <code>range</code> + slice, yielded lazily — the ML <strong>batching / DataLoader</strong> pattern (ML 3). Non-overlapping, unlike the sliding windows in C7; the final slice is a short partial batch.</div></details></div>'
'<div class="cc-block"><div class="cc-title"><span class="cc-badge badge-med">Med</span> C5 — Fibonacci generator</div>'
'<details class="sol"><summary>Solution</summary><div class="code-block">'
'<span class="ck">def</span> <span class="cm">fib</span>():<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;a, b = <span class="cn">0</span>, <span class="cn">1</span><br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">while</span> <span class="ck">True</span>:<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">yield</span> a; a, b = b, a + b</div>'
'<div class="qa-a">Infinite lazy sequence; <code>list(islice(fib(), 10))</code> → <code>[0,1,1,2,3,5,8,13,21,34]</code>.</div></details></div>'
'<div class="cc-block"><div class="cc-title"><span class="cc-badge badge-med">Med</span> C6 — Cumulative sum generator</div>'
'<details class="sol"><summary>Solution</summary><div class="code-block">'
'<span class="ck">def</span> <span class="cm">cumsum</span>(nums):<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;total = <span class="cn">0</span><br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">for</span> n <span class="ck">in</span> nums:<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;total += n; <span class="ck">yield</span> total</div>'
'<div class="qa-a">Running total held in state across yields. <code>[1,2,3,4]</code> → <code>[1,3,6,10]</code> (this is <code>itertools.accumulate</code>).</div></details></div>'
'<div class="cc-block"><div class="cc-title"><span class="cc-badge badge-hard">Hard</span> C7 — Sliding-window generator</div>'
'<details class="sol"><summary>Solution</summary><div class="code-block">'
'<span class="ck">def</span> <span class="cm">windows</span>(seq, k):<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">for</span> i <span class="ck">in</span> <span class="cm">range</span>(<span class="cm">len</span>(seq) - k + <span class="cn">1</span>):<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">yield</span> seq[i:i+k]</div>'
'<div class="qa-a">Yields each length-<code>k</code> slice lazily. <code>windows("abcde", 3)</code> → <code>abc, bcd, cde</code>. The n-gram pattern.</div></details></div>'
'<div class="cc-block"><div class="cc-title"><span class="cc-badge badge-hard">Hard</span> C8 — Infinite prime generator</div>'
'<details class="sol"><summary>Solution</summary><div class="code-block">'
'<span class="ck">def</span> <span class="cm">primes</span>():<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;found, n = [], <span class="cn">2</span><br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">while</span> <span class="ck">True</span>:<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">if</span> <span class="cm">all</span>(n % p <span class="ck">for</span> p <span class="ck">in</span> found):<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;found.<span class="cm">append</span>(n); <span class="ck">yield</span> n<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;n += <span class="cn">1</span></div>'
'<div class="qa-a">Uses <code>all(n % p for p in found)</code> — a short-circuiting genexpr — to test divisibility. <code>islice(primes(), 6)</code> → <code>[2,3,5,7,11,13]</code>.</div></details></div>'
)

md(
'<div class="summary-header"><h2>9. Summary Table — Session 4</h2></div>'
'<table class="summary">'
'<tr><th>Concept</th><th>Why it matters in ML</th><th>Interview frequency</th></tr>'
'<tr><td>List comprehension</td><td>The everyday feature transform / filter</td><td><span class="freq-vh">Very High</span></td></tr>'
'<tr><td>Dict / set comprehension</td><td>Vocab &amp; index maps; dedup + transform</td><td><span class="freq-h">High</span></td></tr>'
'<tr><td>Generator expression (lazy)</td><td>Streaming aggregates in O(1) memory</td><td><span class="freq-vh">Very High</span></td></tr>'
'<tr><td>Generator functions (<code>yield</code>)</td><td>Lazy data loaders, batching, pipelines</td><td><span class="freq-vh">Very High</span></td></tr>'
'<tr><td>Eager vs lazy / one-shot</td><td>Memory reasoning; avoiding re-iteration bugs</td><td><span class="freq-h">High</span></td></tr>'
'<tr><td>Ternary vs filter</td><td>Correct transform vs drop</td><td><span class="freq-m">Medium</span></td></tr>'
'<tr><td>Pipelines (chained generators)</td><td>Constant-memory preprocessing (RAG ingestion)</td><td><span class="freq-h">High</span></td></tr>'
'<tr><td><code>yield from</code></td><td>Composing / flattening generators</td><td><span class="freq-m">Medium</span></td></tr>'
'<tr><td>Nested comp (no aliasing)</td><td>Correct matrix/grid construction</td><td><span class="freq-m">Medium</span></td></tr>'
'</table>'
'<hr class="divider">'
'<div style="background:#1e1e2e; border-left:4px solid #a6e3a1; padding:14px 18px; border-radius:8px; font-family:monospace; color:#cdd6f4;">'
'<strong style="color:#a6e3a1">✅ Session 4 complete.</strong> Comprehensions &amp; generators end to end: '
'list/dict/set comprehensions, generator expressions, lazy evaluation, <code>yield</code> functions, '
'<code>yield from</code>, 4 examples, 5 edge cases, 8 golden rules, 6 traps, 12 exercises, ML connections, '
'12 conceptual Q&amp;A, 8 code challenges, summary table.<br>'
'<span style="color:#6c7086">Next — Session 5: Functions, scope &amp; closures (args/kwargs, default-arg traps, '
'LEGB scope, closures, <code>if __name__ == "__main__"</code>).</span></div>'
)

nb = new_notebook(cells=cells)
nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
nb.metadata["language_info"] = {"name": "python"}
nbf.write(nb, "theory.ipynb")
print("wrote theory.ipynb with", len(cells), "cells")
