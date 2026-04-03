"""Structured content used by the web UI."""

from __future__ import annotations

THEORY_TABS = [
    {
        "id": "history",
        "label": "History",
        "intro": "Twin primes are pairs of primes that differ by 2, such as (3, 5) and (11, 13). The twin prime problem asks whether infinitely many such pairs exist.",
        "sections": [
            {
                "title": "Classical Interest",
                "body": "Prime numbers have been studied since antiquity because they are the basic building blocks of whole numbers. Questions about how often special prime patterns appear, including twin primes, sit naturally inside that tradition.",
            },
            {
                "title": "Conjectural Framework",
                "body": "In the twentieth century, Hardy and Littlewood proposed a broad heuristic framework for predicting how often prime constellations should occur. Their ideas strongly suggest that twin primes should continue forever, although the argument is not a proof.",
            },
            {
                "title": "Modern Milestones",
                "body": "A major modern breakthrough came from work on bounded gaps between primes. Yitang Zhang, James Maynard, and Terence Tao are central figures in this progress, showing that infinitely many primes occur unusually close together even though gap 2 remains unproved.",
            },
        ],
    },
    {
        "id": "approaches",
        "label": "Approaches",
        "intro": "Mathematicians study twin primes through several overlapping methods. Each captures part of the phenomenon, but none currently closes the final gap to a proof.",
        "cards": [
            {
                "title": "Sieve Methods",
                "summary": "Sieve methods filter integers by divisibility conditions to isolate likely prime candidates.",
                "trying": "They try to count or bound how many numbers survive many local divisibility tests at once.",
                "helps": "They are powerful for showing that primes or almost-primes occur with controlled spacing.",
                "falls_short": "They struggle with the parity problem, a barrier that blocks sieve arguments from perfectly distinguishing primes from nearby composite lookalikes.",
            },
            {
                "title": "Analytic Number Theory",
                "summary": "Analytic number theory turns prime questions into questions about functions, sums, and complex-variable behavior.",
                "trying": "It tries to measure global patterns in the distribution of primes by studying generating functions and asymptotic formulas.",
                "helps": "It connects prime questions to deep tools that reveal average behavior over huge ranges.",
                "falls_short": "Average information is often not sharp enough to force a specific gap of exactly 2 infinitely often.",
            },
            {
                "title": "Primes in Arithmetic Progressions",
                "summary": "This approach studies how primes distribute across residue classes such as numbers congruent to 1 or 5 modulo 6.",
                "trying": "It tries to understand whether primes stay evenly spread among allowed modular patterns.",
                "helps": "Twin-prime candidates live inside strict modular constraints, so progress here feeds directly into small-gap questions.",
                "falls_short": "Even strong distribution theorems do not yet provide enough control to isolate infinitely many prime pairs separated by exactly 2.",
            },
            {
                "title": "Heuristic and Probabilistic Models",
                "summary": "Heuristics model primes as if they behave partly like random events, corrected by arithmetic structure.",
                "trying": "They try to predict counts, densities, and local patterns that a true theorem might later explain.",
                "helps": "These models give concrete expectations, such as why twin primes should remain common enough to appear infinitely often.",
                "falls_short": "Heuristics can be persuasive and accurate, but they do not replace rigorous proof.",
            },
            {
                "title": "Computational Experimentation",
                "summary": "Computation searches large ranges, catalogs examples, and tests conjectural patterns.",
                "trying": "It tries to reveal structure, eliminate bad guesses, and guide what formulas or questions deserve attention.",
                "helps": "Experiments often expose residue patterns, gap frequencies, and factorization signals that would be hard to spot by inspection alone.",
                "falls_short": "Checking even enormous ranges can only verify finite evidence; it can never prove infinitude by itself.",
            },
        ],
    },
    {
        "id": "progress",
        "label": "Current Progress",
        "intro": "The strongest modern progress does not prove twin primes directly, but it shows that primes come close together infinitely often in a rigorous sense.",
        "sections": [
            {
                "title": "Bounded Gaps Breakthrough",
                "body": "Mathematicians proved that there exists some fixed bound B such that infinitely many pairs of distinct primes differ by at most B. This was a major shift because it replaced vague hope with a concrete theorem about infinitely many small prime gaps.",
            },
            {
                "title": "Why This Matters",
                "body": "Bounded gaps show that prime clustering is not a rare accident. The methods built by Zhang, Maynard, Tao, and collaborators established that primes can be forced into recurring near-collisions across infinitely many scales.",
            },
            {
                "title": "What Remains Open",
                "body": "This progress still does not prove gap = 2. A theorem about bounded gaps says some small gap appears infinitely often; the twin prime conjecture specifically requires that the gap 2 itself appears infinitely often.",
            },
            {
                "title": "Progress vs Proof",
                "body": "Progress toward twin primes means proving structural statements that move prime gaps closer to 2 or clarify the mechanisms behind them. A proof of the twin prime conjecture would require a final argument that the exact gap 2 occurs infinitely many times.",
            },
        ],
    },
    {
        "id": "why-its-hard",
        "label": "Why It's Hard",
        "intro": "Twin primes sit at the meeting point of randomness and structure, which is exactly what makes the problem so durable.",
        "sections": [
            {
                "title": "Random-Looking but Structured",
                "body": "Primes often look erratic when listed out, yet they obey strict arithmetic rules. Any serious argument has to respect both the apparent randomness and the hidden modular structure at the same time.",
            },
            {
                "title": "Local Divisibility Constraints",
                "body": "A twin-prime pair must dodge divisibility by every small prime in two nearby positions simultaneously. Those local constraints interact in subtle ways, and managing all of them at once is much harder than checking a single candidate pair.",
            },
            {
                "title": "Examples Are Not Enough",
                "body": "It is easy to verify many twin primes computationally, and there are vast numbers of known examples. But proving infinitude means controlling behavior beyond every finite range, not just collecting more evidence inside larger searches.",
            },
            {
                "title": "Computation Has Limits",
                "body": "Computation is invaluable for testing ideas, measuring distributions, and supporting conjectures. It cannot prove an infinite statement simply by extending the search farther, because any computation still stops at a finite boundary.",
            },
        ],
    },
]
