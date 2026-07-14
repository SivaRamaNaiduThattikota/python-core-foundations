# Builder for Session 3 - Strings, theory.ipynb (Part 1, Chunk A).
# Matches the course build pipeline (nbformat) and the Catppuccin Mocha UI system.
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
  table.methods { width:100%; border-collapse:collapse; font-family:'Segoe UI',sans-serif; font-size:0.88em; margin:12px 0; }
  table.methods th { background:#313244; color:#cba6f7; padding:9px 14px; text-align:left; border:1px solid #45475a; }
  table.methods td { background:#1e1e2e; color:#cdd6f4; padding:8px 14px; border:1px solid #313244; vertical-align:top; line-height:1.6; }
  table.methods tr:hover td { background:#252540; }
  table.methods td:first-child { color:#89dceb; font-family:'Courier New',monospace; font-size:0.86em; white-space:nowrap; }
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
'<h1 class="main-title">🐍 Session 3 — Strings</h1>'
'<div class="info-box"><strong>Part 1:</strong> Theory → Example → Edge Cases &nbsp;·&nbsp; '
'delivered in chunks (big method surface).</div>'
'<div class="chunk-badge">Part 1 · Chunk A — The Immutable-Sequence Model + Construction + Core Methods</div>'
'<div class="theory-box" style="border-left-color:#cba6f7;">'
'Strings are the third sequence type, and they sit exactly on the seam of Session 2: a string is '
'<strong style="color:#89b4fa">indexable and sliceable like a list</strong> (2A) but '
'<strong style="color:#89b4fa">immutable and hashable like a tuple</strong> (2B). Everything in this '
'session — the method surface, f-strings, and the famous <code>+=</code> performance trap — falls out '
'of that one fact.</div>'
)

# ── 3.1 The model ──────────────────────────────────────────────────────
md(
'<div class="part-header"><h2>1. Theory</h2></div>'
'<h3 class="sub">🔹 3.1 &nbsp;A string is an immutable sequence of characters</h3>'
'<div class="theory-box">'
'<p style="margin:0 0 10px 0">A <code>str</code> is an ordered sequence of Unicode characters. You can '
'<strong>index</strong> and <strong>slice</strong> it (2A mechanics), but you '
'<strong style="color:#89b4fa">cannot change it in place</strong> (2B immutability). Any "edit" builds a '
'<strong>new</strong> string object and rebinds your name to it.</p>'
'<p style="margin:0">There is no separate "char" type — indexing a string returns another string of '
'length 1.</p></div>'
'<div class="info-box">💡 <strong>SQL / Power BI anchor:</strong> like a text value in a column — you '
'never mutate a cell\'s characters; <code>REPLACE()</code> / DAX <code>SUBSTITUTE()</code> compute and '
'return a <em>new</em> string.</div>'
'<div class="code-block">'
's = <span class="cs">"hello"</span><br>'
's[<span class="cn">0</span>] = <span class="cs">"H"</span>        <span class="cc"># attempt to edit in place</span><br>'
's = <span class="cs">"H"</span> + s[<span class="cn">1</span>:]    <span class="cc"># rebuild -> a brand-new object</span></div>'
'<div class="output-block">'
"TypeError: 'str' object does not support item assignment<br>"
'&gt;&gt;&gt; s<br>&#39;Hello&#39;</div>'
'<div class="mut-grid">'
'<div class="mut-card mc-imm"><div class="mc-title">🔒 Like a tuple (2B)</div>'
'<div class="mc-body">immutable — no item assign<br>hashable → dict key / set member<br>every "change" = new object</div></div>'
'<div class="mut-card mc-mut"><div class="mc-title">🔢 Like a list (2A)</div>'
'<div class="mc-body">indexable&nbsp;&nbsp; s[0], s[-1]<br>sliceable&nbsp;&nbsp; s[1:4], s[::-1]<br>iterable&nbsp;&nbsp; for ch in s</div></div>'
'</div>'
)

# ── 3.2 identity & interning ───────────────────────────────────────────
md(
'<h3 class="sub">🔹 3.2 &nbsp;Immutability → new objects, hashability, interning</h3>'
'<div class="theory-box">Because a string can\'t change, three things follow (all Session 1 callbacks): '
'"changing" it produces a <strong>new object</strong> with a new <code>id</code>; a string is '
'<strong>hashable</strong> (valid dict key / set member); and CPython <strong>interns</strong> some '
'strings, so identical literals may share one object.</div>'
'<div class="code-block">'
's = <span class="cs">"abc"</span><br>'
'<span class="cm">print</span>(<span class="cm">id</span>(s))<br>'
's = s + <span class="cs">"d"</span>          <span class="cc"># NEW object -> different id</span><br>'
'<br>'
'a = <span class="cs">"data"</span>; b = <span class="cs">"data"</span><br>'
'<span class="cm">print</span>(a <span class="ck">is</span> b)                <span class="cc"># True  -> interned literals share one object</span><br>'
'x = <span class="cs">""</span>.<span class="cm">join</span>([<span class="cs">"da"</span>, <span class="cs">"ta"</span>])<br>'
'<span class="cm">print</span>(x == a, x <span class="ck">is</span> a)      <span class="cc"># True False -> equal value, different object</span></div>'
'<div class="output-block">same id after +? False<br>a is b: True<br>built == a: True | built is a: False</div>'
'<div class="why-box"><strong>Why it matters (S1 callback):</strong> never compare string values with '
'<code>is</code> — interning is an implementation detail. Use <code>==</code> for value, <code>is</code> '
'only for identity / <code>None</code>. Same lesson as the small-int cache in Session 1.</div>'
)

# ── 3.3 indexing & slicing ─────────────────────────────────────────────
md(
'<h3 class="sub">🔹 3.3 &nbsp;Indexing &amp; slicing (identical to 2A)</h3>'
'<div class="theory-box">Same <code>[start:stop:step]</code> mechanics as lists — stop is exclusive, '
'negatives count from the end, a negative step walks backward. <code>s[::-1]</code> is the canonical '
'string reverse.</div>'
'<div class="code-block">'
's = <span class="cs">"python"</span><br>'
'<span class="cm">print</span>(s[<span class="cn">0</span>], s[-<span class="cn">1</span>], s[<span class="cn">1</span>:<span class="cn">4</span>], s[::-<span class="cn">1</span>], s[::<span class="cn">2</span>])</div>'
'<div class="output-block">p n yth nohtyp pto</div>'
'<div class="note-box">💡 Slicing a string returns a <strong>new</strong> string (immutability again). '
'Out-of-range <em>slices</em> clamp safely to <code>""</code>; out-of-range <em>indexing</em> raises '
'<code>IndexError</code> — the same asymmetry as lists (2A Edge 4).</div>'
)

# ── 3.4 construction ───────────────────────────────────────────────────
md(
'<h3 class="sub">🔹 3.4 &nbsp;Construction — the ways to build a string</h3>'
'<div class="code-block">'
'<span class="cs">"hi"</span>&nbsp;&nbsp;<span class="cs">\'hi\'</span>&nbsp;&nbsp;<span class="cs">"""multi\\nline"""</span>   <span class="cc"># literals (single/double/triple)</span><br>'
'<span class="cm">str</span>(<span class="cn">42</span>)                 <span class="cc"># \'42\'  -> any object to its string form</span><br>'
'<span class="cs">""</span>.<span class="cm">join</span>([<span class="cs">"a"</span>,<span class="cs">"b"</span>,<span class="cs">"c"</span>])     <span class="cc"># \'abc\' -> THE way to build from pieces (Chunk C: the += trap)</span><br>'
'<span class="cs">"-"</span>.<span class="cm">join</span>([<span class="cs">"2024"</span>,<span class="cs">"01"</span>,<span class="cs">"15"</span>]) <span class="cc"># \'2024-01-15\'</span><br>'
'<span class="cs">"ab"</span> * <span class="cn">3</span>               <span class="cc"># \'ababab\' -> repeat (safe: strings are immutable)</span><br>'
'<span class="cm">chr</span>(<span class="cn">65</span>), <span class="cm">ord</span>(<span class="cs">"A"</span>)      <span class="cc"># \'A\', 65 -> codepoint &lt;-&gt; char</span><br>'
'<span class="ck">r</span><span class="cs">"C:\\new\\test"</span>          <span class="cc"># raw string -> backslashes stay literal</span></div>'
'<div class="output-block">42<br>abc<br>2024-01-15<br>ababab<br>A 65<br>C:\\new\\test</div>'
'<div class="info-box">💡 <code>r"..."</code> (raw) is the fix for Windows paths and regex — no escape '
'processing, so <code>\\n</code> is a backslash + n, not a newline.</div>'
)

# ── 3.5 core method surface ────────────────────────────────────────────
md(
'<h3 class="sub">🔹 3.5 &nbsp;The core method surface — reading, searching, testing</h3>'
'<div class="theory-box">Every string method <strong style="color:#89b4fa">returns a new string (or a '
'number/bool)</strong> and <strong>never mutates</strong> — because strings are immutable. '
'(Transformation methods <code>split</code>/<code>replace</code> and formatting come in Chunk B.)</div>'
'<table class="methods">'
'<tr><th>Method</th><th>Does</th><th>Returns / note</th></tr>'
'<tr><td>.upper() .lower()<br>.title() .capitalize()<br>.swapcase()</td><td>case transforms</td><td>new string</td></tr>'
'<tr><td>.find(sub)</td><td>index of first match</td><td><b>-1</b> if absent (safe)</td></tr>'
'<tr><td>.index(sub)</td><td>index of first match</td><td><b>ValueError</b> if absent (loud)</td></tr>'
'<tr><td>.rfind(sub) / .count(sub)</td><td>last match / how many</td><td>int</td></tr>'
'<tr><td>.startswith() .endswith()</td><td>prefix / suffix test</td><td>bool</td></tr>'
'<tr><td>sub <b>in</b> s</td><td>substring membership</td><td>bool — O(n·m)</td></tr>'
'<tr><td>.isdigit() .isalpha()<br>.isalnum() .isspace()</td><td>content predicates</td><td>bool</td></tr>'
'<tr><td>.strip() .lstrip() .rstrip()</td><td>trim from ends</td><td>new string</td></tr>'
'</table>'
'<div class="code-block">'
's = <span class="cs">"Hello World"</span><br>'
's.<span class="cm">upper</span>(), s.<span class="cm">lower</span>(), s.<span class="cm">title</span>(), s.<span class="cm">swapcase</span>()<br>'
'<br>'
'b = <span class="cs">"banana"</span><br>'
'b.<span class="cm">find</span>(<span class="cs">"na"</span>), b.<span class="cm">find</span>(<span class="cs">"z"</span>), b.<span class="cm">rfind</span>(<span class="cs">"na"</span>), b.<span class="cm">count</span>(<span class="cs">"na"</span>)<br>'
'b.<span class="cm">index</span>(<span class="cs">"z"</span>)      <span class="cc"># ValueError: substring not found</span><br>'
'b.<span class="cm">startswith</span>(<span class="cs">"ban"</span>), <span class="cs">"nan"</span> <span class="ck">in</span> b<br>'
'<br>'
'<span class="cs">"123"</span>.<span class="cm">isdigit</span>(), <span class="cs">"abc"</span>.<span class="cm">isalpha</span>(), <span class="cs">"   "</span>.<span class="cm">isspace</span>()</div>'
'<div class="output-block">'
"('HELLO WORLD', 'hello world', 'Hello World', 'hELLO wORLD')<br>"
'find na: 2 | find z: -1 | rfind na: 4 | count na: 2<br>'
'ValueError: substring not found<br>'
'True True<br>'
'True True True</div>'
'<div class="warn-box">⚠ <strong>Preview trap (full treatment in Chunk C):</strong> '
'<code>.strip("mip")</code> removes any <em>characters in that set</em> from both ends — it is '
'<strong>not</strong> substring removal. <code>"mississippi".strip("mip")</code> → <code>\'ssiss\'</code>, '
'not <code>\'ssissi\'</code>.</div>'
)

# ── Key takeaways + go prompt ──────────────────────────────────────────
md(
'<hr class="divider">'
'<div style="background:#1e1e2e; border-left:4px solid #cba6f7; padding:16px 20px; border-radius:8px; '
'font-family:monospace; color:#cdd6f4;">'
'<h4 style="color:#cba6f7; margin:0 0 12px 0;">🔑 Chunk A — Key Takeaways</h4>'
'<ul style="margin:0; padding-left:20px; line-height:2.1">'
'<li>A string is an <strong>immutable sequence</strong>: indexable/sliceable like a list, frozen &amp; hashable like a tuple</li>'
'<li>Every "edit" builds a <strong>new object</strong>; methods never mutate</li>'
'<li><code>==</code> for value, <code>is</code> only for identity — interning is not a guarantee</li>'
'<li><code>.find</code> returns <code>-1</code>; <code>.index</code> raises — choose by whether absence is normal</li>'
'<li><code>.strip(chars)</code> is a <strong>character set</strong>, not a substring</li>'
'</ul></div>'
)

# ══════════════════════════ CHUNK B ══════════════════════════
# ── 3.6 transformation ─────────────────────────────────────────────────
md(
'<div class="chunk-badge">Part 1 · Chunk B — Transformation · Formatting · Encoding</div>'
'<h3 class="sub">🔹 3.6 &nbsp;Splitting, joining, replacing — the parsing workhorses</h3>'
'<div class="theory-box"><code>split</code> and <code>join</code> are inverses: <code>split</code> '
'turns a string into a list of pieces, <code>join</code> stitches an iterable back into a string. Every '
'method here <strong style="color:#89b4fa">returns a new object</strong> — nothing mutates.</div>'
'<table class="methods">'
'<tr><th>Method</th><th>Does</th><th>Returns / note</th></tr>'
'<tr><td>.split(sep=None)</td><td>string → list of pieces</td><td>no arg = split on whitespace runs, drop empties</td></tr>'
'<tr><td>.splitlines()</td><td>split on line boundaries</td><td>list of lines</td></tr>'
'<tr><td>sep.join(iterable)</td><td>iterable of str → string</td><td>the O(n) string builder</td></tr>'
'<tr><td>.replace(old, new[, n])</td><td>substitute substrings</td><td>optional count limit</td></tr>'
'<tr><td>.partition(sep)</td><td>split once at first sep</td><td>3-tuple (before, sep, after)</td></tr>'
'<tr><td>.removeprefix() .removesuffix()</td><td>strip an exact edge (3.9+)</td><td>substring, not charset</td></tr>'
'<tr><td>.zfill(w) .center() .ljust() .rjust()</td><td>pad to width</td><td>new string</td></tr>'
'</table>'
'<div class="code-block">'
'<span class="cs">"a,b,c"</span>.<span class="cm">split</span>(<span class="cs">","</span>)         <span class="cc"># [\'a\', \'b\', \'c\']</span><br>'
'<span class="cs">"  a  b   c "</span>.<span class="cm">split</span>()     <span class="cc"># [\'a\', \'b\', \'c\']  no arg -> whitespace, no empties</span><br>'
'<span class="cs">"a,b,,c"</span>.<span class="cm">split</span>(<span class="cs">","</span>)       <span class="cc"># [\'a\', \'b\', \'\', \'c\']  explicit sep KEEPS empties</span><br>'
'<span class="cs">","</span>.<span class="cm">join</span>([<span class="cs">"a"</span>,<span class="cs">"b"</span>,<span class="cs">"c"</span>])     <span class="cc"># \'a,b,c\'</span><br>'
'<span class="cs">"aXbXc"</span>.<span class="cm">replace</span>(<span class="cs">"X"</span>,<span class="cs">"-"</span>)   <span class="cc"># \'a-b-c\'</span><br>'
'<span class="cs">"a-b-c"</span>.<span class="cm">replace</span>(<span class="cs">"-"</span>,<span class="cs">"_"</span>,<span class="cn">1</span>) <span class="cc"># \'a_b-c\'  only first</span><br>'
'<span class="cs">"user@example.com"</span>.<span class="cm">partition</span>(<span class="cs">"@"</span>)  <span class="cc"># (\'user\', \'@\', \'example.com\')</span><br>'
'<span class="cs">"file.txt"</span>.<span class="cm">removesuffix</span>(<span class="cs">".txt"</span>)   <span class="cc"># \'file\'</span><br>'
'<span class="cs">"42"</span>.<span class="cm">zfill</span>(<span class="cn">5</span>)               <span class="cc"># \'00042\'</span></div>'
'<div class="output-block">'
"['a', 'b', 'c']<br>['a', 'b', 'c']<br>['a', 'b', '', 'c']<br>a,b,c<br>a-b-c<br>a_b-c<br>"
"('user', '@', 'example.com')<br>file<br>00042</div>"
'<div class="note-box">💡 <code>partition</code> beats <code>split(sep, 1)</code> when a separator might be '
'missing: it always returns a 3-tuple (the sep and after are empty if not found), so unpacking never '
'breaks. SQL/Power BI anchor: <code>split</code>/<code>join</code> are text-to-columns and CONCAT.</div>'
)

# ── 3.7 f-strings & format spec ────────────────────────────────────────
md(
'<h3 class="sub">🔹 3.7 &nbsp;f-strings &amp; the format spec mini-language</h3>'
'<div class="theory-box">An f-string (<code>f"..."</code>) embeds expressions in <code>{ }</code>. After a '
'colon comes the <strong>format spec</strong>: precision, thousands separators, alignment, width, and '
'number bases. This is the modern replacement for <code>%</code> and <code>str.format()</code>.</div>'
'<table class="methods">'
'<tr><th>Spec</th><th>Meaning</th><th>Example → result</th></tr>'
'<tr><td>:.2f</td><td>fixed precision</td><td><code>f"{3.14159:.2f}"</code> → \'3.14\'</td></tr>'
'<tr><td>:,</td><td>thousands separator</td><td><code>f"{1234567:,}"</code> → \'1,234,567\'</td></tr>'
'<tr><td>:&gt;10 :&lt;10 :^10</td><td>right / left / center in width 10</td><td><code>f"{\'hi\':^10}"</code> → \'&nbsp;&nbsp;&nbsp;&nbsp;hi&nbsp;&nbsp;&nbsp;&nbsp;\'</td></tr>'
'<tr><td>:08.2f</td><td>zero-pad + precision</td><td><code>f"{3.14159:08.2f}"</code> → \'00003.14\'</td></tr>'
'<tr><td>:.1%</td><td>percent</td><td><code>f"{0.8734:.1%}"</code> → \'87.3%\'</td></tr>'
'<tr><td>:#x&nbsp; :b&nbsp; :o</td><td>hex / binary / octal</td><td><code>f"{255:#x}"</code> → \'0xff\'</td></tr>'
'<tr><td>{x=}</td><td>debug (name + value, 3.8+)</td><td><code>f"{x=}"</code> → \'x=42\'</td></tr>'
'</table>'
'<div class="code-block">'
'name, age = <span class="cs">"Siva"</span>, <span class="cn">27</span><br>'
'<span class="cm">print</span>(<span class="cs">f"{name} is {age}"</span>)      <span class="cc"># Siva is 27</span><br>'
'<span class="cm">print</span>(<span class="cs">f"{3.14159:.2f}"</span>)         <span class="cc"># 3.14</span><br>'
'<span class="cm">print</span>(<span class="cs">f"{1234567:,}"</span>)           <span class="cc"># 1,234,567</span><br>'
'<span class="cm">print</span>(<span class="cs">f"{0.8734:.1%}"</span>)          <span class="cc"># 87.3%</span><br>'
'<span class="cm">print</span>(<span class="cs">f"{255:#x}"</span>)             <span class="cc"># 0xff</span></div>'
'<div class="output-block">Siva is 27<br>3.14<br>1,234,567<br>87.3%<br>0xff</div>'
'<div class="info-box">💡 <strong>SQL / Power BI anchor:</strong> the format spec is Python\'s '
'<code>FORMAT()</code> — <code>:.1%</code> is a percentage format string, <code>:,</code> is a thousands '
'format, alignment is column padding in a report.</div>'
)

# ── 3.8 str vs bytes / encoding ────────────────────────────────────────
md(
'<h3 class="sub">🔹 3.8 &nbsp;str vs bytes — text vs raw octets</h3>'
'<div class="theory-box"><code>str</code> is <strong>Unicode text</strong> — what you compute with. '
'<code>bytes</code> is <strong>raw octets</strong> — what lives in files, sockets, and API payloads. '
'<code>.encode()</code> turns text → bytes, <code>.decode()</code> turns bytes → text. Always name the '
'codec (<code>"utf-8"</code>).</div>'
'<div class="mut-grid">'
'<div class="mut-card mc-imm"><div class="mc-title">📝 str — text</div>'
'<div class="mc-body">Unicode characters<br>what your code manipulates<br>.encode("utf-8") → bytes</div></div>'
'<div class="mut-card mc-mut"><div class="mc-title">💾 bytes — octets</div>'
'<div class="mc-body">raw 0–255 values<br>files / network / APIs<br>.decode("utf-8") → str</div></div>'
'</div>'
'<div class="code-block">'
's = <span class="cs">"café"</span><br>'
'b = s.<span class="cm">encode</span>(<span class="cs">"utf-8"</span>)     <span class="cc"># b\'caf\\xc3\\xa9\'</span><br>'
'<span class="cm">len</span>(s), <span class="cm">len</span>(b)          <span class="cc"># (4, 5)  -> é is 1 char but 2 bytes in UTF-8</span><br>'
'b.<span class="cm">decode</span>(<span class="cs">"utf-8"</span>)      <span class="cc"># \'café\'</span><br>'
'<span class="cn">b</span><span class="cs">"\\xff"</span>.<span class="cm">decode</span>(<span class="cs">"utf-8"</span>)  <span class="cc"># UnicodeDecodeError -> wrong codec / corrupt bytes</span></div>'
'<div class="output-block">'
"b'caf\\xc3\\xa9'<br>len str: 4 | len bytes: 5<br>café<br>"
"UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0</div>"
'<div class="why-box"><strong>Why it matters:</strong> <code>len(str)</code> counts characters, '
'<code>len(bytes)</code> counts bytes — they differ for non-ASCII. Mismatched codecs are the root of '
'mojibake (<code>café</code> → <code>cafÃ©</code>) and <code>UnicodeDecodeError</code> when reading '
'files/APIs. Specify the encoding explicitly, every time.</div>'
'<hr class="divider">'
'<div style="background:#1e1e2e; border-left:4px solid #cba6f7; padding:16px 20px; border-radius:8px; '
'font-family:monospace; color:#cdd6f4;">'
'<h4 style="color:#cba6f7; margin:0 0 12px 0;">🔑 Chunk B — Key Takeaways</h4>'
'<ul style="margin:0; padding-left:20px; line-height:2.1">'
'<li><code>split</code>/<code>join</code> are inverses; <code>join</code> is the O(n) way to build strings</li>'
'<li><code>split()</code> (no arg) drops empties on whitespace; <code>split(sep)</code> keeps them</li>'
'<li>f-string format spec: <code>:.2f</code> <code>:,</code> <code>:&gt;10</code> <code>:.1%</code> <code>:#x</code></li>'
'<li><code>str</code> = text, <code>bytes</code> = octets; bridge with <code>.encode</code>/<code>.decode</code>, always name the codec</li>'
'</ul></div>'
)

# ══════════════════════════ CHUNK C ══════════════════════════
# ── 2. Examples ────────────────────────────────────────────────────────
md(
'<div class="chunk-badge">Part 1 · Chunk C — Examples &amp; Edge Cases</div>'
'<div class="ex-header"><h2>2. Example</h2></div>'
'<div class="ex-block"><div class="ex-title"><span class="ex-badge">Ex 1</span> Normalize &amp; tokenize (the NLP first step)</div>'
'<div class="code-block">'
'text = <span class="cs">"  The CAT sat ON the Mat  "</span><br>'
'tokens = text.<span class="cm">strip</span>().<span class="cm">lower</span>().<span class="cm">split</span>()<br>'
'<span class="cm">print</span>(tokens)</div>'
'<div class="output-block">[\'the\', \'cat\', \'sat\', \'on\', \'the\', \'mat\']</div>'
'<div class="note-box">Chained methods each return a new string; <code>.split()</code> with no arg handles '
'the messy whitespace for free. This is the exact pre-tokenization step before a Counter/vocab (2D).</div></div>'
'<div class="ex-block"><div class="ex-title"><span class="ex-badge">Ex 2</span> CSV round-trip — join out, split back</div>'
'<div class="code-block">'
'row = <span class="cs">","</span>.<span class="cm">join</span>([<span class="cs">"id1"</span>, <span class="cs">"Siva"</span>, <span class="cs">"ML"</span>])   <span class="cc"># \'id1,Siva,ML\'</span><br>'
'fields = row.<span class="cm">split</span>(<span class="cs">","</span>)                 <span class="cc"># [\'id1\', \'Siva\', \'ML\']</span></div>'
'<div class="output-block">id1,Siva,ML<br>[\'id1\', \'Siva\', \'ML\']</div></div>'
'<div class="ex-block"><div class="ex-title"><span class="ex-badge">Ex 3</span> A formatted metrics report (f-string alignment)</div>'
'<div class="code-block">'
'metrics = {<span class="cs">"precision"</span>: <span class="cn">0.8734</span>, <span class="cs">"recall"</span>: <span class="cn">0.912</span>, <span class="cs">"f1"</span>: <span class="cn">0.892</span>}<br>'
'<span class="ck">for</span> k, v <span class="ck">in</span> metrics.<span class="cm">items</span>():<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="cm">print</span>(<span class="cs">f"{k:&lt;10}{v:&gt;7.1%}"</span>)</div>'
'<div class="output-block">precision   87.3%<br>recall      91.2%<br>f1          89.2%</div>'
'<div class="note-box"><code>:&lt;10</code> left-pads the label, <code>:&gt;7.1%</code> right-aligns a '
'1-decimal percentage — a clean aligned table with no manual spacing.</div></div>'
'<div class="ex-block"><div class="ex-title"><span class="ex-badge">Ex 4</span> Parse "key : value" config lines with partition</div>'
'<div class="code-block">'
'line = <span class="cs">"timeout : 30"</span><br>'
'k, _, v = line.<span class="cm">partition</span>(<span class="cs">":"</span>)<br>'
'<span class="cm">print</span>(k.<span class="cm">strip</span>(), v.<span class="cm">strip</span>())      <span class="cc"># timeout 30</span></div>'
'<div class="output-block">timeout 30</div>'
'<div class="note-box"><code>partition</code> + <code>strip</code> is the robust one-liner for '
'<code>key: value</code> parsing — survives missing separators and stray spaces.</div></div>'
)

# ── 3. Edge Cases ──────────────────────────────────────────────────────
md(
'<div class="warn-header"><h2>3. Edge Cases</h2></div>'
'<p style="color:#cdd6f4;font-family:\'Segoe UI\',sans-serif;font-size:0.92em;margin:0 0 12px 0">All outputs verified by running.</p>'
'<div class="edge-block"><div class="edge-title"><span class="edge-badge">Edge 1</span> The <code>+=</code> string-building trap (2A accumulator callback)</div>'
'<div class="code-block">'
'<span class="cc"># 60,000 single-char appends</span><br>'
'acc = <span class="cs">""</span><br>'
'<span class="ck">for</span> _ <span class="ck">in</span> <span class="cm">range</span>(<span class="cn">60000</span>): acc += <span class="cs">"x"</span>      <span class="cc"># rebuilds the string repeatedly</span><br>'
'parts = []; <span class="ck">for</span> _ <span class="ck">in</span> <span class="cm">range</span>(<span class="cn">60000</span>): parts.<span class="cm">append</span>(<span class="cs">"x"</span>)<br>'
'res = <span class="cs">""</span>.<span class="cm">join</span>(parts)               <span class="cc"># build a list, join ONCE</span></div>'
'<div class="output-block">concat += :     92.7 ms<br>list+join :      8.2 ms   &lt;- ~11x faster here</div>'
'<div class="why-box"><strong>Why it matters:</strong> because strings are immutable, <code>+=</code> in a '
'loop conceptually rebuilds the whole string each time — the O(n²) accumulator trap from 2A, now in string '
'form. <strong>Honest nuance:</strong> CPython has a special in-place optimization that shrinks the gap '
'(so it\'s not always full quadratic), but it\'s fragile and not a language guarantee. '
'<code>"".join(list)</code> is the portable O(n) fix — always.</div></div>'
'<div class="edge-block"><div class="edge-title"><span class="edge-badge">Edge 2</span> <code>.strip(chars)</code> is a character SET, not a substring</div>'
'<div class="code-block">'
'<span class="cs">"mississippi"</span>.<span class="cm">strip</span>(<span class="cs">"mip"</span>)      <span class="cc"># \'ssiss\'  -> strips any of m/i/p from both ends</span><br>'
'<span class="cs">"https://x"</span>.<span class="cm">strip</span>(<span class="cs">"htps:/"</span>)    <span class="cc"># \'x\'      -> NOT "remove the prefix https://"</span></div>'
'<div class="output-block">ssiss<br>x</div>'
'<div class="why-box"><strong>Why it matters:</strong> <code>strip</code> removes leading/trailing '
'characters that are <em>in the set</em>, from both ends, until it hits one that isn\'t. To remove an exact '
'prefix/suffix use <code>.removeprefix()</code> / <code>.removesuffix()</code> (3.9+). This mangles URLs and '
'filenames constantly.</div></div>'
'<div class="edge-block"><div class="edge-title"><span class="edge-badge">Edge 3</span> <code>.split()</code> vs <code>.split(" ")</code> on runs of spaces</div>'
'<div class="code-block">'
'<span class="cs">"a  b"</span>.<span class="cm">split</span>()        <span class="cc"># [\'a\', \'b\']       collapses whitespace, no empties</span><br>'
'<span class="cs">"a  b"</span>.<span class="cm">split</span>(<span class="cs">" "</span>)     <span class="cc"># [\'a\', \'\', \'b\']  explicit sep -> empty string between the two spaces</span></div>'
'<div class="output-block">[\'a\', \'b\'] | [\'a\', \'\', \'b\']</div>'
'<div class="why-box"><strong>Why it matters:</strong> no-arg <code>split()</code> is what you almost always '
'want for human text (any whitespace, no empty tokens). An explicit separator is literal — double spaces '
'produce empty strings you then have to filter.</div></div>'
'<div class="edge-block"><div class="edge-title"><span class="edge-badge">Edge 4</span> <code>is</code> vs <code>==</code> — interning is not a guarantee</div>'
'<div class="code-block">'
'a = <span class="cs">"hi"</span>; b = <span class="cs">"hi"</span><br>'
'built = <span class="cs">"h"</span> + <span class="cs">"i"</span>.<span class="cm">upper</span>().<span class="cm">lower</span>()<br>'
'<span class="cm">print</span>(a <span class="ck">is</span> b)              <span class="cc"># True  -> both interned literals</span><br>'
'<span class="cm">print</span>(built == a, built <span class="ck">is</span> a) <span class="cc"># True False -> equal value, different object</span></div>'
'<div class="output-block">True<br>True False</div>'
'<div class="why-box"><strong>Why it matters:</strong> S1\'s lesson repeats — compare string values with '
'<code>==</code>, never <code>is</code>. Runtime-built strings usually aren\'t interned, so <code>is</code> '
'silently returns False even when the text matches.</div></div>'
'<div class="edge-block"><div class="edge-title"><span class="edge-badge">Edge 5</span> Methods return a new string — you must capture it</div>'
'<div class="code-block">'
'orig = <span class="cs">"aaa"</span><br>'
'orig.<span class="cm">replace</span>(<span class="cs">"a"</span>, <span class="cs">"b"</span>)      <span class="cc"># result DISCARDED -> orig unchanged</span><br>'
'new = orig.<span class="cm">replace</span>(<span class="cs">"a"</span>, <span class="cs">"b"</span>) <span class="cc"># capture it</span><br>'
'<span class="cm">print</span>(orig, new)               <span class="cc"># aaa bbb</span></div>'
'<div class="output-block">aaa bbb</div>'
'<div class="why-box"><strong>Why it matters:</strong> the immutable cousin of 2A\'s "mutating methods return '
'None" trap. Here the method returns a fixed string and <em>you</em> silently drop it if you don\'t assign. '
'<code>s.strip()</code> on its own line does nothing.</div></div>'
'<div class="edge-block"><div class="edge-title"><span class="edge-badge">Edge 6</span> Repeat / index oddities</div>'
'<div class="code-block">'
'<span class="cs">"ab"</span> * <span class="cn">0</span>, <span class="cs">"ab"</span> * -<span class="cn">2</span>   <span class="cc"># (\'\', \'\')  zero/negative repeat -> empty</span><br>'
'<span class="cs">"hello"</span>[<span class="cn">0</span>][<span class="cn">0</span>][<span class="cn">0</span>]      <span class="cc"># \'h\'  a char is a str, so indexing chains forever</span></div>'
'<div class="output-block">(\'\', \'\')<br>h</div>'
'<div class="why-box"><strong>Why it matters:</strong> <code>s * n</code> with <code>n &lt;= 0</code> gives '
'<code>""</code> (no error) — a silent empty when a count goes wrong. And since there is no char type, '
'<code>s[i]</code> is a length-1 string you can keep indexing.</div></div>'
'<hr class="divider">'
'<div class="info-box">📎 <strong>End of Part 1</strong> (Chunks A–C: model, construction, method surface, '
'formatting, encoding, 4 examples, 6 edge cases). <strong>Part 2</strong> — Golden Rules → Common Traps → '
'Exercise. <strong>Part 3</strong> — ML Real-World → Interview Q&amp;A → Summary Table.</div>'
)

# ══════════════════════════ PART 2 ══════════════════════════
# ── 4. Golden Rules ────────────────────────────────────────────────────
md(
'<div class="info-box"><strong>Part 2:</strong> Golden Rules → Common Traps → Exercise</div>'
'<div class="part-header"><h2>4. Golden Rules</h2></div>'
'<div class="rule-block"><div class="rule-title"><span class="rule-badge">Rule 1</span> Build strings with <code>"".join(iterable)</code>, never <code>+=</code> in a loop.</div>'
'<div class="body-txt"><code>join</code> is O(n); repeated <code>+=</code> risks O(n²). Collect pieces in a list, join once.</div></div>'
'<div class="rule-block"><div class="rule-title"><span class="rule-badge">Rule 2</span> <code>==</code> for value, <code>is</code> only for identity / <code>None</code>.</div>'
'<div class="body-txt">Interning is an implementation detail — never compare string <em>values</em> with <code>is</code>.</div></div>'
'<div class="rule-block"><div class="rule-title"><span class="rule-badge">Rule 3</span> Capture the result — methods return a new string, they never mutate.</div>'
'<div class="body-txt"><code>s.strip()</code> on its own line does nothing; write <code>s = s.strip()</code>.</div></div>'
'<div class="rule-block"><div class="rule-title"><span class="rule-badge">Rule 4</span> <code>.find()</code> when absence is normal (-1); <code>.index()</code> when it must exist (raises).</div>'
'<div class="body-txt">The string version of dict <code>[]</code> vs <code>.get()</code> — fail loud vs safe.</div></div>'
'<div class="rule-block"><div class="rule-title"><span class="rule-badge">Rule 5</span> <code>.split()</code> (no arg) for human text; explicit <code>split(sep)</code> only for exact delimiters.</div>'
'<div class="body-txt">No-arg collapses whitespace and drops empties; explicit sep keeps empty fields.</div></div>'
'<div class="rule-block"><div class="rule-title"><span class="rule-badge">Rule 6</span> Prefer f-strings over <code>%</code> and <code>.format()</code>.</div>'
'<div class="body-txt">Use the format spec (<code>:.2f</code>, <code>:,</code>, <code>:&gt;10</code>, <code>:.1%</code>) for precision, alignment, percent.</div></div>'
'<div class="rule-block"><div class="rule-title"><span class="rule-badge">Rule 7</span> Always name the codec on <code>encode</code>/<code>decode</code>/<code>open</code>.</div>'
'<div class="body-txt"><code>str</code> for text, <code>bytes</code> for I/O; use <code>"utf-8"</code> explicitly to avoid mojibake.</div></div>'
'<div class="rule-block"><div class="rule-title"><span class="rule-badge">Rule 8</span> To drop an exact prefix/suffix use <code>removeprefix</code>/<code>removesuffix</code>, not <code>strip</code>.</div>'
'<div class="body-txt"><code>strip(chars)</code> is a character set, not a substring — it mangles URLs and filenames.</div></div>'
)

# ── 5. Common Traps ────────────────────────────────────────────────────
md(
'<div class="trap-header"><h2>5. Common Traps</h2></div>'
'<div class="trap-block"><div class="trap-title"><span class="trap-badge">Trap 1</span> The <code>+=</code> accumulator in a loop.</div>'
'<div class="body-txt"><code>out += piece</code> across a big loop → quadratic. <strong>Fix:</strong> <code>"".join(parts)</code>.</div></div>'
'<div class="trap-block"><div class="trap-title"><span class="trap-badge">Trap 2</span> <code>if s is "yes":</code> — comparing values with <code>is</code>.</div>'
'<div class="body-txt">Works for interned literals, fails silently for runtime-built strings. <strong>Fix:</strong> <code>==</code>.</div></div>'
'<div class="trap-block"><div class="trap-title"><span class="trap-badge">Trap 3</span> Discarded method result.</div>'
'<div class="body-txt"><code>s.replace("a","b")</code> with no assignment → <code>s</code> unchanged. <strong>Fix:</strong> <code>s = s.replace(...)</code>.</div></div>'
'<div class="trap-block"><div class="trap-title"><span class="trap-badge">Trap 4</span> <code>strip("https://")</code> as substring removal.</div>'
'<div class="body-txt">Removes any of <code>h t p s : /</code> from both ends → mangled. <strong>Fix:</strong> <code>removeprefix</code>.</div></div>'
'<div class="trap-block"><div class="trap-title"><span class="trap-badge">Trap 5</span> <code>split(" ")</code> on runs of spaces.</div>'
'<div class="body-txt">Double spaces produce empty strings. <strong>Fix:</strong> no-arg <code>split()</code> for whitespace.</div></div>'
'<div class="trap-block"><div class="trap-title"><span class="trap-badge">Trap 6</span> Encoding mismatch.</div>'
'<div class="body-txt"><code>UnicodeDecodeError</code> / mojibake from wrong codec; <code>len(str)</code> ≠ <code>len(bytes)</code> for non-ASCII. <strong>Fix:</strong> declare <code>utf-8</code>.</div></div>'
)

# ── 6. Exercise ────────────────────────────────────────────────────────
md(
'<div class="part-header"><h2>6. Exercise</h2></div>'
'<div class="body-txt" style="margin-bottom:10px">Twelve problems, easy → hard. Attempt each in <code>01_string.ipynb</code>; hints only here — full worked solutions in <code>solutions.ipynb</code>.</div>'
'<div class="exr-block"><div class="exr-title"><span class="cc-badge badge-easy">Easy</span> E1 — Reverse word order</div>'
'<div class="body-txt"><code>"the cat sat"</code> → <code>"sat cat the"</code>.</div>'
'<div class="hint-box">💡 <code>split()</code> → reverse the list (<code>[::-1]</code>) → <code>" ".join(...)</code>.</div></div>'
'<div class="exr-block"><div class="exr-title"><span class="cc-badge badge-easy">Easy</span> E2 — Count vowels (case-insensitive)</div>'
'<div class="body-txt"><code>"Education"</code> → <code>5</code>.</div>'
'<div class="hint-box">💡 <code>.lower()</code>, then <code>sum(1 for c in s if c in "aeiou")</code>.</div></div>'
'<div class="exr-block"><div class="exr-title"><span class="cc-badge badge-easy">Easy</span> E3 — Title-case a name</div>'
'<div class="body-txt"><code>"siva rama naidu"</code> → <code>"Siva Rama Naidu"</code>.</div>'
'<div class="hint-box">💡 <code>split()</code>, <code>.capitalize()</code> each word, <code>" ".join(...)</code>. (Avoids <code>str.title()</code> quirks with apostrophes.)</div></div>'
'<div class="exr-block"><div class="exr-title"><span class="cc-badge badge-easy">Easy</span> E4 — File extension</div>'
'<div class="body-txt"><code>"report.final.csv"</code> → <code>"csv"</code>.</div>'
'<div class="hint-box">💡 <code>rsplit(".", 1)[-1]</code> (or <code>rpartition(".")[2]</code>). Split from the right so only the last dot matters.</div></div>'
'<div class="exr-block"><div class="exr-title"><span class="cc-badge badge-med">Medium</span> E5 — Clean CSV fields</div>'
'<div class="body-txt"><code>"a, b ,c , d"</code> → <code>[\'a\', \'b\', \'c\', \'d\']</code> (trim each).</div>'
'<div class="hint-box">💡 <code>split(",")</code>, then <code>.strip()</code> each item in a comprehension.</div></div>'
'<div class="exr-block"><div class="exr-title"><span class="cc-badge badge-med">Medium</span> E6 — Valid palindrome</div>'
'<div class="body-txt">Ignore case &amp; non-alphanumerics: <code>"A man, a plan, a canal: Panama"</code> → <code>True</code>.</div>'
'<div class="hint-box">💡 Keep only <code>.isalnum()</code> chars, lower, compare to its reverse.</div></div>'
'<div class="exr-block"><div class="exr-title"><span class="cc-badge badge-med">Medium</span> E7 — Most frequent character</div>'
'<div class="body-txt"><code>"mississippi"</code> → <code>\'i\'</code> (ties broken by first-seen).</div>'
'<div class="hint-box">💡 <code>Counter(s).most_common(1)[0][0]</code> — a 2D callback.</div></div>'
'<div class="exr-block"><div class="exr-title"><span class="cc-badge badge-med">Medium</span> E8 — Aligned report row</div>'
'<div class="body-txt">From <code>("precision", 0.8734)</code> produce <code>\'precision&nbsp;&nbsp;87.3%\'</code> — label left-padded to 10, score as 1-decimal % right-aligned to 6.</div>'
'<div class="hint-box">💡 f-string format spec: <code>f"{name:&lt;10}{score:&gt;6.1%}"</code>.</div></div>'
'<div class="exr-block"><div class="exr-title"><span class="cc-badge badge-med">Medium</span> E9 — Caesar cipher</div>'
'<div class="body-txt">Shift letters by <code>k</code>, wrapping within the alphabet, keeping case; leave non-letters. <code>caesar("xyz", 3)</code> → <code>"abc"</code>.</div>'
'<div class="hint-box">💡 For each letter: <code>base = ord(\'A\')</code> or <code>ord(\'a\')</code>; <code>chr((ord(ch)-base+k) % 26 + base)</code>.</div></div>'
'<div class="exr-block"><div class="exr-title"><span class="cc-badge badge-hard">Hard</span> E10 — Run-length encode</div>'
'<div class="body-txt"><code>"aaabbc"</code> → <code>"a3b2c1"</code>.</div>'
'<div class="hint-box">💡 Track current char + count; on change append <code>char+str(count)</code>; build with <code>join</code>. Handle <code>""</code> and flush the final run.</div></div>'
'<div class="exr-block"><div class="exr-title"><span class="cc-badge badge-hard">Hard</span> E11 — Longest repeated-character run</div>'
'<div class="body-txt"><code>"aaabbbbcc"</code> → <code>(\'b\', 4)</code>.</div>'
'<div class="hint-box">💡 Same accumulator as RLE, but keep the best <code>(char, count)</code> instead of emitting.</div></div>'
'<div class="exr-block"><div class="exr-title"><span class="cc-badge badge-hard">Hard</span> E12 — Reverse only the vowels</div>'
'<div class="body-txt"><code>"leetcode"</code> → <code>"leotcede"</code> (only vowels swap positions).</div>'
'<div class="hint-box">💡 Two pointers from both ends on a list of chars; advance until both point at vowels, then swap.</div></div>'
)

# ══════════════════════════ PART 3 ══════════════════════════
# ── 7. ML Real-World ───────────────────────────────────────────────────
md(
'<div class="info-box"><strong>Part 3:</strong> ML Real-World → Interview Q&amp;A → Code Challenges → Summary</div>'
'<div class="ml-header"><h2>7. ML Real-World Connection</h2></div>'
'<div class="ml-block"><div class="ml-title"><span class="ml-badge">ML 1</span> Text normalization &amp; tokenization</div>'
'<div class="body-txt"><code>text.lower().strip().split()</code> is the pre-processing step before vectorizing — it feeds the vocab/<code>Counter</code> from 2D. Punctuation stripping, casefolding, and splitting are pure string work.</div></div>'
'<div class="ml-block"><div class="ml-title"><span class="ml-badge">ML 2</span> Formatted experiment logs</div>'
'<div class="body-txt"><code>f"epoch {e:03d} | loss {loss:.4f} | acc {acc:.1%}"</code> — the format spec gives aligned, readable training logs and metric reports.</div></div>'
'<div class="ml-block"><div class="ml-title"><span class="ml-badge">ML 3</span> str vs bytes when loading data</div>'
'<div class="body-txt">CSVs, JSON, model artifacts, API responses arrive as <code>bytes</code>; decode with the right codec. This is the root of the <code>UnicodeDecodeError</code> / mojibake you hit reading files — always pass <code>encoding="utf-8"</code>.</div></div>'
'<div class="ml-block"><div class="ml-title"><span class="ml-badge">ML 4</span> join for prompts, rows, serialized features</div>'
'<div class="body-txt">Building an LLM prompt, a CSV line, or a feature string uses <code>join</code>. On large corpora the <code>+=</code> trap becomes a real bottleneck — join keeps it O(n).</div></div>'
'<div class="ml-block"><div class="ml-title"><span class="ml-badge">ML 5</span> Chunking &amp; dedup keys (OpsRAG)</div>'
'<div class="body-txt">RAG splits documents on delimiters and normalizes text into a canonical form for a dedup key (a hash of the normalized string). Directly your OpsRAG dedup — string normalization decides what counts as a duplicate.</div></div>'
)

# ── 8a. Conceptual Q&A ─────────────────────────────────────────────────
md(
'<div class="interview-header"><h2>8. Interview Questions</h2></div>'
'<div class="sub-header"><h3>8a — Conceptual Q&amp;A</h3></div>'
'<div class="qa-block"><div class="qa-q"><span class="q-num">1</span> Are strings mutable? What follows?</div><div class="qa-a">No — immutable. So "edits" build new objects, strings are hashable (dict keys / set members), and methods return new strings.</div></div>'
'<div class="qa-block"><div class="qa-q"><span class="q-num">2</span> <code>is</code> vs <code>==</code> on strings?</div><div class="qa-a"><code>==</code> compares value, <code>is</code> compares identity. Interning can make <code>is</code> return True for literals, but it\'s not guaranteed — always use <code>==</code> for value.</div></div>'
'<div class="qa-block"><div class="qa-q"><span class="q-num">3</span> Why is <code>+=</code> in a loop bad, and the fix?</div><div class="qa-a">Immutability means each <code>+=</code> can rebuild the whole string → risks O(n²). Collect in a list and <code>"".join()</code> once → O(n).</div></div>'
'<div class="qa-block"><div class="qa-q"><span class="q-num">4</span> <code>.find()</code> vs <code>.index()</code>?</div><div class="qa-a">Both return the first position; <code>.find()</code> returns <code>-1</code> if absent, <code>.index()</code> raises <code>ValueError</code>.</div></div>'
'<div class="qa-block"><div class="qa-q"><span class="q-num">5</span> <code>.split()</code> vs <code>.split(" ")</code>?</div><div class="qa-a">No-arg splits on any whitespace run and drops empties; an explicit separator is literal and keeps empty fields between repeats.</div></div>'
'<div class="qa-block"><div class="qa-q"><span class="q-num">6</span> <code>str</code> vs <code>bytes</code>?</div><div class="qa-a"><code>str</code> is Unicode text; <code>bytes</code> is raw octets. <code>.encode(codec)</code> → bytes, <code>.decode(codec)</code> → str.</div></div>'
'<div class="qa-block"><div class="qa-q"><span class="q-num">7</span> What does <code>"...".strip("xy")</code> do?</div><div class="qa-a">Removes any of the characters <code>x</code>/<code>y</code> from both ends — a character set, not a substring. <code>"mississippi".strip("mip")</code> → <code>\'ssiss\'</code>.</div></div>'
'<div class="qa-block"><div class="qa-q"><span class="q-num">8</span> Why can strings be dict keys?</div><div class="qa-a">They\'re immutable → hashable with a stable hash. Same reason tuples can be keys (2B).</div></div>'
'<div class="qa-block"><div class="qa-q"><span class="q-num">9</span> f-string vs <code>.format()</code> vs <code>%</code>?</div><div class="qa-a">All format strings; f-strings are the modern, fastest, most readable — expressions inline with a format spec after the colon.</div></div>'
'<div class="qa-block"><div class="qa-q"><span class="q-num">10</span> <code>len(str)</code> vs <code>len(bytes)</code> for non-ASCII?</div><div class="qa-a">Differ: <code>len(str)</code> counts characters, <code>len(bytes)</code> counts encoded bytes. <code>"café"</code> → 4 chars, 5 UTF-8 bytes.</div></div>'
'<div class="qa-block"><div class="qa-q"><span class="q-num">11</span> How do you reverse a string?</div><div class="qa-a"><code>s[::-1]</code> — a slice with step -1; returns a new string.</div></div>'
'<div class="qa-block"><div class="qa-q"><span class="q-num">12</span> <code>removeprefix</code> vs <code>strip</code>?</div><div class="qa-a"><code>removeprefix</code>/<code>removesuffix</code> drop an exact substring at the edge; <code>strip</code> removes any characters in a set. Use the former for prefixes/suffixes.</div></div>'
)

# ── 8b. Code Challenges ────────────────────────────────────────────────
md(
'<div class="sub-header"><h3>8b — Code Challenges (attempt, then expand the solution)</h3></div>'
# C1
'<div class="cc-block"><div class="cc-title"><span class="cc-badge badge-easy">Easy</span> C1 — Reverse a string</div>'
'<div class="body-txt"><code>reverse("hello")</code> → <code>"olleh"</code>.</div>'
'<details class="sol"><summary>Solution</summary>'
'<div class="code-block"><span class="ck">def</span> <span class="cm">reverse</span>(s): <span class="ck">return</span> s[::-<span class="cn">1</span>]</div>'
'<div class="qa-a">Slice with step −1 builds a new reversed string in O(n). No loop needed.</div></details></div>'
# C2
'<div class="cc-block"><div class="cc-title"><span class="cc-badge badge-easy">Easy</span> C2 — Anagram check</div>'
'<div class="body-txt"><code>("listen","silent")</code> → <code>True</code>.</div>'
'<details class="sol"><summary>Solution</summary>'
'<div class="code-block"><span class="ck">def</span> <span class="cm">is_anagram</span>(a, b): <span class="ck">return</span> <span class="cm">sorted</span>(a) == <span class="cm">sorted</span>(b)</div>'
'<div class="qa-a">Sorting both (O(n log n)) makes anagrams identical. <code>Counter(a)==Counter(b)</code> is the O(n) alternative.</div></details></div>'
# C3
'<div class="cc-block"><div class="cc-title"><span class="cc-badge badge-med">Med</span> C3 — First non-repeating character (2D callback)</div>'
'<div class="body-txt"><code>"leetcode"</code> → <code>"l"</code>; <code>"aabb"</code> → <code>None</code>.</div>'
'<details class="sol"><summary>Solution</summary>'
'<div class="code-block"><span class="ck">from</span> collections <span class="ck">import</span> Counter<br>'
'<span class="ck">def</span> <span class="cm">first_unique</span>(s):<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;c = <span class="cm">Counter</span>(s)<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">for</span> ch <span class="ck">in</span> s:<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">if</span> c[ch] == <span class="cn">1</span>: <span class="ck">return</span> ch<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">return</span> <span class="ck">None</span></div>'
'<div class="qa-a">Count first, then scan in original order — needs counts AND order, exactly the set→dict seam from 2C.</div></details></div>'
# C4
'<div class="cc-block"><div class="cc-title"><span class="cc-badge badge-med">Med</span> C4 — Word frequency</div>'
'<div class="body-txt"><code>"the cat the dog the"</code> → <code>{\'the\':3, \'cat\':1, \'dog\':1}</code>.</div>'
'<details class="sol"><summary>Solution</summary>'
'<div class="code-block"><span class="ck">from</span> collections <span class="ck">import</span> Counter<br>'
'<span class="ck">def</span> <span class="cm">word_freq</span>(text): <span class="ck">return</span> <span class="cm">Counter</span>(text.<span class="cm">split</span>())</div>'
'<div class="qa-a">Split into tokens, count with <code>Counter</code> — string + dict working together.</div></details></div>'
# C5
'<div class="cc-block"><div class="cc-title"><span class="cc-badge badge-med">Med</span> C5 — Valid palindrome</div>'
'<div class="body-txt"><code>"A man, a plan, a canal: Panama"</code> → <code>True</code>.</div>'
'<details class="sol"><summary>Solution</summary>'
'<div class="code-block"><span class="ck">def</span> <span class="cm">is_palindrome</span>(s):<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;t = [c.<span class="cm">lower</span>() <span class="ck">for</span> c <span class="ck">in</span> s <span class="ck">if</span> c.<span class="cm">isalnum</span>()]<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">return</span> t == t[::-<span class="cn">1</span>]</div>'
'<div class="qa-a">Filter to alphanumerics, lowercase, compare to reverse. A two-pointer scan is the O(1)-space variant.</div></details></div>'
# C6
'<div class="cc-block"><div class="cc-title"><span class="cc-badge badge-med">Med</span> C6 — Run-length encode</div>'
'<div class="body-txt"><code>"aaabbc"</code> → <code>"a3b2c1"</code>.</div>'
'<details class="sol"><summary>Solution</summary>'
'<div class="code-block"><span class="ck">def</span> <span class="cm">rle</span>(s):<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">if</span> <span class="ck">not</span> s: <span class="ck">return</span> <span class="cs">""</span><br>'
'&nbsp;&nbsp;&nbsp;&nbsp;out, prev, n = [], s[<span class="cn">0</span>], <span class="cn">1</span><br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">for</span> ch <span class="ck">in</span> s[<span class="cn">1</span>:]:<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">if</span> ch == prev: n += <span class="cn">1</span><br>'
'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">else</span>: out.<span class="cm">append</span>(prev + <span class="cm">str</span>(n)); prev, n = ch, <span class="cn">1</span><br>'
'&nbsp;&nbsp;&nbsp;&nbsp;out.<span class="cm">append</span>(prev + <span class="cm">str</span>(n))<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">return</span> <span class="cs">""</span>.<span class="cm">join</span>(out)</div>'
'<div class="qa-a">Accumulator over runs; build with <code>join</code> (not <code>+=</code>). Note the flush after the loop for the final run.</div></details></div>'
# C7
'<div class="cc-block"><div class="cc-title"><span class="cc-badge badge-hard">Hard</span> C7 — Longest substring without repeating characters</div>'
'<div class="body-txt"><code>"abcabcbb"</code> → <code>3</code>, <code>"bbbbb"</code> → <code>1</code>, <code>"pwwkew"</code> → <code>3</code>.</div>'
'<details class="sol"><summary>Solution</summary>'
'<div class="code-block"><span class="ck">def</span> <span class="cm">length_of_longest</span>(s):<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;seen, start, best = {}, <span class="cn">0</span>, <span class="cn">0</span><br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">for</span> i, ch <span class="ck">in</span> <span class="cm">enumerate</span>(s):<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">if</span> ch <span class="ck">in</span> seen <span class="ck">and</span> seen[ch] &gt;= start: start = seen[ch] + <span class="cn">1</span><br>'
'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;seen[ch] = i<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;best = <span class="cm">max</span>(best, i - start + <span class="cn">1</span>)<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">return</span> best</div>'
'<div class="qa-a">Sliding window + a dict of last-seen index (O(1) lookup, 2D). Move <code>start</code> past a repeat; window width tracks the best.</div></details></div>'
# C8
'<div class="cc-block"><div class="cc-title"><span class="cc-badge badge-hard">Hard</span> C8 — Group anagrams</div>'
'<div class="body-txt"><code>["eat","tea","tan","ate","nat","bat"]</code> → grouped by anagram.</div>'
'<details class="sol"><summary>Solution</summary>'
'<div class="code-block"><span class="ck">from</span> collections <span class="ck">import</span> defaultdict<br>'
'<span class="ck">def</span> <span class="cm">group_anagrams</span>(words):<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;g = <span class="cm">defaultdict</span>(list)<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">for</span> w <span class="ck">in</span> words: g[<span class="cs">""</span>.<span class="cm">join</span>(<span class="cm">sorted</span>(w))].<span class="cm">append</span>(w)<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">return</span> <span class="cm">list</span>(g.<span class="cm">values</span>())</div>'
'<div class="qa-a">Sorted letters are the canonical anagram signature → a hashable dict key. <code>defaultdict(list)</code> groups — the 2D grouping pattern on strings.</div></details></div>'
)

# ── 9. Summary Table ───────────────────────────────────────────────────
md(
'<div class="summary-header"><h2>9. Summary Table — Session 3</h2></div>'
'<table class="summary">'
'<tr><th>Concept</th><th>Why it matters in ML</th><th>Interview frequency</th></tr>'
'<tr><td>Immutable sequence model</td><td>Explains every string behavior; safe to share/hash</td><td><span class="freq-vh">Very High</span></td></tr>'
'<tr><td><code>+=</code> O(n²) vs <code>join</code></td><td>Building prompts/corpora/CSV at scale</td><td><span class="freq-vh">Very High</span></td></tr>'
'<tr><td><code>is</code> vs <code>==</code> (interning)</td><td>Correct comparisons; classic gotcha</td><td><span class="freq-h">High</span></td></tr>'
'<tr><td>split / join / replace / partition</td><td>Parsing &amp; building text — everywhere in prep</td><td><span class="freq-vh">Very High</span></td></tr>'
'<tr><td>f-strings &amp; format spec</td><td>Metric logs, reports, aligned output</td><td><span class="freq-h">High</span></td></tr>'
'<tr><td>str vs bytes / encoding</td><td>Reading files/APIs; UnicodeDecodeError &amp; mojibake</td><td><span class="freq-h">High</span></td></tr>'
'<tr><td><code>.find</code> vs <code>.index</code></td><td>Fail-loud vs safe search</td><td><span class="freq-m">Medium</span></td></tr>'
'<tr><td><code>strip</code> charset vs substring</td><td>Avoiding mangled URLs/filenames</td><td><span class="freq-m">Medium</span></td></tr>'
'<tr><td>Slicing &amp; reversal (<code>s[::-1]</code>)</td><td>Palindromes, tokenizing, windows</td><td><span class="freq-h">High</span></td></tr>'
'</table>'
'<hr class="divider">'
'<div style="background:#1e1e2e; border-left:4px solid #a6e3a1; padding:14px 18px; border-radius:8px; font-family:monospace; color:#cdd6f4;">'
'<strong style="color:#a6e3a1">✅ Session 3 complete.</strong> Strings as an immutable sequence: model, '
'construction, method surface, formatting, encoding, 4 examples, 6 edge cases, 8 golden rules, 6 traps, '
'12 exercises, ML connections, 12 conceptual Q&amp;A, 8 code challenges, summary table.<br>'
'<span style="color:#6c7086">Next — Session 4: Comprehensions &amp; generators (list/dict/set comprehensions, '
'generator expressions, <code>yield</code>, lazy evaluation).</span></div>'
)

nb = new_notebook(cells=cells)
nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
nb.metadata["language_info"] = {"name": "python"}

nbf.write(nb, "theory.ipynb")
print("wrote theory.ipynb with", len(cells), "cells")
