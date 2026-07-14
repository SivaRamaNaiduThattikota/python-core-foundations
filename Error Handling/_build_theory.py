# Builder for Session 9 - Error Handling, theory.ipynb.
# Deep 4-chunk. Chunk A = exceptions basics: raise, try/except, the exception hierarchy.
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
'<h1 class="main-title">🐍 Session 9 — Error Handling</h1>'
'<div class="info-box"><strong>Part 1:</strong> Theory → Example → Edge Cases · deep 4-chunk.</div>'
'<div class="chunk-badge">Part 1 · Chunk A — Exceptions, <code>raise</code>, <code>try/except</code>, the Hierarchy</div>'
'<div class="theory-box" style="border-left-color:#cba6f7;">'
'You\'ve <em>hit</em> exceptions all through this course — <code>ValueError</code>, <code>TypeError</code>, '
'<code>KeyError</code>, <code>StopIteration</code>, <code>AttributeError</code>. Now we handle them '
'deliberately. Chunk A: what an exception is, <code>raise</code>, <code>try/except</code>, and the '
'<strong style="color:#89b4fa">exception hierarchy</strong>. B: the full <code>try/except/else/finally</code>. '
'C: custom exceptions &amp; chaining. D: EAFP vs LBYL and best practices.</div>'
)

# ── 1.1 what is an exception + raise ────────────────────────────────────
md(
'<div class="part-header"><h2>1. Theory</h2></div>'
'<h3 class="sub">🔹 1.1 &nbsp;What an exception is, and <code>raise</code></h3>'
'<div class="theory-box">An <strong>exception</strong> is an object that signals something went wrong. When '
'raised, it <strong>propagates up the call stack</strong>, unwinding functions, until something catches it — '
'or it reaches the top and crashes the program with a traceback. You raise one with <code>raise</code>.</div>'
'<div class="code-block">'
'<span class="ck">def</span> <span class="cm">sqrt</span>(x):<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">if</span> x &lt; <span class="cn">0</span>:<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">raise</span> ValueError(<span class="cs">"negative input"</span>)   <span class="cc"># signal a bad argument</span><br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">return</span> x ** <span class="cn">0.5</span><br>'
'<br>'
'<span class="cm">sqrt</span>(-<span class="cn">1</span>)   <span class="cc"># ValueError: negative input  (crashes if uncaught)</span></div>'
'<div class="output-block">ValueError: negative input</div>'
'<div class="info-box">💡 <strong>SQL / Power BI anchor:</strong> like <code>THROW</code> / <code>RAISERROR</code> '
'in T-SQL — you signal an error condition, and it bubbles up until a <code>TRY…CATCH</code> handles it or the '
'batch aborts.</div>'
'<div class="note-box">💡 Prefer specific built-in types: <code>ValueError</code> (bad value), '
'<code>TypeError</code> (wrong type), <code>KeyError</code>/<code>IndexError</code> (missing key/index), '
'<code>FileNotFoundError</code>, etc. The type communicates <em>what</em> went wrong.</div>'
)

# ── 1.2 try/except ─────────────────────────────────────────────────────
md(
'<h3 class="sub">🔹 1.2 &nbsp;<code>try</code> / <code>except</code> — catch and handle</h3>'
'<div class="theory-box">Wrap risky code in <code>try</code>; handle failures in <code>except</code>. Bind '
'the exception object with <code>as e</code> to inspect it. Catching a failure lets the program '
'<strong>recover</strong> instead of crashing.</div>'
'<div class="code-block">'
'<span class="ck">try</span>:<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;n = <span class="cm">int</span>(<span class="cs">"abc"</span>)          <span class="cc"># raises ValueError</span><br>'
'<span class="ck">except</span> ValueError <span class="ck">as</span> e:<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="cm">print</span>(<span class="cs">"caught:"</span>, e)   <span class="cc"># invalid literal for int() with base 10: \'abc\'</span><br>'
'&nbsp;&nbsp;&nbsp;&nbsp;n = <span class="cn">0</span>                    <span class="cc"># recover with a default</span></div>'
'<div class="output-block">caught: invalid literal for int() with base 10: \'abc\'</div>'
'<div class="note-box">💡 The exception object carries data: <code>e.args</code> holds the arguments it was '
'raised with (e.g. <code>ValueError("bad", 42).args == ("bad", 42)</code>). <code>str(e)</code> is the '
'message.</div>'
)

# ── 1.3 hierarchy ──────────────────────────────────────────────────────
md(
'<h3 class="sub">🔹 1.3 &nbsp;The exception hierarchy — catch specific, not broad</h3>'
'<div class="theory-box">Every exception is a class in a tree rooted at <code>BaseException</code>; almost all '
'you catch inherit from <code>Exception</code>. Catching a <strong>base class catches all its '
'subclasses</strong> — so <code>except LookupError</code> also catches <code>KeyError</code> and '
'<code>IndexError</code>. Match is by <code>isinstance</code>, top-down through the <code>except</code> '
'clauses.</div>'
'<div class="code-block">'
'KeyError.__mro__<br>'
'<span class="cc"># (KeyError, LookupError, Exception, BaseException, object)</span><br>'
'<br>'
'<span class="ck">try</span>:<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">raise</span> KeyError(<span class="cs">"k"</span>)<br>'
'<span class="ck">except</span> LookupError <span class="ck">as</span> e:      <span class="cc"># catches KeyError (a subclass)</span><br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="cm">print</span>(<span class="cm">type</span>(e).__name__)   <span class="cc"># KeyError</span></div>'
'<div class="output-block">(KeyError, LookupError, Exception, BaseException, object)<br>KeyError</div>'
'<div class="mut-grid">'
'<div class="mut-card mc-imm"><div class="mc-title">✅ Catch specific</div>'
'<div class="mc-body">except ValueError:<br>&nbsp;&nbsp;...<br><br>only handles what you expect;<br>real bugs still surface</div></div>'
'<div class="mut-card mc-mut" style="border-color:#f38ba8; background:#2e1e1e;"><div class="mc-title" style="color:#f38ba8;">❌ Bare / too broad</div>'
'<div class="mc-body">except:            # or except Exception<br>&nbsp;&nbsp;pass<br><br>swallows typos, KeyboardInterrupt,<br>everything — hides bugs</div></div>'
'</div>'
'<div class="why-box"><strong>Why it matters:</strong> a bare <code>except:</code> (or overly broad '
'<code>except Exception</code>) catches things you never meant to — including your own typos and '
'<code>KeyboardInterrupt</code> — turning loud bugs into silent wrong behavior. <strong>Catch the '
'narrowest exception that fits.</strong> You can list several: <code>except (ValueError, TypeError) as e:</code>.</div>'
'<hr class="divider">'
'<div style="background:#1e1e2e; border-left:4px solid #cba6f7; padding:16px 20px; border-radius:8px; font-family:monospace; color:#cdd6f4;">'
'<h4 style="color:#cba6f7; margin:0 0 12px 0;">🔑 Chunk A — Key Takeaways</h4>'
'<ul style="margin:0; padding-left:20px; line-height:2.1">'
'<li>An exception is an object; <code>raise</code> signals it and it propagates up until caught (or crashes)</li>'
'<li>Use specific built-in types (<code>ValueError</code>/<code>TypeError</code>/<code>KeyError</code>…) to say <em>what</em> went wrong</li>'
'<li><code>try/except</code> catches and recovers; bind with <code>as e</code>, inspect <code>e.args</code>/<code>str(e)</code></li>'
'<li>Exceptions form a hierarchy under <code>BaseException</code>; catching a base catches subclasses — so catch the <strong>narrowest</strong> one, never bare <code>except:</code></li>'
'</ul></div>'
)

# ══════════════════════════ CHUNK B ══════════════════════════
md(
'<div class="chunk-badge">Part 1 · Chunk B — <code>else</code> / <code>finally</code>, Multiple Handlers, Re-raising</div>'
'<h3 class="sub">🔹 1.4 &nbsp;The full statement — <code>try</code> / <code>except</code> / <code>else</code> / <code>finally</code></h3>'
'<div class="theory-box"><code>else</code> runs only if the <code>try</code> block raised <strong>nothing</strong> '
'(the success path — keeps the risky line isolated in <code>try</code>). <code>finally</code> <strong>always</strong> '
'runs — success, exception, or even a <code>return</code>/<code>break</code> — for guaranteed cleanup.</div>'
'<div class="code-block">'
'<span class="ck">def</span> <span class="cm">parse</span>(s):<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">try</span>:<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;n = <span class="cm">int</span>(s)          <span class="cc"># risky bit, isolated</span><br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">except</span> ValueError:<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">return</span> <span class="ck">None</span><br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">else</span>:<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">return</span> n * <span class="cn">2</span>       <span class="cc"># only if no exception</span><br>'
'<br>'
'<span class="cm">parse</span>(<span class="cs">"5"</span>), <span class="cm">parse</span>(<span class="cs">"x"</span>)   <span class="cc"># (10, None)</span></div>'
'<div class="output-block">10 None</div>'
'<div class="code-block">'
'log = []<br>'
'<span class="ck">try</span>:<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">raise</span> ValueError()<br>'
'<span class="ck">finally</span>:<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;log.<span class="cm">append</span>(<span class="cs">"cleanup"</span>)   <span class="cc"># runs BEFORE the exception propagates</span></div>'
'<div class="output-block">cleanup ran, then ValueError propagated</div>'
'<div class="info-box">💡 <code>finally</code> is the pre-<code>with</code> way to guarantee cleanup (Session 8). '
'A <code>with</code> block is usually cleaner, but <code>finally</code> is there when you need arbitrary '
'teardown logic.</div>'
)

md(
'<h3 class="sub">🔹 1.5 &nbsp;Multiple handlers — order matters</h3>'
'<div class="theory-box"><code>except</code> clauses are tried top-down; the <strong>first matching</strong> one '
'wins. So list <strong>specific before general</strong> — a broad clause placed first makes the specific ones '
'below it unreachable (Edge case in Chunk D).</div>'
'<div class="code-block">'
'<span class="ck">try</span>:<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;risky()<br>'
'<span class="ck">except</span> KeyError:<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;...                    <span class="cc"># most specific</span><br>'
'<span class="ck">except</span> LookupError:<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;...                    <span class="cc"># broader (catches IndexError too)</span><br>'
'<span class="ck">except</span> Exception <span class="ck">as</span> e:<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;...                    <span class="cc"># catch-all last</span></div>'
'<div class="output-block">first matching clause handles it</div>'
'<h3 class="sub">🔹 1.6 &nbsp;Re-raising — handle partially, then let it propagate</h3>'
'<div class="theory-box">A bare <code>raise</code> inside <code>except</code> <strong>re-raises the current '
'exception</strong>, preserving its original traceback — perfect for "log it here, but let the caller decide." '
'Or raise a different exception to translate it (Chunk C).</div>'
'<div class="code-block">'
'<span class="ck">def</span> <span class="cm">wrapper</span>():<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">try</span>:<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="cm">int</span>(<span class="cs">"x"</span>)<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">except</span> ValueError:<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;log.<span class="cm">error</span>(<span class="cs">"parse failed"</span>)   <span class="cc"># do something...</span><br>'
'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">raise</span>                   <span class="cc"># ...then re-raise unchanged (keeps traceback)</span></div>'
'<div class="output-block">logs, then the ValueError propagates to the caller</div>'
'<hr class="divider">'
'<div style="background:#1e1e2e; border-left:4px solid #cba6f7; padding:14px 18px; border-radius:8px; font-family:monospace; color:#cdd6f4;">'
'<h4 style="color:#cba6f7; margin:0 0 10px 0;">🔑 Chunk B — Key Takeaways</h4>'
'<ul style="margin:0; padding-left:20px; line-height:2.0">'
'<li><code>else</code> = the success path (no exception); <code>finally</code> = always runs (cleanup)</li>'
'<li>Multiple <code>except</code> clauses match top-down — specific before general</li>'
'<li>Bare <code>raise</code> in an <code>except</code> re-raises the current exception, preserving the traceback</li>'
'</ul></div>'
)

# ══════════════════════════ CHUNK C ══════════════════════════
md(
'<div class="chunk-badge">Part 1 · Chunk C — Custom Exceptions &amp; Chaining</div>'
'<h3 class="sub">🔹 1.7 &nbsp;Custom exception classes</h3>'
'<div class="theory-box">Define your own by subclassing <code>Exception</code>. Give it attributes for structured '
'error data, and build a <strong>domain hierarchy</strong> so callers can catch a whole family with one base '
'class — the OOP inheritance you learned in 7C, applied to errors.</div>'
'<div class="code-block">'
'<span class="ck">class</span> <span class="cm">ValidationError</span>(Exception):<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">def</span> <span class="cm">__init__</span>(self, field, msg):<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="cm">super</span>().<span class="cm">__init__</span>(<span class="cs">f"{field}: {msg}"</span>)   <span class="cc"># the message</span><br>'
'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;self.field = field                    <span class="cc"># structured attribute</span><br>'
'<br>'
'<span class="ck">try</span>:<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">raise</span> ValidationError(<span class="cs">"email"</span>, <span class="cs">"required"</span>)<br>'
'<span class="ck">except</span> ValidationError <span class="ck">as</span> e:<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="cm">print</span>(e, <span class="cs">"| field:"</span>, e.field)   <span class="cc"># email: required | field: email</span></div>'
'<div class="output-block">email: required | field: email</div>'
'<div class="code-block">'
'<span class="ck">class</span> <span class="cm">AppError</span>(Exception): <span class="ck">pass</span>       <span class="cc"># base for the whole app</span><br>'
'<span class="ck">class</span> <span class="cm">NotFound</span>(AppError): <span class="ck">pass</span><br>'
'<span class="ck">class</span> <span class="cm">Forbidden</span>(AppError): <span class="ck">pass</span><br>'
'<br>'
'<span class="ck">try</span>:<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">raise</span> <span class="cm">NotFound</span>(<span class="cs">"user 5"</span>)<br>'
'<span class="ck">except</span> AppError <span class="ck">as</span> e:      <span class="cc"># one clause catches the whole family (7C hierarchy)</span><br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="cm">print</span>(<span class="cm">type</span>(e).__name__)   <span class="cc"># NotFound</span></div>'
'<div class="output-block">NotFound (caught by AppError)</div>'
)

md(
'<h3 class="sub">🔹 1.8 &nbsp;Exception chaining — <code>raise … from …</code></h3>'
'<div class="theory-box">When you translate a low-level error into a domain one, chain them with '
'<code>raise NewError(...) from original</code>. It sets <code>__cause__</code>, and the traceback shows '
'<em>"The above exception was the direct cause of the following"</em> — so you keep the root cause. '
'(Raising inside an <code>except</code> without <code>from</code> still links via <code>__context__</code> '
'implicitly.)</div>'
'<div class="code-block">'
'<span class="ck">def</span> <span class="cm">load</span>(key):<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;data = {<span class="cs">"a"</span>: <span class="cn">1</span>}<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">try</span>:<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">return</span> data[key]<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">except</span> KeyError <span class="ck">as</span> e:<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">raise</span> ValidationError(<span class="cs">"key"</span>, <span class="cs">"missing"</span>) <span class="ck">from</span> e   <span class="cc"># translate + keep cause</span><br>'
'<br>'
'<span class="ck">try</span>:<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="cm">load</span>(<span class="cs">"z"</span>)<br>'
'<span class="ck">except</span> ValidationError <span class="ck">as</span> e:<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="cm">print</span>(<span class="cm">type</span>(e.__cause__).__name__)   <span class="cc"># KeyError - the root cause</span></div>'
'<div class="output-block">KeyError</div>'
'<div class="why-box"><strong>Why it matters:</strong> chaining gives you a clean public error '
'(<code>ValidationError</code>) <em>and</em> preserves the underlying <code>KeyError</code> for debugging — the '
'best of both. Use <code>raise NewError(...) from None</code> to deliberately <strong>hide</strong> the '
'low-level cause when it\'s noise.</div>'
'<hr class="divider">'
'<div style="background:#1e1e2e; border-left:4px solid #cba6f7; padding:14px 18px; border-radius:8px; font-family:monospace; color:#cdd6f4;">'
'<h4 style="color:#cba6f7; margin:0 0 10px 0;">🔑 Chunk C — Key Takeaways</h4>'
'<ul style="margin:0; padding-left:20px; line-height:2.0">'
'<li>Custom exceptions = subclass <code>Exception</code>; add attributes; build a domain hierarchy (7C)</li>'
'<li>A base exception class lets callers catch a whole family in one clause</li>'
'<li><code>raise New(...) from original</code> translates the error and keeps the root cause (<code>__cause__</code>); <code>from None</code> hides it</li>'
'</ul></div>'
)

# ══════════════════════════ CHUNK D ══════════════════════════
md(
'<div class="chunk-badge">Part 1 · Chunk D — EAFP vs LBYL + Examples &amp; Edge Cases</div>'
'<h3 class="sub">🔹 1.9 &nbsp;EAFP vs LBYL — the Pythonic style</h3>'
'<div class="theory-box"><strong>LBYL</strong> ("Look Before You Leap") checks preconditions first; '
'<strong>EAFP</strong> ("Easier to Ask Forgiveness than Permission") just tries and handles the exception. '
'Python favors <strong>EAFP</strong> — it\'s cleaner and avoids a <strong>race condition</strong>: with LBYL, '
'state can change between the check and the use (TOCTOU); EAFP acts atomically.</div>'
'<div class="code-block">'
'<span class="cc"># LBYL - check, then use (two steps; can race)</span><br>'
'<span class="ck">if</span> key <span class="ck">in</span> d:<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">return</span> d[key]<br>'
'<br>'
'<span class="cc"># EAFP - just try (one atomic step) - preferred</span><br>'
'<span class="ck">try</span>:<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">return</span> d[key]<br>'
'<span class="ck">except</span> KeyError:<br>'
'&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">return</span> <span class="ck">None</span></div>'
'<div class="output-block">both return the value or None; EAFP has no check-then-use gap</div>'
'<div class="mut-grid">'
'<div class="mut-card mc-mut"><div class="mc-title">🔎 LBYL</div>'
'<div class="mc-body">check preconditions first<br>race window (TOCTOU)<br>duplicates the check &amp; the op<br>OK for cheap, local checks</div></div>'
'<div class="mut-card mc-imm"><div class="mc-title">🙏 EAFP (preferred)</div>'
'<div class="mc-body">try, then handle failure<br>atomic — no race<br>fast on the happy path<br>the Pythonic default</div></div>'
'</div>'
'<div class="note-box">💡 <strong>Best practices recap:</strong> catch the narrowest exception; never swallow '
'silently (log or handle); put cleanup in <code>finally</code> or a <code>with</code>; raise specific/custom '
'types; chain with <code>from</code>. Don\'t use exceptions for normal control flow that isn\'t exceptional.</div>'
# ── 2. Examples ──
'<div class="ex-header"><h2>2. Example</h2></div>'
'<div class="ex-block"><div class="ex-title"><span class="ex-badge">Ex 1</span> Safe parse with a default (EAFP)</div>'
'<div class="code-block"><span class="ck">def</span> <span class="cm">safe_int</span>(s, default=<span class="cn">0</span>):<br>&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">try</span>: <span class="ck">return</span> <span class="cm">int</span>(s)<br>&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">except</span> (ValueError, TypeError): <span class="ck">return</span> default<br><br><span class="cm">safe_int</span>(<span class="cs">"5"</span>), <span class="cm">safe_int</span>(<span class="cs">"x"</span>), <span class="cm">safe_int</span>(<span class="ck">None</span>)   <span class="cc"># (5, 0, 0)</span></div>'
'<div class="output-block">5 0 0</div>'
'<div class="note-box">Catch the specific pair; a <code>None</code> input raises <code>TypeError</code>, a bad string raises <code>ValueError</code> — both handled, everything else still surfaces.</div></div>'
'<div class="ex-block"><div class="ex-title"><span class="ex-badge">Ex 2</span> A retry loop</div>'
'<div class="code-block"><span class="ck">def</span> <span class="cm">with_retry</span>(fn, times=<span class="cn">3</span>):<br>&nbsp;&nbsp;&nbsp;&nbsp;last = <span class="ck">None</span><br>&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">for</span> _ <span class="ck">in</span> <span class="cm">range</span>(times):<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">try</span>: <span class="ck">return</span> fn()<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">except</span> Exception <span class="ck">as</span> e: last = e<br>&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">raise</span> last   <span class="cc"># give up after N attempts</span></div>'
'<div class="output-block">returns on first success; re-raises the last error if all fail</div>'
'<div class="note-box">The S6 <code>@retry</code> decorator, as plain error handling — resilience for flaky I/O.</div></div>'
'<div class="ex-block"><div class="ex-title"><span class="ex-badge">Ex 3</span> A domain exception hierarchy</div>'
'<div class="code-block"><span class="ck">class</span> <span class="cm">AppError</span>(Exception): <span class="ck">pass</span><br><span class="ck">class</span> <span class="cm">NotFound</span>(AppError): <span class="ck">pass</span><br><span class="ck">class</span> <span class="cm">Forbidden</span>(AppError): <span class="ck">pass</span><br><br><span class="ck">try</span>:<br>&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">raise</span> <span class="cm">Forbidden</span>(<span class="cs">"no access"</span>)<br><span class="ck">except</span> AppError <span class="ck">as</span> e:   <span class="cc"># handle any app error uniformly</span><br>&nbsp;&nbsp;&nbsp;&nbsp;<span class="cm">print</span>(<span class="cm">type</span>(e).__name__, e)</div>'
'<div class="output-block">Forbidden no access</div>'
'<div class="note-box">One base per subsystem lets callers catch broadly (<code>except AppError</code>) or narrowly (<code>except NotFound</code>).</div></div>'
'<div class="ex-block"><div class="ex-title"><span class="ex-badge">Ex 4</span> Translate a low-level error (chaining)</div>'
'<div class="code-block"><span class="ck">try</span>:<br>&nbsp;&nbsp;&nbsp;&nbsp;value = config[<span class="cs">"db_url"</span>]<br><span class="ck">except</span> KeyError <span class="ck">as</span> e:<br>&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">raise</span> ConfigError(<span class="cs">"db_url missing"</span>) <span class="ck">from</span> e   <span class="cc"># clean public error, keeps cause</span></div>'
'<div class="output-block">ConfigError to callers; KeyError preserved as __cause__</div></div>'
# ── 3. Edge Cases ──
'<div class="warn-header"><h2>3. Edge Cases</h2></div>'
'<p style="color:#cdd6f4;font-family:\'Segoe UI\',sans-serif;font-size:0.92em;margin:0 0 12px 0">All outputs verified by running.</p>'
'<div class="edge-block"><div class="edge-title"><span class="edge-badge">Edge 1</span> A <code>return</code> in <code>finally</code> swallows the exception</div>'
'<div class="code-block"><span class="ck">def</span> <span class="cm">bad</span>():<br>&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">try</span>: <span class="ck">raise</span> ValueError(<span class="cs">"lost"</span>)<br>&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">finally</span>: <span class="ck">return</span> <span class="cs">"swallowed"</span>   <span class="cc"># return here EATS the exception</span><br><span class="cm">bad</span>()   <span class="cc"># \'swallowed\' - the ValueError silently vanishes</span></div>'
'<div class="output-block">swallowed  (the ValueError is gone!)</div>'
'<div class="why-box"><strong>Why:</strong> a <code>return</code> (or <code>break</code>) in <code>finally</code> '
'overrides any in-flight exception, hiding it. Never <code>return</code> from <code>finally</code> — keep it '
'to cleanup only.</div></div>'
'<div class="edge-block"><div class="edge-title"><span class="edge-badge">Edge 2</span> A broad handler before a specific one makes the specific unreachable</div>'
'<div class="code-block"><span class="ck">try</span>: <span class="ck">raise</span> ValueError(<span class="cs">"v"</span>)<br><span class="ck">except</span> Exception: ...     <span class="cc"># catches everything first</span><br><span class="ck">except</span> ValueError: ...    <span class="cc"># DEAD code - never reached</span></div>'
'<div class="output-block">the Exception clause always wins</div>'
'<div class="why-box"><strong>Why:</strong> clauses match top-down; a broad one first shadows the specific ones. '
'Order <strong>specific → general</strong>. (Modern linters flag this.)</div></div>'
'<div class="edge-block"><div class="edge-title"><span class="edge-badge">Edge 3</span> <code>except Exception</code> does NOT catch <code>KeyboardInterrupt</code>/<code>SystemExit</code></div>'
'<div class="code-block"><span class="cm">issubclass</span>(KeyboardInterrupt, Exception)      <span class="cc"># False</span><br><span class="cm">issubclass</span>(KeyboardInterrupt, BaseException)  <span class="cc"># True</span></div>'
'<div class="output-block">False / True</div>'
'<div class="why-box"><strong>Why:</strong> <code>KeyboardInterrupt</code> and <code>SystemExit</code> inherit '
'<code>BaseException</code> directly, so <code>except Exception</code> lets Ctrl-C and <code>sys.exit()</code> '
'through — exactly why you use <code>except Exception</code>, never bare <code>except:</code>.</div></div>'
'<div class="edge-block"><div class="edge-title"><span class="edge-badge">Edge 4</span> A broad <code>except</code> silently swallows real bugs</div>'
'<div class="code-block"><span class="ck">try</span>:<br>&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">return</span> resultt      <span class="cc"># typo! NameError</span><br><span class="ck">except</span> Exception:<br>&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">return</span> <span class="ck">None</span>          <span class="cc"># the typo is hidden as if it were expected</span></div>'
'<div class="output-block">None  (a NameError bug swallowed silently)</div>'
'<div class="why-box"><strong>Why:</strong> over-broad catches hide programming errors (typos, wrong names) as '
'if they were expected failures. Catch the narrowest type; if you must catch broadly, at least log it.</div></div>'
'<div class="edge-block"><div class="edge-title"><span class="edge-badge">Edge 5</span> Implicit chaining (<code>__context__</code>) vs <code>from None</code></div>'
'<div class="code-block"><span class="ck">try</span>:<br>&nbsp;&nbsp;&nbsp;&nbsp;<span class="cm">int</span>(<span class="cs">"x"</span>)<br><span class="ck">except</span> ValueError:<br>&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">raise</span> RuntimeError(<span class="cs">"wrapped"</span>)          <span class="cc"># __context__ = the ValueError (auto)</span><br>&nbsp;&nbsp;&nbsp;&nbsp;<span class="cc"># raise RuntimeError("clean") from None  -> suppresses the context</span></div>'
'<div class="output-block">traceback shows "During handling of the above exception..." unless `from None`</div>'
'<div class="why-box"><strong>Why:</strong> raising inside an <code>except</code> auto-links the original via '
'<code>__context__</code> (shown in the traceback). Use <code>from e</code> to mark a deliberate cause, or '
'<code>from None</code> to hide noisy chaining.</div></div>'
'<hr class="divider">'
'<div class="info-box">📎 <strong>End of Session 9 Part 1</strong> (Chunks A–D: exceptions &amp; hierarchy, '
'<code>try/except/else/finally</code> + re-raising, custom exceptions &amp; chaining, EAFP vs LBYL, 4 '
'examples, 5 edge cases). <strong>Part 2</strong> — Golden Rules → Common Traps → Exercise. '
'<strong>Part 3</strong> — ML Real-World → Interview Q&amp;A → Summary.</div>'
)

# ══════════════════════════ PART 2 ══════════════════════════
md(
'<div class="info-box"><strong>Part 2:</strong> Golden Rules → Common Traps → Exercise</div>'
'<div class="part-header"><h2>4. Golden Rules</h2></div>'
'<div class="rule-block"><div class="rule-title"><span class="rule-badge">Rule 1</span> Catch the narrowest exception that fits.</div>'
'<div class="body-txt">Never bare <code>except:</code>. Prefer <code>except Exception</code> over it, but a specific type over that.</div></div>'
'<div class="rule-block"><div class="rule-title"><span class="rule-badge">Rule 2</span> Don\'t swallow exceptions silently.</div>'
'<div class="body-txt"><code>except: pass</code> hides bugs. Handle meaningfully, log, or re-raise.</div></div>'
'<div class="rule-block"><div class="rule-title"><span class="rule-badge">Rule 3</span> Order handlers specific → general.</div>'
'<div class="body-txt">A broad clause first makes the specific ones below it unreachable.</div></div>'
'<div class="rule-block"><div class="rule-title"><span class="rule-badge">Rule 4</span> Put cleanup in <code>finally</code> or a <code>with</code> — never <code>return</code> from <code>finally</code>.</div>'
'<div class="body-txt">A <code>return</code>/<code>break</code> in <code>finally</code> swallows the in-flight exception.</div></div>'
'<div class="rule-block"><div class="rule-title"><span class="rule-badge">Rule 5</span> Raise specific / custom exception types.</div>'
'<div class="body-txt">Build a domain hierarchy so callers catch broadly or narrowly. The type <em>is</em> the message.</div></div>'
'<div class="rule-block"><div class="rule-title"><span class="rule-badge">Rule 6</span> Chain with <code>raise New(...) from original</code>.</div>'
'<div class="body-txt">Translate low-level errors to your API\'s errors while preserving the root cause for debugging.</div></div>'
'<div class="rule-block"><div class="rule-title"><span class="rule-badge">Rule 7</span> Prefer EAFP; keep the <code>try</code> block small.</div>'
'<div class="body-txt">Wrap only the risky line so you don\'t accidentally catch an exception from elsewhere.</div></div>'
'<div class="rule-block"><div class="rule-title"><span class="rule-badge">Rule 8</span> Don\'t use exceptions for ordinary control flow.</div>'
'<div class="body-txt">They\'re for the <em>exceptional</em>. A predictable branch should be an <code>if</code>, not a caught error.</div></div>'
)

md(
'<div class="trap-header"><h2>5. Common Traps</h2></div>'
'<div class="trap-block"><div class="trap-title"><span class="trap-badge">Trap 1</span> Bare / over-broad <code>except</code>.</div>'
'<div class="body-txt">Swallows typos and <code>KeyboardInterrupt</code> (bare) or every bug (<code>Exception</code>). <strong>Fix:</strong> narrowest type; log if broad.</div></div>'
'<div class="trap-block"><div class="trap-title"><span class="trap-badge">Trap 2</span> <code>return</code> in <code>finally</code>.</div>'
'<div class="body-txt">Silently eats the exception. <strong>Fix:</strong> keep <code>finally</code> to cleanup only.</div></div>'
'<div class="trap-block"><div class="trap-title"><span class="trap-badge">Trap 3</span> Broad handler before specific ones.</div>'
'<div class="body-txt">Makes the specific clauses dead code. <strong>Fix:</strong> order specific → general.</div></div>'
'<div class="trap-block"><div class="trap-title"><span class="trap-badge">Trap 4</span> Losing the traceback / root cause.</div>'
'<div class="body-txt">Raising a new error without <code>from</code> obscures the origin. <strong>Fix:</strong> <code>raise New from original</code>, or bare <code>raise</code> to re-raise.</div></div>'
'<div class="trap-block"><div class="trap-title"><span class="trap-badge">Trap 5</span> Too-large <code>try</code> block.</div>'
'<div class="body-txt">You catch an exception meant for a different line. <strong>Fix:</strong> wrap only the risky statement.</div></div>'
'<div class="trap-block"><div class="trap-title"><span class="trap-badge">Trap 6</span> Exceptions as control flow.</div>'
'<div class="body-txt">Slower and unclear for predictable cases. <strong>Fix:</strong> plain conditionals for expected branches.</div></div>'
)

md(
'<div class="part-header"><h2>6. Exercise</h2></div>'
'<div class="body-txt" style="margin-bottom:10px">Twelve problems, easy → hard, across <code>try/except/else/finally</code>, custom exceptions, chaining, and EAFP. Attempt each in <code>01_errors.ipynb</code>; hints only here — solutions in <code>solutions.ipynb</code>.</div>'
'<div class="exr-block"><div class="exr-title"><span class="cc-badge badge-easy">Easy</span> E1 — <code>safe_divide(a, b)</code> → <code>None</code> on divide-by-zero</div><div class="hint-box">💡 <code>try: return a/b</code> / <code>except ZeroDivisionError: return None</code>.</div></div>'
'<div class="exr-block"><div class="exr-title"><span class="cc-badge badge-easy">Easy</span> E2 — <code>get(coll, k)</code> catching <code>(KeyError, IndexError)</code> together</div><div class="hint-box">💡 One <code>except (KeyError, IndexError):</code> handles both dict &amp; list access.</div></div>'
'<div class="exr-block"><div class="exr-title"><span class="cc-badge badge-easy">Easy</span> E3 — Use <code>else</code> to run success-only code</div><div class="hint-box">💡 Put the parse in <code>try</code>, the "it worked" branch in <code>else</code>.</div></div>'
'<div class="exr-block"><div class="exr-title"><span class="cc-badge badge-med">Medium</span> E4 — Guaranteed cleanup with <code>finally</code> (runs on success &amp; error)</div><div class="hint-box">💡 Append to a log in <code>finally</code>; verify it runs whether or not the body raised.</div></div>'
'<div class="exr-block"><div class="exr-title"><span class="cc-badge badge-med">Medium</span> E5 — Custom <code>InsufficientFunds(Exception)</code> with an <code>.amount</code> attribute</div><div class="hint-box">💡 <code>super().__init__(message)</code>; store <code>self.amount = amount</code>.</div></div>'
'<div class="exr-block"><div class="exr-title"><span class="cc-badge badge-med">Medium</span> E6 — Log, then re-raise the same exception</div><div class="hint-box">💡 In <code>except</code>: do your logging, then a bare <code>raise</code> (keeps the traceback).</div></div>'
'<div class="exr-block"><div class="exr-title"><span class="cc-badge badge-med">Medium</span> E7 — Chain: <code>raise ConfigError("missing") from KeyError</code>, check <code>__cause__</code></div><div class="hint-box">💡 <code>except KeyError as e: raise ConfigError(...) from e</code>.</div></div>'
'<div class="exr-block"><div class="exr-title"><span class="cc-badge badge-med">Medium</span> E8 — <code>my_get(d, k, default)</code> via EAFP (no <code>in</code> check)</div><div class="hint-box">💡 <code>try: return d[k]</code> / <code>except KeyError: return default</code>.</div></div>'
'<div class="exr-block"><div class="exr-title"><span class="cc-badge badge-hard">Hard</span> E9 — <code>validate_record(rec, required)</code> raising on the first missing field</div><div class="hint-box">💡 Loop <code>required</code>; raise a custom <code>ValidationError(f"missing: {f}")</code> on the first absent key.</div></div>'
'<div class="exr-block"><div class="exr-title"><span class="cc-badge badge-hard">Hard</span> E10 — <code>parse_ints(strings)</code> → <code>(values, errors)</code> (partial success)</div><div class="hint-box">💡 Try each; append good ones to <code>values</code>, failed ones to <code>errors</code> — don\'t abort on the first bad item.</div></div>'
'<div class="exr-block"><div class="exr-title"><span class="cc-badge badge-hard">Hard</span> E11 — <code>retry_on(fn, exc, times)</code> — retry only on <code>exc</code>, let others propagate</div><div class="hint-box">💡 <code>except exc as e: last = e</code> — other exceptions aren\'t caught, so they escape immediately.</div></div>'
'<div class="exr-block"><div class="exr-title"><span class="cc-badge badge-hard">Hard</span> E12 — <code>ensure(cond, exc_type, msg)</code> — raise if a condition is false</div><div class="hint-box">💡 <code>if not cond: raise exc_type(msg)</code> — a reusable validation guard.</div></div>'
)

# ══════════════════════════ PART 3 ══════════════════════════
md(
'<div class="info-box"><strong>Part 3:</strong> ML Real-World → Interview Q&amp;A → Code Challenges → Summary</div>'
'<div class="ml-header"><h2>7. ML Real-World Connection</h2></div>'
'<div class="ml-block"><div class="ml-title"><span class="ml-badge">ML 1</span> Robust data pipelines — partial-success parsing</div>'
'<div class="body-txt">Real datasets have bad rows. Wrap per-record parsing in <code>try/except</code> and collect failures (the <code>parse_ints</code> pattern) rather than crashing the whole ingest — log the bad rows, keep the good ones.</div></div>'
'<div class="ml-block"><div class="ml-title"><span class="ml-badge">ML 2</span> Retry flaky I/O</div>'
'<div class="body-txt">Dataset downloads, model-registry pulls, and LLM/API calls fail transiently. <code>retry_on(fn, exc, times)</code> (and the S6 <code>@retry</code> decorator) is the resilience layer — retry only the recoverable exceptions.</div></div>'
'<div class="ml-block"><div class="ml-title"><span class="ml-badge">ML 3</span> Custom exceptions for a clean API surface</div>'
'<div class="body-txt">A library raises its own <code>ModelError</code>/<code>DataError</code> hierarchy, chaining the low-level cause with <code>from</code> — callers catch one family, and you keep the root cause in logs.</div></div>'
'<div class="ml-block"><div class="ml-title"><span class="ml-badge">ML 4</span> Input validation with clear errors</div>'
'<div class="body-txt">Validate shapes/dtypes/ranges up front and raise informative <code>ValueError</code>/<code>TypeError</code> — a <code>ValueError: expected (N, 3), got (N, 4)</code> saves hours vs a deep, cryptic downstream crash.</div></div>'
'<div class="ml-block"><div class="ml-title"><span class="ml-badge">ML 5</span> Don\'t mask real bugs</div>'
'<div class="body-txt">A broad <code>except</code> around a training step can hide a <code>NameError</code> or shape bug as "handled." Catch narrowly (e.g. <code>except RuntimeError</code> for CUDA OOM specifically) so genuine bugs still surface.</div></div>'
)

md(
'<div class="interview-header"><h2>8. Interview Questions</h2></div>'
'<div class="sub-header"><h3>8a — Conceptual Q&amp;A</h3></div>'
'<div class="qa-block"><div class="qa-q"><span class="q-num">1</span> What happens when an exception is raised and not caught?</div><div class="qa-a">It propagates up the call stack, unwinding frames, until a matching <code>except</code> handles it — or it reaches the top and terminates the program with a traceback.</div></div>'
'<div class="qa-block"><div class="qa-q"><span class="q-num">2</span> Difference between <code>except:</code> and <code>except Exception:</code>?</div><div class="qa-a">Bare <code>except:</code> catches <em>everything</em>, including <code>KeyboardInterrupt</code>/<code>SystemExit</code>. <code>except Exception</code> excludes those (they inherit <code>BaseException</code> directly). Prefer specific types over both.</div></div>'
'<div class="qa-block"><div class="qa-q"><span class="q-num">3</span> When do <code>else</code> and <code>finally</code> run?</div><div class="qa-a"><code>else</code> runs only if the <code>try</code> raised nothing; <code>finally</code> runs always — success, exception, or <code>return</code>/<code>break</code>.</div></div>'
'<div class="qa-block"><div class="qa-q"><span class="q-num">4</span> Why avoid <code>return</code> inside <code>finally</code>?</div><div class="qa-a">It overrides any in-flight exception (and any earlier <code>return</code>), silently swallowing errors.</div></div>'
'<div class="qa-block"><div class="qa-q"><span class="q-num">5</span> How do you re-raise the current exception?</div><div class="qa-a">A bare <code>raise</code> inside the <code>except</code> block — it re-raises the same exception, preserving the original traceback.</div></div>'
'<div class="qa-block"><div class="qa-q"><span class="q-num">6</span> How do you make a custom exception?</div><div class="qa-a">Subclass <code>Exception</code> (or a more specific base); optionally add attributes and build a domain hierarchy so callers can catch a family.</div></div>'
'<div class="qa-block"><div class="qa-q"><span class="q-num">7</span> What does <code>raise X from Y</code> do?</div><div class="qa-a">Explicit chaining — sets <code>X.__cause__ = Y</code> and shows "direct cause" in the traceback. <code>from None</code> suppresses the chained context.</div></div>'
'<div class="qa-block"><div class="qa-q"><span class="q-num">8</span> <code>__cause__</code> vs <code>__context__</code>?</div><div class="qa-a"><code>__cause__</code> is set explicitly by <code>from</code>; <code>__context__</code> is set implicitly when an exception is raised while handling another. Both aid debugging.</div></div>'
'<div class="qa-block"><div class="qa-q"><span class="q-num">9</span> EAFP vs LBYL?</div><div class="qa-a">EAFP = try then handle (Pythonic, atomic, no check-then-use race); LBYL = check preconditions first (can race — TOCTOU — and duplicates logic).</div></div>'
'<div class="qa-block"><div class="qa-q"><span class="q-num">10</span> Why order handlers specific → general?</div><div class="qa-a">Clauses match top-down; a broad clause first shadows the specific ones below, making them unreachable.</div></div>'
'<div class="qa-block"><div class="qa-q"><span class="q-num">11</span> When should you NOT use exceptions?</div><div class="qa-a">For ordinary, expected control flow — use a plain <code>if</code>. Exceptions are for exceptional conditions.</div></div>'
'<div class="qa-block"><div class="qa-q"><span class="q-num">12</span> Why keep the <code>try</code> block small?</div><div class="qa-a">So the handler only catches the failure you intend — a large <code>try</code> may catch an exception from an unrelated line and mask it.</div></div>'
)

md(
'<div class="sub-header"><h3>8b — Code Challenges (attempt, then expand the solution)</h3></div>'
'<div class="cc-block"><div class="cc-title"><span class="cc-badge badge-easy">Easy</span> C1 — <code>safe_get(seq, i, default=None)</code></div>'
'<details class="sol"><summary>Solution</summary><div class="code-block"><span class="ck">def</span> <span class="cm">safe_get</span>(seq, i, default=<span class="ck">None</span>):<br>&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">try</span>: <span class="ck">return</span> seq[i]<br>&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">except</span> (IndexError, KeyError): <span class="ck">return</span> default</div><div class="qa-a">EAFP index/key access with a fallback — works for lists and dicts.</div></details></div>'
'<div class="cc-block"><div class="cc-title"><span class="cc-badge badge-easy">Easy</span> C2 — <code>checked_sqrt(x)</code>: raise <code>ValueError</code> on negatives</div>'
'<details class="sol"><summary>Solution</summary><div class="code-block"><span class="ck">def</span> <span class="cm">checked_sqrt</span>(x):<br>&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">if</span> x &lt; <span class="cn">0</span>: <span class="ck">raise</span> ValueError(<span class="cs">"negative"</span>)<br>&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">return</span> x ** <span class="cn">0.5</span></div><div class="qa-a">Validate then compute; the type (<code>ValueError</code>) tells the caller it\'s a bad value.</div></details></div>'
'<div class="cc-block"><div class="cc-title"><span class="cc-badge badge-med">Med</span> C3 — <code>run_all(funcs)</code> → list of <code>(ok, result_or_error)</code></div>'
'<details class="sol"><summary>Solution</summary><div class="code-block"><span class="ck">def</span> <span class="cm">run_all</span>(funcs):<br>&nbsp;&nbsp;&nbsp;&nbsp;out = []<br>&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">for</span> f <span class="ck">in</span> funcs:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">try</span>: out.<span class="cm">append</span>((<span class="ck">True</span>, f()))<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">except</span> Exception <span class="ck">as</span> e: out.<span class="cm">append</span>((<span class="ck">False</span>, <span class="cm">type</span>(e).__name__))<br>&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">return</span> out</div><div class="qa-a">Isolate failures per task so one bad function doesn\'t abort the batch — the partial-success pattern.</div></details></div>'
'<div class="cc-block"><div class="cc-title"><span class="cc-badge badge-med">Med</span> C4 — <code>reraise_as(from_exc, to_exc)</code> context manager (translate errors)</div>'
'<details class="sol"><summary>Solution</summary><div class="code-block"><span class="ck">from</span> contextlib <span class="ck">import</span> contextmanager<br><span class="cm">@contextmanager</span><br><span class="ck">def</span> <span class="cm">reraise_as</span>(from_exc, to_exc):<br>&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">try</span>:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">yield</span><br>&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">except</span> from_exc <span class="ck">as</span> e:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">raise</span> to_exc(<span class="cm">str</span>(e)) <span class="ck">from</span> e</div><div class="qa-a">Combines Session 8 context managers + chaining: <code>with reraise_as(KeyError, ConfigError): ...</code> translates the error and keeps the cause.</div></details></div>'
'<div class="cc-block"><div class="cc-title"><span class="cc-badge badge-med">Med</span> C5 — <code>validate_age(age)</code>: <code>TypeError</code> if not int, <code>ValueError</code> if negative</div>'
'<details class="sol"><summary>Solution</summary><div class="code-block"><span class="ck">def</span> <span class="cm">validate_age</span>(age):<br>&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">if</span> <span class="ck">not</span> <span class="cm">isinstance</span>(age, <span class="cm">int</span>): <span class="ck">raise</span> TypeError(<span class="cs">"age must be int"</span>)<br>&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">if</span> age &lt; <span class="cn">0</span>: <span class="ck">raise</span> ValueError(<span class="cs">"age must be &gt;= 0"</span>)<br>&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">return</span> age</div><div class="qa-a">Different failure modes get different exception <em>types</em> — the caller can distinguish "wrong type" from "bad value."</div></details></div>'
'<div class="cc-block"><div class="cc-title"><span class="cc-badge badge-med">Med</span> C6 — <code>@catch(exc, default)</code> decorator (S6 callback)</div>'
'<details class="sol"><summary>Solution</summary><div class="code-block"><span class="ck">from</span> functools <span class="ck">import</span> wraps<br><span class="ck">def</span> <span class="cm">catch</span>(exc, default):<br>&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">def</span> <span class="cm">deco</span>(fn):<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="cm">@wraps(fn)</span><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">def</span> <span class="cm">w</span>(*a, **k):<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">try</span>: <span class="ck">return</span> fn(*a, **k)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">except</span> exc: <span class="ck">return</span> default<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">return</span> w<br>&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">return</span> deco</div><div class="qa-a">A parameterized decorator (S6 3-layer) that turns a given exception into a default — <code>@catch(ZeroDivisionError, inf)</code>.</div></details></div>'
'<div class="cc-block"><div class="cc-title"><span class="cc-badge badge-hard">Hard</span> C7 — Collect all errors, then raise a combined <code>AggregateError</code></div>'
'<details class="sol"><summary>Solution</summary><div class="code-block"><span class="ck">class</span> <span class="cm">AggregateError</span>(Exception):<br>&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">def</span> <span class="cm">__init__</span>(self, errors):<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="cm">super</span>().<span class="cm">__init__</span>(<span class="cs">f"{len(errors)} errors"</span>); self.errors = errors<br><br><span class="ck">def</span> <span class="cm">process_all</span>(items, fn):<br>&nbsp;&nbsp;&nbsp;&nbsp;results, errors = [], []<br>&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">for</span> it <span class="ck">in</span> items:<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">try</span>: results.<span class="cm">append</span>(fn(it))<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">except</span> Exception <span class="ck">as</span> e: errors.<span class="cm">append</span>((it, e))<br>&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">if</span> errors: <span class="ck">raise</span> AggregateError(errors)<br>&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">return</span> results</div><div class="qa-a">Process everything, gather failures, and report them together at the end — like the built-in <code>ExceptionGroup</code> (3.11+). Great for batch validation.</div></details></div>'
'<div class="cc-block"><div class="cc-title"><span class="cc-badge badge-hard">Hard</span> C8 — Parameterized <code>@retry(times, exc)</code> decorator</div>'
'<details class="sol"><summary>Solution</summary><div class="code-block"><span class="ck">def</span> <span class="cm">retry</span>(times=<span class="cn">3</span>, exc=Exception):<br>&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">def</span> <span class="cm">deco</span>(fn):<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="cm">@wraps(fn)</span><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">def</span> <span class="cm">w</span>(*a, **k):<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;last = <span class="ck">None</span><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">for</span> _ <span class="ck">in</span> <span class="cm">range</span>(times):<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">try</span>: <span class="ck">return</span> fn(*a, **k)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">except</span> exc <span class="ck">as</span> e: last = e<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">raise</span> last<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">return</span> w<br>&nbsp;&nbsp;&nbsp;&nbsp;<span class="ck">return</span> deco</div><div class="qa-a">The Session 6 decorator + this session\'s error handling: retry only on <code>exc</code>, re-raise the last failure after <code>times</code> attempts. This is what tenacity productizes.</div></details></div>'
)

md(
'<div class="summary-header"><h2>9. Summary Table — Session 9</h2></div>'
'<table class="summary">'
'<tr><th>Concept</th><th>Why it matters in ML</th><th>Interview frequency</th></tr>'
'<tr><td><code>try/except</code> + specific types</td><td>Robust pipelines; recover from bad data/IO</td><td><span class="freq-vh">Very High</span></td></tr>'
'<tr><td>The exception hierarchy</td><td>Catching families correctly</td><td><span class="freq-h">High</span></td></tr>'
'<tr><td><code>else</code>/<code>finally</code></td><td>Guaranteed cleanup of resources</td><td><span class="freq-h">High</span></td></tr>'
'<tr><td>Custom exceptions &amp; hierarchy</td><td>Clean library/API error surface</td><td><span class="freq-h">High</span></td></tr>'
'<tr><td>Chaining (<code>raise … from</code>)</td><td>Translate errors, keep root cause</td><td><span class="freq-m">Medium</span></td></tr>'
'<tr><td>Re-raising (bare <code>raise</code>)</td><td>Handle-then-propagate; keep traceback</td><td><span class="freq-m">Medium</span></td></tr>'
'<tr><td>EAFP vs LBYL</td><td>Pythonic, race-free access</td><td><span class="freq-vh">Very High</span></td></tr>'
'<tr><td>Retry / partial-success patterns</td><td>Flaky IO; tolerant batch ingest</td><td><span class="freq-h">High</span></td></tr>'
'<tr><td>Don\'t swallow / narrow catches</td><td>Not hiding real bugs</td><td><span class="freq-h">High</span></td></tr>'
'</table>'
'<hr class="divider">'
'<div style="background:#1e1e2e; border-left:4px solid #a6e3a1; padding:14px 18px; border-radius:8px; font-family:monospace; color:#cdd6f4;">'
'<strong style="color:#a6e3a1">✅ Session 9 complete.</strong> Error handling end to end: exceptions &amp; the '
'hierarchy, <code>try/except/else/finally</code>, custom exceptions &amp; chaining, EAFP vs LBYL, 4 examples, '
'5 edge cases, 8 golden rules, 6 traps, 12 exercises, ML connections, 12 conceptual Q&amp;A, 8 code '
'challenges, summary table.<br>'
'<span style="color:#6c7086">Next — Session 10 (the finale): Typing &amp; dataclasses (type hints, '
'<code>Optional</code>/<code>Union</code>/generics, <code>@dataclass</code>) — feeds clean FastAPI &amp; '
'Pydantic code.</span></div>'
)

nb = new_notebook(cells=cells)
nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
nb.metadata["language_info"] = {"name": "python"}
nbf.write(nb, "theory.ipynb")
print("wrote theory.ipynb with", len(cells), "cells")
