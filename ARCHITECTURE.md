# Core Python Foundations — Architecture & Teaching System

> The canonical reference for **how this course is built and how it functions** — the curriculum
> structure, the teaching flow, the two-artifact learning model, and the notebook UI design system.
> Read this before authoring or editing any lesson so every session stays consistent.

---

## The Flow, In One Read (Synthesis)

### 1. The macro flow is a dependency chain, not a list of topics
The 10 sessions are ordered so each one requires the last. And Session 2 splits into four
sub-sessions whose very ordering is the argument:

- **2A List** — mutable, ordered, "array of references" → builds on S1's "mutable shared object."
- **2B Tuple** — introduced explicitly as the immutable counterpart to list. The contrast *is* the lesson.
- **2C Set** — immutability (2B) → hashability → why membership is O(1).
- **2D Dict** — the synthesis: keys hashable like tuple/set, values arbitrary like a list, ordered like a sequence. The finale.

The clearest proof: `first_unique` at the end of 2C fails on purpose — a set knows only
present/absent, but the task needs **counts + order**, which a `Counter` gives. That failure is the
deliberate seam that justifies why Dict follows Set. The curriculum earns each next structure.

### 2. There's one spine threaded through everything
The through-line from S1 never drops: **a name is a tag on an object → objects are mutable/immutable
→ mutability decides hashability → hashability decides what can be a set element / dict key.** Plus
the second axis: **hash-based (set/dict, O(1) lookup) vs array-based (list/tuple, O(1) index, O(n)
search).**

Traceable callbacks:

- Mutable-default-arg trap (S1) → `dict.fromkeys(keys, [])` aliasing (2D) → mutable class attribute.
- `[[0]*3]*3` (S1) → the list matrix trap (2A) → nested-comprehension fix.
- `+=` mutate-vs-rebind (S1) → list `+=` vs `+` (2A) → tuple `+=` always rebinds (2B).
- `x in list` O(n) (2A) → set O(1) (2C) → dict key O(1) (2D).
- SettingWithCopyWarning (S1 ML) → NumPy views share memory (2A ML).
- The OpsRAG dedup thread runs S1 → 2C → 2D.

### 3. Each lesson runs a fixed 9-section arc — and the order is pedagogical
Theory (concept-first + Power BI/SQL anchor) → Example (runnable, step-by-step) → Edge Cases (5–8,
outputs verified by running) → Golden Rules → Common Traps → Exercise (easy→hard, with hints) → ML
Real-World → Interview Q&A (conceptual + code challenges) → Summary Table (concept | ML value |
interview frequency).

The logic of that sequence: **understand → verify → break at the sharp corners → codify into rules
→ warn → active recall → transfer to your domain → assess → compress.** And long lessons are
delivered in Parts (1: Theory/Example/Edge, 2: Rules/Traps/Exercise, 3: ML/Interview/Summary),
further split into Chunks (A/B/C) — one at a time, waiting for "go."

### 4. How you actually learn in this repo (the two-artifact pattern)
This is the part that matters most for teaching well:

- `theory.ipynb` = the delivered lesson (the heavily-styled teaching artifact; `_build_01_dict.py`
  confirms these are generated programmatically).
- `01_*.ipynb` / `02_*.ipynb` = your hands-on re-derivation, where you retype, run, experiment, err,
  and self-correct.

And you genuinely work it — visible in the notebooks:

- You write wrong answers and iterate: `running_max` first threw `'>' not supported between int and
  list`, then you fixed it to the clean accumulator. In the mutability exercise you wrote a backwards
  comment ("copies the list not pointer") and there's a correction block owning that misconception.
- You go past the assignment — the `SneakyKey` experiment (mutating a hashed key to break dict
  lookup) wasn't required; that's curiosity.
- You solve the same thing multiple ways: `safe_update` via `.copy()`, then `{**d}`, then `d | {}`;
  dedup via `dict.fromkeys` and an explicit seen-set.
- You anchor to your real work — OpsRAG dedup, Commercial Wire pandas.

So the style is calibrated to you: **BI/data person → ML engineer**, hence the SQL/Power BI analogies
and the ML + interview framing on every concept.

### 5. The rules held to
From the "locked-in" format: all 9 sections in order every lesson, concept before mechanics,
code-heavy and runnable, push back honestly and verify outputs by actually running code rather than
asserting them, no project branding, direct tone, ask before assuming, and close each lesson with a
summary table + preview of the next. Triggers: `"Quiz me with 20 code interview questions"` and
`"Review my notebook and give feedback"`.

---

**The flow, in one line:** a dependency-ordered spiral built on a single object-model spine, each
concept taught in a fixed 9-section arc, delivered in parts, then re-derived by you in a practice
notebook where mistakes are the point.

---

## 1. Purpose & Audience

A 10-session, depth-first track that takes a **BI / data professional (SQL + Power BI background)
moving into ML engineering** through core Python, one concept per session, gone deep.

Two design commitments shape everything:

- **Concept first, mechanics second** — build the mental model, *then* the syntax.
- **Anchored to what the learner already knows** — Power BI / SQL analogies as bridges, and an
  ML / interview payoff attached to every concept.

Source of truth for the format: `00_course_outline.ipynb` (the syllabus + the locked-in teaching format).

---

## 2. Curriculum Architecture — a dependency chain, not a topic list

The 10 sessions are ordered so each one *requires* the previous. Session 2 (Sequences) is further
split into four sub-sessions whose ordering is itself the argument.

```
1. Mutability & the Object Model      ← the foundation everything rests on
2. Sequences (deep)
     2A List    mutable, ordered, "array of references"      (builds on S1)
     2B Tuple   the IMMUTABLE counterpart to list            (contrast IS the lesson)
     2C Set     hash table of unique hashable elements        (immutability → hashability → O(1))
     2D Dict    hash table WITH values — the synthesis        (keys like set/tuple, values like list)
3. Strings                            immutable sequence      (builds on 2A + 2B)  ← NEXT
4. Comprehensions & generators
5. Functions, scope & closures
6. Decorators
7. OOP & dunder methods
8. Iterators & context managers
9. Error handling
10. Typing & dataclasses
```

**The seam that proves the ordering:** at the end of 2C, `first_unique` deliberately fails with a
plain set — a set knows only *present/absent*, but the task needs **counts + order**, which a
`Counter` gives. That failure is the bridge that justifies why Dict follows Set.

---

## 3. The Through-Line (the spine every session reinforces)

One mental model runs from Session 1 forward:

> **A name is a tag on an object → objects are mutable or immutable → mutability decides
> hashability → hashability decides what can be a set element / dict key.**

Plus a second axis introduced in Session 2:

> **Hash-based (set / dict → O(1) lookup) vs array-based (list / tuple → O(1) index, O(n) search).
> Choosing a structure = choosing a complexity for your access pattern.**

Concrete callbacks that recur (author new lessons to keep threading these):

| Idea introduced | Reappears as |
|---|---|
| Mutable default argument (S1) | `dict.fromkeys(keys, [])` aliasing (2D); mutable class attribute |
| `[[0]*3]*3` aliasing (S1) | list matrix trap (2A) |
| `+=` mutate-vs-rebind (S1) | list `+=` vs `+` (2A); tuple `+=` always rebinds (2B); string `+=` O(n²) (S3) |
| `x in list` is O(n) (2A) | convert to set O(1) (2C); dict key membership O(1) (2D) |
| Tuple hashability (2B) | set elements must be hashable (2C); dict keys must be hashable (2D) |
| SettingWithCopyWarning (S1 ML) | NumPy views share memory (2A ML) |
| OpsRAG dedup thread | S1 → 2C (seen-set) → 2D (Counter/defaultdict) |

---

## 4. The Lesson Template — 9 mandatory sections, fixed order

Every lesson hits all nine, in this order, every time. No skipping, no merging.

1. **THEORY** — concept first; Power BI / SQL analogy as the anchor.
2. **EXAMPLE** — runnable code, step by step.
3. **EDGE CASES** — 5–8 cases; code + output + why it matters. **Outputs verified by running.**
4. **GOLDEN RULES** — production patterns to memorize.
5. **COMMON TRAPS** — named bugs that bite beginners *and* seniors.
6. **EXERCISE** — 10–12 problems, easy → hard, **hints only** (worked solutions live in a separate `solutions.ipynb`).
7. **ML REAL-WORLD CONNECTION** — feature engineering, sklearn, pipelines, RAG, etc.
8. **INTERVIEW QUESTIONS** — 8a conceptual Q&A (10–12), 8b code challenges (7–10, Easy/Med/Hard).
9. **SUMMARY TABLE** — concept | why it matters in ML | interview frequency.

**Section → logic:** understand → verify → break at the corners → codify → warn → practice →
transfer → assess → compress.

### Delivery cadence
- Long lessons are split into **Parts**: Part 1 (Theory/Example/Edge), Part 2 (Rules/Traps/Exercise),
  Part 3 (ML/Interview/Summary). Deliver **one part at a time; wait for "go"** before the next.
- Theory within a part is further split into **Chunks (A / B / C)** when dense.
- Close each session with the summary table **plus a preview of the next lesson**.

---

## 5. The Three-Artifact Learning Model

Each concept lives in up to three kinds of notebook:

| Artifact | Role | Character |
|---|---|---|
| `theory.ipynb` | The **delivered lesson** | Heavily styled HTML-in-markdown; the teaching artifact |
| `01_*.ipynb`, `02_*.ipynb` | The learner's **hands-on re-derivation** | Real runnable code; retype, run, err, self-correct — the attempt space |
| `solutions.ipynb` | The **answer key** | Runnable, verified solutions for the Exercises + Code Challenges; each cell prints its result |

> The `solutions.ipynb` is deliberately separate from `theory.ipynb`: theory gives **hints only** so the
> learner attempts in `01_*`, and checks against `solutions` afterward. Keeping them apart preserves the
> "mistakes are the point" loop.

The practice notebooks are where genuine learning shows: wrong first attempts that get corrected
(e.g. `running_max` throwing before the accumulator version lands), exploration beyond the prompt
(the `SneakyKey` hash-breaking experiment), multiple solutions to one problem (`safe_update` via
`.copy()` → `{**d}` → `d | {}`), and ties to the learner's real work.

**Implication for teaching:** correct honestly and specifically; treat mistakes in the practice
notebooks as the point, not noise.

---

## 6. Repository Layout

```
Python Core Foundations/
├── 00_course_outline.ipynb              # syllabus + locked-in teaching format
├── ARCHITECTURE.md                      # this file
├── Mutability & the Object Model/
│   ├── theory.ipynb                     # delivered lesson (Session 1)
│   └── 01_mutability_and_object_model.ipynb   # hands-on practice
├── Sequences/                          # Session 2 (sub-split: 2A–2D)
│   ├── practice.ipynb
│   ├── leetcode-solutions.ipynb
│   ├── List/            theory.ipynb · 01_list.ipynb · 02_list.ipynb
│   ├── tuple/           theory.ipynb · 01_tuple.ipynb
│   ├── Set & frozenset/ theory.ipynb · 01_set.ipynb
│   └── Dictionaries/    theory.ipynb · 01_dict.ipynb · _build_01_dict.py
├── Strings/                            # Session 3
│   └── theory.ipynb · 01_string.ipynb · solutions.ipynb · _build_{theory,practice,solutions}.py
├── Comprehensions & Generators/        # Session 4
│   └── theory.ipynb · 01_comprehensions.ipynb · solutions.ipynb · _build_{theory,practice,solutions}.py
├── Functions, Scope & Closures/        # Session 5
│   └── theory.ipynb · 01_functions.ipynb · solutions.ipynb · _build_{theory,practice,solutions}.py
├── Decorators/                         # Session 6
│   └── theory.ipynb · 01_decorators.ipynb · solutions.ipynb · _build_{theory,practice,solutions}.py
└── OOP/                                 # Session 7 (sub-split: 7A–7E)
    ├── 00_four_pillars.ipynb        overview: the 4 pillars defined + demoed in one page · _build_pillars.py
    ├── Classes & Instances/     (7A) theory.ipynb · 01_classes.ipynb · solutions.ipynb · _build_*.py
    ├── Dunder Methods/          (7B) theory.ipynb · 01_dunders.ipynb · solutions.ipynb · _build_*.py
    ├── Inheritance & MRO/       (7C) theory.ipynb · 01_inheritance.ipynb · solutions.ipynb · _build_*.py
    ├── Properties & Methods/    (7D) theory.ipynb · 01_properties.ipynb · solutions.ipynb · _build_*.py
    └── GIL & Concurrency/       (7E) theory.ipynb · 01_concurrency.ipynb · solutions.ipynb · _build_*.py
```

From Session 3 on, each session folder follows the same three-artifact + three-builder shape
(`theory` / `01_*` practice / `solutions`, each generated by its `_build_*.py`). This folder is its
**own git repository** (has its own `.git`).

---

## 7. The Markdown UI Design System

Theory is **not** plain markdown. Each theory cell is a **markdown cell containing raw HTML + an
inline `<style>` block**, rendered by Jupyter / VS Code.

### 7.1 Palette — Catppuccin Mocha (color is semantic)

| Role | Hex | Usage |
|---|---|---|
| base / mantle / crust | `#1e1e2e` / `#181825` / `#11111b` | panel bg / code bg / output bg (darkest) |
| surface0 / surface1 | `#313244` / `#45475a` | borders, inline-code bg |
| text / subtext / overlay | `#cdd6f4` / `#a6adc8` / `#6c7086` | body / secondary / muted + comments |
| **mauve** | `#cba6f7` | Theory, titles, "Why it matters" |
| **blue** | `#89b4fa` | info, key terms, Summary header |
| **sky** | `#89dceb` | `h3.sub` sub-headings |
| **green** | `#a6e3a1` | Examples, "verified / good", code text |
| **yellow** | `#f9e2af` | Edge Cases, warnings, string literals |
| **red / maroon** | `#f38ba8` | Traps, danger, errors |
| **peach** | `#fab387` | numeric literals |

Color carries **meaning**: green border = safe / verified / good, red = trap / danger, blue = info,
mauve = theory / why. Fonts: `'Segoe UI'` for prose/UI, `'Courier New'` for code.

### 7.2 Section → accent-header mapping

Each of the 9 sections has a signature header so you know where you are at a glance:

| Section | Header class | Accent |
|---|---|---|
| Theory / Golden Rules | `.part-header` | mauve `#cba6f7` |
| Examples / ML | `.ex-header` / `.ml-header` | green `#a6e3a1` |
| Edge Cases | `.warn-header` | yellow `#f9e2af` |
| Common Traps | `.trap-header` | red `#f38ba8` |
| Interview | `.interview-header` | mauve |
| Summary | `.summary-header` | blue `#89b4fa` |

Headers use a gradient bar: `background:linear-gradient(90deg,#313244,#1e1e2e); border-left:5px solid <accent>`.

### 7.3 Component library (reusable pieces)

- **Callout boxes** (left-border tinted panels): `.theory-box` (blue), `.info-box` (blue 💡 — the
  SQL/PBI anchor), `.note-box` (green), `.warn-box` (yellow), `.danger-box` (red),
  `.why-box` ("Why it matters", mauve), `.step-box` ("Step by step", blue), `.nuance-box` (cyan),
  `.verified-box` ("✅ Verified", green).
- **Code + output**: `.code-block` (`#181825`, syntax spans) and `.output-block` (`#11111b`).
- **Syntax spans**: `.cc` comment `#6c7086` · `.cs` string `#f9e2af` · `.ck` keyword `#cba6f7` ·
  `.cm` function/method `#f38ba8` · `.cn` number `#fab387`.
- **Badged blocks**: `.ex-block`+`.ex-badge`, `.edge-block`+`.edge-badge`, `.rule-block`+`.rule-badge`,
  `.trap-block`+`.trap-badge`, `.qa-block` with a circular `.q-num` + difficulty pills
  (`.badge-basic/medium/trap/deep`). Pills are `border-radius:20px`, tinted bg + matching border.
- **Fake two-column grids** (deliberately `inline-block`, *not* flexbox, for Jupyter reliability):
  `.mut-grid`/`.mut-card` (`.mc-imm` blue vs `.mc-mut` green), `.hash-card` (`.hc-good`/`.hc-bad`),
  `.compare-grid`.
- **`.vocab-box`/`.vocab-row`/`.vocab-term`** — definition-list styling.
- **`table.summary`** — `#313244` mauve header, `#1e1e2e` cells, hover `#252540`, first column cyan
  monospace, last column frequency with `.freq-vh` (red) / `.freq-h` (yellow) / `.freq-m` (blue) /
  `.freq-ds` (green).
- **`.divider`** — `border-top:1px solid #313244`.
- Emoji as section markers: 🐍 title · 🔹 sub-points · 💡 info · ⚠ warning · ❌/✅ bad/good ·
  🔑 takeaways · 📎 session tag · 📊 summary · 🔒/🔓 immutable/mutable · 🧊/❄️ frozenset.

### 7.4 Two style generations

- **Classic Catppuccin dark** (most cells): flat dark panels with left-border accents.
- **Liquid glass / glassmorphism** (some Set cells): translucent `rgba()` backgrounds, blurred
  `filter:blur()` "orbs", glossy `box-shadow: inset 0 1px 0 rgba(255,255,255,…)` top edges,
  `border-radius:20–28px`, classes `.glass-card`/`.orb`/`.glass-pill`/`.glossy-btn`/`.frosted-banner`,
  Tabler icons (`<i class="ti ti-…">`), CSS variables (`var(--text-primary)`), and an interactive
  `onclick="sendPrompt(...)"` button. A fancier layer over the same palette.

### 7.5 Robustness patterns (why it survives different renderers)

- **Per-cell self-contained `<style>`**: every theory cell *re-declares* the classes it uses, because
  notebook cells don't reliably share a global `<style>` and renderers sanitize CSS. Duplication is
  intentional.
- **Defensive reset** at cell top:
  ```css
  * { box-sizing:border-box; word-wrap:break-word; overflow-wrap:break-word; }
  body, .jp-RenderedHTMLCommon { padding:0 !important; margin:0 !important; overflow-x:hidden !important; }
  /* + force max-width:100%; overflow-x:auto on component classes */
  ```
  This keeps wide styled content inside the cell and consistent across VS Code / Jupyter / nbviewer.

---

## 8. The Build Pipeline

Theory notebooks are **generated programmatically**, not hand-authored cell by cell.
`Dictionaries/_build_01_dict.py` is the reference pattern:

```python
import nbformat as nbf
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell

cells = []
def md(t):   cells.append(new_markdown_cell(t.strip("\n")))
def code(t): cells.append(new_code_cell(t.strip("\n")))

CARD = ('<div style="background:#1e1e2e; padding:16px 20px; border-radius:8px; '
        'font-family:monospace; color:#cdd6f4; line-height:1.8">\n{body}\n</div>')
def card(body): md(CARD.format(body=body))

# ... md()/code()/card() calls build the lesson ...

nb = new_notebook(cells=cells)
nb.metadata["kernelspec"]     = {"display_name": "Python 3", "language": "python", "name": "python3"}
nb.metadata["language_info"]  = {"name": "python"}
nbf.write(nb, "01_dict.ipynb")
```

Templating (the `card()` helper + `CARD` constant) is what keeps styling reproducible and consistent
rather than re-typed each time.

---

## 9. Teaching & Interaction Rules (locked in)

From `00_course_outline.ipynb` — non-negotiable:

- All 9 sections, in order, every lesson.
- Concept first, mechanics second; Power BI / SQL analogies as anchors.
- Code-heavy — every concept gets a runnable example.
- **Push back honestly; verify outputs by actually running code when challenged** — never assert an
  output you haven't produced.
- No project branding in code, files, or examples.
- Direct tone — no excessive apologies or hedging.
- Ask before assuming — use the questions tool when there's a real choice.
- Long lessons in parts; deliver Part 1, wait for go.
- Close with summary table + preview of the next lesson.

**Command triggers:**
- `"Quiz me with 20 code interview questions"` → standalone quiz session.
- `"Review my notebook and give feedback"` → structured feedback on an uploaded notebook.

---

## 10. How to Add a New Lesson (runbook)

1. **Place it in the dependency chain** — confirm what it builds on and what through-line callbacks
   it should thread (Section 3).
2. **Author `theory.ipynb`** using the 9-section template (Section 4) and the UI system (Section 7);
   generate via an `_build_*.py` in the nbformat pattern (Section 8) for consistency.
3. **Verify every output** by running the code; label outputs as verified.
4. **Add the SQL/Power BI anchor** in Theory and the ML payoff in Section 7 of the lesson.
5. **Create `01_*.ipynb`** (attempt scaffold: 10–12 exercises + code challenges as problem comments +
   empty cells) and **`solutions.ipynb`** (runnable, verified answer key — execute it end-to-end to confirm).
6. **Close** with the summary table (concept | ML value | interview frequency) + next-lesson preview.
7. **Match the visual identity exactly** — Catppuccin Mocha tokens, semantic color coding,
   per-cell self-contained styles, the defensive reset.
8. **Split into sub-sessions ONLY** when the topic contains genuinely distinct models each deserving a
   full 9-section lesson (e.g. list/tuple/set/dict). Same syntax on different targets (e.g. list/dict/set
   comprehensions) is a *chunk*, not a sub-session.
9. **Don't spoil the exercises.** An Exercise (hints-only) must not be a verbatim copy of a worked Theory
   example, and Code Challenges must be distinct from both the Theory examples and the Exercises. If a
   pattern is fully shown in Theory, make the exercise a *variation* that forces adapting it (e.g.
   `repeat`→`collect`, `retry`→`default_on_error`). Established fixing this in Sessions 4 (C4 swap) and 6
   (four exercises de-spoiled).

---

## 11. Current Status

- ✅ **Session 1** — Mutability & the Object Model (theory + practice complete).
- ✅ **Session 2** — Sequences: 2A List, 2B Tuple, 2C Set, 2D Dict (all theory + practice complete).
- ✅ **Session 3** — Strings: full 9-section lesson (Parts 1–3), 12 exercises, 8 code challenges,
  `theory.ipynb` + `01_string.ipynb` + `solutions.ipynb`. First session to use the three-artifact model.
- ✅ **Session 4** — Comprehensions & generators: single chunked session (Part 1 Chunks A–D deep),
  12 exercises, 8 code challenges, `theory.ipynb` + `01_comprehensions.ipynb` + `solutions.ipynb`.
- ✅ **Session 5** — Functions, scope & closures: deep 4-chunk session (argument model, `*args`/`**kwargs`,
  LEGB/global/nonlocal, closures + late binding + `__main__`), 8 traps, 12 exercises (hardened),
  8 code challenges, `theory.ipynb` + `01_functions.ipynb` + `solutions.ipynb`.
- ✅ **Session 6** — Decorators: deep 4-chunk session (mechanism, `functools.wraps`, decorators with
  arguments, stacking/class-based/stdlib), 6 traps, 12 exercises (de-spoiled variations), 8 code challenges,
  `theory.ipynb` + `01_decorators.ipynb` + `solutions.ipynb`.
- ✅ **Session 7** — OOP & dunder methods (**complete**): sub-split into `OOP/` → 7A–7E, each a deep
  4-chunk 9-section lesson. The four pillars map across it (encapsulation→7A/7D, inheritance→7C,
  polymorphism→7B/7C, abstraction→7C), with duck typing / `typing.Protocol` added explicitly in 7C.
  Deferred by design: `@dataclass`+typing → S10, context managers → S8.
  - ✅ **7A** Classes & Instances (theory + `01_classes` + solutions).
  - ✅ **7B** Dunder Methods (theory + `01_dunders` + solutions).
  - ✅ **7C** Inheritance & MRO (theory + `01_inheritance` + solutions) — four pillars framed, duck typing + `Protocol` + ABC + composition.
  - ✅ **7D** Properties & Methods (theory + `01_properties` + solutions) — `@property`/setters, `@classmethod`/`@staticmethod`, name mangling, `__slots__`, `cached_property`.
  - ✅ **7E** GIL & Concurrency (theory + `01_concurrency` + solutions) — GIL, threads for I/O, multiprocessing for CPU, asyncio; multiprocessing solutions run as scripts (`__main__` guard).
- ✅ **Session 8** — Iterators & context managers: deep 4-chunk (iterator protocol, building iterators +
  generators, context managers, `contextlib`), 12 exercises, 8 code challenges, `theory.ipynb` +
  `01_iterators.ipynb` + `solutions.ipynb`. Folder: `Iterators & Context Managers/`.
- ✅ **Session 9** — Error handling: deep 4-chunk (exceptions & hierarchy, try/except/else/finally +
  re-raising, custom exceptions & chaining, EAFP vs LBYL), 12 exercises, 8 code challenges,
  `theory.ipynb` + `01_errors.ipynb` + `solutions.ipynb`. Folder: `Error Handling/`.
- ✅ **Session 10** (finale) — Typing & dataclasses: deep 4-chunk (A: hint basics — annotations,
  container generics, not-runtime-enforced; B: the typing toolkit — `Optional`/`Union`/`Any`/`Callable`/
  `TypeVar`/`Literal`/aliases; C: `@dataclass` — auto `__init__`/`__repr__`/`__eq__`, `default_factory`,
  `frozen`, `order`; D: advanced — `TypedDict`/`Protocol`/`NamedTuple`, dataclass helpers, the **Pydantic
  bridge** [shown read-only — `pydantic` not installed here], + §2 Examples & §3 Edge Cases consolidated),
  12 exercises, 8 code challenges, `theory.ipynb` + `01_typing.ipynb` + `solutions.ipynb` (executes clean).
  Folder: `Typing & Dataclasses/`. **This completes the 10-session Core Python Foundations track.**

🎓 **Course complete** — all 10 sessions authored, code-verified, and following the 9-section format.

Open scaffolds: `Sequences/practice.ipynb` (nearly empty) and `Sequences/leetcode-solutions.ipynb`
(only a couple of problems) — available for more practice.
