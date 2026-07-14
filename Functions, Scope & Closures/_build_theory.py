# Builder for Session 5 - Functions, Scope & Closures, theory.ipynb.
# Deep 4-chunk session. Chunk A = function fundamentals & the argument model. Catppuccin Mocha UI.
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
  .ex-block, .edge-block { background:#1e1e2e; border:1px solid #313244; border-radius:10px; padding:16px 20px; margin:12px 0; }
  .ex-title { color:#a6e3a1; font-family:'Segoe UI',sans-serif; font-weight:bold; font-size:0.95em; margin-bottom:10px; }
  .ex-badge { display:inline-block; background:#1a2e1a; border:1px solid #a6e3a1; color:#a6e3a1; border-radius:20px; padding:2px 10px; font-size:0.8em; font-family:'Courier New',monospace; margin-right:8px; }
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
'<h1 class="main-title">🐍 Session 5 — Functions, Scope &amp; Closures</h1>'
'<div class="info-box"><strong>Part 1:</strong> Theory → Example → Edge Cases &nbsp;·&nbsp; '
'deep 4-chunk treatment.</div>'
'<div class="chunk-badge">Part 1 · Chunk A — Function Fundamentals &amp; the Argument Model</div>'
'<div class="theory-box" style="border-left-color:#cba6f7;">'
'Functions are where several Session 1 threads come home: default arguments re-expose the '
'<strong style="color:#89b4fa">mutable-default trap</strong>, argument passing <em>is</em> '
'<strong style="color:#89b4fa">call by object reference</strong>, and (in Chunk D) closures re-expose '
'<strong style="color:#89b4fa">late binding</strong>. Chunk A nails the argument model; B adds '
'<code>*args</code>/<code>**kwargs</code>; C is scope; D is closures — and the whole thing feeds '
'Session 6 (decorators).</div>'
)

# ── 1.1 first-class ────────────────────────────────────────────────────
md(
'<div class="part-header"><h2>1. Theory</h2></div>'
'<h3 class="sub">🔹 1.1 &nbsp;Functions are first-class objects</h3>'
'<div class="theory-box"><code>def</code> creates a <strong>function object</strong> and binds it to a '
'name — just another object (Session 1). You can assign it to a variable, put it in a list, pass it as an '
'argument, and return it from another function. That\'s what "first-class" means, and it\'s the foundation '
'for higher-order functions, <code>key=</code> sorts (2A), and decorators (Session 6).</div>'
'<div class="info-box">💡 <strong>SQL / Power BI anchor:</strong> a function is like a stored procedure or a '
'reusable measure — defined once, invoked many times. "First-class" is like passing a <em>reference</em> to '
'a measure around, not its result.</div>'
'<div class="code-block">'
'<span class="ck">def</span> <span class="cm">greet</span>(name, greeting=<span class="cs">"Hi"</span>):<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">return</span> <span class="cs">f"{greeting}, {name}!"</span><br>'
'<br>'
'say = greet              <span class="cc"># bind the SAME function object to another name</span><br>'
'say(<span class="cs">"Bob"</span>)               <span class="cc"># \'Hi, Bob!\' - callable through either name</span></div>'
'<div class="output-block">Hi, Bob!</div>'
)

# ── 1.2 params vs args ─────────────────────────────────────────────────
md(
'<h3 class="sub">🔹 1.2 &nbsp;Parameters vs arguments; positional vs keyword</h3>'
'<div class="theory-box">A <strong>parameter</strong> is the name in the <code>def</code>; an '
'<strong>argument</strong> is the value at the call. Arguments can be passed <strong>positionally</strong> '
'(by order) or by <strong>keyword</strong> (by name) — keywords can come in any order and document intent '
'at the call site.</div>'
'<div class="code-block">'
'greet(<span class="cs">"Siva"</span>)                    <span class="cc"># positional -> \'Hi, Siva!\'</span><br>'
'greet(<span class="cs">"Siva"</span>, <span class="cs">"Hello"</span>)           <span class="cc"># positional -> \'Hello, Siva!\'</span><br>'
'greet(greeting=<span class="cs">"Hey"</span>, name=<span class="cs">"A"</span>)   <span class="cc"># keyword (any order) -> \'Hey, A!\'</span></div>'
'<div class="output-block">Hi, Siva!<br>Hello, Siva!<br>Hey, A!</div>'
'<div class="note-box">💡 Positional args must come before keyword args at the call site. Keyword arguments '
'make calls self-documenting — <code>train(lr=0.01, epochs=100)</code> reads better than '
'<code>train(0.01, 100)</code>.</div>'
)

# ── 1.3 default args + trap ────────────────────────────────────────────
md(
'<h3 class="sub">🔹 1.3 &nbsp;Default arguments — and the mutable-default trap (S1 callback)</h3>'
'<div class="theory-box">A default gives a parameter a fallback value: <code>def f(a, b=10)</code>. The '
'critical rule: <strong>the default is evaluated once, at definition time</strong> — not on each call. For '
'an immutable default that\'s harmless; for a <strong>mutable</strong> one it\'s the most famous bug in '
'Python.</div>'
'<div class="code-block">'
'<span class="ck">def</span> <span class="cm">add_to</span>(item, acc=[]):   <span class="cc"># [] created ONCE, shared across calls</span><br>'
'&nbsp;&nbsp;&nbsp;&nbsp;acc.<span class="cm">append</span>(item)<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">return</span> acc<br>'
'<br>'
'<span class="cm">print</span>(<span class="cm">add_to</span>(<span class="cn">1</span>))   <span class="cc"># [1]</span><br>'
'<span class="cm">print</span>(<span class="cm">add_to</span>(<span class="cn">2</span>))   <span class="cc"># [1, 2]   &lt;- accumulates!</span><br>'
'<span class="cm">print</span>(<span class="cm">add_to</span>(<span class="cn">3</span>))   <span class="cc"># [1, 2, 3]</span></div>'
'<div class="output-block">[1]<br>[1, 2]<br>[1, 2, 3]</div>'
'<div class="why-box"><strong>The fix (S1 Golden Rule 1):</strong> use <code>None</code> as the sentinel and '
'build the mutable inside.</div>'
'<div class="code-block">'
'<span class="ck">def</span> <span class="cm">add_to</span>(item, acc=<span class="ck">None</span>):<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">if</span> acc <span class="ck">is</span> <span class="ck">None</span>: acc = []   <span class="cc"># fresh list per call</span><br>'
'&nbsp;&nbsp;&nbsp;&nbsp;acc.<span class="cm">append</span>(item); <span class="ck">return</span> acc<br>'
'<br>'
'<span class="cm">print</span>(<span class="cm">add_to</span>(<span class="cn">1</span>), <span class="cm">add_to</span>(<span class="cn">2</span>))   <span class="cc"># [1] [2]  - no accumulation</span></div>'
'<div class="output-block">[1] [2]</div>'
'<div class="note-box">💡 Verified: two calls to the buggy version share one list object (same <code>id</code>). '
'The default is part of the function object, created when <code>def</code> runs — the direct consequence of '
'Session 1\'s object model.</div>'
)

# ── 1.4 pos-only / kw-only ─────────────────────────────────────────────
md(
'<h3 class="sub">🔹 1.4 &nbsp;Positional-only <code>/</code> and keyword-only <code>*</code> markers</h3>'
'<div class="theory-box">Two markers in the parameter list control <em>how</em> arguments may be passed. '
'Everything before <code>/</code> is <strong>positional-only</strong>; everything after <code>*</code> is '
'<strong>keyword-only</strong>. They exist for API stability (rename a positional-only param freely) and '
'clarity (force callers to name flag-like args).</div>'
'<div class="code-block">'
'<span class="ck">def</span> <span class="cm">g</span>(a, b, /, c, *, d):   <span class="cc"># a,b: positional-only | c: either | d: keyword-only</span><br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">return</span> (a, b, c, d)<br>'
'<br>'
'g(<span class="cn">1</span>, <span class="cn">2</span>, <span class="cn">3</span>, d=<span class="cn">4</span>)     <span class="cc"># (1, 2, 3, 4)  ok</span><br>'
'g(<span class="cn">1</span>, <span class="cn">2</span>, c=<span class="cn">3</span>, d=<span class="cn">4</span>)   <span class="cc"># (1, 2, 3, 4)  ok</span><br>'
'g(a=<span class="cn">1</span>, b=<span class="cn">2</span>, c=<span class="cn">3</span>, d=<span class="cn">4</span>)  <span class="cc"># TypeError: a,b are positional-only</span><br>'
'g(<span class="cn">1</span>, <span class="cn">2</span>, <span class="cn">3</span>, <span class="cn">4</span>)       <span class="cc"># TypeError: d is keyword-only</span></div>'
'<div class="output-block">(1, 2, 3, 4)<br>(1, 2, 3, 4)<br>TypeError: g() got some positional-only arguments passed as keyword ...<br>TypeError: g() takes 3 positional arguments but 4 were given</div>'
'<div class="note-box">💡 You\'ll see <code>/</code> in built-in signatures (e.g. <code>len(obj, /)</code>) and '
'<code>*</code> whenever a library wants you to spell out options — <code>sorted(it, *, key=None, '
'reverse=False)</code>.</div>'
)

# ── 1.5 multiple return + 1.6 call by object reference ─────────────────
md(
'<h3 class="sub">🔹 1.5 &nbsp;Return values — one object, and "multiple" via a tuple (2B callback)</h3>'
'<div class="theory-box">A function returns exactly one object. "Returning several values" packs them into a '
'<strong>tuple</strong> (2B), which the caller unpacks. No <code>return</code> (or a bare <code>return</code>) '
'yields <code>None</code>.</div>'
'<div class="code-block">'
'<span class="ck">def</span> <span class="cm">minmax</span>(xs):<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">return</span> <span class="cm">min</span>(xs), <span class="cm">max</span>(xs)   <span class="cc"># packs a tuple (min, max)</span><br>'
'lo, hi = <span class="cm">minmax</span>([<span class="cn">3</span>, <span class="cn">1</span>, <span class="cn">4</span>, <span class="cn">1</span>, <span class="cn">5</span>])   <span class="cc"># unpack -> lo=1, hi=5</span><br>'
'<br>'
'<span class="ck">def</span> <span class="cm">noop</span>(): <span class="ck">pass</span><br>'
'<span class="cm">print</span>(<span class="cm">noop</span>())                    <span class="cc"># None</span></div>'
'<div class="output-block">lo, hi = 1 5<br>None</div>'
'<h3 class="sub">🔹 1.6 &nbsp;Argument passing is "call by object reference" (S1 callback)</h3>'
'<div class="theory-box">Python passes the <strong>binding</strong>, not a copy. Inside the function the '
'parameter points at the same object the caller passed. <strong>Mutate</strong> that object and the caller '
'sees it; <strong>rebind</strong> the local name and the caller does not. Exactly Session 1, Example 3.</div>'
'<div class="mut-grid">'
'<div class="mut-card mc-mut"><div class="mc-title">🔓 Mutate — caller sees it</div>'
'<div class="mc-body">def mutate(lst):<br>&nbsp;&nbsp;lst.append(99)<br><br>a=[1,2]; mutate(a)<br>a -> [1, 2, 99]</div></div>'
'<div class="mut-card mc-imm"><div class="mc-title">🔒 Rebind — caller does not</div>'
'<div class="mc-body">def rebind(lst):<br>&nbsp;&nbsp;lst = [0]<br><br>b=[1,2]; rebind(b)<br>b -> [1, 2]</div></div>'
'</div>'
'<div class="output-block">mutate: [1, 2, 99] | rebind: [1, 2]</div>'
'<div class="why-box"><strong>Why it matters:</strong> "pass by value vs reference" is the wrong frame for '
'Python — it\'s <strong>call by sharing</strong>. This is why a helper that <code>.append</code>s to a list '
'you passed corrupts your data (2A Trap), and why reassigning a parameter never affects the caller.</div>'
'<hr class="divider">'
'<div style="background:#1e1e2e; border-left:4px solid #cba6f7; padding:16px 20px; border-radius:8px; '
'font-family:monospace; color:#cdd6f4;">'
'<h4 style="color:#cba6f7; margin:0 0 12px 0;">🔑 Chunk A — Key Takeaways</h4>'
'<ul style="margin:0; padding-left:20px; line-height:2.1">'
'<li>Functions are first-class objects — assign, pass, return them</li>'
'<li>Args pass positionally or by keyword; keywords self-document the call</li>'
'<li>Defaults evaluate <strong>once</strong> at def time — never use a mutable default; use <code>None</code></li>'
'<li><code>/</code> = positional-only, <code>*</code> = keyword-only</li>'
'<li>"Multiple returns" = a tuple; no return = <code>None</code></li>'
'<li>Call by object reference: mutate → caller sees it; rebind → it doesn\'t</li>'
'</ul></div>'
)

# ══════════════════════════ CHUNK B ══════════════════════════
md(
'<div class="chunk-badge">Part 1 · Chunk B — *args / **kwargs &amp; Unpacking</div>'
'<h3 class="sub">🔹 1.7 &nbsp;<code>*args</code> — collect extra positional arguments into a tuple</h3>'
'<div class="theory-box">A parameter written <code>*args</code> gathers any <strong>extra positional</strong> '
'arguments into a <strong>tuple</strong> (2B). It lets a function accept a variable number of positionals. '
'The name is a convention; the <code>*</code> is what matters.</div>'
'<div class="code-block">'
'<span class="ck">def</span> <span class="cm">total</span>(*args):        <span class="cc"># args is a tuple of everything passed</span><br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">return</span> <span class="cm">sum</span>(args)<br>'
'<br>'
'<span class="cm">total</span>(<span class="cn">1</span>, <span class="cn">2</span>, <span class="cn">3</span>)   <span class="cc"># 6</span><br>'
'<span class="cm">total</span>()          <span class="cc"># 0  - args is ()</span></div>'
'<div class="output-block">6<br>0</div>'
'<h3 class="sub">🔹 1.8 &nbsp;<code>**kwargs</code> — collect extra keyword arguments into a dict</h3>'
'<div class="theory-box"><code>**kwargs</code> gathers any <strong>extra keyword</strong> arguments into a '
'<strong>dict</strong> (2D) of <code>name → value</code>. Ideal for optional config / passing options '
'through.</div>'
'<div class="code-block">'
'<span class="ck">def</span> <span class="cm">config</span>(**kwargs):     <span class="cc"># kwargs is a dict</span><br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">return</span> kwargs<br>'
'<br>'
'<span class="cm">config</span>(lr=<span class="cn">0.01</span>, epochs=<span class="cn">100</span>)   <span class="cc"># {\'lr\': 0.01, \'epochs\': 100}</span></div>'
'<div class="output-block">{\'lr\': 0.01, \'epochs\': 100}</div>'
'<div class="info-box">💡 <code>*args</code> → tuple (positional), <code>**kwargs</code> → dict (keyword). '
'Together they let a function accept <em>anything</em> — the basis of wrappers and decorators (Session 6).</div>'
)

md(
'<h3 class="sub">🔹 1.9 &nbsp;The full parameter order</h3>'
'<div class="theory-box">All five kinds have a fixed order in a signature:</div>'
'<table class="summary">'
'<tr><th>Position</th><th>Kind</th><th>Example</th></tr>'
'<tr><td>1</td><td>positional-only</td><td><code>a, b, /</code></td></tr>'
'<tr><td>2</td><td>positional-or-keyword</td><td><code>c</code></td></tr>'
'<tr><td>3</td><td>var-positional</td><td><code>*args</code></td></tr>'
'<tr><td>4</td><td>keyword-only</td><td><code>d</code> (after <code>*args</code> or a bare <code>*</code>)</td></tr>'
'<tr><td>5</td><td>var-keyword</td><td><code>**kwargs</code></td></tr>'
'</table>'
'<div class="code-block">'
'<span class="ck">def</span> <span class="cm">h</span>(a, b, /, c, *args, d, **kwargs):<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">return</span> (a, b, c, args, d, kwargs)<br>'
'<br>'
'<span class="cm">h</span>(<span class="cn">1</span>, <span class="cn">2</span>, <span class="cn">3</span>, <span class="cn">4</span>, <span class="cn">5</span>, d=<span class="cn">6</span>, e=<span class="cn">7</span>)   <span class="cc"># (1, 2, 3, (4, 5), 6, {\'e\': 7})</span></div>'
'<div class="output-block">(1, 2, 3, (4, 5), 6, {\'e\': 7})</div>'
'<div class="note-box">💡 Anything after <code>*args</code> (or a bare <code>*</code>) is keyword-only. You '
'rarely use all five at once — but knowing the order explains any signature you meet.</div>'
)

md(
'<h3 class="sub">🔹 1.10 &nbsp;Call-site unpacking — <code>f(*seq)</code> and <code>f(**dict)</code></h3>'
'<div class="theory-box">The same <code>*</code>/<code>**</code> work in reverse at the call site: '
'<code>*</code> spreads an iterable into positional arguments, <code>**</code> spreads a dict into keyword '
'arguments. (This is the sibling of star-unpacking from 2A/2B.)</div>'
'<div class="code-block">'
'<span class="ck">def</span> <span class="cm">add</span>(a, b, c): <span class="ck">return</span> a + b + c<br>'
'<br>'
'<span class="cm">add</span>(*[<span class="cn">1</span>, <span class="cn">2</span>, <span class="cn">3</span>])              <span class="cc"># 6  - list spread into a, b, c</span><br>'
'<span class="cm">add</span>(**{<span class="cs">"a"</span>:<span class="cn">1</span>, <span class="cs">"b"</span>:<span class="cn">2</span>, <span class="cs">"c"</span>:<span class="cn">3</span>})   <span class="cc"># 6  - dict spread by name</span><br>'
'<span class="cm">add</span>(*[<span class="cn">1</span>], **{<span class="cs">"b"</span>:<span class="cn">2</span>, <span class="cs">"c"</span>:<span class="cn">3</span>})     <span class="cc"># 6  - mix both</span></div>'
'<div class="output-block">6<br>6<br>6</div>'
'<div class="note-box">💡 Symmetry: <code>*</code>/<code>**</code> in a <em>definition</em> collect arguments; '
'<code>*</code>/<code>**</code> at a <em>call</em> spread them. Same syntax, opposite direction.</div>'
)

md(
'<h3 class="sub">🔹 1.11 &nbsp;Argument forwarding — the wrapper pattern (Session 6 preview)</h3>'
'<div class="theory-box">Collect with <code>*args, **kwargs</code> and immediately spread them into another '
'call. This "accept anything, pass it through" pattern is exactly how decorators wrap a function without '
'knowing its signature.</div>'
'<div class="code-block">'
'<span class="ck">def</span> <span class="cm">logged</span>(fn, *args, **kwargs):<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="cm">print</span>(<span class="cs">"calling"</span>, fn.__name__)<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">return</span> fn(*args, **kwargs)     <span class="cc"># forward everything unchanged</span><br>'
'<br>'
'<span class="cm">logged</span>(<span class="cm">add</span>, <span class="cn">1</span>, <span class="cn">2</span>, <span class="cn">3</span>)   <span class="cc"># prints "calling add", returns 6</span></div>'
'<div class="output-block">calling add<br>6</div>'
'<div class="why-box"><strong>Why it matters:</strong> forwarding is the backbone of decorators, retries, '
'timers, and caching wrappers (Session 6). A wrapper stays generic precisely because <code>*args, '
'**kwargs</code> capture and replay any call.</div>'
'<hr class="divider">'
'<div style="background:#1e1e2e; border-left:4px solid #cba6f7; padding:16px 20px; border-radius:8px; font-family:monospace; color:#cdd6f4;">'
'<h4 style="color:#cba6f7; margin:0 0 12px 0;">🔑 Chunk B — Key Takeaways</h4>'
'<ul style="margin:0; padding-left:20px; line-height:2.1">'
'<li><code>*args</code> collects extra positionals into a <strong>tuple</strong>; <code>**kwargs</code> collects extra keywords into a <strong>dict</strong></li>'
'<li>Parameter order: positional-only <code>/</code> → normal → <code>*args</code> → keyword-only → <code>**kwargs</code></li>'
'<li>At the call site, <code>*</code> spreads an iterable and <code>**</code> spreads a dict — the reverse of collecting</li>'
'<li><code>def wrapper(*args, **kwargs): return fn(*args, **kwargs)</code> is the decorator/forwarding backbone</li>'
'</ul></div>'
)

# ══════════════════════════ CHUNK C ══════════════════════════
md(
'<div class="chunk-badge">Part 1 · Chunk C — Scope: LEGB, global, nonlocal</div>'
'<h3 class="sub">🔹 1.12 &nbsp;The LEGB rule — how names are resolved</h3>'
'<div class="theory-box">When you <em>read</em> a name, Python searches four scopes in order: '
'<strong>L</strong>ocal (inside the current function) → <strong>E</strong>nclosing (any outer function) → '
'<strong>G</strong>lobal (module level) → <strong>B</strong>uilt-in (<code>len</code>, <code>sum</code>, …). '
'First match wins.</div>'
'<div class="code-block">'
'x = <span class="cs">"global"</span><br>'
'<span class="ck">def</span> <span class="cm">outer</span>():<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;x = <span class="cs">"enclosing"</span><br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">def</span> <span class="cm">inner</span>():<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x = <span class="cs">"local"</span><br>'
'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">return</span> x        <span class="cc"># finds Local first</span><br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">return</span> <span class="cm">inner</span>(), x    <span class="cc"># inner sees local; outer sees enclosing</span><br>'
'<br>'
'<span class="cm">outer</span>()   <span class="cc"># (\'local\', \'enclosing\')   -- module x stays \'global\'</span></div>'
'<div class="output-block">(\'local\', \'enclosing\')</div>'
'<h3 class="sub">🔹 1.13 &nbsp;Reading vs assigning — the UnboundLocalError trap</h3>'
'<div class="theory-box"><strong>Reading</strong> a name searches LEGB. But <strong>assigning</strong> to a '
'name anywhere in a function makes it <strong>local for the whole function</strong> — so referencing it '
'before that assignment fails, even if a global of the same name exists.</div>'
'<div class="code-block">'
'count = <span class="cn">0</span><br>'
'<span class="ck">def</span> <span class="cm">bad</span>():<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;count += <span class="cn">1</span>      <span class="cc"># UnboundLocalError: count is local (it\'s assigned), used before assignment</span><br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">return</span> count<br>'
'<br>'
'<span class="ck">def</span> <span class="cm">read</span>():<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">return</span> count      <span class="cc"># 0 - pure read of the global is fine</span></div>'
'<div class="output-block">bad()  -> UnboundLocalError: cannot access local variable \'count\' ...<br>read() -> 0</div>'
'<div class="why-box"><strong>Why it matters:</strong> <code>count += 1</code> is a read <em>and</em> an '
'assignment. The assignment marks <code>count</code> local, so the read half has nothing to read yet. The '
'fix is <code>global</code> (or <code>nonlocal</code>) — next.</div>'
)

md(
'<h3 class="sub">🔹 1.14 &nbsp;<code>global</code> — rebind a module-level name</h3>'
'<div class="code-block">'
'c = <span class="cn">0</span><br>'
'<span class="ck">def</span> <span class="cm">inc</span>():<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">global</span> c      <span class="cc"># "c refers to the module-level c"</span><br>'
'&nbsp;&nbsp;&nbsp;&nbsp;c += <span class="cn">1</span><br>'
'<span class="cm">inc</span>(); <span class="cm">inc</span>()   <span class="cc"># c == 2</span></div>'
'<div class="output-block">2</div>'
'<h3 class="sub">🔹 1.15 &nbsp;<code>nonlocal</code> — rebind an enclosing name (closures)</h3>'
'<div class="theory-box"><code>nonlocal</code> is the enclosing-scope version of <code>global</code>: it lets '
'an inner function rebind a variable in the <em>enclosing</em> function. It\'s what makes stateful closures '
'(counters, accumulators) work.</div>'
'<div class="code-block">'
'<span class="ck">def</span> <span class="cm">make_counter</span>():<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;n = <span class="cn">0</span><br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">def</span> <span class="cm">bump</span>():<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">nonlocal</span> n   <span class="cc"># rebind the enclosing n, not create a new local</span><br>'
'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;n += <span class="cn">1</span>; <span class="ck">return</span> n<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">return</span> <span class="cm">bump</span><br>'
'<br>'
'b = <span class="cm">make_counter</span>()<br>'
'b(), b(), b()   <span class="cc"># 1, 2, 3 - state persists in the closure</span></div>'
'<div class="output-block">1 2 3</div>'
)

md(
'<h3 class="sub">🔹 1.16 &nbsp;Mutate vs rebind in scope, &amp; shadowing built-ins</h3>'
'<div class="theory-box">You only need <code>global</code>/<code>nonlocal</code> to <strong>rebind</strong> a '
'name. <strong>Mutating</strong> an object a name already points at needs no declaration — the S1 '
'mutate-vs-rebind distinction, now at scope level.</div>'
'<div class="code-block">'
'items = []<br>'
'<span class="ck">def</span> <span class="cm">add</span>(v):<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;items.<span class="cm">append</span>(v)   <span class="cc"># MUTATES the global list - no \'global\' needed</span><br>'
'<span class="cm">add</span>(<span class="cn">1</span>); <span class="cm">add</span>(<span class="cn">2</span>)      <span class="cc"># items == [1, 2]</span></div>'
'<div class="output-block">[1, 2]</div>'
'<div class="warn-box">⚠ <strong>Shadowing a built-in:</strong> assigning <code>sum = 0</code> (or '
'<code>list</code>, <code>id</code>, <code>str</code>…) hides the built-in in that scope — <code>sum([1,2])</code> '
'then raises <code>TypeError: \'int\' object is not callable</code>. Never name variables after built-ins.</div>'
'<hr class="divider">'
'<div style="background:#1e1e2e; border-left:4px solid #cba6f7; padding:14px 18px; border-radius:8px; font-family:monospace; color:#cdd6f4;">'
'<h4 style="color:#cba6f7; margin:0 0 10px 0;">🔑 Chunk C — Key Takeaways</h4>'
'<ul style="margin:0; padding-left:20px; line-height:2.0">'
'<li>Name lookup: <strong>L→E→G→B</strong>, first match wins</li>'
'<li>Assigning a name <em>anywhere</em> in a function makes it local → <code>UnboundLocalError</code> if read first</li>'
'<li><code>global</code> rebinds a module name; <code>nonlocal</code> rebinds an enclosing one</li>'
'<li>Mutating needs no declaration; only rebinding does. Don\'t shadow built-ins</li>'
'</ul></div>'
)

# ══════════════════════════ CHUNK D ══════════════════════════
md(
'<div class="chunk-badge">Part 1 · Chunk D — Closures, Late Binding &amp; <code>__main__</code></div>'
'<h3 class="sub">🔹 1.17 &nbsp;Closures — a function that remembers its enclosing scope</h3>'
'<div class="theory-box">When an inner function references variables from its enclosing function, it becomes '
'a <strong>closure</strong>: it keeps those variables alive even after the outer function has returned. '
'That captured state lives in <code>fn.__closure__</code> cells.</div>'
'<div class="code-block">'
'<span class="ck">def</span> <span class="cm">make_multiplier</span>(n):<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">def</span> <span class="cm">mult</span>(v):<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">return</span> v * n     <span class="cc"># captures n from the enclosing scope</span><br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">return</span> <span class="cm">mult</span><br>'
'<br>'
'double, triple = <span class="cm">make_multiplier</span>(<span class="cn">2</span>), <span class="cm">make_multiplier</span>(<span class="cn">3</span>)<br>'
'double(<span class="cn">5</span>), triple(<span class="cn">5</span>)                <span class="cc"># 10, 15</span><br>'
'double.__closure__[<span class="cn">0</span>].cell_contents   <span class="cc"># 2 - n lives on inside the closure</span></div>'
'<div class="output-block">10 15<br>2</div>'
'<div class="info-box">💡 Each call to <code>make_multiplier</code> makes a <strong>fresh</strong> closure with '
'its own captured <code>n</code> — <code>double</code> and <code>triple</code> are independent. Closures are '
'how you build function factories, and the mechanism behind decorators (Session 6).</div>'
)

md(
'<h3 class="sub">🔹 1.18 &nbsp;The late-binding closure trap (S1 callback)</h3>'
'<div class="theory-box">A closure captures the <strong>variable</strong>, not its value at creation time. '
'Build closures in a loop and they all see the loop variable\'s <em>final</em> value.</div>'
'<div class="code-block">'
'funcs = [<span class="ck">lambda</span>: i <span class="ck">for</span> i <span class="ck">in</span> <span class="cm">range</span>(<span class="cn">3</span>)]<br>'
'[f() <span class="ck">for</span> f <span class="ck">in</span> funcs]          <span class="cc"># [2, 2, 2]  - not [0, 1, 2]!</span><br>'
'<br>'
'fixed = [<span class="ck">lambda</span> i=i: i <span class="ck">for</span> i <span class="ck">in</span> <span class="cm">range</span>(<span class="cn">3</span>)]   <span class="cc"># bind now via default arg</span><br>'
'[f() <span class="ck">for</span> f <span class="ck">in</span> fixed]          <span class="cc"># [0, 1, 2]</span></div>'
'<div class="output-block">[2, 2, 2]<br>[0, 1, 2]</div>'
'<div class="why-box"><strong>Why it matters (S1 callback):</strong> all three lambdas close over the same '
'<code>i</code>; by the time they run, the loop is done and <code>i == 2</code>. The fix '
'<code>lambda i=i: i</code> captures the <em>value</em> at definition time via a default argument (Chunk A) '
'— evaluated once, per iteration.</div>'
)

md(
'<h3 class="sub">🔹 1.19 &nbsp;<code>if __name__ == "__main__"</code> — script vs import</h3>'
'<div class="theory-box">Every module has a <code>__name__</code>. When you <strong>run</strong> a file '
'directly, <code>__name__ == "__main__"</code>; when it\'s <strong>imported</strong>, <code>__name__</code> '
'is the module\'s name. The guard runs entry-point code only when the file is the program, not when it\'s '
'imported as a library.</div>'
'<div class="code-block">'
'<span class="ck">def</span> <span class="cm">main</span>():<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="cm">print</span>(<span class="cs">"running as a script"</span>)<br>'
'<br>'
'<span class="ck">if</span> __name__ == <span class="cs">"__main__"</span>:   <span class="cc"># True only when run directly</span><br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="cm">main</span>()</div>'
'<div class="output-block">running as a script   # when executed directly; silent when imported</div>'
'<div class="note-box">💡 Without the guard, importing the module would execute its top-level code (and any '
'test/demo calls) as a side effect. The guard is the standard entry point for CLIs and scripts.</div>'
# ── 2. Example ──
'<div class="ex-header"><h2>2. Example</h2></div>'
'<div class="ex-block"><div class="ex-title"><span class="ex-badge">Ex 1</span> Stateful counter (closure + nonlocal)</div>'
'<div class="code-block">'
'<span class="ck">def</span> <span class="cm">make_counter</span>():<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;n = <span class="cn">0</span><br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">def</span> <span class="cm">bump</span>():<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">nonlocal</span> n; n += <span class="cn">1</span>; <span class="ck">return</span> n<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">return</span> <span class="cm">bump</span><br>'
'c = <span class="cm">make_counter</span>(); c(), c(), c()   <span class="cc"># 1, 2, 3</span></div>'
'<div class="output-block">1 2 3</div></div>'
'<div class="ex-block"><div class="ex-title"><span class="ex-badge">Ex 2</span> Running average (closure holds total &amp; n)</div>'
'<div class="code-block">'
'<span class="ck">def</span> <span class="cm">averager</span>():<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;total = n = <span class="cn">0</span><br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">def</span> <span class="cm">add</span>(v):<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">nonlocal</span> total, n; total += v; n += <span class="cn">1</span>; <span class="ck">return</span> total / n<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">return</span> <span class="cm">add</span><br>'
'a = <span class="cm">averager</span>(); a(<span class="cn">10</span>), a(<span class="cn">20</span>), a(<span class="cn">30</span>)   <span class="cc"># 10.0, 15.0, 20.0</span></div>'
'<div class="output-block">10.0 15.0 20.0</div></div>'
'<div class="ex-block"><div class="ex-title"><span class="ex-badge">Ex 3</span> Memoize (cache in a closure) — decorator preview</div>'
'<div class="code-block">'
'<span class="ck">def</span> <span class="cm">memoize</span>(fn):<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;cache = {}                 <span class="cc"># captured, persists across calls</span><br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">def</span> <span class="cm">wrapper</span>(k):<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">if</span> k <span class="ck">not in</span> cache: cache[k] = fn(k)<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">return</span> cache[k]<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">return</span> <span class="cm">wrapper</span><br>'
'sq = <span class="cm">memoize</span>(<span class="ck">lambda</span> v: v * v); sq(<span class="cn">4</span>), sq(<span class="cn">4</span>)   <span class="cc"># 16, 16 (2nd from cache)</span></div>'
'<div class="output-block">16 16</div>'
'<div class="note-box">A closure over <code>cache</code> is exactly what <code>functools.lru_cache</code> does — and it\'s the shape of a decorator (Session 6).</div></div>'
'<div class="ex-block"><div class="ex-title"><span class="ex-badge">Ex 4</span> Function factory (parameterized behavior)</div>'
'<div class="code-block">'
'<span class="ck">def</span> <span class="cm">power_of</span>(exp):<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">return</span> <span class="ck">lambda</span> base: base ** exp<br>'
'square, cube = <span class="cm">power_of</span>(<span class="cn">2</span>), <span class="cm">power_of</span>(<span class="cn">3</span>)<br>'
'square(<span class="cn">5</span>), cube(<span class="cn">5</span>)   <span class="cc"># 25, 125</span></div>'
'<div class="output-block">25 125</div></div>'
# ── 3. Edge Cases ──
'<div class="warn-header"><h2>3. Edge Cases</h2></div>'
'<p style="color:#cdd6f4;font-family:\'Segoe UI\',sans-serif;font-size:0.92em;margin:0 0 12px 0">All outputs verified by running.</p>'
'<div class="edge-block"><div class="edge-title"><span class="edge-badge">Edge 1</span> Assignment makes a name local for the whole function</div>'
'<div class="code-block">count = <span class="cn">0</span><br><span class="ck">def</span> <span class="cm">bad</span>(): count += <span class="cn">1</span>   <span class="cc"># UnboundLocalError</span></div>'
'<div class="output-block">UnboundLocalError: cannot access local variable \'count\' where it is not associated with a value</div>'
'<div class="why-box"><strong>Why:</strong> the assignment makes <code>count</code> local, so the read half of '
'<code>+=</code> has nothing to read. Fix with <code>global</code>/<code>nonlocal</code>, or pass it in.</div></div>'
'<div class="edge-block"><div class="edge-title"><span class="edge-badge">Edge 2</span> Late binding — closures capture the variable, not the value</div>'
'<div class="code-block">[f() <span class="ck">for</span> f <span class="ck">in</span> [<span class="ck">lambda</span>: i <span class="ck">for</span> i <span class="ck">in</span> <span class="cm">range</span>(<span class="cn">3</span>)]]   <span class="cc"># [2, 2, 2]</span></div>'
'<div class="output-block">[2, 2, 2]</div>'
'<div class="why-box"><strong>Why:</strong> all lambdas share one <code>i</code>, read at call time (= 2). Fix: '
'<code>lambda i=i: i</code> captures the value per iteration.</div></div>'
'<div class="edge-block"><div class="edge-title"><span class="edge-badge">Edge 3</span> <code>global</code> to rebind, but not to mutate</div>'
'<div class="code-block">items = []<br><span class="ck">def</span> <span class="cm">add</span>(v): items.<span class="cm">append</span>(v)   <span class="cc"># works - mutation, no \'global\'</span><br>total = <span class="cn">0</span><br><span class="ck">def</span> <span class="cm">inc</span>(): total += <span class="cn">1</span>       <span class="cc"># UnboundLocalError - rebinding needs \'global\'</span></div>'
'<div class="output-block">add: [1, 2]  |  inc: UnboundLocalError</div>'
'<div class="why-box"><strong>Why (S1 callback):</strong> mutating the object a global points at is fine; '
'rebinding the global name requires <code>global</code>.</div></div>'
'<div class="edge-block"><div class="edge-title"><span class="edge-badge">Edge 4</span> Shadowing a built-in</div>'
'<div class="code-block">sum = <span class="cn">0</span><br>sum([<span class="cn">1</span>, <span class="cn">2</span>])   <span class="cc"># TypeError: \'int\' object is not callable</span></div>'
'<div class="output-block">TypeError: \'int\' object is not callable</div>'
'<div class="why-box"><strong>Why:</strong> the local/global <code>sum</code> shadows the built-in in LEGB. '
'Avoid names like <code>list</code>, <code>dict</code>, <code>id</code>, <code>sum</code>, <code>type</code>.</div></div>'
'<div class="edge-block"><div class="edge-title"><span class="edge-badge">Edge 5</span> <code>nonlocal</code> needs an existing enclosing binding</div>'
'<div class="code-block"><span class="ck">def</span> <span class="cm">outer</span>():<br>&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">def</span> <span class="cm">inner</span>(): <span class="ck">nonlocal</span> z   <span class="cc"># SyntaxError: no binding for nonlocal \'z\'</span></div>'
'<div class="output-block">SyntaxError: no binding for nonlocal \'z\' found</div>'
'<div class="why-box"><strong>Why:</strong> <code>nonlocal</code> must point at a variable that already exists '
'in an enclosing function — it can\'t create one. (Unlike <code>global</code>, which can bind a new module '
'name.)</div></div>'
'<hr class="divider">'
'<div class="info-box">📎 <strong>End of Part 1</strong> (Chunks A–D: argument model, <code>*args</code>/'
'<code>**kwargs</code>, LEGB scope, closures, 4 examples, 5 edge cases). <strong>Part 2</strong> — Golden '
'Rules → Common Traps → Exercise. <strong>Part 3</strong> — ML Real-World → Interview Q&amp;A → Summary Table.</div>'
)

# ══════════════════════════ PART 2 ══════════════════════════
md(
'<div class="info-box"><strong>Part 2:</strong> Golden Rules → Common Traps → Exercise</div>'
'<div class="part-header"><h2>4. Golden Rules</h2></div>'
'<div class="rule-block"><div class="rule-title"><span class="rule-badge">Rule 1</span> Never use a mutable default argument — use <code>None</code> as the sentinel, checked with <code>is None</code>.</div>'
'<div class="body-txt">Defaults evaluate once at def time. Write <code>if acc is None: acc = []</code> — <strong>not</strong> <code>acc = acc or []</code>, which silently discards a legitimately-passed empty list (Trap 7).</div></div>'
'<div class="rule-block"><div class="rule-title"><span class="rule-badge">Rule 2</span> Favor keyword arguments for clarity; force them with <code>*</code>.</div>'
'<div class="body-txt"><code>train(lr=0.01, epochs=100)</code> beats <code>train(0.01, 100)</code>; make flags keyword-only.</div></div>'
'<div class="rule-block"><div class="rule-title"><span class="rule-badge">Rule 3</span> Use <code>*args</code>/<code>**kwargs</code> for wrappers &amp; forwarding — not to hide a real signature.</div>'
'<div class="body-txt">Great for decorators; a public API should still name its parameters.</div></div>'
'<div class="rule-block"><div class="rule-title"><span class="rule-badge">Rule 4</span> Return a tuple for multiple values; keep a function returning one logical thing.</div>'
'<div class="body-txt"><code>return lo, hi</code> then <code>lo, hi = f()</code> (2B). Avoid grab-bag returns.</div></div>'
'<div class="rule-block"><div class="rule-title"><span class="rule-badge">Rule 5</span> Reach for <code>global</code>/<code>nonlocal</code> only when you must rebind — prefer passing/returning.</div>'
'<div class="body-txt">Assignment makes a name local; shared global state is hard to test and reason about.</div></div>'
'<div class="rule-block"><div class="rule-title"><span class="rule-badge">Rule 6</span> Prefer pure functions — return new values instead of mutating arguments.</div>'
'<div class="body-txt">If you must mutate (call by object reference), name it clearly and document it (S1 Rule 5).</div></div>'
'<div class="rule-block"><div class="rule-title"><span class="rule-badge">Rule 7</span> In loops that build closures, bind the loop value with a default arg.</div>'
'<div class="body-txt"><code>lambda i=i: i</code> — captures the value now, avoiding late binding.</div></div>'
'<div class="rule-block"><div class="rule-title"><span class="rule-badge">Rule 8</span> Guard entry points with <code>if __name__ == "__main__"</code>; don\'t shadow built-ins.</div>'
'<div class="body-txt">Keeps modules importable; avoid variable names like <code>sum</code>, <code>list</code>, <code>id</code>.</div></div>'
)

md(
'<div class="trap-header"><h2>5. Common Traps</h2></div>'
'<div class="trap-block"><div class="trap-title"><span class="trap-badge">Trap 1</span> Mutable default argument.</div>'
'<div class="body-txt"><code>def f(x, acc=[])</code> accumulates across calls. <strong>Fix:</strong> <code>acc=None</code> sentinel.</div></div>'
'<div class="trap-block"><div class="trap-title"><span class="trap-badge">Trap 2</span> <code>UnboundLocalError</code>.</div>'
'<div class="body-txt">Assigning a name you meant to read from an outer scope makes it local. <strong>Fix:</strong> <code>global</code>/<code>nonlocal</code>, or pass it in.</div></div>'
'<div class="trap-block"><div class="trap-title"><span class="trap-badge">Trap 3</span> Late binding in a loop.</div>'
'<div class="body-txt">Closures built in a loop all see the final loop value. <strong>Fix:</strong> <code>lambda i=i: …</code>.</div></div>'
'<div class="trap-block"><div class="trap-title"><span class="trap-badge">Trap 4</span> Silent argument mutation.</div>'
'<div class="body-txt">A helper that <code>.append</code>s to the list you passed corrupts caller data. <strong>Fix:</strong> copy or return new.</div></div>'
'<div class="trap-block"><div class="trap-title"><span class="trap-badge">Trap 5</span> Overusing <code>global</code>.</div>'
'<div class="body-txt">Hidden shared state makes functions non-reproducible and hard to test. <strong>Fix:</strong> parameters + return values, or a closure.</div></div>'
'<div class="trap-block"><div class="trap-title"><span class="trap-badge">Trap 6</span> Shadowing a built-in.</div>'
'<div class="body-txt"><code>sum = 0</code> then <code>sum([1,2])</code> → <code>TypeError</code>. <strong>Fix:</strong> pick a different name.</div></div>'
'<div class="trap-block"><div class="trap-title"><span class="trap-badge">Trap 7</span> The <code>acc = acc or []</code> false-empty pitfall.</div>'
'<div class="body-txt">A <em>passed-in</em> empty list is falsy, so <code>acc or []</code> throws it away and builds a new one — the caller\'s list is never filled. Verified: with <code>or []</code>, <code>result is passed_list</code> is <code>False</code>; with <code>if acc is None</code> it\'s <code>True</code>. <strong>Fix:</strong> the sentinel must be checked with <code>is None</code>, never truthiness.</div></div>'
'<div class="trap-block"><div class="trap-title"><span class="trap-badge">Trap 8</span> <code>**kwargs</code> collision with an explicit parameter.</div>'
'<div class="body-txt"><code>def f(a, **kw)</code> called as <code>f(1, **{"a": 2})</code> → <code>TypeError: f() got multiple values for argument \'a\'</code>. The dict supplies <code>a</code> which was already given positionally. <strong>Fix:</strong> don\'t let a forwarded dict carry a key that\'s also a named parameter.</div></div>'
)

md(
'<div class="part-header"><h2>6. Exercise</h2></div>'
'<div class="body-txt" style="margin-bottom:10px">Twelve problems, leaning hard — most are closures / higher-order functions that preview decorators (Session 6). Attempt each in <code>01_functions.ipynb</code>; hints only here — full solutions in <code>solutions.ipynb</code>.</div>'
'<div class="exr-block"><div class="exr-title"><span class="cc-badge badge-easy">Easy</span> E1 — <code>build_url(base, **params)</code> → <code>"base?k=v&amp;k2=v2"</code></div><div class="hint-box">💡 <code>**params</code> is a dict → <code>"&amp;".join(f"{k}={v}" for k,v in params.items())</code>.</div></div>'
'<div class="exr-block"><div class="exr-title"><span class="cc-badge badge-easy">Easy</span> E2 — Fix <em>both</em> bugs in <code>def add(item, acc=[])</code></div><div class="hint-box">💡 Mutable default → <code>acc=None</code>; and check <code>if acc is None</code>, NOT <code>acc or []</code> (Trap 7). Prove a passed-in empty list gets filled (<code>result is passed_list</code>).</div></div>'
'<div class="exr-block"><div class="exr-title"><span class="cc-badge badge-med">Medium</span> E3 — <code>make_counter(start=0, step=1)</code> — configurable closure</div><div class="hint-box">💡 <code>nonlocal</code> over a captured <code>n</code>; first call returns <code>start</code>, then increments by <code>step</code>.</div></div>'
'<div class="exr-block"><div class="exr-title"><span class="cc-badge badge-med">Medium</span> E4 — <code>apply_n(f, x, n)</code> → apply <code>f</code> to <code>x</code>, <code>n</code> times</div><div class="hint-box">💡 Loop <code>n</code> times, rebinding <code>x = f(x)</code>. Generalizes "apply twice".</div></div>'
'<div class="exr-block"><div class="exr-title"><span class="cc-badge badge-med">Medium</span> E5 — <code>calc(a, b, /, *, op)</code> with a keyword-only callable <code>op</code></div><div class="hint-box">💡 <code>a, b</code> positional-only; <code>op</code> keyword-only → <code>return op(a, b)</code>. Test <code>op=max</code>.</div></div>'
'<div class="exr-block"><div class="exr-title"><span class="cc-badge badge-med">Medium</span> E6 — <code>trace(fn)</code> — a wrapper factory (decorator shape)</div><div class="hint-box">💡 Return an inner <code>wrapper(*args, **kwargs)</code> that prints the call then forwards. It <em>returns a function</em>, unlike a one-shot forwarder.</div></div>'
'<div class="exr-block"><div class="exr-title"><span class="cc-badge badge-med">Medium</span> E7 — <code>running_stats()</code> → each call returns <code>(count, mean)</code></div><div class="hint-box">💡 Closure over <code>total</code> and <code>n</code>; <code>nonlocal</code> both.</div></div>'
'<div class="exr-block"><div class="exr-title"><span class="cc-badge badge-hard">Hard</span> E8 — <code>memoize(fn)</code> — cache results, keyed by <code>*args</code></div><div class="hint-box">💡 Closure over a <code>cache</code> dict; use the <code>args</code> <strong>tuple</strong> as the key (hashable, 2B). Recompute only on a miss.</div></div>'
'<div class="exr-block"><div class="exr-title"><span class="cc-badge badge-hard">Hard</span> E9 — <code>compose(*funcs)</code> → apply left-to-right</div><div class="hint-box">💡 Return an inner function that threads <code>x</code> through each func in order.</div></div>'
'<div class="exr-block"><div class="exr-title"><span class="cc-badge badge-hard">Hard</span> E10 — <code>partial(fn, *fixed)</code> → pre-fill leading arguments</div><div class="hint-box">💡 Return <code>inner(*rest): return fn(*fixed, *rest)</code>. This is a mini <code>functools.partial</code>.</div></div>'
'<div class="exr-block"><div class="exr-title"><span class="cc-badge badge-hard">Hard</span> E11 — Build <code>[f0, f1, f2]</code> where <code>fi()</code> returns <code>i</code>, and explain why the naive version fails</div><div class="hint-box">💡 Naive <code>[lambda: i …]</code> → all return 2 (late binding). Fix: <code>lambda i=i: i</code>. Be able to say <em>why</em>.</div></div>'
'<div class="exr-block"><div class="exr-title"><span class="cc-badge badge-hard">Hard</span> E12 — <code>once(fn)</code> — run <code>fn</code> the first time only, cache &amp; return that result forever</div><div class="hint-box">💡 Closure with a <code>done</code> flag + <code>result</code>; <code>nonlocal</code> both. Prove <code>fn</code> ran exactly once even across repeated calls.</div></div>'
)

# ══════════════════════════ PART 3 ══════════════════════════
md(
'<div class="info-box"><strong>Part 3:</strong> ML Real-World → Interview Q&amp;A → Code Challenges → Summary</div>'
'<div class="ml-header"><h2>7. ML Real-World Connection</h2></div>'
'<div class="ml-block"><div class="ml-title"><span class="ml-badge">ML 1</span> Pure transform functions over data</div>'
'<div class="body-txt">Preprocessing steps should <em>return</em> new arrays/frames, not mutate inputs — call by object reference means a careless <code>.append</code>/in-place op corrupts a shared split (train/test leakage). Keep transforms pure.</div></div>'
'<div class="ml-block"><div class="ml-title"><span class="ml-badge">ML 2</span> <code>**kwargs</code> for flexible model/config APIs</div>'
'<div class="body-txt"><code>Model(**config)</code>, <code>fit(X, y, **fit_params)</code> — every sklearn estimator and training loop takes a hyperparameter dict spread as keyword arguments. Keyword-only params (<code>*</code>) force callers to name options.</div></div>'
'<div class="ml-block"><div class="ml-title"><span class="ml-badge">ML 3</span> Closures for stateful callbacks</div>'
'<div class="body-txt">A learning-rate scheduler, a running-metric accumulator, or an early-stopping monitor is naturally a closure — it holds state (best loss, step count) across calls via <code>nonlocal</code>, without a class.</div></div>'
'<div class="ml-block"><div class="ml-title"><span class="ml-badge">ML 4</span> Memoization / caching (closure → decorator)</div>'
'<div class="body-txt">Caching expensive feature computations or embeddings is a closure over a <code>cache</code> dict — exactly <code>functools.lru_cache</code>. The <code>*args, **kwargs</code> forwarding pattern is what lets a decorator wrap any model function (Session 6).</div></div>'
'<div class="ml-block"><div class="ml-title"><span class="ml-badge">ML 5</span> The reproducibility traps</div>'
'<div class="body-txt">A mutable-default config (<code>def train(params={...})</code>) mutates across runs — the "why did my learning rate change between experiments?" bug (S1 ML). And <code>if __name__ == "__main__"</code> guards training scripts so importing them for reuse doesn\'t kick off a run.</div></div>'
)

md(
'<div class="interview-header"><h2>8. Interview Questions</h2></div>'
'<div class="sub-header"><h3>8a — Conceptual Q&amp;A</h3></div>'
'<div class="qa-block"><div class="qa-q"><span class="q-num">1</span> What does "first-class function" mean?</div><div class="qa-a">Functions are objects — you can assign them to names, store them in containers, pass them as arguments, and return them. Enables higher-order functions, <code>key=</code> sorts, and decorators.</div></div>'
'<div class="qa-block"><div class="qa-q"><span class="q-num">2</span> Why is a mutable default argument dangerous, and the fix?</div><div class="qa-a">The default is created once at def time and shared across calls, so it accumulates state. Fix: <code>def f(x, acc=None): </code> then <code>if acc is None: acc = []</code> — never <code>acc or []</code> (discards a passed empty list).</div></div>'
'<div class="qa-block"><div class="qa-q"><span class="q-num">3</span> <code>*args</code> vs <code>**kwargs</code>?</div><div class="qa-a"><code>*args</code> collects extra positional arguments into a tuple; <code>**kwargs</code> collects extra keyword arguments into a dict. At a call site they spread an iterable / dict.</div></div>'
'<div class="qa-block"><div class="qa-q"><span class="q-num">4</span> Why positional-only <code>/</code> and keyword-only <code>*</code>?</div><div class="qa-a">API stability (rename positional-only params freely) and clarity (force callers to name flag-like options). Everything before <code>/</code> is positional-only; after <code>*</code>, keyword-only.</div></div>'
'<div class="qa-block"><div class="qa-q"><span class="q-num">5</span> Is Python pass-by-value or pass-by-reference?</div><div class="qa-a">Neither — <strong>call by object reference</strong> (call by sharing). Mutating the passed object is visible to the caller; rebinding the parameter is not.</div></div>'
'<div class="qa-block"><div class="qa-q"><span class="q-num">6</span> What is the LEGB rule?</div><div class="qa-a">Name lookup order: Local → Enclosing → Global → Built-in. The first scope with a match wins.</div></div>'
'<div class="qa-block"><div class="qa-q"><span class="q-num">7</span> When do you need <code>global</code> vs <code>nonlocal</code>?</div><div class="qa-a">To <em>rebind</em> (not just mutate) a name from an inner scope: <code>global</code> for a module-level name, <code>nonlocal</code> for an enclosing-function name.</div></div>'
'<div class="qa-block"><div class="qa-q"><span class="q-num">8</span> What causes <code>UnboundLocalError</code>?</div><div class="qa-a">Assigning a name anywhere in a function makes it local for the whole function, so reading it before that assignment fails — even if a global of the same name exists.</div></div>'
'<div class="qa-block"><div class="qa-q"><span class="q-num">9</span> What is a closure, and how does it keep state?</div><div class="qa-a">An inner function that captures variables from its enclosing scope; those variables stay alive after the outer function returns, stored in <code>fn.__closure__</code> cells. With <code>nonlocal</code> it can update that state.</div></div>'
'<div class="qa-block"><div class="qa-q"><span class="q-num">10</span> Explain the late-binding closure trap and the fix.</div><div class="qa-a">Closures capture the variable, not its value; closures built in a loop all see the final value. Fix: bind the value at definition time with a default arg — <code>lambda i=i: i</code>.</div></div>'
'<div class="qa-block"><div class="qa-q"><span class="q-num">11</span> How does a function return multiple values?</div><div class="qa-a">It returns one object — a <strong>tuple</strong>. <code>return a, b</code> packs <code>(a, b)</code>; the caller unpacks with <code>x, y = f()</code>.</div></div>'
'<div class="qa-block"><div class="qa-q"><span class="q-num">12</span> What is <code>if __name__ == "__main__"</code> for?</div><div class="qa-a"><code>__name__</code> is <code>"__main__"</code> when the file is run directly, else the module name. The guard runs entry-point code only when executed as a script, not when imported.</div></div>'
)

md(
'<div class="sub-header"><h3>8b — Code Challenges (attempt, then expand the solution)</h3></div>'
'<div class="cc-block"><div class="cc-title"><span class="cc-badge badge-easy">Easy</span> C1 — <code>flip(fn)</code>: return a function that calls <code>fn</code> with its two args swapped</div>'
'<details class="sol"><summary>Solution</summary><div class="code-block"><span class="ck">def</span> <span class="cm">flip</span>(fn): <span class="ck">return</span> <span class="ck">lambda</span> a, b: fn(b, a)</div><div class="qa-a"><code>flip(pow)(2, 3)</code> → <code>pow(3, 2)</code> → <code>9</code>. A closure over <code>fn</code>.</div></details></div>'
'<div class="cc-block"><div class="cc-title"><span class="cc-badge badge-easy">Easy</span> C2 — <code>negate(pred)</code>: return the logical NOT of a predicate</div>'
'<details class="sol"><summary>Solution</summary><div class="code-block"><span class="ck">def</span> <span class="cm">negate</span>(pred): <span class="ck">return</span> <span class="ck">lambda</span> *a, **k: <span class="ck">not</span> pred(*a, **k)</div><div class="qa-a"><code>negate(str.isdigit)("a")</code> → <code>True</code>. Forwards any args to the wrapped predicate.</div></details></div>'
'<div class="cc-block"><div class="cc-title"><span class="cc-badge badge-med">Med</span> C3 — <code>count_calls(fn)</code>: wrapper that tracks how many times it was called</div>'
'<details class="sol"><summary>Solution</summary><div class="code-block">'
'<span class="ck">def</span> <span class="cm">count_calls</span>(fn):<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">def</span> <span class="cm">wrapper</span>(*a, **k):<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wrapper.calls += <span class="cn">1</span><br>'
'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">return</span> fn(*a, **k)<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;wrapper.calls = <span class="cn">0</span>       <span class="cc"># state on the function object</span><br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">return</span> wrapper</div>'
'<div class="qa-a">Functions are objects, so you can hang a <code>.calls</code> attribute on the wrapper. The decorator counting pattern.</div></details></div>'
'<div class="cc-block"><div class="cc-title"><span class="cc-badge badge-med">Med</span> C4 — <code>group_by(items, key_fn)</code> → dict of lists</div>'
'<details class="sol"><summary>Solution</summary><div class="code-block">'
'<span class="ck">from</span> collections <span class="ck">import</span> defaultdict<br>'
'<span class="ck">def</span> <span class="cm">group_by</span>(items, key_fn):<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;g = <span class="cm">defaultdict</span>(list)<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">for</span> it <span class="ck">in</span> items: g[key_fn(it)].<span class="cm">append</span>(it)<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">return</span> <span class="cm">dict</span>(g)</div>'
'<div class="qa-a"><code>group_by([1,2,3,4,5], lambda x: x%2)</code> → <code>{1:[1,3,5], 0:[2,4]}</code>. Higher-order function + 2D grouping.</div></details></div>'
'<div class="cc-block"><div class="cc-title"><span class="cc-badge badge-med">Med</span> C5 — <code>with_retry(fn, times)</code>: retry on exception, else re-raise the last</div>'
'<details class="sol"><summary>Solution</summary><div class="code-block">'
'<span class="ck">def</span> <span class="cm">with_retry</span>(fn, times):<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">def</span> <span class="cm">wrapper</span>(*a, **k):<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;last = <span class="ck">None</span><br>'
'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">for</span> _ <span class="ck">in</span> <span class="cm">range</span>(times):<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">try</span>: <span class="ck">return</span> fn(*a, **k)<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">except</span> Exception <span class="ck">as</span> e: last = e<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">raise</span> last<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">return</span> wrapper</div>'
'<div class="qa-a">Closure over <code>fn</code>/<code>times</code>; forwards args. The retry-decorator pattern (Session 6 / 9). Re-raises the last error if all attempts fail.</div></details></div>'
'<div class="cc-block"><div class="cc-title"><span class="cc-badge badge-med">Med</span> C6 — <code>pipe(x, *funcs)</code>: thread a value through functions left-to-right</div>'
'<details class="sol"><summary>Solution</summary><div class="code-block">'
'<span class="ck">def</span> <span class="cm">pipe</span>(x, *funcs):<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">for</span> f <span class="ck">in</span> funcs: x = f(x)<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">return</span> x</div>'
'<div class="qa-a"><code>pipe(3, lambda x: x+1, lambda x: x*2)</code> → <code>8</code>. Eager sibling of <code>compose</code> — applies immediately to a value rather than returning a function.</div></details></div>'
'<div class="cc-block"><div class="cc-title"><span class="cc-badge badge-hard">Hard</span> C7 — <code>curry3(fn)</code>: turn a 3-arg function into <code>f(a)(b)(c)</code></div>'
'<details class="sol"><summary>Solution</summary><div class="code-block"><span class="ck">def</span> <span class="cm">curry3</span>(fn): <span class="ck">return</span> <span class="ck">lambda</span> a: <span class="ck">lambda</span> b: <span class="ck">lambda</span> c: fn(a, b, c)</div><div class="qa-a"><code>curry3(add)(1)(2)(3)</code> → <code>6</code>. Nested closures — each lambda captures one argument until all three are collected.</div></details></div>'
'<div class="cc-block"><div class="cc-title"><span class="cc-badge badge-hard">Hard</span> C8 — <code>make_stack()</code>: return <code>(push, pop)</code> sharing one hidden list</div>'
'<details class="sol"><summary>Solution</summary><div class="code-block">'
'<span class="ck">def</span> <span class="cm">make_stack</span>():<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;items = []<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">def</span> <span class="cm">push</span>(x): items.<span class="cm">append</span>(x)<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">def</span> <span class="cm">pop</span>(): <span class="ck">return</span> items.<span class="cm">pop</span>()<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">return</span> push, pop</div>'
'<div class="qa-a">Two closures over the <strong>same</strong> captured <code>items</code> list — shared private state, no class. <code>push(1); push(2); pop()</code> → <code>2</code>. This is encapsulation via closures.</div></details></div>'
)

md(
'<div class="summary-header"><h2>9. Summary Table — Session 5</h2></div>'
'<table class="summary">'
'<tr><th>Concept</th><th>Why it matters in ML</th><th>Interview frequency</th></tr>'
'<tr><td>First-class functions</td><td>Callbacks, <code>key=</code>, higher-order transforms</td><td><span class="freq-vh">Very High</span></td></tr>'
'<tr><td>Mutable default trap (<code>None</code> sentinel)</td><td>Reproducibility — config not shared across runs</td><td><span class="freq-vh">Very High</span></td></tr>'
'<tr><td><code>*args</code> / <code>**kwargs</code></td><td>Flexible model/config APIs; wrappers</td><td><span class="freq-vh">Very High</span></td></tr>'
'<tr><td>Call by object reference</td><td>Avoiding silent data corruption / leakage</td><td><span class="freq-h">High</span></td></tr>'
'<tr><td>LEGB / global / nonlocal</td><td>Reasoning about state; stateful closures</td><td><span class="freq-h">High</span></td></tr>'
'<tr><td>Closures</td><td>Schedulers, accumulators, caches without a class</td><td><span class="freq-vh">Very High</span></td></tr>'
'<tr><td>Late-binding trap</td><td>Correct callbacks/handlers built in loops</td><td><span class="freq-h">High</span></td></tr>'
'<tr><td>Positional-only / keyword-only</td><td>Clear, stable library signatures</td><td><span class="freq-m">Medium</span></td></tr>'
'<tr><td><code>__name__ == "__main__"</code></td><td>Importable, reusable training scripts</td><td><span class="freq-m">Medium</span></td></tr>'
'</table>'
'<hr class="divider">'
'<div style="background:#1e1e2e; border-left:4px solid #a6e3a1; padding:14px 18px; border-radius:8px; font-family:monospace; color:#cdd6f4;">'
'<strong style="color:#a6e3a1">✅ Session 5 complete.</strong> Functions, scope &amp; closures end to end: '
'argument model, <code>*args</code>/<code>**kwargs</code>, LEGB / global / nonlocal, closures &amp; late '
'binding, <code>__main__</code>, 4 examples, 5 edge cases, 8 golden rules, 8 traps, 12 exercises, ML '
'connections, 12 conceptual Q&amp;A, 8 code challenges, summary table.<br>'
'<span style="color:#6c7086">Next — Session 6: Decorators (function wrapping, <code>functools.wraps</code>, '
'practical decorator patterns) — the direct payoff of closures + <code>*args</code>/<code>**kwargs</code> forwarding.</span></div>'
)

nb = new_notebook(cells=cells)
nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
nb.metadata["language_info"] = {"name": "python"}
nbf.write(nb, "theory.ipynb")
print("wrote theory.ipynb with", len(cells), "cells")
