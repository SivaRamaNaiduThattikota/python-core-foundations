# Builder for Session 3 - Strings, solutions.ipynb (answer key).
# Runnable, verified solutions for all 12 Exercises and 8 Code Challenges.
import nbformat as nbf
from nbformat.v4 import new_notebook, new_code_cell, new_markdown_cell

cells = []
def md(t):   cells.append(new_markdown_cell(t))
def code(t): cells.append(new_code_cell(t))

md('<div style="background:#1e1e2e; padding:16px 20px; border-radius:8px; font-family:monospace; '
   'color:#cdd6f4; line-height:1.8">'
   '<p style="margin:0 0 8px 0; color:#cba6f7; font-weight:bold; font-size:1.05em;">✅ Session 3 — Strings · Solutions</p>'
   '<p style="margin:0;">Worked, runnable solutions for the 12 <strong>Exercises</strong> and 8 '
   '<strong>Code Challenges</strong>. Every cell is self-contained and prints its result — run top to '
   'bottom to verify. Try them yourself in <code>01_string.ipynb</code> first.</p></div>')

md("### Exercises — Solutions")

code('# E1 (Easy) — Reverse word order\n'
     'def reverse_words(s):\n'
     '    return " ".join(s.split()[::-1])\n\n'
     'print(reverse_words("the cat sat"))   # sat cat the')

code('# E2 (Easy) — Count vowels (case-insensitive)\n'
     'def count_vowels(s):\n'
     '    return sum(1 for c in s.lower() if c in "aeiou")\n\n'
     'print(count_vowels("Education"))       # 5')

code('# E3 (Easy) — Title-case a name (avoids str.title() apostrophe quirks)\n'
     'def title_name(s):\n'
     '    return " ".join(w.capitalize() for w in s.split())\n\n'
     'print(title_name("siva rama naidu"))   # Siva Rama Naidu')

code('# E4 (Easy) — File extension\n'
     'def extension(name):\n'
     '    return name.rsplit(".", 1)[-1]      # split from the right, last piece\n\n'
     'print(extension("report.final.csv"))   # csv')

code('# E5 (Medium) — Clean CSV fields\n'
     'def clean_fields(s):\n'
     '    return [x.strip() for x in s.split(",")]\n\n'
     'print(clean_fields("a, b ,c , d"))      # [\'a\', \'b\', \'c\', \'d\']')

code('# E6 (Medium) — Valid palindrome (alnum, case-insensitive)\n'
     'def is_palindrome(s):\n'
     '    t = [c.lower() for c in s if c.isalnum()]\n'
     '    return t == t[::-1]\n\n'
     'print(is_palindrome("A man, a plan, a canal: Panama"))  # True\n'
     'print(is_palindrome("race a car"))                      # False')

code('# E7 (Medium) — Most frequent character (ties -> first-seen)\n'
     'from collections import Counter\n'
     'def most_frequent(s):\n'
     '    return Counter(s).most_common(1)[0][0]\n\n'
     'print(most_frequent("mississippi"))    # i')

code('# E8 (Medium) — Aligned report row\n'
     'def report_row(name, score):\n'
     '    return f"{name:<10}{score:>6.1%}"\n\n'
     'print(report_row("precision", 0.8734)) # precision  87.3%')

code('# E9 (Medium) — Caesar cipher (wrap, keep case, leave non-letters)\n'
     'def caesar(s, k):\n'
     '    out = []\n'
     '    for ch in s:\n'
     '        if ch.isalpha():\n'
     '            base = ord("A") if ch.isupper() else ord("a")\n'
     '            out.append(chr((ord(ch) - base + k) % 26 + base))\n'
     '        else:\n'
     '            out.append(ch)\n'
     '    return "".join(out)\n\n'
     'print(caesar("xyz", 3), caesar("Hello, World!", 3))  # abc  Khoor, Zruog!')

code('# E10 (Hard) — Run-length encode\n'
     'def rle(s):\n'
     '    if not s:\n'
     '        return ""\n'
     '    out, prev, n = [], s[0], 1\n'
     '    for ch in s[1:]:\n'
     '        if ch == prev:\n'
     '            n += 1\n'
     '        else:\n'
     '            out.append(prev + str(n)); prev, n = ch, 1\n'
     '    out.append(prev + str(n))            # flush the final run\n'
     '    return "".join(out)\n\n'
     'print(rle("aaabbc"))                     # a3b2c1')

code('# E11 (Hard) — Longest repeated-character run\n'
     'def longest_run(s):\n'
     '    if not s:\n'
     '        return ("", 0)\n'
     '    best_ch, best_n = s[0], 1\n'
     '    ch, n = s[0], 1\n'
     '    for c in s[1:]:\n'
     '        n = n + 1 if c == ch else 1\n'
     '        if c != ch:\n'
     '            ch = c\n'
     '        if n > best_n:\n'
     '            best_ch, best_n = ch, n\n'
     '    return (best_ch, best_n)\n\n'
     'print(longest_run("aaabbbbcc"))          # (\'b\', 4)')

code('# E12 (Hard) — Reverse only the vowels (two pointers)\n'
     'def reverse_vowels(s):\n'
     '    vowels = set("aeiouAEIOU")\n'
     '    chars = list(s)\n'
     '    i, j = 0, len(chars) - 1\n'
     '    while i < j:\n'
     '        if chars[i] not in vowels:\n'
     '            i += 1\n'
     '        elif chars[j] not in vowels:\n'
     '            j -= 1\n'
     '        else:\n'
     '            chars[i], chars[j] = chars[j], chars[i]\n'
     '            i += 1; j -= 1\n'
     '    return "".join(chars)\n\n'
     'print(reverse_vowels("leetcode"))        # leotcede')

md("### Code Challenges — Solutions")

code('# C1 (Easy) — Reverse a string\n'
     'def reverse(s):\n'
     '    return s[::-1]\n\n'
     'print(reverse("hello"))                  # olleh')

code('# C2 (Easy) — Anagram check\n'
     'def is_anagram(a, b):\n'
     '    return sorted(a) == sorted(b)        # or Counter(a) == Counter(b) for O(n)\n\n'
     'print(is_anagram("listen", "silent"))    # True')

code('# C3 (Medium) — First non-repeating character (2D seam: counts + order)\n'
     'from collections import Counter\n'
     'def first_unique(s):\n'
     '    c = Counter(s)\n'
     '    for ch in s:\n'
     '        if c[ch] == 1:\n'
     '            return ch\n'
     '    return None\n\n'
     'print(first_unique("leetcode"), first_unique("aabb"))   # l None')

code('# C4 (Medium) — Word frequency\n'
     'from collections import Counter\n'
     'def word_freq(text):\n'
     '    return Counter(text.split())\n\n'
     'print(word_freq("the cat the dog the"))  # Counter({\'the\': 3, \'cat\': 1, \'dog\': 1})')

code('# C5 (Medium) — Valid palindrome\n'
     'def is_palindrome(s):\n'
     '    t = [c.lower() for c in s if c.isalnum()]\n'
     '    return t == t[::-1]\n\n'
     'print(is_palindrome("A man, a plan, a canal: Panama"))  # True')

code('# C6 (Medium) — Run-length encode\n'
     'def rle(s):\n'
     '    if not s:\n'
     '        return ""\n'
     '    out, prev, n = [], s[0], 1\n'
     '    for ch in s[1:]:\n'
     '        if ch == prev:\n'
     '            n += 1\n'
     '        else:\n'
     '            out.append(prev + str(n)); prev, n = ch, 1\n'
     '    out.append(prev + str(n))\n'
     '    return "".join(out)\n\n'
     'print(rle("aaabbc"))                     # a3b2c1')

code('# C7 (Hard) — Longest substring without repeating characters (sliding window + dict)\n'
     'def length_of_longest(s):\n'
     '    seen, start, best = {}, 0, 0\n'
     '    for i, ch in enumerate(s):\n'
     '        if ch in seen and seen[ch] >= start:\n'
     '            start = seen[ch] + 1         # jump past the repeat\n'
     '        seen[ch] = i\n'
     '        best = max(best, i - start + 1)\n'
     '    return best\n\n'
     'print(length_of_longest("abcabcbb"), length_of_longest("bbbbb"), length_of_longest("pwwkew"))  # 3 1 3')

code('# C8 (Hard) — Group anagrams (sorted signature -> dict key)\n'
     'from collections import defaultdict\n'
     'def group_anagrams(words):\n'
     '    g = defaultdict(list)\n'
     '    for w in words:\n'
     '        g["".join(sorted(w))].append(w)\n'
     '    return list(g.values())\n\n'
     'print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))')

nb = new_notebook(cells=cells)
nb.metadata["kernelspec"] = {"display_name": "Python 3", "language": "python", "name": "python3"}
nb.metadata["language_info"] = {"name": "python"}
nbf.write(nb, "solutions.ipynb")
print("wrote solutions.ipynb with", len(cells), "cells")
