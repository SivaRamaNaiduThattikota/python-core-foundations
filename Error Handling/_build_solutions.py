# Builder for Session 9, solutions.ipynb (answer key).
# Runnable, verified solutions for all 12 Exercises and 8 Code Challenges.
import nbformat as nbf
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell

cells = []
def md(t):   cells.append(new_markdown_cell(t))
def code(t): cells.append(new_code_cell(t))

md('<div style="background:#1e1e2e; padding:16px 20px; border-radius:8px; font-family:monospace; '
   'color:#cdd6f4; line-height:1.8">'
   '<p style="margin:0 0 8px 0; color:#cba6f7; font-weight:bold; font-size:1.05em;">✅ Session 9 — Error Handling · Solutions</p>'
   '<p style="margin:0;">Worked, runnable solutions for the 12 <strong>Exercises</strong> and 8 '
   '<strong>Code Challenges</strong>. Run top to bottom to verify. Try them in '
   '<code>01_errors.ipynb</code> first.</p></div>')

md("### Exercises — Solutions")
code('from functools import wraps\n'
    'from contextlib import contextmanager')
code('# E1 — safe_divide\n'
    'def safe_divide(a, b):\n'
    '    try: return a / b\n'
    '    except ZeroDivisionError: return None\n\n'
    'print(safe_divide(6, 2), safe_divide(1, 0))   # 3.0 None')
code('# E2 — catch (KeyError, IndexError) together\n'
    'def get(coll, k):\n'
    '    try: return coll[k]\n'
    '    except (KeyError, IndexError): return None\n\n'
    'print(get({"a": 1}, "a"), get([1, 2], 5))     # 1 None')
code('# E3 — else runs on success only\n'
    'def run(s):\n'
    '    try: n = int(s)\n'
    '    except ValueError: return "err"\n'
    '    else: return "ok"\n\n'
    'print(run("5"), run("x"))                     # ok err')
code('# E4 — finally always runs\n'
    'log = []\n'
    'def op(fail):\n'
    '    try:\n'
    '        if fail: raise ValueError()\n'
    '    finally:\n'
    '        log.append("cleanup")\n'
    'try: op(True)\n'
    'except ValueError: pass\n'
    'op(False)\n'
    'print(log)                                    # [\'cleanup\', \'cleanup\']')
code('# E5 — custom exception with an attribute\n'
    'class InsufficientFunds(Exception):\n'
    '    def __init__(self, amount):\n'
    '        super().__init__(f"need {amount}")\n'
    '        self.amount = amount\n\n'
    'try: raise InsufficientFunds(50)\n'
    'except InsufficientFunds as e: print(e, "| amount:", e.amount)   # need 50 | amount: 50')
code('# E6 — log then re-raise\n'
    'def logged():\n'
    '    try: int("x")\n'
    '    except ValueError:\n'
    '        print("logging..."); raise        # bare raise re-raises the same exception\n\n'
    'try: logged()\n'
    'except ValueError: print("re-raised OK")')
code('# E7 — chain with `from`\n'
    'class ConfigError(Exception): pass\n'
    'def load(cfg, key):\n'
    '    try: return cfg[key]\n'
    '    except KeyError as e: raise ConfigError("missing") from e\n\n'
    'try: load({}, "db")\n'
    'except ConfigError as e: print("cause:", type(e.__cause__).__name__)   # KeyError')
code('# E8 — my_get via EAFP\n'
    'def my_get(d, k, default=None):\n'
    '    try: return d[k]\n'
    '    except KeyError: return default\n\n'
    'print(my_get({"a": 1}, "a"), my_get({"a": 1}, "z", -1))   # 1 -1')
code('# E9 — validate_record raises on first missing field\n'
    'class ValidationError(Exception): pass\n'
    'def validate_record(rec, required):\n'
    '    for f in required:\n'
    '        if f not in rec: raise ValidationError(f"missing: {f}")\n'
    '    return True\n\n'
    'try: validate_record({"name": "x"}, ["name", "email"])\n'
    'except ValidationError as e: print(e)         # missing: email')
code('# E10 — parse_ints: partial success\n'
    'def parse_ints(strings):\n'
    '    values, errors = [], []\n'
    '    for s in strings:\n'
    '        try: values.append(int(s))\n'
    '        except ValueError: errors.append(s)\n'
    '    return values, errors\n\n'
    'print(parse_ints(["1", "x", "3", "y"]))       # ([1, 3], [\'x\', \'y\'])')
code('# E11 — retry only on a specific exception\n'
    'def retry_on(fn, exc, times):\n'
    '    last = None\n'
    '    for _ in range(times):\n'
    '        try: return fn()\n'
    '        except exc as e: last = e            # other exceptions propagate immediately\n'
    '    raise last\n\n'
    'st = {"n": 0}\n'
    'def flaky():\n'
    '    st["n"] += 1\n'
    '    if st["n"] < 2: raise ValueError()\n'
    '    return "ok"\n'
    'print(retry_on(flaky, ValueError, 3))         # ok')
code('# E12 — ensure(cond, exc_type, msg)\n'
    'def ensure(cond, exc_type, msg):\n'
    '    if not cond: raise exc_type(msg)\n\n'
    'try: ensure(False, ValueError, "bad")\n'
    'except ValueError as e: print(e)              # bad')

md("### Code Challenges — Solutions")
code('# C1 — safe_get\n'
    'def safe_get(seq, i, default=None):\n'
    '    try: return seq[i]\n'
    '    except (IndexError, KeyError): return default\n\n'
    'print(safe_get([1, 2, 3], 1), safe_get([1, 2], 9, "?"))   # 2 ?')
code('# C2 — checked_sqrt\n'
    'def checked_sqrt(x):\n'
    '    if x < 0: raise ValueError("negative")\n'
    '    return x ** 0.5\n\n'
    'print(checked_sqrt(9))                        # 3.0\n'
    'try: checked_sqrt(-1)\n'
    'except ValueError as e: print("raised:", e)')
code('# C3 — run_all -> (ok, result_or_error) per func\n'
    'def run_all(funcs):\n'
    '    out = []\n'
    '    for f in funcs:\n'
    '        try: out.append((True, f()))\n'
    '        except Exception as e: out.append((False, type(e).__name__))\n'
    '    return out\n\n'
    'print(run_all([lambda: 1, lambda: 1/0, lambda: int("x")]))')
code('# C4 — reraise_as context manager (translate + chain)\n'
    'class ConfigError(Exception): pass\n'
    '@contextmanager\n'
    'def reraise_as(from_exc, to_exc):\n'
    '    try:\n'
    '        yield\n'
    '    except from_exc as e:\n'
    '        raise to_exc(str(e)) from e\n\n'
    'try:\n'
    '    with reraise_as(KeyError, ConfigError):\n'
    '        {}["x"]\n'
    'except ConfigError as e: print("cause:", type(e.__cause__).__name__)   # KeyError')
code('# C5 — validate_age (type vs value errors)\n'
    'def validate_age(age):\n'
    '    if not isinstance(age, int): raise TypeError("age must be int")\n'
    '    if age < 0: raise ValueError("age must be >= 0")\n'
    '    return age\n\n'
    'print(validate_age(30))                       # 30\n'
    'try: validate_age(-1)\n'
    'except ValueError as e: print("raised:", e)')
code('# C6 — @catch(exc, default) decorator\n'
    'def catch(exc, default):\n'
    '    def deco(fn):\n'
    '        @wraps(fn)\n'
    '        def w(*a, **k):\n'
    '            try: return fn(*a, **k)\n'
    '            except exc: return default\n'
    '        return w\n'
    '    return deco\n\n'
    '@catch(ZeroDivisionError, float("inf"))\n'
    'def recip(x): return 1 / x\n'
    'print(recip(4), recip(0))                     # 0.25 inf')
code('# C7 — collect all errors, then raise AggregateError\n'
    'class AggregateError(Exception):\n'
    '    def __init__(self, errors):\n'
    '        super().__init__(f"{len(errors)} errors")\n'
    '        self.errors = errors\n\n'
    'def process_all(items, fn):\n'
    '    results, errors = [], []\n'
    '    for it in items:\n'
    '        try: results.append(fn(it))\n'
    '        except Exception as e: errors.append((it, type(e).__name__))\n'
    '    if errors: raise AggregateError(errors)\n'
    '    return results\n\n'
    'try: process_all(["1", "x", "3"], int)\n'
    'except AggregateError as e: print(e, "|", e.errors)   # 1 errors | [(\'x\', \'ValueError\')]')
code('# C8 — parameterized @retry(times, exc)\n'
    'def retry(times=3, exc=Exception):\n'
    '    def deco(fn):\n'
    '        @wraps(fn)\n'
    '        def w(*a, **k):\n'
    '            last = None\n'
    '            for _ in range(times):\n'
    '                try: return fn(*a, **k)\n'
    '                except exc as e: last = e\n'
    '            raise last\n'
    '        return w\n'
    '    return deco\n\n'
    'st2 = {"n": 0}\n'
    '@retry(times=5, exc=ValueError)\n'
    'def f2():\n'
    '    st2["n"] += 1\n'
    '    if st2["n"] < 3: raise ValueError()\n'
    '    return "done"\n'
    'print(f2(), "after", st2["n"])                # done after 3')

nb = new_notebook(cells=cells)
nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
nb.metadata["language_info"] = {"name": "python"}
nbf.write(nb, "solutions.ipynb")
print("wrote solutions.ipynb with", len(cells), "cells")
