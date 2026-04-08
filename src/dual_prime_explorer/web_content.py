"""Structured content used by the web UI."""

from __future__ import annotations

THEORY_TABS = [
    {
        "id": "history",
        "label": "History",
        "intro": "The history of twin primes begins with the study of prime numbers in ancient mathematics and leads to the twin prime conjecture, one of the most famous unsolved problems in number theory. The central question asks whether there are infinitely many pairs of prime numbers that differ by exactly 2.",
        "nav_hint": "Twin prime conjecture history, timeline, FAQ, and references.",
        "updated": "Last reviewed: April 2026",
        "sections": [
            {
                "title": "History Overview of the Twin Prime Problem",
                "body": "Twin primes are pairs of prime numbers that differ by 2, such as (3, 5) and (11, 13). The twin prime conjecture, also called the twin prime problem, asks whether infinitely many such pairs exist. Despite centuries of study and major modern breakthroughs, this question remains unsolved.",
            },
            {
                "title": "Early Foundations: Euclid and Prime Numbers",
                "body": "Around 300 BCE, Euclid proved that there are infinitely many prime numbers. This result, known as the infinitude of primes, established that primes do not stop and provided the foundation for all later work on prime distribution. Although Euclid's proof does not address twin primes directly, it made meaningful questions about patterns in primes, such as gaps between primes, mathematically possible.",
            },
            {
                "title": "From Prime Patterns to the Twin Prime Conjecture",
                "body": "As number theory developed, mathematicians shifted from studying primes as isolated numbers to studying how primes are distributed. This shift brought prime gaps, the frequency of small gaps, and recurring structures in prime numbers into central focus. Twin primes represent the simplest nontrivial pattern in prime gaps, making them a natural focus of study and leading directly to the twin prime conjecture.",
            },
            {
                "title": "Hardy-Littlewood and the Prime Pair Conjecture",
                "body": "In the early 20th century, G. H. Hardy and J. E. Littlewood proposed the prime pair conjecture, which gives a quantitative prediction for how often twin primes should occur. Their framework introduced the twin prime constant, a correction factor that accounts for how divisibility constraints affect prime distribution. The Hardy-Littlewood conjecture strongly suggests that infinitely many twin primes exist, but the Hardy-Littlewood conjecture is a heuristic framework rather than a proof.",
            },
            {
                "title": "Modern Progress: Zhang, Polymath, and Maynard-Tao",
                "body": "A major breakthrough occurred in 2013 when Yitang Zhang proved that bounded gaps between primes occur infinitely often. Zhang showed there exists a fixed number B such that infinitely many pairs of primes differ by at most B, and his original bound was 70 million. The Polymath Project rapidly reduced the bound through collaborative effort, and James Maynard and Terence Tao developed new methods that independently proved bounded gaps and generalized the approach. These results show that primes appear infinitely often within small distances, but they do not prove that gap 2 occurs infinitely often.",
            },
            {
                "title": "Current Status of the Twin Prime Problem",
                "body": "The modern mathematical picture is clear: Euclid proved that infinitely many primes exist, Zhang-Maynard-Tao style results prove that infinitely many bounded gaps between primes exist, and Hardy-Littlewood heuristics strongly predict infinitely many twin primes. However, the twin prime conjecture remains unproven. Mathematicians have come close, but a proof that infinitely many prime pairs differ by exactly 2 is still unknown.",
            },
        ],
        "timeline": [
            {
                "label": "c. 300 BCE",
                "title": "Euclid proves infinitely many primes",
                "body": "Establishes the foundation for studying prime distribution and gaps.",
            },
            {
                "label": "19th-20th century",
                "title": "Prime distribution becomes central",
                "body": "Focus shifts toward understanding patterns, densities, and gaps between primes.",
            },
            {
                "label": "1923",
                "title": "Hardy-Littlewood prime pair conjecture",
                "body": "Introduces a predictive framework for twin primes and the twin prime constant.",
            },
            {
                "label": "2013",
                "title": "Yitang Zhang proves bounded gaps between primes",
                "body": "First proof that infinitely many prime pairs occur within a fixed finite distance.",
            },
            {
                "label": "2013-2014",
                "title": "Polymath Project reduces bounds",
                "body": "Collaborative work significantly improves Zhang's numerical bound.",
            },
            {
                "label": "2013-2014",
                "title": "Maynard-Tao refinement",
                "body": "New techniques provide independent and more flexible bounded-gap results.",
            },
            {
                "label": "Today",
                "title": "Twin primes remain unproven",
                "body": "The conjecture remains open despite major progress.",
            },
        ],
        "faq": [
            {
                "question": "What are twin primes?",
                "answer": "Twin primes are pairs of prime numbers that differ by exactly 2, such as (3, 5), (5, 7), and (11, 13).",
            },
            {
                "question": "Has the twin prime conjecture been solved?",
                "answer": "No. The twin prime conjecture remains unsolved, although modern results show that primes occur infinitely often within small gaps.",
            },
            {
                "question": "What did Yitang Zhang prove?",
                "answer": "In 2013, Yitang Zhang proved that there exists a fixed bound B such that infinitely many pairs of primes differ by at most B. This was the first proof of bounded gaps between primes.",
            },
            {
                "question": "What is the Hardy-Littlewood conjecture?",
                "answer": "The Hardy-Littlewood prime pair conjecture is a heuristic formula that predicts how often twin primes occur, incorporating the twin prime constant.",
            },
            {
                "question": "Why is the twin prime problem difficult?",
                "answer": "The problem requires proving infinitely many exact gap-2 prime pairs, which demands far more precision than proving that some bounded gap occurs infinitely often.",
            },
        ],
        "references": [
            {
                "title": "Euclid - Elements, Book IX, Proposition 20",
                "note": "Classical proof of the infinitude of prime numbers.",
            },
            {
                "title": "Hardy & Littlewood - Prime Pair Conjecture",
                "note": "Heuristic framework predicting the frequency of twin primes.",
            },
            {
                "title": "Yitang Zhang (2013)",
                "note": "First proof that bounded gaps between primes occur infinitely often.",
            },
            {
                "title": "Polymath Project",
                "note": "Collaborative refinement of bounded-gap results.",
            },
            {
                "title": "Maynard & Tao - Small Gaps Between Primes",
                "note": "Modern techniques expanding the theory of prime gaps.",
            },
        ],
        "explore_next": [
            {
                "title": "See twin centers in the Lab",
                "body": "Use the visual field to watch twin primes and twin centers appear together across a live range.",
                "href": "/lab#visualization-title",
                "link_label": "Open the Lab",
                "destination": "Lab",
            },
            {
                "title": "Read: What are twin primes?",
                "body": "Use the standalone page when you want the shortest clear definition before diving back into the interactive views.",
                "href": "/what-are-twin-primes",
                "link_label": "Open the article",
                "destination": "Read",
            },
            {
                "title": "Read: What did Yitang Zhang prove?",
                "body": "Use the standalone page to keep bounded gaps and the twin prime conjecture clearly separated.",
                "href": "/what-did-yitang-zhang-prove",
                "link_label": "Open the article",
                "destination": "Read",
            },
            {
                "title": "Trace prime gaps in Analysis",
                "body": "Move from the history of the problem into the Gaps and Modular views to inspect the structure directly.",
                "href": "/analysis#analysis-views-title",
                "link_label": "Open Analysis",
                "destination": "Analysis",
            },
        ],
    },
    {
        "id": "approaches",
        "label": "Approaches",
        "intro": "Mathematicians study the twin prime conjecture using several complementary approaches. Each method captures part of how primes behave, but no single approach has yet overcome the final barrier needed to prove that infinitely many twin primes exist.",
        "nav_hint": "Sieve methods, analytic number theory, arithmetic progressions, heuristics, and computation.",
        "cards": [
            {
                "title": "Sieve Methods",
                "summary": "Sieve methods filter integers by applying divisibility constraints to isolate numbers that are likely to be prime.",
                "trying": "Sieve methods attempt to count or bound how many integers remain after removing numbers divisible by small primes. The goal is to detect patterns where primes or numbers very close to primes cluster together.",
                "helps": "Sieve techniques are highly effective at showing that primes and almost-primes, numbers with few prime factors, occur with controlled spacing. They are central to modern results on bounded gaps between primes.",
                "falls_short": "Sieve methods are limited by the parity problem, a fundamental barrier that prevents them from reliably distinguishing true primes from composite numbers that closely mimic prime behavior. This limitation blocks sieve-based proofs of twin primes.",
            },
            {
                "title": "Analytic Number Theory",
                "summary": "Analytic number theory studies primes by translating discrete questions into problems involving functions, infinite series, and complex variables.",
                "trying": "This approach analyzes the global distribution of primes through tools such as generating functions, asymptotic formulas, and objects like the Riemann zeta function.",
                "helps": "Analytic methods reveal large-scale patterns in how primes are distributed and provide powerful estimates for how often primes occur within given ranges.",
                "falls_short": "These techniques typically yield average results over large intervals. That level of control is not yet precise enough to guarantee infinitely many prime pairs with an exact gap of 2.",
            },
            {
                "title": "Primes in Arithmetic Progressions",
                "summary": "This approach studies how primes are distributed across modular patterns, such as numbers congruent to 1 or 5 modulo 6.",
                "trying": "It seeks to understand whether primes remain evenly distributed among allowable residue classes and how those distributions interact.",
                "helps": "Twin primes must satisfy strict modular constraints, so understanding primes in arithmetic progressions directly informs the structure of possible twin prime pairs.",
                "falls_short": "Even the strongest known results on prime distribution in arithmetic progressions do not provide enough precision to isolate infinitely many prime pairs separated by exactly 2.",
            },
            {
                "title": "Heuristic and Probabilistic Models",
                "summary": "Heuristic models treat primes as partly random, while incorporating known arithmetic constraints.",
                "trying": "These models aim to predict how often certain prime patterns, such as twin primes, should occur, including estimates for their density.",
                "helps": "Heuristics like the Hardy-Littlewood conjecture give strong quantitative predictions and explain why twin primes are expected to occur infinitely often.",
                "falls_short": "Heuristic arguments are not proofs. Even highly accurate predictions cannot establish the existence of infinitely many twin primes without rigorous justification.",
            },
            {
                "title": "Computational Experimentation",
                "summary": "Computational methods explore primes by searching large numerical ranges and analyzing observed patterns.",
                "trying": "Computation identifies examples, measures gap frequencies, and tests conjectural formulas against real data.",
                "helps": "Large-scale experiments reveal structure in prime gaps, highlight repeating residue patterns, and guide the development of new conjectures and techniques.",
                "falls_short": "No amount of computation can prove infinitude. Even extremely large numerical verification only provides finite evidence and cannot resolve the twin prime conjecture.",
            },
        ],
        "sections": [
            {
                "title": "Synthesis: Why the Twin Prime Problem Persists",
                "body": "Each approach contributes a different kind of insight. Sieve methods control local structure but hit the parity barrier, analytic methods describe global behavior but lack exact local precision, arithmetic progressions constrain where primes can occur, heuristics predict what should happen, and computation shows what does happen in large finite ranges. The twin prime conjecture sits at the intersection of all these methods, requiring both global understanding and exact local control. That combination is what makes the twin prime problem so resistant to a final proof.",
            },
        ],
        "explore_next": [
            {
                "title": "Try Mod 6 in the Lab",
                "body": "Use the Mod 6 view to see why primes greater than 3 fall into narrow residue classes and why twin centers matter.",
                "href": "/lab#visualization-title",
                "link_label": "Open the Lab",
                "destination": "Lab",
            },
            {
                "title": "Read: Why Mod 6 shows up so often",
                "body": "Use the standalone page when the modular pattern is the main idea you want in plain language.",
                "href": "/why-mod-6-shows-up-so-often",
                "link_label": "Open the article",
                "destination": "Read",
            },
            {
                "title": "Read: Why twin centers matter",
                "body": "Use the standalone page when you want the shortest explanation of why the site highlights centers so strongly.",
                "href": "/why-twin-centers-matter",
                "link_label": "Open the article",
                "destination": "Read",
            },
            {
                "title": "Inspect divisibility in Explorer",
                "body": "Use row-level divisor and neighborhood views when you want the local arithmetic detail behind the theory.",
                "href": "/explorer#number-table-title",
                "link_label": "Open Explorer",
                "destination": "Explorer",
            },
        ],
    },
    {
        "id": "progress",
        "label": "Current Progress",
        "intro": "Modern progress on the twin prime conjecture does not yet prove that infinitely many twin primes exist, but it establishes that primes come arbitrarily close together infinitely often in a precise, provable sense.",
        "nav_hint": "Bounded gaps between primes, proof vs progress, and what remains unsolved.",
        "sections": [
            {
                "title": "Bounded Gaps Breakthrough",
                "body": "A major breakthrough in 2013 showed that there exists a fixed number B such that infinitely many pairs of distinct prime numbers differ by at most B. This result, first proved by Yitang Zhang, transformed the study of prime gaps by replacing conjectural expectations with a concrete theorem about infinitely many small gaps between primes. Subsequent work by James Maynard and Terence Tao, along with large-scale collaboration through the Polymath Project, significantly improved both the methods and the numerical bounds.",
            },
            {
                "title": "Why This Matters",
                "body": "Bounded gap results show that prime clustering is not a rare or accidental phenomenon. Instead, they prove that primes repeatedly appear within small distances of each other across infinitely many scales. This establishes a key structural insight: prime numbers are not only infinite, they also exhibit recurring local proximity. This shift from existence to structured behavior is one of the most important advances in modern number theory.",
            },
            {
                "title": "What Remains Open",
                "body": "Despite this progress, the twin prime conjecture itself remains unresolved. Bounded gap theorems guarantee that some fixed finite gap between primes occurs infinitely often. However, the twin prime conjecture requires a much stronger statement: that the specific gap of exactly 2 occurs infinitely often. Current methods do not yet isolate this exact gap.",
            },
            {
                "title": "Progress vs Proof",
                "body": "Progress toward the twin prime conjecture involves proving increasingly precise structural results about prime gaps, including reducing upper bounds on prime gaps, improving distribution results for primes, and developing new methods to control local behavior. A full proof would require a final step: demonstrating that the exact gap of 2 occurs infinitely many times. This distinction is critical: progress shows primes come arbitrarily close together, while proof requires showing they come exactly two apart infinitely often.",
            },
            {
                "title": "Synthesis: Where We Stand",
                "body": "The current state of the twin prime problem can be summarized clearly. Infinitely many primes exist. Infinitely many bounded gaps between primes exist. Strong heuristics predict infinitely many twin primes. But no proof yet guarantees infinitely many gap-2 pairs. The gap between arbitrarily close and exactly 2 remains the final unresolved step.",
            },
        ],
        "explore_next": [
            {
                "title": "Open Analysis for gap structure",
                "body": "Use the Gaps and Expected views to connect bounded-gap theory to a concrete range.",
                "href": "/analysis#analysis-views-title",
                "link_label": "Open Analysis",
                "destination": "Analysis",
            },
            {
                "title": "See local proximity in the Lab",
                "body": "Use the visual field to scan twin-prime clusters and twin centers before you move into the deeper metrics.",
                "href": "/lab#visualization-title",
                "link_label": "Open the Lab",
                "destination": "Lab",
            },
        ],
    },
    {
        "id": "why-its-hard",
        "label": "Why It's Hard",
        "intro": "The twin prime conjecture is difficult because it lies at the intersection of randomness and strict arithmetic structure. Any successful proof must simultaneously control both aspects of how prime numbers behave.",
        "nav_hint": "Randomness, divisibility constraints, global vs local control, and the limits of computation.",
        "sections": [
            {
                "title": "Random-Looking but Structured",
                "body": "Prime numbers often appear irregular and unpredictable when listed, yet they obey rigid arithmetic constraints. Any argument about twin primes must reconcile two competing realities: apparent randomness in how primes are spaced and hidden structure imposed by divisibility and modular arithmetic. This tension makes it difficult to predict when primes will align closely enough to form infinitely many gap-2 pairs.",
            },
            {
                "title": "Local Divisibility Constraints",
                "body": "A twin prime pair (p, p+2) must avoid divisibility by every small prime in both positions at once. If p avoids divisibility by a small prime, p+2 must also avoid it. These constraints stack together across all primes, creating a dense web of conditions that must be satisfied simultaneously. Managing these overlapping restrictions is far more complex than checking whether a single number is prime.",
            },
            {
                "title": "Global vs Local Tension",
                "body": "Modern methods can describe the global distribution of primes very well, but twin primes require precise local control. Analytic techniques show how primes behave on average, sieve methods control large sets of candidates, and bounded gap results show primes come close together. But none of these tools yet provide the exact precision needed to force gap 2 infinitely often. This gap between average behavior and exact alignment is one of the central obstacles.",
            },
            {
                "title": "Examples Are Not Enough",
                "body": "There are many known twin primes, and computation continues to find more at extremely large scales. However, verifying examples is fundamentally different from proving infinitude: computation shows what happens within a finite range, while a proof must control behavior beyond all finite bounds. No amount of observed evidence can guarantee that twin primes continue forever.",
            },
            {
                "title": "Computation Has Limits",
                "body": "Computation plays a crucial role in modern number theory by testing conjectures, measuring prime gap distributions, and guiding new theoretical ideas. But computation cannot resolve the twin prime conjecture on its own. Every computational search ends at a finite limit, while the conjecture concerns behavior across the infinite number line.",
            },
            {
                "title": "Synthesis: The Core Difficulty",
                "body": "The twin prime problem persists because it requires global understanding of how primes are distributed, local precision to isolate exact gap-2 pairs, and control over infinitely many constraints at once. Each existing method solves part of this puzzle, but no approach yet unifies all three requirements into a single proof.",
            },
        ],
        "explore_next": [
            {
                "title": "Inspect divisor structure in Explorer",
                "body": "Use the number table when you want to see prime neighborhoods, divisors, and exact composite structure one row at a time.",
                "href": "/explorer#number-table-title",
                "link_label": "Open Explorer",
                "destination": "Explorer",
            },
            {
                "title": "Compare local structure in Analysis",
                "body": "Use Modular, Gaps, and Density when you want to move from abstract difficulty to measurable structure.",
                "href": "/analysis#analysis-views-title",
                "link_label": "Open Analysis",
                "destination": "Analysis",
            },
        ],
    },
]


EXPLANATORY_PAGES = [
    {
        "route": "/what-are-twin-primes",
        "nav_label": "What Are Twin Primes?",
        "title": "Twin Prime Exploration Lab | What Are Twin Primes?",
        "meta_description": "A clear introduction to twin primes, why gap 2 matters, and how Twin Prime Exploration Lab helps you explore the pattern.",
        "eyebrow": "Twin Primes",
        "hero_title": "What are twin primes?",
        "hero_text": "Twin primes are pairs of prime numbers that differ by exactly 2. They are simple to state, easy to spot in small ranges, and still connected to one of the best-known open questions in number theory.",
        "intro_title": "A short introduction",
        "intro_text": "Start here if you want the core idea in plain language, then move back into the Lab, Explorer, Analysis, or Theory pages when you want to see the pattern from a different angle.",
        "sections": [
            {
                "title": "The basic definition",
                "body": "A twin-prime pair is a pair of prime numbers with a difference of 2, such as (3, 5), (5, 7), or (11, 13). Once numbers get larger, twin primes become less frequent, but they continue to appear in many finite ranges.",
            },
            {
                "title": "Why gap 2 matters",
                "body": "A gap of 2 is the smallest possible gap between odd prime numbers. That makes twin primes the simplest nontrivial prime-gap pattern, and it is one reason they sit so close to the center of prime-number research.",
            },
            {
                "title": "Why people care about them",
                "body": "The twin prime conjecture asks whether infinitely many twin-prime pairs exist. That question is still open. The pattern is easy to understand, but proving it continues forever is much harder than finding many examples.",
            },
            {
                "title": "How this site uses the idea",
                "body": "Twin Prime Exploration Lab treats twin primes as something you can see, inspect, and interpret from several angles. The Lab makes the pattern visible, Explorer shows the exact rows, Analysis summarizes the structure, and Theory explains why mathematicians still care about the problem.",
            },
        ],
        "related_links": [
            {"title": "See the pattern in the Lab", "body": "Start with a live range and watch twin primes and twin centers appear together.", "href": "/lab#visualization-title", "label": "Open the Lab"},
            {"title": "Read the longer history", "body": "Use Theory when you want the conjecture, timeline, and current mathematical status in one place.", "href": "/theory#history", "label": "Open Theory: History"},
            {"title": "Check the key terms", "body": "Use the Glossary when you want quick definitions for twin prime, twin center, and prime gap.", "href": "/glossary#glossary-term-twin-prime", "label": "Open the Glossary"},
        ],
    },
    {
        "route": "/what-did-yitang-zhang-prove",
        "nav_label": "What Did Yitang Zhang Prove?",
        "title": "Twin Prime Exploration Lab | What Did Yitang Zhang Prove?",
        "meta_description": "A concise explanation of Yitang Zhang's bounded-gaps breakthrough, what it proved, and what it did not prove about twin primes.",
        "eyebrow": "Modern Progress",
        "hero_title": "What did Yitang Zhang prove?",
        "hero_text": "In 2013, Yitang Zhang proved that there is some fixed finite bound B such that infinitely many pairs of primes differ by at most B. It was a major breakthrough, but it did not prove the twin prime conjecture.",
        "intro_title": "What this page clarifies",
        "intro_text": "Zhang's breakthrough is often mentioned in one sentence and misunderstood in the next. This page keeps the distinction clear: bounded gaps were proved, but gap 2 was not.",
        "sections": [
            {
                "title": "The theorem in plain language",
                "body": "Zhang proved that prime numbers do not drift apart forever. Instead, there exists at least one fixed distance B so that infinitely many prime pairs appear with a gap no larger than B.",
            },
            {
                "title": "Why this mattered immediately",
                "body": "Before Zhang, no one had proved that primes come close together infinitely often in any bounded way. His result changed the field by turning a long-standing expectation into a theorem.",
            },
            {
                "title": "What it did not prove",
                "body": "Zhang did not prove that the gap is 2 infinitely often. The twin prime conjecture asks for the exact gap of 2, while bounded-gap results only guarantee that some finite gap occurs infinitely many times.",
            },
            {
                "title": "Why the result still belongs in the twin-prime story",
                "body": "The theorem showed that prime clustering is not just a heuristic guess. It established that small prime gaps recur across infinitely many scales, which is one of the strongest pieces of progress connected to the twin prime problem.",
            },
        ],
        "related_links": [
            {"title": "See the broader progress picture", "body": "Theory puts Zhang, Polymath, and Maynard-Tao into the same timeline.", "href": "/theory#progress", "label": "Open Theory: Current Progress"},
            {"title": "Look at gap structure directly", "body": "Analysis helps connect the idea of small gaps to concrete ranges and repeated spacing.", "href": "/analysis#analysis-views-title", "label": "Open Analysis"},
            {"title": "Check the bounded-gaps definition", "body": "The Glossary keeps the distinction between bounded gaps and twin primes short and clear.", "href": "/glossary#glossary-term-bounded-gaps-between-primes", "label": "Open the Glossary"},
        ],
    },
    {
        "route": "/why-mod-6-shows-up-so-often",
        "nav_label": "Why Mod 6 Shows Up So Often",
        "title": "Twin Prime Exploration Lab | Why Mod 6 Shows Up So Often",
        "meta_description": "Why mod 6 appears so often in prime-number discussions, and how residue classes help make twin-prime structure easier to see.",
        "eyebrow": "Mod 6",
        "hero_title": "Why Mod 6 shows up so often",
        "hero_text": "When people study primes greater than 3, mod 6 keeps appearing because divisibility by 2 and 3 removes most residue classes immediately. That leaves a much narrower structure to inspect.",
        "intro_title": "Why this helps",
        "intro_text": "You do not need a long lesson in modular arithmetic to get the basic idea. This page gives the shortest useful explanation, then points you back to the visual and analytical views where the pattern becomes easier to see.",
        "sections": [
            {
                "title": "What mod 6 means",
                "body": "Looking at numbers mod 6 means grouping them by their remainder after division by 6. Every integer falls into one of six residue classes: 0, 1, 2, 3, 4, or 5 mod 6.",
            },
            {
                "title": "Why primes narrow to two classes",
                "body": "Any number congruent to 0, 2, or 4 mod 6 is even, so it cannot be prime unless it is 2. Any number congruent to 3 mod 6 is divisible by 3, so it cannot be prime unless it is 3. For primes greater than 3, that leaves only residue classes 1 and 5 mod 6.",
            },
            {
                "title": "Why this matters for twin primes",
                "body": "A typical twin-prime pair above (3, 5) looks like (6k - 1, 6k + 1). That means mod 6 quickly reveals why the pair members and the center between them keep falling into a narrow pattern.",
            },
            {
                "title": "Why the site highlights it",
                "body": "Mod 6 is one of the fastest ways to move from raw numbers to visible structure. The Lab uses it as a visual mode, Analysis uses it as a structural read, and the Glossary keeps the key terms short when you do not want a longer explanation.",
            },
        ],
        "related_links": [
            {"title": "See it in the Lab", "body": "Use the Mod 6 view to see the residue pattern rather than only reading about it.", "href": "/lab#visualization-title", "label": "Open the Lab"},
            {"title": "Read the modular interpretation", "body": "Analysis summarizes the pair and center residue counts across the selected range, so you can compare the article idea with live data.", "href": "/analysis#analysis-views-title", "label": "Open Analysis"},
            {"title": "Keep the terms nearby", "body": "Use the Glossary for Mod 6, residue class, and arithmetic progression definitions.", "href": "/glossary#glossary-term-mod-6", "label": "Open the Glossary"},
        ],
    },
    {
        "route": "/why-twin-centers-matter",
        "nav_label": "Why Twin Centers Matter",
        "title": "Twin Prime Exploration Lab | Why Twin Centers Matter",
        "meta_description": "Why twin centers are useful for seeing, organizing, and interpreting twin-prime structure across the site.",
        "eyebrow": "Twin Centers",
        "hero_title": "Why twin centers matter",
        "hero_text": "Twin centers are the numbers exactly between twin-prime pairs. They are not prime themselves, but they often make the surrounding pair structure easier to see and talk about.",
        "intro_title": "Why this page exists",
        "intro_text": "Twin centers are one of the site's distinctive ideas. This page explains why they are useful without turning them into a bigger theory than they need to be.",
        "sections": [
            {
                "title": "What a twin center is",
                "body": "If (p, p + 2) is a twin-prime pair, then the number in the middle is p + 1. That middle value is the twin center. For example, 12 is the twin center between 11 and 13.",
            },
            {
                "title": "Why the center is useful",
                "body": "The center compresses a pair into one location. That makes it easier to see where twin-prime structure sits inside a larger range, especially when you want a visual or counting-based summary rather than only a list of pairs.",
            },
            {
                "title": "Why centers connect naturally to mod 6",
                "body": "For twin-prime pairs above the earliest exceptions, the center typically lands on a multiple of 6. That makes centers a clean bridge between the visual pattern and the modular explanation.",
            },
            {
                "title": "How the site uses centers",
                "body": "The Lab highlights centers visually, Explorer treats them as a neighborhood role, and Analysis uses them for factor and modular summaries. They are not a replacement for the primes themselves, but they are often the fastest way to see the structure they create.",
            },
        ],
        "related_links": [
            {"title": "See twin centers visually", "body": "The Lab makes centers easy to spot inside a live number field.", "href": "/lab#visualization-title", "label": "Open the Lab"},
            {"title": "Inspect exact center rows", "body": "Explorer shows the number-by-number detail behind each center and its neighbors.", "href": "/explorer#number-table-title", "label": "Open Explorer"},
            {"title": "Connect centers to reference context", "body": "Use the Glossary for the short definition first, then move into Theory when you want the broader twin-prime context.", "href": "/glossary#glossary-term-twin-center", "label": "Open the Glossary"},
        ],
    },
]



GLOSSARY_SECTIONS = [
    {
        "title": "Core Number Types",
        "intro": "These terms describe the basic kinds of numbers users see throughout the Lab and Explorer.",
        "terms": [
            {
                "term": "Prime",
                "summary": "A prime number is a whole number greater than 1 with exactly two positive divisors: 1 and itself.",
                "detail": "Examples include 2, 3, 5, 7, and 11. Prime numbers are the main building blocks of the Twin Prime Exploration Lab.",
            },
            {
                "term": "Composite",
                "summary": "A composite number is a whole number greater than 1 with more than two positive divisors.",
                "detail": "Examples include 4, 6, 8, 9, and 12. Composite numbers matter because their divisor structure helps explain why primes become rarer.",
            },
            {
                "term": "Unit",
                "summary": "In this project, the number 1 is treated as a unit rather than a prime or a composite number.",
                "detail": "The number 1 has only one positive divisor, so it sits outside the prime-versus-composite split. Keeping 1 separate makes the number classification model clearer.",
            },
            {
                "term": "Divisor",
                "summary": "A divisor of a number is a whole number that divides it evenly with no remainder.",
                "detail": "For example, the divisors of 12 are 1, 2, 3, 4, 6, and 12. Divisor views help users inspect how composite structure differs from prime structure.",
            },
        ],
    },
    {
        "title": "Twin Prime Structure",
        "intro": "These terms describe the main pattern entities the product highlights visually and analytically.",
        "terms": [
            {
                "term": "Twin Prime",
                "summary": "Twin primes are pairs of prime numbers that differ by exactly 2.",
                "detail": "Examples include (3, 5), (5, 7), and (11, 13). Twin primes are the central object of study in the Twin Prime Exploration Lab.",
                "article_link": {
                    "label": "Read more: What Are Twin Primes?",
                    "href": "/what-are-twin-primes",
                },
            },
            {
                "term": "Twin Center",
                "summary": "A twin center is the number exactly between two twin primes.",
                "detail": "For example, 12 is the twin center between 11 and 13. The Lab treats twin centers as a first-class structure because they often make pair behavior easier to see.",
                "theory_link": {
                    "label": "See this in Theory: History",
                    "href": "/theory#history",
                },
                "article_link": {
                    "label": "Read more: Why Twin Centers Matter",
                    "href": "/why-twin-centers-matter",
                },
            },
            {
                "term": "Single Prime",
                "summary": "A single prime is a prime that is not part of a twin-prime pair within the selected range.",
                "detail": "This is a product-facing label used in Explorer. It helps separate primes that participate in twin-prime structure from primes that do not.",
            },
            {
                "term": "Not Prime",
                "summary": "Not Prime is the Explorer label for numbers that are not prime in the current classification view.",
                "detail": "This label includes the unit 1 and composite numbers. It is a product-facing grouping that keeps filtering simple while preserving the deeper number-type detail in the table.",
            },
            {
                "term": "Prime Neighborhood",
                "summary": "Prime neighborhood describes the local role a number plays relative to nearby primes.",
                "detail": "Examples in the product include Prime, Twin Center, Next to one prime, No adjacent primes, and Prime edge case. This field helps users inspect local structure instead of only global classification.",
            },
        ],
    },
    {
        "title": "Patterns and Residues",
        "intro": "These terms help users understand the structural views shown on the Lab and Analysis pages.",
        "terms": [
            {
                "term": "Prime Gap",
                "summary": "A prime gap is the difference between one prime number and the next prime number.",
                "detail": "Twin primes are the special case where the prime gap is exactly 2. Gap analysis helps users see spacing patterns and clustering behavior.",
            },
            {
                "term": "Mod 6",
                "summary": "Mod 6 refers to looking at numbers by their remainder after division by 6.",
                "detail": "Primes greater than 3 must fall into the 1 or 5 residue classes modulo 6. That is why the Mod 6 view is useful for seeing twin-prime structure quickly.",
                "theory_link": {
                    "label": "See this in Theory: Approaches",
                    "href": "/theory#approaches",
                },
                "article_link": {
                    "label": "Read more: Why Mod 6 Shows Up So Often",
                    "href": "/why-mod-6-shows-up-so-often",
                },
            },
            {
                "term": "Residue Class",
                "summary": "A residue class groups numbers that leave the same remainder after division by a fixed modulus.",
                "detail": "For example, modulo 6, the numbers 1, 7, 13, and 19 all belong to the same residue class. Residue classes are important because primes must avoid many classes for divisibility reasons.",
            },
            {
                "term": "Arithmetic Progression",
                "summary": "An arithmetic progression is a sequence of numbers with a constant step size between consecutive terms.",
                "detail": "Examples include 1, 7, 13, 19 and 5, 11, 17, 23. Studying primes inside arithmetic progressions helps explain why certain modular structures matter for twin primes.",
            },
        ],
    },
    {
        "title": "Theory and Research Terms",
        "intro": "These terms connect the interactive product to the major ideas that appear in the Theory page.",
        "terms": [
            {
                "term": "Twin Prime Conjecture",
                "summary": "The twin prime conjecture is the claim that infinitely many twin-prime pairs exist.",
                "detail": "This remains one of the most famous unsolved problems in number theory. The project explores structure related to the conjecture without claiming a proof.",
            },
            {
                "term": "Bounded Gaps Between Primes",
                "summary": "Bounded gaps between primes means there exists some fixed number B such that infinitely many prime pairs differ by at most B.",
                "detail": "This was first proved by Yitang Zhang in 2013. It is a major breakthrough toward the twin prime conjecture, but it does not prove gap 2 occurs infinitely often.",
                "theory_link": {
                    "label": "See this in Theory: Current Progress",
                    "href": "/theory#progress",
                },
                "article_link": {
                    "label": "Read more: What Did Yitang Zhang Prove?",
                    "href": "/what-did-yitang-zhang-prove",
                },
            },
            {
                "term": "Hardy-Littlewood Conjecture",
                "summary": "The Hardy-Littlewood prime pair conjecture is a heuristic framework for predicting how often twin primes should occur.",
                "detail": "It gives a quantitative expectation for twin-prime frequency and is one of the main reasons mathematicians expect infinitely many twin primes to exist.",
            },
            {
                "term": "Twin Prime Constant",
                "summary": "The twin prime constant is a numerical factor that appears in heuristic estimates for how often twin primes occur.",
                "detail": "It adjusts naive probability-style estimates to account for divisibility constraints. The constant belongs to the Hardy-Littlewood heuristic framework, not to a proof.",
            },
        ],
    },
]
