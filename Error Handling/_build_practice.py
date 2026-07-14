# Builder for Session 9, 01_errors.ipynb (hands-on practice scaffold).
import nbformat as nbf
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell

cells = []
def md(t):   cells.append(new_markdown_cell(t))
def code(t): cells.append(new_code_cell(t))

md('<div style="background:#1e1e2e; padding:16px 20px; border-radius:8px; font-family:monospace; '
   'color:#cdd6f4; line-height:1.8">'
   '<p style="margin:0 0 8px 0; color:#cba6f7; font-weight:bold; font-size:1.05em;">📎 Session 9 — Error Handling · Hands-on</p>'
   '<p style="margin:0;">Attempt space for the 12 <strong>Exercises</strong> and 8 <strong>Code Challenges</strong>. '
   'Hints in <code>theory.ipynb</code>; worked solutions in <code>solutions.ipynb</code> — try each yourself first.</p></div>')

md("### Exercises (Part 2 · §6) — 12 problems")
EX = [
 ('E1 (Easy)', 'safe_divide(a, b) -> None on divide-by-zero', 'except ZeroDivisionError: return None'),
 ('E2 (Easy)', 'get(coll, k) catching (KeyError, IndexError) together', 'one except (KeyError, IndexError)'),
 ('E3 (Easy)', 'Use else to run success-only code', 'parse in try; "worked" branch in else'),
 ('E4 (Med)',  'Guaranteed cleanup with finally (runs on success & error)', 'append to a log in finally'),
 ('E5 (Med)',  'Custom InsufficientFunds(Exception) with .amount', 'super().__init__(msg); self.amount = amount'),
 ('E6 (Med)',  'Log, then re-raise the same exception', 'except ...: log; then bare raise'),
 ('E7 (Med)',  'Chain: raise ConfigError("missing") from KeyError; check __cause__', 'except KeyError as e: raise ConfigError(...) from e'),
 ('E8 (Med)',  'my_get(d, k, default) via EAFP (no `in` check)', 'try: return d[k] / except KeyError: return default'),
 ('E9 (Hard)', 'validate_record(rec, required) raising on first missing field', 'loop required; raise ValidationError(f"missing: {f}")'),
 ('E10 (Hard)','parse_ints(strings) -> (values, errors) partial success', 'try each; good->values, bad->errors; do not abort'),
 ('E11 (Hard)','retry_on(fn, exc, times): retry only on exc, others propagate', 'except exc as e: last=e; raise last after loop'),
 ('E12 (Hard)','ensure(cond, exc_type, msg): raise if condition false', 'if not cond: raise exc_type(msg)'),
]
for tag, prob, hint in EX:
    code(f"# {tag} — {prob}\n# Hint: {hint}\n\n")

md("### Code Challenges (Part 3 · §8b) — 8 problems")
CC = [
 ('C1 (Easy)', 'safe_get(seq, i, default=None)'),
 ('C2 (Easy)', 'checked_sqrt(x): raise ValueError on negatives'),
 ('C3 (Med)',  'run_all(funcs) -> list of (ok, result_or_error)'),
 ('C4 (Med)',  'reraise_as(from_exc, to_exc) context manager (translate errors)'),
 ('C5 (Med)',  'validate_age(age): TypeError if not int, ValueError if negative'),
 ('C6 (Med)',  '@catch(exc, default) decorator (return default on exc)'),
 ('C7 (Hard)', 'Collect all errors, then raise a combined AggregateError'),
 ('C8 (Hard)', 'Parameterized @retry(times, exc) decorator'),
]
for tag, prob in CC:
    code(f"# {tag} — {prob}\n\n")

nb = new_notebook(cells=cells)
nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
nb.metadata["language_info"] = {"name": "python"}
nbf.write(nb, "01_errors.ipynb")
print("wrote 01_errors.ipynb with", len(cells), "cells")
