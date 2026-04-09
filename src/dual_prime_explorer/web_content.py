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
                "title": "Read: Has the twin prime conjecture been solved?",
                "body": "Use the standalone page when you want the short answer and the exact reason the conjecture remains open.",
                "href": "/has-the-twin-prime-conjecture-been-solved",
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
        "intro": "Mathematicians study the twin prime conjecture using several complementary approaches. Each one captures a different piece of the problem: local divisibility, large-scale prime distribution, modular structure, quantitative expectation, or finite evidence. The challenge is that no single method yet joins all of those pieces tightly enough to force infinitely many exact gap-2 pairs.",
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
                "title": "What each approach is really trying to control",
                "body": "The twin prime problem is not just about finding examples. It asks for a proof that exact gap-2 pairs keep appearing forever. Sieve methods try to control local divisibility constraints, analytic methods try to describe prime distribution at scale, arithmetic-progression results track where primes can and cannot sit modulo small numbers, heuristics estimate how often the pattern should occur, and computation tests all of those ideas in finite ranges. The difficulty is that success on one layer does not automatically finish the others.",
            },
            {
                "title": "Why sieve methods are both powerful and limited",
                "body": "Modern progress on bounded gaps depends heavily on sieve ideas because sieves are excellent at ruling out impossible candidates and counting structured survivors. But sieves also run into the parity barrier: they can often tell that numbers behave almost like primes without being able to force the final distinction between a true prime and a cleverly disguised composite. That is why sieve breakthroughs can get very close to twin primes while still stopping short of gap 2.",
            },
            {
                "title": "Why residue classes keep returning",
                "body": "Twin primes are tightly constrained by modular arithmetic. Once you remove divisibility by 2 and 3, primes greater than 3 are pushed into narrow residue classes such as 1 and 5 mod 6. That is why the Lab's modulus views, the Analysis modular summaries, and the theory of primes in arithmetic progressions all reinforce one another: they are different ways of describing the same structural filter.",
            },
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
                "title": "Read: How mathematicians study twin primes",
                "body": "Use the standalone page when you want the major research approaches in one shorter read.",
                "href": "/how-mathematicians-study-twin-primes",
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
                "title": "What the theorem literally says",
                "body": "The bounded-gaps result is stronger than a numerical observation and weaker than the twin prime conjecture. It proves that one finite bound works infinitely many times. In other words, prime numbers do not eventually spread out so far that every fixed gap disappears. That is a precise theorem about recurring local proximity, even though it does not identify which specific gap repeats forever.",
            },
            {
                "title": "Why This Matters",
                "body": "Bounded gap results show that prime clustering is not a rare or accidental phenomenon. Instead, they prove that primes repeatedly appear within small distances of each other across infinitely many scales. This establishes a key structural insight: prime numbers are not only infinite, they also exhibit recurring local proximity. This shift from existence to structured behavior is one of the most important advances in modern number theory.",
            },
            {
                "title": "What changed after Zhang",
                "body": "Zhang's original proof was the breakthrough, but it was not the end of the story. The Polymath Project rapidly improved the numerical bound through large-scale collaboration, and James Maynard and Terence Tao developed methods that broadened the bounded-gap picture further. Together, these results turned one spectacular theorem into a more flexible modern framework for studying small gaps between primes.",
            },
            {
                "title": "Closest unconditional statements worth knowing",
                "body": "Modern progress is not limited to bounded gaps alone. Results such as Chen's theorem show that infinitely many primes p have the property that p + 2 is either prime or semiprime. That still falls short of twin primes, but it helps explain why mathematicians say the field has come close in meaningful, theorem-level ways without crossing the final exact-gap threshold.",
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
                "title": "Heuristics still guide the picture",
                "body": "Theorems and heuristics play different roles here. Bounded-gap results are proofs, so they belong to the known side of the story. Hardy-Littlewood style predictions belong to the expected side: they give the best-known quantitative reason to think twin primes should continue forever. Keeping those categories separate is one of the healthiest ways to read modern progress.",
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
        "intro": "The twin prime conjecture is difficult because it lies at the intersection of randomness and strict arithmetic structure. Any successful proof must simultaneously control both aspects of how prime numbers behave, and it must do so with exact local precision rather than only average large-scale information.",
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
                "title": "The parity barrier",
                "body": "One famous obstacle is the parity barrier in sieve theory. Roughly speaking, sieve methods are very good at removing numbers with obvious small factors, but they struggle to tell apart true primes and composites that survive the same divisibility filters. That barrier helps explain why modern methods can prove strong almost-twin-prime statements and bounded-gap theorems without yet isolating infinitely many exact twin-prime pairs.",
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
        "route": "/prime-numbers",
        "nav_label": "Prime Numbers Explained",
        "title": "TwinPrimeExplorer.com | Prime Numbers Explained",
        "meta_description": "A clear introduction to prime numbers, how they differ from composite numbers, why they matter, and how they connect to twin primes.",
        "eyebrow": "Prime Numbers",
        "hero_title": "Prime numbers explained",
        "hero_text": "Prime numbers are the basic building blocks of arithmetic. They are easy to define, endlessly rich in pattern, and the starting point for understanding twin primes.",
        "intro_title": "Start with the basics",
        "intro_text": "This page is for first-time visitors who want a clean explanation of what prime numbers are before moving into twin primes, prime gaps, or the site's interactive views.",
        "sections": [
            {
                "title": "What a prime number is",
                "body": "A prime number is a whole number greater than 1 with exactly two positive divisors: 1 and itself. Numbers such as 2, 3, 5, 7, and 11 are prime because they cannot be broken into smaller whole-number factors other than 1 and the number itself.",
            },
            {
                "title": "How primes differ from composite numbers",
                "body": "Composite numbers have more than two positive divisors. For example, 12 is composite because it can be divided evenly by 2, 3, 4, and 6 as well as 1 and 12. This prime-versus-composite split is the first structural filter behind everything else on the site.",
            },
            {
                "title": "Why prime numbers matter",
                "body": "Primes are the basic pieces from which all whole numbers are built. Every integer greater than 1 can be factored into primes. That is why prime numbers sit at the center of number theory: they are simple to define, but their overall distribution still contains deep open questions and striking visible patterns.",
            },
            {
                "title": "How primes connect to twin primes",
                "body": "Twin primes are just a special pattern inside the larger prime landscape. They are pairs of primes that differ by 2. Once you understand what primes are, the next natural questions become how they are spaced, when they appear near one another, and why gap-2 pairs are so mathematically interesting.",
            },
            {
                "title": "How to explore primes on this site",
                "body": "Use the Lab when you want to see primes and twin centers appear across a live range. Use Explorer when you want exact row-by-row inspection. Use Analysis when you want structured summaries of gaps, modular patterns, and density. The Glossary keeps the core terms short when you do not want a full article every time.",
            },
        ],
        "related_links": [
            {"title": "Continue to twin primes", "body": "Use the twin-primes page once you want to move from basic primes into the simplest major gap pattern on the site.", "href": "/what-are-twin-primes", "label": "Read What Are Twin Primes?"},
            {"title": "See primes in the Lab", "body": "Open a live range and watch primes, composites, and twin centers separate visually.", "href": "/lab#visualization-title", "label": "Open the Lab"},
            {"title": "Keep the vocabulary nearby", "body": "Use the Glossary for prime, composite, divisor, and related terms.", "href": "/glossary#glossary-term-prime", "label": "Open the Glossary"},
        ],
    },
    {
        "route": "/twin-prime-conjecture",
        "nav_label": "Twin Prime Conjecture Explained",
        "title": "TwinPrimeExplorer.com | Twin Prime Conjecture Explained",
        "meta_description": "An accessible explanation of the twin prime conjecture, what it claims, why it is still open, and how modern bounded-gap results relate to it.",
        "eyebrow": "Twin Prime Conjecture",
        "hero_title": "Twin prime conjecture explained",
        "hero_text": "The twin prime conjecture asks whether there are infinitely many pairs of prime numbers that differ by exactly 2. The statement is short. Proving it has turned out to be one of the most persistent open problems in number theory.",
        "intro_title": "The big question behind the site",
        "intro_text": "This page gives the cleanest nontechnical overview of the conjecture itself: what it says, what infinity means in this context, what has been proved nearby, and why the problem remains open.",
        "sections": [
            {
                "title": "What the conjecture says",
                "body": "The twin prime conjecture claims that there are infinitely many twin-prime pairs. A twin-prime pair is a pair of prime numbers with a gap of exactly 2, such as (11, 13) or (17, 19). The conjecture says that this pattern never runs out permanently.",
            },
            {
                "title": "What infinite means here",
                "body": "Infinite does not mean that twin primes are common or evenly spaced. It means that no matter how far you go along the number line, there should always be more twin-prime pairs beyond that point. The claim is about endless continuation, not about regular frequency.",
            },
            {
                "title": "Why the conjecture sounds simpler than it is",
                "body": "The statement only mentions prime pairs separated by 2, but a proof would need to control infinitely many local divisibility constraints at once. That is much harder than showing that primes exist forever or even that some small gap occurs infinitely often.",
            },
            {
                "title": "What has been proved nearby",
                "body": "Modern results show that primes come within some bounded distance of each other infinitely often. This is major progress, but it is still weaker than proving that the exact gap of 2 occurs infinitely often. That difference between bounded gaps and twin primes is one of the most important distinctions on the site.",
            },
            {
                "title": "How this connects to the tools",
                "body": "The site cannot prove or disprove the conjecture, but it can help you see why the pattern is compelling. The Lab makes gap-2 structure visible, Explorer lets you inspect concrete examples, and Analysis summarizes how pairs, centers, and gaps behave in a chosen range. Theory then connects those observations back to the mathematical story.",
            },
        ],
        "related_links": [
            {"title": "Need the short answer?", "body": "Use the shorter page when you want a clean yes-or-no explanation before reading the larger conjecture context.", "href": "/has-the-twin-prime-conjecture-been-solved", "label": "Read the short answer"},
            {"title": "See the modern progress", "body": "The Zhang page explains the most famous modern theorem that moved the field forward without finishing the conjecture.", "href": "/what-did-yitang-zhang-prove", "label": "Read about Zhang"},
            {"title": "See the pattern in the Lab", "body": "Use the Lab when you want the conjecture tied back to visible structure.", "href": "/lab#visualization-title", "label": "Open the Lab"},
        ],
    },
    {
        "route": "/how-to-find-twin-primes",
        "nav_label": "How To Find Twin Primes",
        "title": "TwinPrimeExplorer.com | How To Find Twin Primes",
        "meta_description": "A practical guide to finding twin primes, checking gap-2 pairs, avoiding false candidates, and using TwinPrimeExplorer.com to inspect the pattern.",
        "eyebrow": "Finding Twin Primes",
        "hero_title": "How to find twin primes",
        "hero_text": "Finding a twin-prime pair is straightforward in small ranges: look for two prime numbers that differ by exactly 2. The deeper challenge is learning which candidates are worth checking and why simple modular filters help.",
        "intro_title": "A practical pattern guide",
        "intro_text": "This page is about procedure rather than proof. It shows how to recognize twin-prime candidates, what quick filters help, and how the site's tools let you move from a simple search idea to richer structural inspection.",
        "sections": [
            {
                "title": "Start with the definition",
                "body": "A twin-prime pair is a pair of primes with a gap of 2. So the simplest search method is: take a prime p, check whether p + 2 is also prime, and record the pair if it is. In small ranges this is enough to generate real examples quickly.",
            },
            {
                "title": "Use prime lists and quick filters",
                "body": "In practice, people rarely test every whole number from scratch. They work from a list of primes or from candidates that have already passed small divisibility filters. That is why residue classes such as 1 and 5 mod 6 matter so much: they eliminate many impossible cases before you do deeper checking.",
            },
            {
                "title": "Why Mod 6 helps but does not solve the problem",
                "body": "For primes greater than 3, only two residue classes mod 6 remain possible. That means a typical twin-prime pair above (3, 5) looks like (6k - 1, 6k + 1). This is a useful candidate pattern, not a proof that those numbers are prime. Modular filters tell you where to look, but primality still has to be checked.",
            },
            {
                "title": "Common false candidates",
                "body": "Many numbers fit the right-looking shape and still fail. A pair can land in the correct residue classes and still contain a composite number with a nontrivial factor. That is why it helps to treat modular structure as a fast screening tool rather than as a guarantee.",
            },
            {
                "title": "How to do it on this site",
                "body": "Use Explorer when you want the most direct working surface: row-by-row values, prime roles, twin centers, and divisor details. Use the Lab when you want to scan visually first. Then move into Analysis if you want to understand how the examples you found fit into larger spacing or modular patterns.",
            },
        ],
        "related_links": [
            {"title": "Use Explorer for exact inspection", "body": "Explorer is the clearest place to test candidate pairs and inspect neighborhood roles one row at a time.", "href": "/explorer#number-table-title", "label": "Open Explorer"},
            {"title": "Need the residue-class shortcut?", "body": "Use the modular explainer if you want the residue filter idea in plain language first.", "href": "/why-mod-6-shows-up-so-often", "label": "Read Why Mod 6 Shows Up So Often"},
            {"title": "Compare what you found in Analysis", "body": "Analysis helps connect the candidate-finding process to larger gap and density structure.", "href": "/analysis#analysis-views-title", "label": "Open Analysis"},
        ],
    },
    {
        "route": "/prime-gaps",
        "nav_label": "What Are Prime Gaps?",
        "title": "TwinPrimeExplorer.com | What Are Prime Gaps?",
        "meta_description": "A clear introduction to prime gaps, including small and large examples, why twin primes are the gap-2 case, and why bounded gaps matter.",
        "eyebrow": "Prime Gaps",
        "hero_title": "What are prime gaps?",
        "hero_text": "A prime gap is the difference between one prime number and the next. Some gaps are small, some grow much larger, and the special case of gap 2 is exactly where twin primes live.",
        "intro_title": "A bridge concept for the site",
        "intro_text": "Prime gaps connect the site's basic prime pages to its deeper twin-prime and bounded-gap pages. This is the cleanest place to understand what a gap is before moving into more specialized questions.",
        "sections": [
            {
                "title": "The basic definition",
                "body": "If one prime is followed by the next prime, the difference between them is a prime gap. For example, the gap between 11 and 13 is 2, while the gap between 23 and 29 is 6. Prime gaps measure spacing rather than primality itself.",
            },
            {
                "title": "Twin primes are the gap-2 case",
                "body": "Twin primes are the smallest nontrivial example of a prime-gap pattern. When two consecutive primes differ by 2, they form a twin-prime pair. That is why studying prime gaps naturally leads to the twin prime conjecture.",
            },
            {
                "title": "Why gaps tend to grow",
                "body": "As numbers get larger, primes become less frequent on average, so larger gaps become more common. That does not mean small gaps disappear. It means the overall spacing picture becomes more uneven, which is one reason small recurring gaps remain interesting.",
            },
            {
                "title": "Why bounded gaps matter",
                "body": "A bounded-gap theorem says that some fixed finite prime gap occurs infinitely often. That is a powerful statement because it proves recurring close proximity between primes at arbitrarily large scales. It still does not settle the special gap-2 case, but it sits very close to the twin-prime story.",
            },
            {
                "title": "How this site lets you inspect gaps",
                "body": "Analysis is the best place to study gap structure directly because it summarizes repeated spacing across a chosen range. Explorer helps when you want exact examples, and the Lab helps when you want to see clusters and separation before reading the structured summaries.",
            },
        ],
        "related_links": [
            {"title": "Start with the gap-2 case", "body": "Use the twin-primes page when you want the special gap-2 pattern explained before the broader gap story.", "href": "/what-are-twin-primes", "label": "Read What Are Twin Primes?"},
            {"title": "Inspect gaps in Analysis", "body": "The Analysis page is the clearest place to compare spacing patterns in a live range.", "href": "/analysis#analysis-views-title", "label": "Open Analysis"},
            {"title": "Read the bounded-gap breakthrough", "body": "The Zhang page explains how modern theorems turned small prime gaps into a proof-level result.", "href": "/what-did-yitang-zhang-prove", "label": "Read about Zhang"},
        ],
    },
    {
        "route": "/what-are-twin-primes",
        "nav_label": "What Are Twin Primes?",
        "title": "TwinPrimeExplorer.com | What Are Twin Primes?",
        "meta_description": "A fuller introduction to twin primes, including examples, structure, what is known versus conjectured, and how to explore the pattern on TwinPrimeExplorer.com.",
        "eyebrow": "Twin Primes",
        "hero_title": "What are twin primes?",
        "hero_text": "Twin primes are pairs of prime numbers that differ by exactly 2. They are simple to state, easy to spot in small ranges, and still connected to one of the best-known open questions in number theory.",
        "intro_title": "Start with the core pattern",
        "intro_text": "This page is the plain-language entry point for the site's central idea. It explains what twin primes are, why they matter mathematically, what is known versus still unproved, and how to follow the pattern through the live tools.",
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
                "title": "The early exception and the usual pattern",
                "body": "The pair (3, 5) is a special early case because it includes the only odd prime that is also divisible by 3. After that, twin-prime pairs typically look like (6k - 1, 6k + 1). This does not force a number to be prime, but it explains why Mod 6 keeps appearing in twin-prime discussions and why the middle value, the twin center, usually lands on a multiple of 6.",
            },
            {
                "title": "Why twin centers help",
                "body": "Instead of tracking a pair as two separate primes, the site often highlights the number in the middle. If (p, p + 2) is a twin-prime pair, then p + 1 is its twin center. This compression makes it easier to count, visualize, and compare twin-prime structure across a range, especially in the Lab and the Analysis views.",
            },
            {
                "title": "Why people care about them",
                "body": "The twin prime conjecture asks whether infinitely many twin-prime pairs exist. That question is still open. The pattern is easy to understand, but proving it continues forever is much harder than finding many examples.",
            },
            {
                "title": "What is known and what is still conjectured",
                "body": "Some important facts are already proven. Brun's theorem shows that twin primes are sparse enough that the sum of their reciprocals converges, and bounded-gap results show that primes come within some fixed finite distance infinitely often. But neither of those results proves that gap 2 itself repeats forever. The expectation that infinitely many twin primes exist comes from strong heuristics and extensive computation, not from a completed proof.",
            },
            {
                "title": "How to explore twin primes on this site",
                "body": "TwinPrimeExplorer.com treats twin primes as something you can see, inspect, and interpret from several angles. Open the Lab when you want the pattern field first, especially with twin centers and Mod 6 structure visible at the same time. Use Explorer when you want exact examples row by row. Use Analysis when you want modular summaries, spacing behavior, density, and a rough expected-count benchmark. Use Theory when you want the broader research story around the same pattern.",
            },
        ],
        "related_links": [
            {"title": "See the pattern in the Lab", "body": "Start with a live range and watch twin primes and twin centers appear together.", "href": "/lab#visualization-title", "label": "Open the Lab"},
            {"title": "Inspect exact examples in Explorer", "body": "Use row-by-row inspection when you want to move from the definition to concrete cases.", "href": "/explorer#number-table-title", "label": "Open Explorer"},
            {"title": "Interpret the pattern in Analysis", "body": "Analysis connects the same idea to modular structure, pair spacing, and local density.", "href": "/analysis#analysis-views-title", "label": "Open Analysis"},
            {"title": "Follow the bigger question", "body": "Use the conjecture page when you want the exact infinite-question framing behind twin primes.", "href": "/twin-prime-conjecture", "label": "Read the conjecture page"},
            {"title": "Read the longer history", "body": "Use Theory when you want the conjecture, timeline, and current mathematical status in one place.", "href": "/theory#history", "label": "Open Theory: History"},
            {"title": "Check the key terms", "body": "Use the Glossary when you want quick definitions for twin prime, twin center, and prime gap.", "href": "/glossary#glossary-term-twin-prime", "label": "Open the Glossary"},
        ],
    },
    {
        "route": "/what-did-yitang-zhang-prove",
        "nav_label": "What Did Yitang Zhang Prove?",
        "title": "TwinPrimeExplorer.com | What Did Yitang Zhang Prove?",
        "meta_description": "A fuller explanation of Yitang Zhang's bounded-gaps breakthrough, what the theorem literally proved, what happened after it, and why it still stops short of twin primes.",
        "eyebrow": "Modern Progress",
        "hero_title": "What did Yitang Zhang prove?",
        "hero_text": "In 2013, Yitang Zhang proved that there is some fixed finite bound B such that infinitely many pairs of primes differ by at most B. It was a major breakthrough, but it did not prove the twin prime conjecture.",
        "intro_title": "What this page clarifies",
        "intro_text": "Zhang's breakthrough is often mentioned in one sentence and misunderstood in the next. This page separates the theorem itself, why it mattered so much, what later work changed, and why bounded gaps still does not mean twin primes were proved.",
        "sections": [
            {
                "title": "The theorem in plain language",
                "body": "Zhang proved that prime numbers do not drift apart forever. Instead, there exists at least one fixed distance B so that infinitely many prime pairs appear with a gap no larger than B.",
            },
            {
                "title": "The theorem in notation and in English",
                "body": "If p_n denotes the nth prime number, Zhang's result can be summarized by saying that the liminf of p_(n+1) - p_n is finite. In plain language, that means there is some fixed bound that keeps recurring between consecutive primes infinitely often. The theorem does not tell us that the recurring bound is 2, only that it does not have to grow without limit.",
            },
            {
                "title": "Why this mattered immediately",
                "body": "Before Zhang, no one had proved that primes come close together infinitely often in any bounded way. His result changed the field by turning a long-standing expectation into a theorem.",
            },
            {
                "title": "Why the breakthrough was so surprising",
                "body": "Mathematicians already had strong heuristic reasons to believe in small prime gaps, but a proof required new control over how primes are distributed in arithmetic progressions. Zhang supplied enough of that control to push bounded gaps from a hope into a theorem. That is why the result was treated as a genuine field-changing breakthrough rather than just one more improved estimate.",
            },
            {
                "title": "What it did not prove",
                "body": "Zhang did not prove that the gap is 2 infinitely often. The twin prime conjecture asks for the exact gap of 2, while bounded-gap results only guarantee that some finite gap occurs infinitely many times.",
            },
            {
                "title": "What happened after Zhang",
                "body": "Zhang opened the door, and the next wave of work pushed through it quickly. The Polymath Project reduced the original numerical bound through large-scale collaboration, while James Maynard and Terence Tao developed methods that broadened bounded-gap theory beyond Zhang's first theorem. Modern discussion of prime gaps now includes all of these advances, but Zhang's 2013 result remains the turning point.",
            },
            {
                "title": "Why the result still belongs in the twin-prime story",
                "body": "The theorem showed that prime clustering is not just a heuristic guess. It established that small prime gaps recur across infinitely many scales, which is one of the strongest pieces of progress connected to the twin prime problem.",
            },
            {
                "title": "How to see the idea in TwinPrimeExplorer",
                "body": "The site cannot reproduce the proof, but it can help you build intuition for what bounded gaps are about. In Analysis, the Gaps tab lets you inspect repeated small spacings in a selected range. In the Lab, you can watch clusters of twin-prime candidates and centers appear rather than treating prime gaps as an abstract theorem statement. That shift from theorem language to visible structure is exactly why this page belongs next to the tools.",
            },
        ],
        "related_links": [
            {"title": "See the broader progress picture", "body": "Theory puts Zhang, Polymath, and Maynard-Tao into the same timeline.", "href": "/theory#progress", "label": "Open Theory: Current Progress"},
            {"title": "Need the short answer first?", "body": "Use the short answer page for a clear explanation of why bounded gaps still do not solve the twin prime conjecture.", "href": "/has-the-twin-prime-conjecture-been-solved", "label": "Read the short answer"},
            {"title": "Look at gap structure directly", "body": "Analysis helps connect the idea of small gaps to concrete ranges and repeated spacing.", "href": "/analysis#analysis-views-title", "label": "Open Analysis"},
            {"title": "Step back to prime gaps", "body": "Use the prime-gaps page when you want bounded gaps placed inside the broader spacing story first.", "href": "/prime-gaps", "label": "Read What Are Prime Gaps?"},
            {"title": "Check the bounded-gaps definition", "body": "The Glossary keeps the distinction between bounded gaps and twin primes short and clear.", "href": "/glossary#glossary-term-bounded-gaps-between-primes", "label": "Open the Glossary"},
        ],
    },
    {
        "route": "/why-mod-6-shows-up-so-often",
        "nav_label": "Why Mod 6 Shows Up So Often",
        "title": "TwinPrimeExplorer.com | Why Mod 6 Shows Up So Often",
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
        "title": "TwinPrimeExplorer.com | Why Twin Centers Matter",
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
    {
        "route": "/has-the-twin-prime-conjecture-been-solved",
        "nav_label": "Has The Twin Prime Conjecture Been Solved?",
        "title": "TwinPrimeExplorer.com | Has The Twin Prime Conjecture Been Solved?",
        "meta_description": "A clear explanation of whether the twin prime conjecture has been solved and how bounded-gap progress differs from a full proof.",
        "eyebrow": "Twin Prime Conjecture",
        "hero_title": "Has the twin prime conjecture been solved?",
        "hero_text": "No. The twin prime conjecture remains unsolved. Modern progress shows that primes come within some bounded distance infinitely often, but that is not the same as proving infinitely many gap-2 pairs.",
        "intro_title": "The short answer",
        "intro_text": "If you only need the answer in one line, it is no. This page exists to make the next sentence clear too: important progress has happened, but the exact twin-prime claim still has not been proved.",
        "sections": [
            {
                "title": "What the conjecture actually says",
                "body": "The twin prime conjecture claims that there are infinitely many pairs of prime numbers that differ by exactly 2. It is not a claim about small gaps in general. It is a claim about the exact gap of 2 repeating forever.",
            },
            {
                "title": "Why people sometimes think it was solved",
                "body": "News about bounded gaps between primes can sound very close to the twin prime conjecture. If you hear that primes come close together infinitely often, it is easy to assume that twin primes were proved too. That last step is exactly the part that remains open.",
            },
            {
                "title": "What modern results do prove",
                "body": "Modern theorems show that there exists some fixed finite bound B such that infinitely many prime pairs differ by at most B. That is a major breakthrough, because it proves recurring small gaps. But the bound is not known to be 2.",
            },
            {
                "title": "Why the distinction matters",
                "body": "This is one of the clearest examples in number theory of progress versus proof. The field has moved much closer to the conjecture, but the exact statement mathematicians want to prove is still unresolved.",
            },
        ],
        "related_links": [
            {"title": "Read the bounded-gap breakthrough", "body": "Use the Zhang page when you want the cleanest explanation of what bounded gaps actually proved.", "href": "/what-did-yitang-zhang-prove", "label": "Read about Zhang"},
            {"title": "See the current progress summary", "body": "Theory collects the larger progress picture in one place.", "href": "/theory#progress", "label": "Open Theory: Current Progress"},
            {"title": "Check the conjecture terms", "body": "Use the Glossary when you want short definitions for twin prime conjecture and bounded gaps.", "href": "/glossary#glossary-term-twin-prime-conjecture", "label": "Open the Glossary"},
        ],
    },
    {
        "route": "/what-bounded-gaps-between-primes-actually-proved",
        "nav_label": "What Bounded Gaps Between Primes Actually Proved",
        "title": "TwinPrimeExplorer.com | What Bounded Gaps Between Primes Actually Proved",
        "meta_description": "What bounded gaps between primes really proved, why it matters, and why it still stops short of proving infinitely many twin primes.",
        "eyebrow": "Bounded Gaps",
        "hero_title": "What bounded gaps between primes actually proved",
        "hero_text": "Bounded-gap results proved that primes come within some fixed finite distance infinitely often. That is a major structural theorem about prime clustering, but it is still not the same as proving infinitely many twin primes.",
        "intro_title": "Why this page helps",
        "intro_text": "Bounded gaps is one of the most important phrases in the modern twin-prime story, but it is also one of the easiest to blur into something it does not say. This page keeps the claim precise.",
        "sections": [
            {
                "title": "What bounded gaps means",
                "body": "A bounded-gap theorem says there is some fixed number B so that infinitely many prime pairs differ by at most B. The key point is that the same finite bound works infinitely often.",
            },
            {
                "title": "What the breakthrough changed",
                "body": "Before these results, it was not known whether primes could be proved to recur within any fixed finite distance infinitely many times. The breakthrough turned that possibility into a theorem and changed how mathematicians talk about small prime gaps.",
            },
            {
                "title": "Why it still falls short of twin primes",
                "body": "Twin primes require the exact gap of 2. Bounded-gap theorems only prove that some finite bound works. Even if that bound is much smaller than earlier ones, it is still not the same as isolating the exact twin-prime pattern.",
            },
            {
                "title": "Why the result still matters so much",
                "body": "These theorems prove that local prime clustering is a real structural phenomenon, not just something suggested by computations or heuristics. That is why bounded gaps sits so close to the center of the modern twin-prime story.",
            },
        ],
        "related_links": [
            {"title": "Read the Zhang milestone", "body": "Use the Zhang page when you want the breakthrough framed around the person and the 2013 result.", "href": "/what-did-yitang-zhang-prove", "label": "Read about Zhang"},
            {"title": "See how Theory summarizes the progress", "body": "The Current Progress tab keeps the wider bounded-gap picture connected to the conjecture itself.", "href": "/theory#progress", "label": "Open Theory: Current Progress"},
            {"title": "Use Analysis for gap structure", "body": "Analysis lets you compare the article idea with gap patterns in a concrete finite range.", "href": "/analysis#analysis-views-title", "label": "Open Analysis"},
        ],
    },
    {
        "route": "/why-the-twin-prime-problem-is-hard",
        "nav_label": "Why The Twin Prime Problem Is Hard",
        "title": "TwinPrimeExplorer.com | Why The Twin Prime Problem Is Hard",
        "meta_description": "Why the twin prime problem is difficult, including local divisibility constraints, global versus local control, and the limits of computation.",
        "eyebrow": "Why It Is Hard",
        "hero_title": "Why the twin prime problem is hard",
        "hero_text": "The twin prime problem sounds simple because the statement is short. The difficulty is that any proof has to control both the large-scale distribution of primes and the exact local conditions that produce gap-2 pairs.",
        "intro_title": "The short version",
        "intro_text": "This problem is hard because primes look partly irregular but obey strict arithmetic rules at the same time. A proof has to manage both sides at once.",
        "sections": [
            {
                "title": "Exact gaps are harder than small gaps",
                "body": "It is one thing to prove that primes come close together infinitely often. It is a stronger and more delicate task to prove that the exact gap of 2 occurs infinitely often. That extra precision is where current methods still fall short.",
            },
            {
                "title": "Divisibility constraints pile up",
                "body": "For a twin-prime pair (p, p+2), both numbers must avoid divisibility by many small primes at the same time. Those restrictions overlap and accumulate, which makes the local arithmetic much harder to control than the primality of a single number.",
            },
            {
                "title": "Average information is not enough",
                "body": "Modern methods often describe how primes behave on average or across large scales. The twin prime problem needs more than that. It asks for infinitely many exact local alignments, not just broad tendencies.",
            },
            {
                "title": "Computation does not finish the job",
                "body": "Computers can find enormous twin-prime examples and measure real patterns, but every computation ends at a finite range. The conjecture is about what happens beyond every finite limit, so examples alone can never complete the proof.",
            },
        ],
        "related_links": [
            {"title": "Read the Theory summary", "body": "Theory keeps the full difficulty story connected to the rest of the conjecture context.", "href": "/theory#why-its-hard", "label": "Open Theory: Why It's Hard"},
            {"title": "Inspect local arithmetic in Explorer", "body": "Explorer helps make divisibility and neighborhood structure concrete one row at a time.", "href": "/explorer#number-table-title", "label": "Open Explorer"},
            {"title": "Use the Glossary for quick support", "body": "Glossary definitions help if terms like bounded gaps, divisor, or twin center feel unfamiliar while you read.", "href": "/glossary#glossary-term-bounded-gaps-between-primes", "label": "Open the Glossary"},
        ],
    },
    {
        "route": "/how-mathematicians-study-twin-primes",
        "nav_label": "How Mathematicians Study Twin Primes",
        "title": "TwinPrimeExplorer.com | How Mathematicians Study Twin Primes",
        "meta_description": "An overview of how mathematicians study twin primes through sieve methods, analytic number theory, arithmetic progressions, heuristics, and computation.",
        "eyebrow": "Approaches",
        "hero_title": "How mathematicians study twin primes",
        "hero_text": "There is no single method that solves the twin prime problem. Instead, mathematicians approach it from several angles, each of which captures part of the structure but not yet the final proof.",
        "intro_title": "Why there are several approaches",
        "intro_text": "The twin prime problem sits at the intersection of local arithmetic structure, global distribution, and repeated small gaps. That is why different methods each illuminate a different part of the picture.",
        "sections": [
            {
                "title": "Sieve methods",
                "body": "Sieve methods filter large sets of integers by divisibility conditions. They are powerful for finding numbers that behave almost like primes and for proving bounded-gap style results, but they run into the parity barrier before reaching a full twin-prime proof.",
            },
            {
                "title": "Analytic number theory",
                "body": "Analytic methods study primes through functions, asymptotic estimates, and large-scale distribution patterns. They reveal deep structure, but often at the level of averages rather than exact local pair formation.",
            },
            {
                "title": "Primes in arithmetic progressions",
                "body": "Modular structure matters because primes must land in certain residue classes to avoid small divisors. Studying primes in arithmetic progressions helps explain why patterns like mod 6 keep reappearing in twin-prime discussions.",
            },
            {
                "title": "Heuristics and computation",
                "body": "Heuristic models predict that twin primes should continue forever, and computation gives large-scale evidence for those predictions. Both are valuable, but neither replaces a proof.",
            },
        ],
        "related_links": [
            {"title": "Read the Theory approaches tab", "body": "Theory keeps the method-level overview together in one reference surface.", "href": "/theory#approaches", "label": "Open Theory: Approaches"},
            {"title": "See Mod 6 in the Lab", "body": "Use the visual mode that makes arithmetic-progression structure easier to spot quickly.", "href": "/lab#visualization-title", "label": "Open the Lab"},
            {"title": "Read the modular explainer", "body": "Use the standalone Mod 6 page when you want the shortest clear explanation of why residue classes matter here.", "href": "/why-mod-6-shows-up-so-often", "label": "Read the Mod 6 page"},
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
                "detail": "Examples include 2, 3, 5, 7, and 11. Prime numbers are the main building blocks of TwinPrimeExplorer.com.",
                "article_link": {
                    "label": "Read more: Prime Numbers Explained",
                    "href": "/prime-numbers",
                },
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
                "detail": "Examples include (3, 5), (5, 7), and (11, 13). Twin primes are the central object of study on TwinPrimeExplorer.com.",
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
                "article_link": {
                    "label": "Read more: What Are Prime Gaps?",
                    "href": "/prime-gaps",
                },
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
                "article_link": {
                    "label": "Read more: Twin Prime Conjecture Explained",
                    "href": "/twin-prime-conjecture",
                },
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
                "article_link": {
                    "label": "Read more: How Mathematicians Study Twin Primes",
                    "href": "/how-mathematicians-study-twin-primes",
                },
            },
            {
                "term": "Twin Prime Constant",
                "summary": "The twin prime constant is a numerical factor that appears in heuristic estimates for how often twin primes occur.",
                "detail": "It adjusts naive probability-style estimates to account for divisibility constraints. The constant belongs to the Hardy-Littlewood heuristic framework, not to a proof.",
            },
        ],
    },
]
