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
        "route": "/start-here",
        "nav_label": "Start Here",
        "title": "TwinPrimeExplorer.com | Start Here",
        "meta_description": "A reading guide to the most important TwinPrimeExplorer.com pages, including where to start with prime numbers, twin primes, conjectures, and the interactive tools.",
        "eyebrow": "Reading Guide",
        "hero_title": "Start here",
        "hero_text": "If you are new to TwinPrimeExplorer.com, this page gives you a clean route into the educational side of the site before you decide which tool, background topic, or theory path to open next.",
        "intro_title": "A simple reading path",
        "intro_text": "This guide is for first-time visitors and returning readers who want the information side of the site in a sensible order. It points to the strongest foundation pages first, then helps you branch toward conjecture and progress pages, or toward the shorter pattern-reading pages that connect directly back to the tools. If you only want a quick plan, think in three steps: basics first, the twin-prime pattern second, then either theory progress or tool-reading pages once the pattern feels familiar.",
        "reviewed": "Last reviewed: April 2026",
        "sections": [
            {
                "title": "Start with prime numbers if you want the basics",
                "body": "If words like prime, composite, divisor, or factor still feel slightly loose, begin with Prime Numbers Explained. That page gives the shortest clean foundation for everything else on the site, including twin primes, prime gaps, and the modular patterns that show up later. It is the best first stop if you want the site to feel cumulative rather than fragmented.",
            },
            {
                "title": "Move to twin primes for the central pattern",
                "body": "Once the basic idea of a prime number is settled, the next best page is What Are Twin Primes? It introduces the site's main pattern, explains why gap 2 matters, and separates what mathematicians know from what they still expect but have not proved. If you only read one central explainer after the basics, this is usually the right one.",
            },
            {
                "title": "Use prime gaps and the conjecture pages for context",
                "body": "Prime gaps gives the broader spacing story, while Twin Prime Conjecture Explained gives the larger unresolved question behind the site. Those two pages help connect a concrete visible pattern to the deeper mathematical problem that makes twin primes so interesting. A good rule is: read prime gaps when you want the surrounding spacing language, read the conjecture page when you want the biggest open question stated cleanly, and use Prime Gaps vs Prime Pairs if those two ideas are starting to blur together.",
            },
            {
                "title": "Use the shorter explainers when you want one idea at a time",
                "body": "Pages such as Why Mod 6 Shows Up So Often, Why Twin Centers Matter, Prime Gaps vs Prime Pairs, and What Bounded Gaps Between Primes Actually Proved are meant to answer one question clearly without forcing you through a longer theory overview. They work well when one concept keeps showing up in the tools and you want it unpacked quickly. They are best treated as short side paths that sharpen one idea before you return to the main reading flow.",
            },
            {
                "title": "Choose the branch that matches your next question",
                "body": "If your next question is about background mathematics, go to The Prime Number Theorem In Plain Language or Why log n Appears In Prime Number Theory. If your next question is about progress on the open problem, go to Are There Infinitely Many Twin Primes?, Twin Prime Conjecture Explained, or Hardy-Littlewood For Twin Primes. If your next question is about how to read what the tools are showing, go to How To Read Prime Patterns In The Lab or the Analysis Guide.",
            },
            {
                "title": "Then bring the ideas back into the tools",
                "body": "The Lab is best for seeing the pattern first, Explorer is best for checking exact numbers and neighborhood roles, and Analysis is best for structured summaries such as modular counts, gap behavior, density, and rough expectation comparisons. Theory and Glossary stay available as reference companions while you do that. A common reading loop on this site is: learn one concept, open a live range, then come back to the explanation with concrete examples in mind.",
            },
        ],
        "references": [
            {"label": "Britannica: prime numbers", "href": "https://www.britannica.com/story/prime-numbers", "note": "General background for the basic prime-number reading path."},
            {"label": "MathWorld: Twin Primes", "href": "https://mathworld.wolfram.com/TwinPrimes.html", "note": "Compact reference for the site's central pattern."},
            {"label": "Britannica: prime number theorem", "href": "https://www.britannica.com/science/number-theory/Prime-number-theorem", "note": "Background for the average-density pages in the reading path."},
        ],
        "related_links": [
            {"title": "Begin with prime numbers", "body": "Use the basic page first if you want the cleanest foundation for the rest of the site.", "href": "/prime-numbers", "label": "Read Prime Numbers Explained"},
            {"title": "See why primes thin out", "body": "The prime number theorem page explains the average thinning pattern that sits behind later density and expected-count language.", "href": "/prime-number-theorem", "label": "Read The Prime Number Theorem In Plain Language"},
            {"title": "Move to the main pattern", "body": "Go next to the twin-primes page if you want the core idea behind the whole site.", "href": "/what-are-twin-primes", "label": "Read What Are Twin Primes?"},
            {"title": "See the broader spacing story", "body": "Open the prime-gaps page when you want the twin-prime pattern placed inside the larger question of spacing between consecutive primes.", "href": "/prime-gaps", "label": "Read What Are Prime Gaps?"},
            {"title": "See the larger open question", "body": "Use the conjecture page when you want the strongest plain-language statement of what remains unproved.", "href": "/twin-prime-conjecture", "label": "Read Twin Prime Conjecture Explained"},
            {"title": "Ask the big yes-or-no question", "body": "Use the direct infinite-question page when you want the most search-friendly answer to whether twin primes keep going forever.", "href": "/are-there-infinitely-many-twin-primes", "label": "Read Are There Infinitely Many Twin Primes?"},
            {"title": "See the heuristic side of the expectation", "body": "Hardy-Littlewood is the clearest next page if you want to know why mathematicians expect infinitely many twin primes without calling that expectation a proof.", "href": "/hardy-littlewood-twin-primes", "label": "Read Hardy-Littlewood For Twin Primes"},
            {"title": "See why log n keeps returning", "body": "This background page explains why logarithms appear in prime-density and twin-prime heuristic language across the site.", "href": "/why-log-n-appears-in-prime-number-theory", "label": "Read Why log n Appears In Prime Number Theory"},
            {"title": "Separate spacing language from pair language", "body": "Use this clarification page when prime gaps, named prime pairs, and bounded-gap language are starting to blur together.", "href": "/prime-gaps-vs-prime-pairs", "label": "Read Prime Gaps vs Prime Pairs"},
            {"title": "Bring the reading into the tools", "body": "Open the Lab when you are ready to move from explanation back to a live range.", "href": "/lab#visualization-title", "label": "Open the Lab"},
            {"title": "Learn how to read the Lab", "body": "Use the Lab-reading page if you want a more deliberate first-pass workflow for interpreting the visual patterns.", "href": "/how-to-read-prime-patterns-in-the-lab", "label": "Read How To Read Prime Patterns In The Lab"},
        ],
    },
    {
        "route": "/prime-numbers",
        "nav_label": "Prime Numbers Explained",
        "title": "TwinPrimeExplorer.com | Prime Numbers Explained",
        "meta_description": "A fuller introduction to prime numbers, including examples, how primes differ from composite numbers, why they matter, and how they lead into twin primes and prime gaps.",
        "eyebrow": "Prime Numbers",
        "hero_title": "Prime numbers explained",
        "hero_text": "Prime numbers are the basic building blocks of arithmetic. They are easy to define, surprisingly hard to predict, and the starting point for understanding twin primes, prime gaps, and much of elementary number theory.",
        "intro_title": "Start with the basics",
        "intro_text": "This page is the site's foundational introduction to prime numbers. It explains what primes are, how they differ from composite numbers, why mathematicians care about them, and how they connect naturally to the twin-prime and prime-gap pages elsewhere on TwinPrimeExplorer.com.",
        "reviewed": "Last reviewed: April 2026",
        "sections": [
            {
                "title": "What a prime number is",
                "body": "A prime number is a whole number greater than 1 with exactly two positive divisors: 1 and itself. Numbers such as 2, 3, 5, 7, and 11 are prime because they cannot be broken into smaller whole-number factors other than 1 and the number itself. By contrast, 1 is not prime because it has only one positive divisor, while numbers like 4 or 9 are not prime because they split into smaller whole-number factors.",
            },
            {
                "title": "How primes differ from composite numbers",
                "body": "Composite numbers have more than two positive divisors. For example, 12 is composite because it can be divided evenly by 2, 3, 4, and 6 as well as 1 and 12. Another simple comparison is 13 versus 15: 13 is prime because only 1 and 13 divide it evenly, while 15 is composite because 3 times 5 equals 15. This prime-versus-composite split is the first structural filter behind everything else on the site.",
            },
            {
                "title": "Why primes matter in number theory",
                "body": "Primes are the basic pieces from which all whole numbers are built. Every integer greater than 1 can be factored into primes, and that factorization is unique up to order. For example, 84 breaks into 2 times 2 times 3 times 7, while 90 breaks into 2 times 3 times 3 times 5. That is why prime numbers sit at the center of number theory: they are the irreducible pieces behind multiplication, divisibility, and factorization across the whole number system. Many later questions about residues, divisors, prime gaps, and twin-prime pairs are really refinements of this same basic fact: primes are the atoms of integer arithmetic.",
            },
            {
                "title": "Why primes become harder to predict",
                "body": "The definition of a prime is simple, but the long-range pattern is not. There is no short repeating recipe that tells you exactly where the next prime must appear. As numbers grow, primes become less frequent on average, but they still arrive in uneven ways: sometimes close together, sometimes separated by larger gaps. Even small ranges can show streaks of quick arrivals followed by quieter stretches. That combination of simple definition and irregular distribution is one reason prime numbers remain mathematically rich.",
            },
            {
                "title": "How primes connect to twin primes and prime gaps",
                "body": "Twin primes are a special pattern inside the larger prime landscape: they are pairs of primes that differ by 2. Prime gaps generalize the same idea by asking how far apart consecutive primes are in general. Once you understand what a prime number is, the next natural questions become how primes are spaced, when they appear near one another, and why a gap-2 pair is so special. That is the bridge from basic arithmetic into the twin-prime conjecture and modern bounded-gap results.",
            },
            {
                "title": "How to explore primes on this site",
                "body": "Use the Lab when you want to see primes and twin centers appear across a live range. Use Explorer when you want exact row-by-row inspection of individual numbers and divisors. Use Analysis when you want structured summaries of gaps, modular patterns, and density. Theory gives the larger mathematical story, while the Glossary keeps the core terms short when you do not want a full article every time.",
            },
        ],
        "references": [
            {"label": "Britannica: prime number", "href": "https://www.britannica.com/science/prime-number", "note": "Clear definition and basic number-theory context."},
            {"label": "Britannica: number theory", "href": "https://www.britannica.com/science/number-theory", "note": "Broader context for why primes matter in mathematics."},
            {"label": "Britannica: prime number theorem", "href": "https://www.britannica.com/science/number-theory/Prime-number-theorem", "note": "Useful companion for the distribution side of the page."},
        ],
        "related_links": [
            {"title": "Continue to twin primes", "body": "Use the twin-primes page once you want to move from basic primes into the simplest major gap pattern on the site.", "href": "/what-are-twin-primes", "label": "Read What Are Twin Primes?"},
            {"title": "Step into prime gaps", "body": "Use the prime-gaps page when you want the broader spacing story that sits between basic primes and the twin-prime conjecture.", "href": "/prime-gaps", "label": "Read What Are Prime Gaps?"},
            {"title": "See primes in the Lab", "body": "Open a live range and watch primes, composites, and twin centers separate visually.", "href": "/lab#visualization-title", "label": "Open the Lab"},
            {"title": "Inspect exact numbers in Explorer", "body": "Explorer is the clearest place to move from the definition of a prime to specific rows, divisors, and nearby values.", "href": "/explorer#number-table-title", "label": "Open Explorer"},
            {"title": "Keep the vocabulary nearby", "body": "Use the Glossary for prime, composite, divisor, and related terms.", "href": "/glossary#glossary-term-prime", "label": "Open the Glossary"},
        ],
    },
    {
        "route": "/twin-prime-conjecture",
        "nav_label": "Twin Prime Conjecture Explained",
        "title": "TwinPrimeExplorer.com | Twin Prime Conjecture Explained",
        "meta_description": "A fuller explanation of the twin prime conjecture, including what it claims, what 'infinitely many' means, what has been proved nearby, and what remains open.",
        "eyebrow": "Twin Prime Conjecture",
        "hero_title": "Twin prime conjecture explained",
        "hero_text": "The twin prime conjecture asks whether there are infinitely many pairs of prime numbers that differ by exactly 2. The statement is short enough to explain in one sentence. Proving it has turned out to be one of the most persistent open problems in number theory.",
        "intro_title": "The big question behind the site",
        "intro_text": "This page gives the cleanest nontechnical overview of the conjecture itself: the exact statement, what infinity means in this context, why the problem is so hard, what nearby progress has been proved, and what still remains outside theorem territory.",
        "reviewed": "Last reviewed: April 2026",
        "sections": [
            {
                "title": "What the conjecture says",
                "body": "The twin prime conjecture claims that there are infinitely many twin-prime pairs. A twin-prime pair is a pair of prime numbers with a gap of exactly 2, such as (11, 13), (17, 19), or (29, 31). The conjecture says that this exact gap-2 pattern never runs out permanently. It is not a claim about one long streak near the beginning of the number line. It is a claim about endless recurrence no matter how far you go.",
            },
            {
                "title": "What 'infinitely many' means here",
                "body": "Infinite does not mean that twin primes are common or evenly spaced. It means that no matter how far you go along the number line, there should still be more twin-prime pairs beyond that point. For example, if someone checked all twin primes below one million, the conjecture would still be asking whether more pairs exist above one million, above one billion, and beyond every other finite cutoff. The claim is about endless continuation, not regular frequency.",
            },
            {
                "title": "Why the conjecture sounds simpler than it is",
                "body": "The statement only mentions prime pairs separated by 2, but a proof would need to control infinitely many local divisibility constraints at once. Numbers that look promising can be ruined by divisibility by 3, 5, 7, or larger primes, and those obstructions interact across the whole number line. That is why the conjecture is harder than proving that primes never end, and harder than proving that some small gap recurs infinitely often without naming the exact gap 2.",
            },
            {
                "title": "What has been proved nearby",
                "body": "Modern results show that primes come within some bounded distance of each other infinitely often. Zhang's breakthrough, and the later Polymath and Maynard-Tao advances, prove that small prime gaps recur at arbitrarily large scales. This is major progress, but it is still weaker than proving that the exact gap of 2 occurs infinitely often. The difference between bounded gaps and twin primes is one of the most important distinctions on the site.",
            },
            {
                "title": "What has not been proved",
                "body": "No theorem currently proves that infinitely many gap-2 prime pairs exist. This is the key misconception to avoid. Seeing many twin primes in a finite range, or even proving that some bounded gap recurs infinitely often, does not settle the exact twin-prime conjecture. The conjecture remains open because the final step from 'some fixed gap' to 'the specific gap 2' has not been proved.",
            },
            {
                "title": "Why mathematicians still expect the conjecture to be true",
                "body": "The expectation comes from strong heuristics, statistical models, and enormous finite computation, not from a theorem that settles the conjecture. Twin primes appear often enough in practice to make endless continuation plausible, and conjectural models such as Hardy-Littlewood predict that they should keep appearing, although more rarely, as numbers grow. On this site that expectation is always treated as heuristic or conjectural, not as established theorem-level fact.",
            },
            {
                "title": "How this connects to the tools",
                "body": "The site cannot prove or disprove the conjecture, but it can help you see why the pattern is compelling and why finite evidence is not the same thing as a proof. The Lab makes gap-2 structure visible, Explorer lets you inspect concrete examples row by row, and Analysis summarizes how pairs, centers, and gaps behave in a chosen range. Theory and the Zhang page then connect those observations back to the larger mathematical story.",
            },
        ],
        "references": [
            {"label": "PrimePages: Twin Primes", "href": "https://primes.utm.edu/glossary/page.php?sort=TwinPrime", "note": "Concise reference on twin primes and the open conjecture."},
            {"label": "Yitang Zhang, Bounded gaps between primes", "href": "https://annals.math.princeton.edu/2014/179-3/p07", "note": "Primary theorem showing some bounded prime gap recurs infinitely often."},
            {"label": "Polymath8: bounded gaps between primes", "href": "https://michaelnielsen.org/polymath/index.php?title=Bounded_gaps_between_primes", "note": "Context for later bound improvements and current bounded-gap framing."},
        ],
        "related_links": [
            {"title": "Need the short answer?", "body": "Use the shorter page when you want a clean yes-or-no explanation before reading the larger conjecture context.", "href": "/has-the-twin-prime-conjecture-been-solved", "label": "Read the short answer"},
            {"title": "See the modern progress", "body": "The Zhang page explains the most famous modern theorem that moved the field forward without finishing the conjecture.", "href": "/what-did-yitang-zhang-prove", "label": "Read about Zhang"},
            {"title": "Compare the broader gap story", "body": "Use the prime-gaps page when you want the conjecture placed inside the larger language of prime spacing.", "href": "/prime-gaps", "label": "Read What Are Prime Gaps?"},
            {"title": "See the pattern in the Lab", "body": "Use the Lab when you want the conjecture tied back to visible structure.", "href": "/lab#visualization-title", "label": "Open the Lab"},
            {"title": "Inspect examples in Explorer", "body": "Explorer is the clearest place to move from the conjecture statement to concrete gap-2 pairs in a live range.", "href": "/explorer#number-table-title", "label": "Open Explorer"},
        ],
    },
    {
        "route": "/how-to-find-twin-primes",
        "nav_label": "How To Find Twin Primes",
        "title": "TwinPrimeExplorer.com | How To Find Twin Primes",
        "meta_description": "A fuller practical guide to finding twin primes, checking gap-2 pairs, avoiding false candidates, and using TwinPrimeExplorer.com to inspect the pattern.",
        "eyebrow": "Finding Twin Primes",
        "hero_title": "How to find twin primes",
        "hero_text": "Finding a twin-prime pair is straightforward in small ranges: look for two prime numbers that differ by exactly 2. The deeper challenge is learning which candidates are worth checking, which shortcuts are only filters, and how to move from quick spotting to real inspection.",
        "intro_title": "A practical pattern guide",
        "intro_text": "This page is about procedure rather than proof. It shows how to recognize twin-prime candidates, what quick filters help, where false candidates come from, and how the site's tools let you move from a simple search idea to richer structural inspection.",
        "reviewed": "Last reviewed: April 2026",
        "sections": [
            {
                "title": "Start with the definition",
                "body": "A twin-prime pair is a pair of primes with a gap of 2. So the simplest search method is: take a prime p, check whether p + 2 is also prime, and record the pair if it is. In small ranges this is enough to generate real examples quickly. If p equals 11 and p plus 2 equals 13, you have a twin-prime pair. If p equals 13 and p plus 2 equals 15, the pattern fails because 15 is composite.",
            },
            {
                "title": "Use prime lists and quick filters",
                "body": "In practice, people rarely test every whole number from scratch. They work from a list of primes or from candidates that have already passed small divisibility filters. That is why residue classes such as 1 and 5 mod 6 matter so much: they eliminate many impossible cases before you do deeper checking. A practical workflow is often: narrow the candidates quickly, then inspect the survivors more carefully.",
            },
            {
                "title": "Why Mod 6 helps but does not solve the problem",
                "body": "For primes greater than 3, only two residue classes mod 6 remain possible. That means a typical twin-prime pair above (3, 5) looks like (6k - 1, 6k + 1). This is a useful candidate pattern, not a proof that those numbers are prime. Modular filters tell you where to look, but primality still has to be checked. In other words, Mod 6 is a search shortcut, not a guarantee.",
            },
            {
                "title": "Common false candidates",
                "body": "Many numbers fit the right-looking shape and still fail. A pair can land in the correct residue classes and still contain a composite number with a nontrivial factor. For example, (35, 37) has the right-looking gap of 2, but 35 is composite. So does (77, 79), where 77 is composite even though the pair shape looks promising at first glance. That is why it helps to treat modular structure as a fast screening tool rather than as a guarantee.",
            },
            {
                "title": "What finding twin primes does and does not tell you",
                "body": "Finding examples is useful for building intuition, checking ranges, and understanding how twin-prime patterns appear in practice. But no matter how many examples you collect in finite ranges, you still have not proved that infinitely many twin-prime pairs exist. This is a good place to keep the difference between observing a pattern and proving an infinite statement clear.",
            },
            {
                "title": "How to do it on this site",
                "body": "Use Explorer when you want the most direct working surface: row-by-row values, prime roles, twin centers, and divisor details. Use the Lab when you want to scan visually first and notice likely clusters. Then move into Analysis if you want to understand how the examples you found fit into larger spacing or modular patterns. The Mod 6 page, prime-gaps page, and twin-prime page all help explain why the candidates you see behave the way they do.",
            },
        ],
        "references": [
            {"label": "MathWorld: Twin Primes", "href": "https://mathworld.wolfram.com/TwinPrimes.html", "note": "Definition, examples, and the 6n ? 1 pattern."},
            {"label": "Britannica: modular arithmetic", "href": "https://www.britannica.com/science/modular-arithmetic", "note": "Background for residue-based candidate filtering."},
            {"label": "Britannica: prime number", "href": "https://www.britannica.com/science/prime-number", "note": "Basic reference for primality checks and examples."},
        ],
        "related_links": [
            {"title": "Use Explorer for exact inspection", "body": "Explorer is the clearest place to test candidate pairs and inspect neighborhood roles one row at a time.", "href": "/explorer#number-table-title", "label": "Open Explorer"},
            {"title": "Need the residue-class shortcut?", "body": "Use the modular explainer if you want the residue filter idea in plain language first.", "href": "/why-mod-6-shows-up-so-often", "label": "Read Why Mod 6 Shows Up So Often"},
            {"title": "Step back to the twin-prime overview", "body": "The twin-primes page gives the larger mathematical context around the exact pattern you are trying to find.", "href": "/what-are-twin-primes", "label": "Read What Are Twin Primes?"},
            {"title": "Compare what you found in Analysis", "body": "Analysis helps connect the candidate-finding process to larger gap and density structure.", "href": "/analysis#analysis-views-title", "label": "Open Analysis"},
        ],
    },
    {
        "route": "/prime-gaps",
        "nav_label": "What Are Prime Gaps?",
        "title": "TwinPrimeExplorer.com | What Are Prime Gaps?",
        "meta_description": "A fuller introduction to prime gaps, including examples, why gaps tend to grow on average, why twin primes are the gap-2 case, and why bounded gaps matter.",
        "eyebrow": "Prime Gaps",
        "hero_title": "What are prime gaps?",
        "hero_text": "A prime gap is the difference between one prime number and the next. Some gaps are very small, some eventually become much larger, and the special case of gap 2 is exactly where twin primes live.",
        "intro_title": "A bridge concept for the site",
        "intro_text": "Prime gaps connect the site's basic prime pages to its deeper twin-prime and bounded-gap pages. This page explains the basic definition, shows how small and large gaps differ, and clarifies why bounded-gap theorems matter without overstating what they prove.",
        "reviewed": "Last reviewed: April 2026",
        "sections": [
            {
                "title": "The basic definition",
                "body": "If one prime is followed by the next prime, the difference between them is a prime gap. For example, the gap between 11 and 13 is 2, while the gap between 23 and 29 is 6. Later on, the gap between 89 and 97 is 8. Prime gaps measure spacing rather than primality itself, so they are one of the cleanest ways to talk about how primes are distributed along the number line. They let you ask not just whether primes exist, but how tightly or loosely they cluster as you move through larger ranges.",
            },
            {
                "title": "Small gaps and large gaps tell different stories",
                "body": "A small gap shows that two consecutive primes land unusually close together. A larger gap shows a longer stretch of composite numbers between one prime and the next. Both are important. A gap of 2 gives you twin primes, a gap of 4 or 6 still shows close clustering, and larger gaps remind you that prime spacing becomes increasingly uneven as numbers grow. Looking at both small and large gaps helps prevent the false idea that primes either stay close forever or spread out smoothly in a simple pattern.",
            },
            {
                "title": "Twin primes are the gap-2 case",
                "body": "Twin primes are the smallest nontrivial example of a prime-gap pattern. When two consecutive odd primes differ by 2, they form a twin-prime pair. Examples include (11, 13), (17, 19), and (29, 31). That is why studying prime gaps naturally leads to the twin prime conjecture: the conjecture is asking whether this smallest recurring odd-prime gap appears infinitely many times.",
            },
            {
                "title": "Why gaps tend to grow on average",
                "body": "As numbers get larger, primes become less frequent on average, so larger gaps become more common. This does not mean small gaps disappear forever. It means the overall spacing picture becomes more uneven. You should expect more room between many consecutive primes at large scales, while still allowing special close pairs to keep appearing here and there. On this site, that distinction matters because visible examples in a finite range are observations, not proofs about what must happen forever. The average trend toward larger gaps is real, but the local behavior remains jagged rather than smooth.",
            },
            {
                "title": "Why bounded gaps matter",
                "body": "A bounded-gap theorem says that some fixed finite prime gap occurs infinitely often. That is a powerful statement because it proves recurring close proximity between primes at arbitrarily large scales. Zhang's result and the work that followed show that primes do not drift apart without ever coming close again. But bounded gaps still do not settle the special gap-2 case. The theorem-level fact is that some bounded gap repeats infinitely often; the unproved conjectural claim is that the exact gap 2 also repeats infinitely often.",
            },
            {
                "title": "How this site lets you inspect gaps",
                "body": "Analysis is the best place to study gap structure directly because it summarizes repeated spacing across a chosen range. Explorer helps when you want exact examples and exact neighboring primes, while the Lab helps when you want to see clusters and separation before reading structured summaries. The twin-primes page, the Zhang page, and the conjecture page then connect those visible gap patterns back to the broader mathematical story.",
            },
        ],
        "references": [
            {"label": "MathWorld: Prime Gaps", "href": "https://mathworld.wolfram.com/PrimeGaps.html", "note": "Direct reference for prime-gap definitions and larger-gap context."},
            {"label": "Yitang Zhang, Bounded gaps between primes", "href": "https://annals.math.princeton.edu/2014/179-3/p07", "note": "Primary bounded-gaps theorem."},
            {"label": "Britannica: prime number theorem", "href": "https://www.britannica.com/science/number-theory/Prime-number-theorem", "note": "Average-density background for why gaps grow on average."},
        ],
        "related_links": [
            {"title": "Start with the gap-2 case", "body": "Use the twin-primes page when you want the special gap-2 pattern explained before the broader gap story.", "href": "/what-are-twin-primes", "label": "Read What Are Twin Primes?"},
            {"title": "Read the bounded-gap breakthrough", "body": "The Zhang page explains how modern theorems turned small prime gaps into a proof-level result.", "href": "/what-did-yitang-zhang-prove", "label": "Read about Zhang"},
            {"title": "Follow the larger open question", "body": "Use the conjecture page when you want the exact difference between bounded gaps and the twin-prime conjecture spelled out clearly.", "href": "/twin-prime-conjecture", "label": "Read Twin Prime Conjecture Explained"},
            {"title": "Inspect gaps in Analysis", "body": "The Analysis page is the clearest place to compare spacing patterns in a live range.", "href": "/analysis#analysis-views-title", "label": "Open Analysis"},
            {"title": "See the range visually first", "body": "Use the Lab when you want the spacing story tied back to a visual range before opening structured summaries.", "href": "/lab#visualization-title", "label": "Open the Lab"},
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
        "reviewed": "Last reviewed: April 2026",
        "sections": [
            {
                "title": "The basic definition",
                "body": "A twin-prime pair is a pair of prime numbers with a difference of 2, such as (3, 5), (5, 7), or (11, 13). Once numbers get larger, twin primes become less frequent, but they continue to appear in many finite ranges. In that sense, twin primes are both easy to define and easy to observe locally, which is part of why they are so inviting as an entry point into deeper number theory.",
            },
            {
                "title": "Why gap 2 matters",
                "body": "A gap of 2 is the smallest possible gap between odd prime numbers. That makes twin primes the simplest nontrivial prime-gap pattern, and it is one reason they sit so close to the center of prime-number research. The prime-gaps page broadens that same idea by asking how far apart consecutive primes are in general, while the twin-prime story focuses on the most tightly packed odd-prime case.",
            },
            {
                "title": "The early exception and the usual pattern",
                "body": "The pair (3, 5) is a special early case because it includes the only odd prime that is also divisible by 3. After that, twin-prime pairs typically look like (6k - 1, 6k + 1). This does not force a number to be prime, but it explains why Mod 6 keeps appearing in twin-prime discussions and why the middle value, the twin center, usually lands on a multiple of 6.",
            },
            {
                "title": "Why twin centers help",
                "body": "Instead of tracking a pair as two separate primes, the site often highlights the number in the middle. If (p, p + 2) is a twin-prime pair, then p + 1 is its twin center. This compression makes it easier to count, visualize, and compare twin-prime structure across a range, especially in the Lab and the Analysis views. It is one of the clearest examples of how the site turns the same mathematics into a more readable structure.",
            },
            {
                "title": "Why people care about them",
                "body": "The twin prime conjecture asks whether infinitely many twin-prime pairs exist. That question is still open. The pattern is easy to understand, but proving it continues forever is much harder than finding many examples. That contrast between visible finite evidence and a missing infinite proof is exactly what makes twin primes so educationally rich.",
            },
            {
                "title": "What is known and what is still conjectured",
                "body": "Some important facts are already proven. Brun's theorem shows that twin primes are sparse enough that the sum of their reciprocals converges, and bounded-gap results show that primes come within some fixed finite distance infinitely often. But neither of those results proves that gap 2 itself repeats forever. The expectation that infinitely many twin primes exist comes from strong heuristics and extensive computation, not from a theorem that settles the conjecture. This is why the conjecture page, the short solved-or-not page, and the bounded-gap pages all sit close to this one in the site's reading path.",
            },
            {
                "title": "How to explore twin primes on this site",
                "body": "TwinPrimeExplorer.com treats twin primes as something you can see, inspect, and interpret from several angles. Open the Lab when you want the pattern field first, especially with twin centers and Mod 6 structure visible at the same time. Use Explorer when you want exact examples row by row. Use Analysis when you want modular summaries, spacing behavior, density, and a rough expected-count benchmark. Use Theory when you want the broader research story around the same pattern. A useful next step after this page is often to compare the visible gap-2 pattern in the tools with the more careful theorem-versus-conjecture language on the conjecture and Zhang pages.",
            },
        ],
        "references": [
            {"label": "MathWorld: Twin Primes", "href": "https://mathworld.wolfram.com/TwinPrimes.html", "note": "Definition, examples, and 6n ? 1 structure."},
            {"label": "MathWorld: Twin Prime Conjecture", "href": "https://mathworld.wolfram.com/TwinPrimeConjecture.html", "note": "Reference for the open conjecture status."},
            {"label": "Yitang Zhang, Bounded gaps between primes", "href": "https://annals.math.princeton.edu/2014/179-3/p07", "note": "Nearby theorem-level progress that still stops short of gap 2."},
        ],
        "related_links": [
            {"title": "See the pattern in the Lab", "body": "Start with a live range and watch twin primes and twin centers appear together.", "href": "/lab#visualization-title", "label": "Open the Lab"},
            {"title": "Inspect exact examples in Explorer", "body": "Use row-by-row inspection when you want to move from the definition to concrete cases.", "href": "/explorer#number-table-title", "label": "Open Explorer"},
            {"title": "Interpret the pattern in Analysis", "body": "Analysis connects the same idea to modular structure, pair spacing, and local density.", "href": "/analysis#analysis-views-title", "label": "Open Analysis"},
            {"title": "Step back to prime gaps", "body": "Use the prime-gaps page when you want the broader spacing language that surrounds the special gap-2 case.", "href": "/prime-gaps", "label": "Read What Are Prime Gaps?"},
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
        "reviewed": "Last reviewed: April 2026",
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
                "body": "The theorem showed that prime clustering is not just a heuristic expectation. It established that small prime gaps recur across infinitely many scales, which is one of the strongest pieces of progress connected to the twin prime problem.",
            },
            {
                "title": "How to see the idea in TwinPrimeExplorer",
                "body": "The site cannot reproduce the proof, but it can help you build intuition for what bounded gaps are about. In Analysis, the Gaps tab lets you inspect repeated small spacings in a selected range. In the Lab, you can watch clusters of twin-prime candidates and centers appear rather than treating prime gaps as an abstract theorem statement. That shift from theorem language to visible structure is exactly why this page belongs next to the tools.",
            },
        ],
        "references": [
            {"label": "Yitang Zhang, Bounded gaps between primes", "href": "https://annals.math.princeton.edu/2014/179-3/p07", "note": "Primary source for the original bounded-gaps theorem."},
            {"label": "James Maynard, Small gaps between primes", "href": "https://annals.math.princeton.edu/2015/181-1/p07", "note": "Major follow-on theorem that broadened the bounded-gaps picture."},
            {"label": "Polymath8: bounded gaps between primes", "href": "https://michaelnielsen.org/polymath/index.php?title=Bounded_gaps_between_primes", "note": "Collaborative retrospective and bound-improvement timeline."},
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
        "reviewed": "Last reviewed: April 2026",
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
                "title": "Why this is a filter rather than a proof",
                "body": "The mod-6 pattern tells you where prime candidates can survive once divisibility by 2 and 3 is removed. It does not tell you that every number in those residue classes is prime. Numbers such as 25 and 35 sit in allowed residue classes and are still composite. That is why modular structure helps narrow the search without settling it.",
            },
            {
                "title": "Why twin centers make the same pattern easier to see",
                "body": "If a twin-prime pair looks like (6k - 1, 6k + 1), then the number in the middle is 6k. That is why twin centers so often land on multiples of 6. The center compresses the pair into one visual anchor, which makes the same modular story easier to scan in the Lab and easier to summarize in Analysis.",
            },
            {
                "title": "Why the site highlights it",
                "body": "Mod 6 is one of the fastest ways to move from raw numbers to visible structure. The Lab uses it as a visual mode, Analysis uses it as a structural read, and the Glossary keeps the key terms short when you do not want a longer explanation.",
            },
            {
                "title": "How to read this pattern on the site",
                "body": "Use the Lab when you want the quickest visual impression of how residue classes narrow the field. Use Analysis when you want counts and summaries for the same structure. Use the Glossary when you only need short definitions for modulus, residue class, or arithmetic progression instead of a fuller article.",
            },
        ],
        "references": [
            {"label": "Britannica: modular arithmetic", "href": "https://www.britannica.com/science/modular-arithmetic", "note": "Background for residues and congruence classes."},
            {"label": "MathWorld: Twin Primes", "href": "https://mathworld.wolfram.com/TwinPrimes.html", "note": "Reference for the 6n ? 1 twin-prime pattern above (3, 5)."},
            {"label": "Britannica: prime number", "href": "https://www.britannica.com/science/prime-number", "note": "General prime-number background for the filtering discussion."},
        ],
        "related_links": [
            {"title": "See it in the Lab", "body": "Use the Mod 6 view to see the residue pattern rather than only reading about it.", "href": "/lab#visualization-title", "label": "Open the Lab"},
            {"title": "Read the modular interpretation", "body": "Analysis summarizes the pair and center residue counts across the selected range, so you can compare the article idea with live data.", "href": "/analysis#analysis-views-title", "label": "Open Analysis"},
            {"title": "Keep the terms nearby", "body": "Use the Glossary for Mod 6, residue class, and arithmetic progression definitions.", "href": "/glossary#glossary-term-mod-6", "label": "Open the Glossary"},
            {"title": "Connect the pattern to candidate finding", "body": "The finding guide shows how residue-class filters help you search for likely twin-prime candidates.", "href": "/how-to-find-twin-primes", "label": "Read How To Find Twin Primes"},
        ],
    },
    {
        "route": "/why-twin-centers-matter",
        "nav_label": "Why Twin Centers Matter",
        "title": "TwinPrimeExplorer.com | Why Twin Centers Matter",
        "meta_description": "A fuller explanation of why twin centers are useful for seeing, organizing, and interpreting twin-prime structure across the site.",
        "eyebrow": "Twin Centers",
        "hero_title": "Why twin centers matter",
        "hero_text": "Twin centers are the numbers exactly between twin-prime pairs. They are not prime themselves, but they often make the surrounding pair structure easier to see, compare, and talk about.",
        "intro_title": "Why this page exists",
        "intro_text": "Twin centers are one of the site's distinctive ideas. This page explains why they are useful without turning them into a bigger theory than they need to be, and why the midpoint can sometimes be the clearest way to study the same twin-prime pattern.",
        "reviewed": "Last reviewed: April 2026",
        "sections": [
            {
                "title": "What a twin center is",
                "body": "If (p, p + 2) is a twin-prime pair, then the number in the middle is p + 1. That middle value is the twin center. For example, 12 is the twin center between 11 and 13, and 30 is the twin center between 29 and 31.",
            },
            {
                "title": "Why the center is useful",
                "body": "The center compresses a pair into one location. That makes it easier to see where twin-prime structure sits inside a larger range, especially when you want a visual or counting-based summary rather than only a list of pairs. One midpoint is often easier to track across a display than two separate prime endpoints.",
            },
            {
                "title": "Why centers are a structural shortcut",
                "body": "A twin-prime pair occupies two prime positions, but its center gives you one even position to track instead. That makes centers a practical shortcut for counting and mapping the pattern. When a site or article talks about center counts, center gaps, or center factors, it is not changing the mathematics of twin primes. It is choosing the cleaner coordinate system for the same pattern.",
            },
            {
                "title": "Why centers connect naturally to mod 6",
                "body": "For twin-prime pairs above the earliest exceptions, the center typically lands on a multiple of 6. That makes centers a clean bridge between the visual pattern and the modular explanation. If a pair looks like (6k - 1, 6k + 1), the center is simply 6k, so the midpoint carries the residue-class story in one number.",
            },
            {
                "title": "Why centers help with comparison",
                "body": "Centers make it easier to compare one twin-prime occurrence with another because they behave like single marked points across the number line. That is useful when you want to compare spacing between occurrences, local neighborhoods around occurrences, or factorization patterns of the even numbers that sit between twin primes. In practice, center-to-center comparisons can be easier to scan than left-prime-to-left-prime or pair-to-pair comparisons.",
            },
            {
                "title": "How the site uses centers",
                "body": "The Lab highlights centers visually, Explorer treats them as a neighborhood role, and Analysis uses them for factor and modular summaries. They are not a replacement for the primes themselves, but they are often the fastest way to see the structure they create. This is especially helpful when the same pair pattern needs to be summarized repeatedly across one selected range.",
            },
            {
                "title": "Why this matters for readers and not just for the UI",
                "body": "Twin centers help translate a two-number pattern into a simpler explanatory story. Instead of repeatedly saying 'the prime on the left and the prime on the right,' you can talk about the midpoint that ties the pair together. That makes the visual, structural, and explanatory layers of the site line up more naturally, which is exactly why twin centers are worth treating as a concept rather than only as a display convenience.",
            },
        ],
        "references": [
            {"label": "MathWorld: Twin Primes", "href": "https://mathworld.wolfram.com/TwinPrimes.html", "note": "Supports the gap-2 pair structure summarized by twin centers."},
            {"label": "Britannica: modular arithmetic", "href": "https://www.britannica.com/science/modular-arithmetic", "note": "Background for the midpoint and residue-class discussion."},
            {"label": "MathWorld: Twin Prime Conjecture", "href": "https://mathworld.wolfram.com/TwinPrimeConjecture.html", "note": "Broader context for why the pair pattern matters mathematically."},
        ],
        "related_links": [
            {"title": "See twin centers visually", "body": "The Lab makes centers easy to spot inside a live number field.", "href": "/lab#visualization-title", "label": "Open the Lab"},
            {"title": "Inspect exact center rows", "body": "Explorer shows the number-by-number detail behind each center and its neighbors.", "href": "/explorer#number-table-title", "label": "Open Explorer"},
            {"title": "Connect centers to the twin-prime overview", "body": "The twin-primes page explains the pair pattern that the center is summarizing.", "href": "/what-are-twin-primes", "label": "Read What Are Twin Primes?"},
            {"title": "Connect centers to reference context", "body": "Use the Glossary for the short definition first, then move into Theory when you want the broader twin-prime context.", "href": "/glossary#glossary-term-twin-center", "label": "Open the Glossary"},
            {"title": "Tie centers back to Mod 6", "body": "The modular explainer shows why centers and multiples of 6 keep appearing together in the same story.", "href": "/why-mod-6-shows-up-so-often", "label": "Read Why Mod 6 Shows Up So Often"},
        ],
    },
    {
        "route": "/has-the-twin-prime-conjecture-been-solved",
        "nav_label": "Has The Twin Prime Conjecture Been Solved?",
        "title": "TwinPrimeExplorer.com | Has The Twin Prime Conjecture Been Solved?",
        "meta_description": "A clearer short-answer explanation of whether the twin prime conjecture has been solved, what people often misunderstand, and how bounded-gap progress differs from a full proof.",
        "eyebrow": "Twin Prime Conjecture",
        "hero_title": "Has the twin prime conjecture been solved?",
        "hero_text": "No. The twin prime conjecture remains unsolved. Modern progress shows that primes come within some bounded distance infinitely often, but that is not the same as proving infinitely many gap-2 pairs.",
        "intro_title": "The short answer",
        "intro_text": "If you only need the answer in one line, it is no. This page exists to make the next sentence clear too: important progress has happened, but the exact twin-prime claim still has not been proved, and that last distinction is where many summaries become misleading.",
        "reviewed": "Last reviewed: April 2026",
        "sections": [
            {
                "title": "What the conjecture actually says",
                "body": "The twin prime conjecture claims that there are infinitely many pairs of prime numbers that differ by exactly 2. It is not a claim about small gaps in general. It is a claim about the exact gap of 2 repeating forever, no matter how far out on the number line you go.",
            },
            {
                "title": "Why people sometimes think it was solved",
                "body": "News about bounded gaps between primes can sound very close to the twin prime conjecture. If you hear that primes come close together infinitely often, it is easy to assume that twin primes were proved too. That last step is exactly the part that remains open. The misunderstanding usually comes from replacing the word exact with the word close, even though those two ideas are not interchangeable in a theorem statement.",
            },
            {
                "title": "What modern results do prove",
                "body": "Modern theorems show that there exists some fixed finite bound B such that infinitely many prime pairs differ by at most B. That is a major breakthrough, because it proves recurring small gaps. But the bound is not known to be 2. A useful comparison is this: proving that some gap inside a bounded range keeps returning is already a theorem, while proving that the particular gap 2 returns infinitely often is still open.",
            },
            {
                "title": "Why the distinction matters",
                "body": "This is one of the clearest examples in number theory of progress versus proof. The field has moved much closer to the conjecture, but the exact statement mathematicians want to prove is still unresolved. Finite examples, large computations, and bounded-gap theorems all matter, but none of them by themselves complete the final argument for infinitely many twin primes.",
            },
            {
                "title": "Where to go after the short answer",
                "body": "If you want the longer explanation of the open problem itself, move next to Twin Prime Conjecture Explained. If you want the best-known modern breakthrough nearby, go to the Zhang page. If you want to see why the distinction between finite evidence and proof matters visually, open the Lab or Analysis and compare what a real finite range can show with what a theorem about infinity would need to establish.",
            },
        ],
        "references": [
            {"label": "MathWorld: Twin Prime Conjecture", "href": "https://mathworld.wolfram.com/TwinPrimeConjecture.html", "note": "Direct reference that the conjecture remains open."},
            {"label": "Yitang Zhang, Bounded gaps between primes", "href": "https://annals.math.princeton.edu/2014/179-3/p07", "note": "Primary source for nearby bounded-gap progress."},
            {"label": "Polymath8: bounded gaps between primes", "href": "https://michaelnielsen.org/polymath/index.php?title=Bounded_gaps_between_primes", "note": "Helpful context for why bounded gaps still does not mean gap 2."},
        ],
        "related_links": [
            {"title": "Read the full conjecture page", "body": "Use the longer conjecture explainer when you want the exact statement, what infinity means here, and what remains unproved.", "href": "/twin-prime-conjecture", "label": "Read Twin Prime Conjecture Explained"},
            {"title": "Read the bounded-gap breakthrough", "body": "Use the Zhang page when you want the cleanest explanation of what bounded gaps actually proved.", "href": "/what-did-yitang-zhang-prove", "label": "Read about Zhang"},
            {"title": "See the current progress summary", "body": "Theory collects the larger progress picture in one place.", "href": "/theory#progress", "label": "Open Theory: Current Progress"},
            {"title": "See the pattern in a live range", "body": "The Lab helps connect the short answer back to visible gap-2 examples without confusing finite evidence with proof.", "href": "/lab#visualization-title", "label": "Open the Lab"},
        ],
    },
    {
        "route": "/what-bounded-gaps-between-primes-actually-proved",
        "nav_label": "What Bounded Gaps Between Primes Actually Proved",
        "title": "TwinPrimeExplorer.com | What Bounded Gaps Between Primes Actually Proved",
        "meta_description": "A fuller explanation of what bounded gaps between primes really proved, why it matters, and why it still stops short of proving infinitely many twin primes.",
        "eyebrow": "Bounded Gaps",
        "hero_title": "What bounded gaps between primes actually proved",
        "hero_text": "Bounded-gap results proved that primes come within some fixed finite distance infinitely often. That is a major structural theorem about prime clustering, but it is still not the same as proving infinitely many twin primes.",
        "intro_title": "Why this page helps",
        "intro_text": "Bounded gaps is one of the most important phrases in the modern twin-prime story, but it is also one of the easiest to blur into something it does not say. This page keeps the claim precise and connects it back to the broader conjecture and gap story.",
        "reviewed": "Last reviewed: April 2026",
        "sections": [
            {
                "title": "What bounded gaps means",
                "body": "A bounded-gap theorem says there is some fixed number B so that infinitely many prime pairs differ by at most B. The key point is that the same finite bound works infinitely often. This is already much stronger than merely observing many small gaps in computation, because it is a theorem about endless recurrence rather than a pattern in one large checked range.",
            },
            {
                "title": "What the breakthrough changed",
                "body": "Before these results, it was not known whether primes could be proved to recur within any fixed finite distance infinitely many times. The breakthrough turned that possibility into a theorem and changed how mathematicians talk about small prime gaps. It moved the conversation from heuristic expectation to theorem-level progress on a nearby version of the twin-prime problem.",
            },
            {
                "title": "What the theorem does and does not name",
                "body": "A bounded-gap theorem does not identify one exact gap and say that it repeats forever. It proves that at least one finite gap inside a bounded range repeats infinitely many times. That is a strong structural claim, but it leaves open which specific gaps are doing the work. The distinction between some bounded gap and the exact gap 2 is the center of the whole interpretation problem.",
            },
            {
                "title": "Why it still falls short of twin primes",
                "body": "Twin primes require the exact gap of 2. Bounded-gap theorems only prove that some finite bound works. Even if that bound is much smaller than earlier ones, it is still not the same as isolating the exact twin-prime pattern. This is why people say bounded gaps is very close to the twin-prime conjecture without saying it solves it.",
            },
            {
                "title": "Why people understandably blur the distinction",
                "body": "From a distance, 'primes come very close together infinitely often' sounds almost identical to 'twin primes happen infinitely often.' The difference only becomes clear when you focus on the word exact. Twin primes ask for one exact gap. Bounded-gap theorems prove repeated small proximity without pinning the answer down to 2. That one missing step is exactly where the conjecture still remains open.",
            },
            {
                "title": "Why the result still matters so much",
                "body": "These theorems prove that local prime clustering is a real structural phenomenon, not just something suggested by computations or heuristics. That is why bounded gaps sits so close to the center of the modern twin-prime story. It shows that primes do keep returning near one another in a provable way, even if the final gap-2 statement is still beyond reach.",
            },
            {
                "title": "How this page fits with the rest of the site",
                "body": "This page works best as a precision tool. Use it when headlines or summaries make progress sound closer to a completed proof than it really is. Then move back to the twin-prime conjecture page, the Zhang page, Theory, or the prime-gaps page to place the bounded-gap statement inside the larger research story. Analysis can then help you compare the explanatory idea with real spacing patterns in a chosen finite range.",
            },
        ],
        "references": [
            {"label": "Yitang Zhang, Bounded gaps between primes", "href": "https://annals.math.princeton.edu/2014/179-3/p07", "note": "Original bounded-gaps theorem."},
            {"label": "James Maynard, Small gaps between primes", "href": "https://annals.math.princeton.edu/2015/181-1/p07", "note": "Follow-on bounded-gaps breakthrough."},
            {"label": "Polymath8: bounded gaps between primes", "href": "https://michaelnielsen.org/polymath/index.php?title=Bounded_gaps_between_primes", "note": "Bound-improvement context and current best-known range story."},
        ],
        "related_links": [
            {"title": "Read the Zhang milestone", "body": "Use the Zhang page when you want the breakthrough framed around the person and the 2013 result.", "href": "/what-did-yitang-zhang-prove", "label": "Read about Zhang"},
            {"title": "See how Theory summarizes the progress", "body": "The Current Progress tab keeps the wider bounded-gap picture connected to the conjecture itself.", "href": "/theory#progress", "label": "Open Theory: Current Progress"},
            {"title": "Compare bounded gaps to the conjecture", "body": "The conjecture page keeps the exact gap-2 question separate from nearby theorem progress.", "href": "/twin-prime-conjecture", "label": "Read Twin Prime Conjecture Explained"},
            {"title": "See Chen's theorem as another near miss", "body": "Chen's theorem is another major theorem-level result that gets very close to twin primes without proving them.", "href": "/chens-theorem", "label": "Read Chen's Theorem Explained"},
            {"title": "Use Analysis for gap structure", "body": "Analysis lets you compare the article idea with gap patterns in a concrete finite range.", "href": "/analysis#analysis-views-title", "label": "Open Analysis"},
            {"title": "Step back to the broader gap story", "body": "The prime-gaps page gives the larger spacing framework around the bounded-gap breakthrough.", "href": "/prime-gaps", "label": "Read What Are Prime Gaps?"},
        ],
    },
    {
        "route": "/why-the-twin-prime-problem-is-hard",
        "nav_label": "Why The Twin Prime Problem Is Hard",
        "title": "TwinPrimeExplorer.com | Why The Twin Prime Problem Is Hard",
        "meta_description": "Why the twin prime problem is difficult, including the gap between finite evidence and proof, exact gap-2 control, local divisibility constraints, and the limits of current methods.",
        "eyebrow": "Why It Is Hard",
        "hero_title": "Why the twin prime problem is hard",
        "hero_text": "The twin prime problem sounds simple because the statement is short. The difficulty is that any proof has to control both the large-scale distribution of primes and the exact local conditions that produce gap-2 pairs.",
        "intro_title": "The short version",
        "intro_text": "This problem is hard because primes look partly irregular but obey strict arithmetic rules at the same time. A proof has to manage both sides at once, and it has to do so across infinitely many scales rather than just inside a large computed range.",
        "reviewed": "Last reviewed: April 2026",
        "sections": [
            {
                "title": "Exact gaps are harder than small gaps",
                "body": "It is one thing to prove that primes come close together infinitely often. It is a stronger and more delicate task to prove that the exact gap of 2 occurs infinitely often. That extra precision is where current methods still fall short. Bounded-gap theorems tell you that some fixed small distance returns forever. The twin prime conjecture asks for one exact distance and will not accept a near miss.",
            },
            {
                "title": "Divisibility constraints pile up",
                "body": "For a twin-prime pair (p, p+2), both numbers must avoid divisibility by many small primes at the same time. Those restrictions overlap and accumulate, which makes the local arithmetic much harder to control than the primality of a single number. A simple example is the usual 6k minus 1 and 6k plus 1 pattern: it filters out many impossible cases quickly, but it still leaves lots of composites behind. The real proof problem begins after the easy residue-class filtering has already been done.",
            },
            {
                "title": "Finite evidence is not the same as an infinite proof",
                "body": "A computer can find many twin-prime pairs in huge ranges, and those examples are genuinely interesting. But every computation ends at a finite cutoff. The conjecture asks what happens beyond every finite limit. That is why a million examples, a billion examples, or even vastly larger searches still do not by themselves produce a proof that infinitely many gap-2 pairs exist.",
            },
            {
                "title": "Average information is not enough",
                "body": "Modern methods often describe how primes behave on average or across large scales. The twin prime problem needs more than that. It asks for infinitely many exact local alignments, not just broad tendencies. Knowing that primes are well distributed on average is valuable, but it does not automatically force the exact local pairing needed for infinitely many twin primes.",
            },
            {
                "title": "Why distribution results still matter",
                "body": "Even though average distribution results are not enough by themselves, they are still part of the path forward. Progress on primes in arithmetic progressions, sieve methods, and bounded gaps all improves how much control mathematicians have over prime behavior. That is why the conjecture page, the Zhang page, and the Theory overview belong next to this page: they show which pieces of the larger puzzle have moved and which part remains unsolved.",
            },
            {
                "title": "How this fits with the rest of the site",
                "body": "Use this page when the conjecture seems easy to state but mysteriously hard to finish. Then move to Twin Prime Conjecture Explained for the clean statement of the problem, to the Zhang page for the biggest nearby theorem, or to Explorer and Analysis if you want to compare theorem language with concrete local patterns in a chosen range.",
            },
        ],
        "references": [
            {"label": "MathWorld: Twin Prime Conjecture", "href": "https://mathworld.wolfram.com/TwinPrimeConjecture.html", "note": "Reference for the exact conjecture that remains open."},
            {"label": "Yitang Zhang, Bounded gaps between primes", "href": "https://annals.math.princeton.edu/2014/179-3/p07", "note": "Shows the strongest nearby theorem-level progress."},
            {"label": "James Maynard, Small gaps between primes", "href": "https://annals.math.princeton.edu/2015/181-1/p07", "note": "Follow-on bounded-gaps context for the modern difficulty discussion."},
        ],
        "related_links": [
            {"title": "Read the conjecture page", "body": "The full conjecture explainer gives the clearest statement of the exact gap-2 claim this page is discussing.", "href": "/twin-prime-conjecture", "label": "Read Twin Prime Conjecture Explained"},
            {"title": "See the nearby theorem", "body": "The Zhang page shows what modern mathematics did manage to prove without finishing the twin prime problem.", "href": "/what-did-yitang-zhang-prove", "label": "Read about Zhang"},
            {"title": "Read the Theory summary", "body": "Theory keeps the full difficulty story connected to the rest of the conjecture context.", "href": "/theory#why-its-hard", "label": "Open Theory: Why It's Hard"},
            {"title": "Inspect local arithmetic in Explorer", "body": "Explorer helps make divisibility and neighborhood structure concrete one row at a time.", "href": "/explorer#number-table-title", "label": "Open Explorer"},
            {"title": "Compare patterns in Analysis", "body": "Analysis helps connect the idea of local patterns and repeated small gaps to a real finite range.", "href": "/analysis#analysis-views-title", "label": "Open Analysis"},
        ],
    },
    {
        "route": "/how-mathematicians-study-twin-primes",
        "nav_label": "How Mathematicians Study Twin Primes",
        "title": "TwinPrimeExplorer.com | How Mathematicians Study Twin Primes",
        "meta_description": "A fuller overview of how mathematicians study twin primes through sieve methods, analytic number theory, arithmetic progressions, heuristics, computation, and bounded-gap work.",
        "eyebrow": "Approaches",
        "hero_title": "How mathematicians study twin primes",
        "hero_text": "There is no single method that solves the twin prime problem. Instead, mathematicians approach it from several angles, each of which captures part of the structure but not yet the final proof.",
        "intro_title": "Why there are several approaches",
        "intro_text": "The twin prime problem sits at the intersection of local arithmetic structure, global distribution, and repeated small gaps. That is why different methods each illuminate a different part of the picture.",
        "reviewed": "Last reviewed: April 2026",
        "sections": [
            {
                "title": "Sieve methods",
                "body": "Sieve methods filter large sets of integers by divisibility conditions. They are powerful for finding numbers that behave almost like primes and for proving bounded-gap style results, but they run into the parity barrier before reaching a full twin-prime proof. In rough terms, sieves are very good at narrowing the field and detecting prime-like structure, but they struggle to separate an exact two-prime pattern from nearby almost-prime behavior with enough strength to finish the problem.",
            },
            {
                "title": "Analytic number theory",
                "body": "Analytic methods study primes through functions, asymptotic estimates, and large-scale distribution patterns. They reveal deep structure, but often at the level of averages rather than exact local pair formation. This is one reason the twin prime problem is so difficult: the subject needs both broad distribution information and exact local pair control at the same time.",
            },
            {
                "title": "Primes in arithmetic progressions",
                "body": "Modular structure matters because primes must land in certain residue classes to avoid small divisors. Studying primes in arithmetic progressions helps explain why patterns like mod 6 keep reappearing in twin-prime discussions. It also connects the problem to deeper questions about how evenly primes distribute across allowed residue classes as numbers grow.",
            },
            {
                "title": "Heuristics and computation",
                "body": "Heuristic models predict that twin primes should continue forever, and computation gives large-scale evidence for those predictions. For example, heuristic models suggest the twin-prime pattern should keep recurring with a predictable long-run density trend, while computation shows enormous finite examples where the pattern persists. Both are valuable, but neither replaces a proof.",
            },
            {
                "title": "Bounded-gap work",
                "body": "Bounded-gap methods sit especially close to the twin-prime problem because they prove that some fixed small prime gap recurs infinitely often. Zhang, Polymath, and Maynard-Tao did not settle gap 2, but they showed that prime clustering can be captured at theorem strength. That is why bounded-gap results are both a separate achievement and part of the larger twin-prime story.",
            },
            {
                "title": "Why several methods are needed at once",
                "body": "The twin prime problem sits between local arithmetic and global distribution. One method may explain divisibility filters, another may control average spacing, and another may predict long-run frequency. Mathematicians keep several approaches in play because no single method currently captures all of those demands at proof strength.",
            },
            {
                "title": "What progress looks like in practice",
                "body": "Progress does not always mean getting directly to gap 2. Sometimes it means improving how well primes can be controlled in arithmetic progressions. Sometimes it means proving bounded-gap results. Sometimes it means turning a heuristic expectation into a theorem about a nearby phenomenon. That is why the modern story of twin primes is full of partial advances that are still genuinely important.",
            },
            {
                "title": "How this helps a reader use the site better",
                "body": "This page is most useful when the site starts mentioning sieve methods, bounded gaps, heuristics, or modular structure and you want a compact overview of how those ideas fit together. It gives enough orientation that the Theory page, Zhang page, and conjecture page feel connected rather than like isolated references. Once the method names stop feeling abstract, the rest of the site's research and progress pages become much easier to follow.",
            },
        ],
        "references": [
            {"label": "Yitang Zhang, Bounded gaps between primes", "href": "https://annals.math.princeton.edu/2014/179-3/p07", "note": "Primary bounded-gaps source."},
            {"label": "James Maynard, Small gaps between primes", "href": "https://annals.math.princeton.edu/2015/181-1/p07", "note": "Major follow-on theorem in the modern methods story."},
            {"label": "Hardy and Littlewood, Some Problems of Partitio Numerorum (V)", "href": "https://academic.oup.com/plms/article-pdf/s2-22/1/46/4372641/s2-22-1-46.pdf", "note": "Classic heuristic framework behind prime-pair expectations."},
        ],
        "related_links": [
            {"title": "Read the Theory approaches tab", "body": "Theory keeps the method-level overview together in one reference surface.", "href": "/theory#approaches", "label": "Open Theory: Approaches"},
            {"title": "Follow the progress story", "body": "The Zhang page shows what one of the biggest modern advances looked like in theorem form.", "href": "/what-did-yitang-zhang-prove", "label": "Read about Zhang"},
            {"title": "See Mod 6 in the Lab", "body": "Use the visual mode that makes arithmetic-progression structure easier to spot quickly.", "href": "/lab#visualization-title", "label": "Open the Lab"},
            {"title": "Read the modular explainer", "body": "Use the standalone Mod 6 page when you want the shortest clear explanation of why residue classes matter here.", "href": "/why-mod-6-shows-up-so-often", "label": "Read the Mod 6 page"},
            {"title": "Go deeper into arithmetic progressions", "body": "This background page explains why residue classes and arithmetic progressions matter beyond the quick Mod 6 shortcut.", "href": "/arithmetic-progressions-primes", "label": "Read Arithmetic Progressions Explained For Prime Patterns"},
            {"title": "Compare methods with the conjecture itself", "body": "The conjecture page gives the cleanest statement of the problem these methods are trying to solve.", "href": "/twin-prime-conjecture", "label": "Read Twin Prime Conjecture Explained"},
            {"title": "See the difficulty summary", "body": "Use the difficulty page when you want the gap between these methods and a finished proof stated directly.", "href": "/why-the-twin-prime-problem-is-hard", "label": "Read Why The Twin Prime Problem Is Hard"},
        ],
    },
    {
        "route": "/prime-number-theorem",
        "nav_label": "The Prime Number Theorem In Plain Language",
        "title": "TwinPrimeExplorer.com | The Prime Number Theorem In Plain Language",
        "meta_description": "A plain-language explanation of the prime number theorem, why primes thin out on average, and how this connects to expected counts on TwinPrimeExplorer.com.",
        "eyebrow": "Prime Distribution",
        "hero_title": "The prime number theorem in plain language",
        "hero_text": "The prime number theorem explains the average large-scale behavior of primes. It does not tell you exactly where the next prime will appear, but it does explain why primes thin out as numbers grow.",
        "intro_title": "What this theorem is really about",
        "intro_text": "This page gives a plain-language version of one of the central background results in number theory. The theorem describes the average density of prime numbers, which helps explain why large gaps become more common, why logarithms keep appearing in prime discussions, and why the site's expected-count language is framed as an average guide rather than an exact rule.",
        "reviewed": "Last reviewed: April 2026",
        "sections": [
            {
                "title": "What the prime number theorem says",
                "body": "In rough language, the prime number theorem says that primes become less common in a predictable average way as numbers grow. More precisely, the number of primes up to a large number N is approximately N divided by log N. The theorem is not telling you that every block of numbers contains exactly that many primes. It is describing the long-run average trend.",
            },
            {
                "title": "Why primes thin out on average",
                "body": "Early on, primes appear fairly often: 2, 3, 5, 7, and 11 arrive quickly. Later on, you still find primes, but they are spread across larger stretches of numbers. The prime number theorem captures that gradual thinning. For example, the average prime density near 100 is much higher than the average prime density near one million. The theorem explains the trend, not the exact local pattern.",
            },
            {
                "title": "Why this does not make primes predictable",
                "body": "A common misunderstanding is that an average law should let you predict the next prime exactly. It does not. The theorem says that primes thin out in a broad statistical sense, but the local behavior is still jagged. One range can contain several primes close together, while the next range may contain a noticeably larger gap. That is why the theorem is powerful without behaving like a recipe.",
            },
            {
                "title": "A concrete way to read the formula",
                "body": "Suppose you compare two large cutoffs, one moderate and one much larger. N divided by log N grows, so the total number of primes keeps increasing. But the ratio also shows that the fraction of numbers that are prime becomes smaller. That is the core idea: primes never stop, but they become rarer on average. This is exactly the kind of average-density statement that later supports prime-gaps discussions and expected-count heuristics.",
            },
            {
                "title": "Why the theorem matters for this site",
                "body": "TwinPrimeExplorer.com often talks about prime density, prime gaps, and rough expected counts. The prime number theorem is one of the main reasons that language makes sense. It gives the background for why primes thin out, why larger gaps become more plausible on average, and why any rough benchmark involving log terms must be treated as a large-scale guide rather than as an exact prediction for one chosen interval.",
            },
            {
                "title": "How this connects to the Analysis page",
                "body": "The Analysis page includes an Expected view that compares observed twin-prime counts with a rough benchmark. That benchmark is not the prime number theorem itself, but it lives in the same family of average-density thinking. The theorem helps explain why log terms appear in these comparisons, while the Analysis Guide explains why such comparisons must stay rough and should never be confused with proof.",
            },
        ],
        "references": [
            {"label": "Prime Number Theorem", "href": "https://mathworld.wolfram.com/PrimeNumberTheorem.html", "note": "Compact reference for the asymptotic density statement."},
            {"label": "Britannica: number theory overview", "href": "https://www.britannica.com/science/number-theory", "note": "General reference context for prime-number distribution within number theory."},
            {"label": "PrimePages: twin prime constant", "href": "https://primes.utm.edu/glossary/page.php?sort=TwinPrimeConstant", "note": "Useful companion for understanding why twin-prime heuristics add more than one log term."},
        ],
        "related_links": [
            {"title": "Start from the basic definition of primes", "body": "Use the prime-numbers page first if you want the cleanest foundation before moving into average distribution questions.", "href": "/prime-numbers", "label": "Read Prime Numbers Explained"},
            {"title": "See how spacing changes", "body": "The prime-gaps page turns the same thinning idea into a direct discussion of spacing between consecutive primes.", "href": "/prime-gaps", "label": "Read What Are Prime Gaps?"},
            {"title": "Connect it to expected-count language", "body": "The Analysis Guide explains how rough expected benchmarks are used on the site and why they are not theorem-level predictions for each range.", "href": "/analysis-guide", "label": "Read the Analysis Guide"},
            {"title": "Open the live Analysis view", "body": "Use Analysis when you want to compare average-density ideas with a real selected range.", "href": "/analysis#analysis-views-title", "label": "Open Analysis"},
        ],
    },
    {
        "route": "/are-there-infinitely-many-twin-primes",
        "nav_label": "Are There Infinitely Many Twin Primes?",
        "title": "TwinPrimeExplorer.com | Are There Infinitely Many Twin Primes?",
        "meta_description": "A plain-language answer to whether there are infinitely many twin primes, including what mathematicians expect, what is proved, and what remains unproved.",
        "eyebrow": "Twin Prime Question",
        "hero_title": "Are there infinitely many twin primes?",
        "hero_text": "No one has proved it yet, but many mathematicians expect the answer is yes. That mix of strong expectation and missing proof is exactly why the twin prime conjecture matters.",
        "intro_title": "The short answer and the careful answer",
        "intro_text": "If you ask whether there are infinitely many twin primes, the careful answer is: this is strongly expected, but still unproved. This page is written for the direct search-style version of the question, so it separates the short answer, the mathematical expectation, and the theorem-level situation without assuming you already know the formal conjecture language.",
        "reviewed": "Last reviewed: April 2026",
        "sections": [
            {
                "title": "The short answer",
                "body": "Mathematicians have not proved that infinitely many twin-prime pairs exist. So the fully honest answer is: it is unproved. At the same time, the dominant expectation is that twin primes do continue forever. This means the best short answer is not simply yes or no. It is unproved, but strongly expected to be true.",
            },
            {
                "title": "What mathematicians expect",
                "body": "The expectation comes from heuristics, large-scale computation, and the way twin-prime patterns keep appearing across many finite ranges. For example, pairs such as (11, 13), (17, 19), and (29, 31) show the basic pattern early, and much larger examples continue to appear as computation pushes farther out. None of this is a proof, but it is a major reason the conjecture remains plausible.",
            },
            {
                "title": "What is proved and what is not",
                "body": "Some nearby results are proved. Bounded-gap theorems show that primes come within some fixed finite distance infinitely often. Brun's theorem proves an important fact about the sparsity of twin primes if they continue. But no theorem currently proves that the exact gap 2 occurs infinitely many times. That final step from small bounded gaps to the specific twin-prime pattern is still missing.",
            },
            {
                "title": "How this differs from 'has the conjecture been solved?'",
                "body": "The solved-or-not page is built for the direct status question: was the conjecture proved? This page is answering a slightly different search-style question: what should I believe about infinitely many twin primes? The answer there is more nuanced. The conjecture is unsolved, but the expectation remains yes. Keeping those two page types separate helps avoid mixing up proof status with mathematical belief.",
            },
            {
                "title": "How this relates to the formal conjecture page",
                "body": "The formal conjecture page states the exact problem and explains what 'infinitely many' means with more precision. This page is the more conversational companion. It is meant to be the landing page for a reader who asks the obvious question first and only afterward wants the stricter theorem-versus-conjecture framing.",
            },
            {
                "title": "How to use this site after reading this page",
                "body": "If you want the formal mathematical statement, move next to Twin Prime Conjecture Explained. If you want the direct solved-or-not clarification, use the short-answer page. If you want to see the visible finite pattern before returning to the theory, open the Lab or Explorer and look at real twin-prime examples in a selected range.",
            },
        ],
        "references": [
            {"label": "MathWorld: Twin Prime Conjecture", "href": "https://mathworld.wolfram.com/TwinPrimeConjecture.html", "note": "Direct source for the conjecture's open status."},
            {"label": "MathWorld: Twin Primes", "href": "https://mathworld.wolfram.com/TwinPrimes.html", "note": "Reference for finite examples and the broader twin-prime pattern."},
            {"label": "Yitang Zhang, Bounded gaps between primes", "href": "https://annals.math.princeton.edu/2014/179-3/p07", "note": "Nearby theorem-level progress that does not settle infinitude of gap 2."},
        ],
        "related_links": [
            {"title": "Read the formal conjecture page", "body": "Use the full conjecture explainer for the exact statement, what infinity means here, and what remains unproved.", "href": "/twin-prime-conjecture", "label": "Read Twin Prime Conjecture Explained"},
            {"title": "Read the direct solved-or-not page", "body": "Use the short-answer clarification when you want the proof-status question handled as directly as possible.", "href": "/has-the-twin-prime-conjecture-been-solved", "label": "Read the short answer"},
            {"title": "Return to the main pattern", "body": "The twin-primes page gives the best plain-language introduction to the pattern itself before you think about the infinite question.", "href": "/what-are-twin-primes", "label": "Read What Are Twin Primes?"},
            {"title": "See why mathematicians still expect yes", "body": "The Hardy-Littlewood page is the clearest next stop if you want the heuristic case for expecting infinitely many twin primes.", "href": "/hardy-littlewood-twin-primes", "label": "Read Hardy-Littlewood For Twin Primes"},
            {"title": "See the broader theory context", "body": "Theory keeps the conjecture, research approaches, and current progress in one place.", "href": "/theory#history", "label": "Open Theory"},
        ],
    },
    {
        "route": "/prime-gaps-vs-prime-pairs",
        "nav_label": "Prime Gaps vs Prime Pairs",
        "title": "TwinPrimeExplorer.com | Prime Gaps vs Prime Pairs",
        "meta_description": "A clear explanation of the difference between prime gaps and prime pairs, and why that distinction matters for twin primes, bounded gaps, and Analysis.",
        "eyebrow": "Clarification",
        "hero_title": "Prime gaps vs prime pairs",
        "hero_text": "Prime gaps and prime pairs are closely related, but they are not the same idea. The distinction matters whenever you move between twin primes, bounded gaps, and the site's Analysis views.",
        "intro_title": "Why this distinction helps",
        "intro_text": "This page is a clarification bridge. It explains the difference between talking about the distance between consecutive primes and talking about particular pairs of primes that fit a named pattern. That distinction makes several other pages on the site easier to read correctly.",
        "reviewed": "Last reviewed: April 2026",
        "sections": [
            {
                "title": "What a prime gap is",
                "body": "A prime gap is the difference between one prime and the next prime after it. If the primes are 11 and 13, the gap is 2. If the primes are 23 and 29, the gap is 6. Prime-gap language focuses on spacing between consecutive primes.",
            },
            {
                "title": "What a prime pair is in this site's context",
                "body": "A prime pair is a pair of primes being discussed as a recognizable pattern. On this site, the most important example is a twin-prime pair: two primes that differ by 2. In that sense, a prime pair is about a named relationship, while a prime gap is about a measured spacing value.",
            },
            {
                "title": "Why twin primes are a special case rather than the whole story",
                "body": "Twin primes are one especially famous prime-pair pattern, but prime-gap language is broader. Every pair of consecutive primes has a gap, but not every pair belongs to a named pattern people focus on. That is why the twin-prime story sits inside the larger study of prime gaps rather than replacing it.",
            },
            {
                "title": "A concrete comparison",
                "body": "Consider the primes 11, 13, 17, and 19. The pair (11, 13) is a twin-prime pair, and so is (17, 19). The gap from 13 to 17 is 4, but that gap is not itself a twin-prime pair. This is a good example of why gap language and pair language should not be collapsed into one thing. One is a spacing measurement, the other is a pattern name attached to a pair.",
            },
            {
                "title": "Why people blur these ideas together",
                "body": "The confusion is understandable because twin primes are literally the gap-2 case. So one page may talk about pairs and another about gaps while pointing to the same examples. But once you move into bounded gaps, Analysis summaries, or broader spacing questions, the distinction becomes important. Gap language supports the larger distribution story, while pair language highlights named special configurations inside it.",
            },
            {
                "title": "Why this helps with bounded gaps and Analysis",
                "body": "Bounded-gap theorems say that some small prime gap recurs infinitely often, but they do not name one exact prime-pair pattern such as twin primes. The Analysis page also makes more sense when you keep this distinction clear: some tabs summarize spacing, while others help you interpret recurring pair structure. This page exists so those shifts in language feel intentional rather than confusing.",
            },
        ],
        "references": [
            {"label": "MathWorld: Prime Gaps", "href": "https://mathworld.wolfram.com/PrimeGaps.html", "note": "Reference for consecutive-prime spacing language."},
            {"label": "MathWorld: Twin Primes", "href": "https://mathworld.wolfram.com/TwinPrimes.html", "note": "Reference for the named gap-2 pair pattern."},
            {"label": "Yitang Zhang, Bounded gaps between primes", "href": "https://annals.math.princeton.edu/2014/179-3/p07", "note": "Useful for the bounded-gaps distinction discussed on the page."},
        ],
        "related_links": [
            {"title": "Read the broader gap page", "body": "Use the prime-gaps page when you want the full spacing story rather than only the distinction itself.", "href": "/prime-gaps", "label": "Read What Are Prime Gaps?"},
            {"title": "Return to the twin-prime pattern", "body": "The twin-primes page shows the named pair pattern that motivates this whole comparison.", "href": "/what-are-twin-primes", "label": "Read What Are Twin Primes?"},
            {"title": "Compare the bounded-gap result", "body": "This page helps you see why bounded-gap progress is close to, but not the same as, a twin-prime proof.", "href": "/what-bounded-gaps-between-primes-actually-proved", "label": "Read What Bounded Gaps Between Primes Actually Proved"},
            {"title": "See the direct infinite-question page", "body": "This page helps connect the pair-versus-gap distinction back to the search-style question about infinitely many twin primes.", "href": "/are-there-infinitely-many-twin-primes", "label": "Read Are There Infinitely Many Twin Primes?"},
            {"title": "Use the Analysis Guide", "body": "The guide explains how the site's analysis views shift between structural and spacing questions.", "href": "/analysis-guide", "label": "Read the Analysis Guide"},
        ],
    },
    {
        "route": "/hardy-littlewood-twin-primes",
        "nav_label": "Hardy-Littlewood For Twin Primes",
        "title": "TwinPrimeExplorer.com | Hardy-Littlewood For Twin Primes",
        "meta_description": "A plain-language guide to the Hardy-Littlewood twin-prime heuristic, including why the twin prime constant matters and why the framework is persuasive but not a proof.",
        "eyebrow": "Heuristic Framework",
        "hero_title": "Hardy-Littlewood for twin primes",
        "hero_text": "The Hardy-Littlewood prime-pair conjecture is one of the main reasons mathematicians expect infinitely many twin primes. It gives a quantitative prediction for how often twin-prime pairs should appear, while still stopping short of proof.",
        "intro_title": "Why this heuristic matters",
        "intro_text": "This page explains the Hardy-Littlewood framework in plain language. It is not a theorem page. It is a heuristic page: it shows why mathematicians think twin primes should keep appearing, why a simple random model is not quite enough, and why the famous twin prime constant enters the story.",
        "reviewed": "Last reviewed: April 2026",
        "sections": [
            {
                "title": "What Hardy-Littlewood is trying to predict",
                "body": "The Hardy-Littlewood prime-pair conjecture gives an expected count for how often pairs of primes with a fixed spacing should occur. In the twin-prime case, it predicts how often primes p and p + 2 should both be prime as numbers grow. The point is not to say where the next twin-prime pair must be. The point is to describe the long-run frequency mathematicians expect on average.",
            },
            {
                "title": "Why naive probability is not enough",
                "body": "A first guess might say: if primes near a large number N appear with rough probability about 1 divided by log N, then maybe a twin-prime pair appears with rough probability about 1 divided by log squared N. That guess captures part of the story, but it misses a crucial detail. Two nearby numbers share divisibility constraints, so their chances are not independent in a clean random sense. Hardy-Littlewood corrects for that.",
            },
            {
                "title": "Where the twin prime constant enters",
                "body": "The twin prime constant is the correction factor that adjusts the naive estimate. It accounts for the fact that divisibility by small primes changes the expected frequency of twin-prime candidates. In plain language, the constant is the price of taking arithmetic structure seriously instead of pretending primes are random without constraints. That is why the constant belongs naturally to the heuristic.",
            },
            {
                "title": "A concrete way to think about the correction",
                "body": "Consider a potential twin-prime pair like N and N + 2. If N is divisible by 3, the pair immediately fails. If N is not divisible by 3, then N + 2 might still fail for another small-prime reason. The point is that small divisibility filters change how often gap-2 candidates survive. Hardy-Littlewood builds those filters into the long-run expectation instead of ignoring them.",
            },
            {
                "title": "Why mathematicians find the heuristic persuasive",
                "body": "The framework lines up well with large-scale computation and with the broader expectation that prime patterns behave regularly on average once arithmetic constraints are accounted for. It also fits naturally with the prime number theorem, which explains why primes thin out on average, and with the observed persistence of twin-prime pairs across large finite ranges. That combination makes the heuristic influential even though it is not a proof.",
            },
            {
                "title": "Why this is still not a proof",
                "body": "A heuristic can be convincing, accurate, and mathematically useful without becoming a theorem. Hardy-Littlewood predicts what should happen on average. The twin prime conjecture asks for a proof that infinitely many exact gap-2 pairs really do occur. Bridging that gap from prediction to proof is exactly the hard part. This is why the site keeps Hardy-Littlewood language explicitly on the expected or heuristic side of the story, not the proved side.",
            },
            {
                "title": "How this connects to the site",
                "body": "This page helps connect several other parts of TwinPrimeExplorer.com. The prime number theorem page explains why log terms appear in average-density thinking, the conjecture pages explain what remains unproved, and the Analysis Guide explains why expected-count views are rough comparison tools rather than theorem engines. Once you know what Hardy-Littlewood is doing, those pages fit together more naturally.",
            },
        ],
        "references": [
            {"label": "Hardy and Littlewood, Some Problems of Partitio Numerorum (V)", "href": "https://academic.oup.com/plms/article-pdf/s2-22/1/46/4372641/s2-22-1-46.pdf", "note": "Classic source for the prime-pair heuristic framework."},
            {"label": "PrimePages: twin prime constant", "href": "https://primes.utm.edu/glossary/page.php?sort=TwinPrimeConstant", "note": "Compact reference for the constant that corrects the naive estimate."},
            {"label": "PrimePages: Twin Primes", "href": "https://primes.utm.edu/glossary/page.php?sort=TwinPrime", "note": "Accessible summary of the heuristic and observed twin-prime pattern."},
        ],
        "related_links": [
            {"title": "Start from average prime density", "body": "The prime number theorem page explains the broad thinning pattern that sits behind Hardy-Littlewood style estimates.", "href": "/prime-number-theorem", "label": "Read The Prime Number Theorem In Plain Language"},
            {"title": "See why log n keeps showing up", "body": "This background page is the shortest route from prime-density language to the repeated log terms inside twin-prime heuristics.", "href": "/why-log-n-appears-in-prime-number-theory", "label": "Read Why log n Appears In Prime Number Theory"},
            {"title": "Return to the formal conjecture", "body": "Use the conjecture page when you want the exact problem statement that this heuristic is trying to predict.", "href": "/twin-prime-conjecture", "label": "Read Twin Prime Conjecture Explained"},
            {"title": "Read the softer expectation page", "body": "Use the expectation page if you want the same idea explained more conversationally before the full Hardy-Littlewood framework.", "href": "/why-twin-primes-are-expected-to-continue-forever", "label": "Read Why Twin Primes Are Expected To Continue Forever"},
            {"title": "Compare proof and expectation", "body": "The bounded-gaps page helps keep theorem-level progress separate from heuristic prediction.", "href": "/what-bounded-gaps-between-primes-actually-proved", "label": "Read What Bounded Gaps Between Primes Actually Proved"},
            {"title": "See how expected views are used on the site", "body": "The Analysis Guide explains why expected-count comparisons are rough interpretive tools rather than proofs.", "href": "/analysis-guide", "label": "Read the Analysis Guide"},
        ],
    },
    {
        "route": "/why-log-n-appears-in-prime-number-theory",
        "nav_label": "Why log n Appears In Prime Number Theory",
        "title": "TwinPrimeExplorer.com | Why log n Appears In Prime Number Theory",
        "meta_description": "A plain-language explanation of why log n shows up so often in prime number theory, especially in density estimates, expected counts, and twin-prime heuristics.",
        "eyebrow": "Prime Number Background",
        "hero_title": "Why log n appears in prime number theory",
        "hero_text": "Logarithms show up all over prime number theory because prime density changes slowly and average prime counts are tied to that slow thinning. The appearance of log n is not decorative notation. It is part of the structure of the subject.",
        "intro_title": "Why this symbol keeps returning",
        "intro_text": "This page is for readers who keep seeing log n on the site and want to know why. It explains, in plain language, why logarithms appear in average prime-density statements, why twin-prime heuristics often involve log squared n, and why those formulas should be read as rough guides rather than exact local predictions.",
        "reviewed": "Last reviewed: April 2026",
        "sections": [
            {
                "title": "Where log n first enters the story",
                "body": "The prime number theorem says that the number of primes up to a large number N is approximately N divided by log N. That means the average density of primes near large values behaves like 1 divided by log N. So log N first appears because primes thin out slowly, not because someone arbitrarily chose a complicated symbol.",
            },
            {
                "title": "Why slow thinning leads to logarithms",
                "body": "Primes do not disappear quickly. They become rarer in a gradual way. A logarithm is one of the natural mathematical tools for describing a quantity that changes slowly across large scales. That is why log terms appear when mathematicians describe the broad average behavior of primes rather than the exact location of the next prime.",
            },
            {
                "title": "A concrete way to read 1 over log n",
                "body": "If you compare moderate numbers with much larger numbers, the value of log N increases, but slowly. So 1 divided by log N becomes smaller, also slowly. That matches the real picture of primes: they keep appearing, but the average share of numbers that are prime gradually drops. The formula is about trend, not exact prediction.",
            },
            {
                "title": "Why twin-prime heuristics use log squared n",
                "body": "If one prime near N behaves roughly like a 1 over log N event in an average-density model, then asking for two primes in a tightly related pattern naturally introduces a second log factor. That is why twin-prime heuristics often involve 1 over log squared N, together with an additional correction factor such as the twin prime constant. The squared log comes from asking for a more demanding pattern than a single prime.",
            },
            {
                "title": "Why the formulas stay rough",
                "body": "Even when log terms are structurally meaningful, they do not turn prime locations into clockwork. One selected interval may have more primes or twin-prime pairs than a rough log-based estimate suggests, while another may have fewer. The point of the formula is to describe average behavior across scale, not to promise a local count in every range.",
            },
            {
                "title": "How this helps when reading the site",
                "body": "This page is useful whenever the site mentions expected counts, rough density, or heuristic predictions. It helps explain why the Analysis page compares observed behavior with a log-based benchmark, why the prime number theorem page matters for background, and why Hardy-Littlewood style predictions for twin primes use stronger log terms without becoming proofs.",
            },
        ],
        "references": [
            {"label": "Britannica: prime number theorem", "href": "https://www.britannica.com/science/number-theory/Prime-number-theorem", "note": "Background for the x/log x density statement."},
            {"label": "PrimePages: twin prime constant", "href": "https://primes.utm.edu/glossary/page.php?sort=TwinPrimeConstant", "note": "Companion reference for the extra log factor in twin-prime heuristics."},
            {"label": "Hardy and Littlewood, Some Problems of Partitio Numerorum (V)", "href": "https://academic.oup.com/plms/article-pdf/s2-22/1/46/4372641/s2-22-1-46.pdf", "note": "Classic source behind the heuristic side of the page."},
        ],
        "related_links": [
            {"title": "Read the main theorem first", "body": "The prime number theorem page is the clearest starting point for the average-density story that produces log terms.", "href": "/prime-number-theorem", "label": "Read The Prime Number Theorem In Plain Language"},
            {"title": "See the twin-prime heuristic side", "body": "The Hardy-Littlewood page explains why twin-prime expectations add more structure on top of the basic log pattern.", "href": "/hardy-littlewood-twin-primes", "label": "Read Hardy-Littlewood For Twin Primes"},
            {"title": "Connect it to expected-count reading", "body": "The Analysis Guide explains how rough benchmark language is used on the site without pretending to prove anything.", "href": "/analysis-guide", "label": "Read the Analysis Guide"},
            {"title": "Open the Analysis page", "body": "Use Analysis when you want to compare the site's rough benchmark language with an actual selected range.", "href": "/analysis#analysis-views-title", "label": "Open Analysis"},
        ],
    },
    {
        "route": "/how-to-read-prime-patterns-in-the-lab",
        "nav_label": "How To Read Prime Patterns In The Lab",
        "title": "TwinPrimeExplorer.com | How To Read Prime Patterns In The Lab",
        "meta_description": "A practical guide to reading the Lab view on TwinPrimeExplorer.com, including how to spot twin centers, use Mod 6 structure, and know when to switch to Explorer or Analysis.",
        "eyebrow": "Lab Guide",
        "hero_title": "How to read prime patterns in the Lab",
        "hero_text": "The Lab is easiest to use when you treat it as a pattern-reading surface instead of a proof machine. This page gives a simple workflow for seeing structure first, then using Explorer and Analysis when you need more detail.",
        "intro_title": "A practical first-pass workflow",
        "intro_text": "This page is for readers who can open the Lab but are not yet sure what to look for. It shows how to start with one visual question, use twin centers and modular structure as anchors, and know when to switch from a visual pattern to a more exact tool.",
        "reviewed": "Last reviewed: April 2026",
        "sections": [
            {
                "title": "Start with one visual question",
                "body": "Do not try to read every color and count at once. A better first step is to choose one question, such as: where are the twin-prime pairs, where are the twin centers, or how do the primes cluster in this range? The Lab becomes much easier once you decide what kind of pattern you are trying to notice first.",
            },
            {
                "title": "Use twin centers as anchors",
                "body": "Twin centers are often easier to spot and compare than the prime pairs themselves. If you can see where the centers line up, you can often recover the surrounding gap-2 structure mentally. That is why TwinPrimeExplorer.com highlights centers so strongly: they turn a pair-pattern question into a simpler structural anchor.",
            },
            {
                "title": "Use Mod 6 when the field feels noisy",
                "body": "If the full pattern feels visually busy, switch attention to the Mod 6 structure. Primes greater than 3 are forced into narrow residue classes, and that immediately removes much of the noise. Mod 6 is not a proof of anything by itself, but it is one of the fastest ways to make the visual field feel interpretable.",
            },
            {
                "title": "Look for spacing and clustering separately",
                "body": "One common mistake is to treat every nearby prime pair as the same kind of phenomenon. The Lab is better when you separate two questions: where do you see visible local clusters, and where do you see the specific gap-2 twin-prime pattern? That distinction prepares you for later pages about prime gaps, prime pairs, and bounded gaps.",
            },
            {
                "title": "Move to Explorer when you want exact arithmetic",
                "body": "The Lab is built for recognition, not for line-by-line verification. When you want to inspect the exact numbers, divisors, neighbors, or local classifications behind something you noticed visually, move to Explorer. That handoff keeps the Lab lightweight while still letting you verify what you think you saw.",
            },
            {
                "title": "Move to Analysis when you want summaries",
                "body": "If your question is no longer visual but comparative, Analysis is usually the better next step. It summarizes modular counts, prime-gap behavior, density patterns, and rough expected-count comparisons. In practice, a good workflow is: see something in the Lab, verify it in Explorer if needed, then use Analysis if you want a structured summary of the same range.",
            },
            {
                "title": "A good first-visit workflow",
                "body": "A simple first route is: open the Lab, look for twin centers first, check the Mod 6 pattern second, then switch to Explorer or Analysis once one concrete question emerges. That keeps the Lab from feeling like a wall of information. It also matches the larger philosophy of the site: explanation first, then structured inspection, then broader theory if the pattern raises a deeper question.",
            },
        ],
        "references": [
            {"label": "MathWorld: Twin Primes", "href": "https://mathworld.wolfram.com/TwinPrimes.html", "note": "Reference for the gap-2 structure the Lab highlights."},
            {"label": "Britannica: modular arithmetic", "href": "https://www.britannica.com/science/modular-arithmetic", "note": "Background for the Mod 6 reading cues."},
            {"label": "MathWorld: Prime Gaps", "href": "https://mathworld.wolfram.com/PrimeGaps.html", "note": "Useful for the spacing-versus-pattern distinction in the guide."},
        ],
        "related_links": [
            {"title": "Open the Lab", "body": "Use the live visualization first, then come back to this guide once you have one pattern question in mind.", "href": "/lab#visualization-title", "label": "Open the Lab"},
            {"title": "Read the twin-centers explainer", "body": "This page helps explain why the Lab uses centers as such a strong structural cue.", "href": "/why-twin-centers-matter", "label": "Read Why Twin Centers Matter"},
            {"title": "Read the Mod 6 explainer", "body": "Use the modular page when you want the fastest plain-language explanation of the residue pattern behind the Lab.", "href": "/why-mod-6-shows-up-so-often", "label": "Read Why Mod 6 Shows Up So Often"},
            {"title": "Clarify spacing versus named patterns", "body": "This bridge page helps when what you noticed visually needs to be separated into prime-gap language versus prime-pair language.", "href": "/prime-gaps-vs-prime-pairs", "label": "Read Prime Gaps vs Prime Pairs"},
            {"title": "Move into structured interpretation", "body": "The Analysis Guide explains how to read the summary views once the visual pattern is no longer the main question.", "href": "/analysis-guide", "label": "Read the Analysis Guide"},
        ],
    },
    {
        "route": "/chens-theorem",
        "nav_label": "Chen's Theorem Explained",
        "title": "TwinPrimeExplorer.com | Chen's Theorem Explained",
        "meta_description": "A plain-language explanation of Chen's theorem, why it is a major near-miss result in the twin-prime story, and why it still stops short of a proof of infinitely many twin primes.",
        "eyebrow": "Progress Result",
        "hero_title": "Chen's theorem explained",
        "hero_text": "Chen's theorem is one of the strongest theorem-level near misses in the twin-prime story. It proves that infinitely many primes sit 2 away from a number that is either prime or semiprime.",
        "intro_title": "Why this theorem matters",
        "intro_text": "This page explains Chen's theorem in plain language: what it says, why mathematicians treat it as serious progress, and why the result is close to twin primes without actually becoming a twin-prime proof.",
        "reviewed": "Last reviewed: April 2026",
        "sections": [
            {"title": "What Chen's theorem says", "body": "In twin-prime language, Chen's theorem says that there are infinitely many primes p such that p + 2 is either also prime or else a semiprime, meaning a product of two primes. So the theorem does not guarantee infinitely many pairs (p, p + 2) where both entries are prime. It guarantees infinitely many cases where the second number is only one step away from that exact target."},
            {"title": "Why semiprime matters here", "body": "A semiprime is simpler than a general composite number because it still has very limited factor structure. For example, 91 = 7 x 13 is semiprime. So Chen's theorem is not saying p + 2 can be any composite at all. It says p + 2 is forced into a narrow almost-prime category. That is why the theorem feels much closer to twin primes than a loose statement about composites would."},
            {"title": "Why mathematicians view it as a near miss", "body": "Twin primes ask for exact gap-2 pairs where both numbers are prime. Chen's theorem gets one side exactly right and constrains the other side very strongly, but it still leaves open the possibility that p + 2 has two prime factors instead of one. In plain language, the theorem comes extremely close to the twin-prime pattern while still stopping just short of it."},
            {"title": "A concrete comparison", "body": "A true twin-prime example is (11, 13). A Chen-type outcome could look like a prime p where p + 2 behaves more like 91, which is 7 x 13. Both situations preserve the same shift by 2, but only the first gives an exact twin-prime pair. This comparison helps explain why Chen's theorem is celebrated without being mistaken for a proof of infinitely many twin primes."},
            {"title": "Why this was important before bounded gaps", "body": "Chen's theorem was already a major achievement because it showed that sieve methods could force prime patterns into a remarkably tight near-twin shape. Long before bounded-gap results, it gave the field one of its clearest theorem-level signs that the twin-prime problem could be approached by proving strong nearby statements first."},
            {"title": "How this fits with the modern progress story", "body": "The modern twin-prime story includes several kinds of progress: Chen's theorem, bounded gaps, heuristic predictions, and better control of primes in arithmetic progressions. Chen's theorem belongs to the near-miss side of that story. It shows how close theorem-level progress can come to the exact twin-prime pattern without actually settling gap 2."},
            {"title": "How to use this page on the site", "body": "Use this page when you want a stronger sense of what mathematicians mean by progress that is substantial but still incomplete. It works especially well beside the bounded-gaps page, the difficulty page, and the broader conjecture explainer. Together, those pages make it easier to understand why modern results are impressive without overstating what has been proved."}
        ],
        "references": [
            {"label": "MathWorld: Chen's Theorem", "href": "https://mathworld.wolfram.com/ChensTheorem.html", "note": "Compact statement of the theorem and its classical references."},
            {"label": "MathWorld: Chen Prime", "href": "https://mathworld.wolfram.com/ChenPrime.html", "note": "Accessible route into the prime-or-semiprime condition discussed on the page."},
            {"label": "MathWorld: Twin Prime Conjecture", "href": "https://mathworld.wolfram.com/TwinPrimeConjecture.html", "note": "Reference for the exact gap-2 conjecture Chen's theorem approaches but does not settle."}
        ],
        "related_links": [
            {"title": "Compare Chen to bounded gaps", "body": "Use the bounded-gaps page when you want another major near-miss theorem stated in plain language.", "href": "/what-bounded-gaps-between-primes-actually-proved", "label": "Read What Bounded Gaps Between Primes Actually Proved"},
            {"title": "See why the exact last step is hard", "body": "The difficulty page explains why the final move from near misses to exact twin primes is so resistant.", "href": "/why-the-twin-prime-problem-is-hard", "label": "Read Why The Twin Prime Problem Is Hard"},
            {"title": "Return to the formal open problem", "body": "Use the conjecture page when you want the exact gap-2 claim that Chen's theorem does not yet prove.", "href": "/twin-prime-conjecture", "label": "Read Twin Prime Conjecture Explained"},
            {"title": "See the wider progress cluster", "body": "Theory keeps Chen, bounded gaps, and other progress pages in a broader research frame.", "href": "/theory#progress", "label": "Open Theory: Current Progress"}
        ]
    }
    ,
    {
        "route": "/why-twin-primes-are-expected-to-continue-forever",
        "nav_label": "Why Twin Primes Are Expected To Continue Forever",
        "title": "TwinPrimeExplorer.com | Why Twin Primes Are Expected To Continue Forever",
        "meta_description": "A plain-language explanation of why mathematicians expect twin primes to continue forever, even though that expectation is still not a proof.",
        "eyebrow": "Heuristic Expectation",
        "hero_title": "Why twin primes are expected to continue forever",
        "hero_text": "Mathematicians do not have a proof that twin primes continue forever, but they do have strong reasons to expect that they do. This page explains that expectation without blurring it into a theorem.",
        "intro_title": "Why expectation is not the same as proof",
        "intro_text": "This page is the softer companion to the more technical Hardy-Littlewood explainer. It answers the natural question of why mathematicians keep expecting more twin primes while still being careful about what has and has not been proved.",
        "reviewed": "Last reviewed: April 2026",
        "sections": [
            {"title": "The pattern keeps surviving larger searches", "body": "Twin primes appear early, and they continue to appear in very large computed ranges. That does not prove they go on forever, but it does remove the feeling that the pattern is only a small-number accident. The basic shape keeps recurring instead of dying out quickly."},
            {"title": "Average-density models still leave room for them", "body": "Primes thin out on average, but they do not disappear. Heuristic models suggest that the thinning is slow enough that gap-2 pairs should still keep showing up from time to time. In other words, twin primes should become rarer on average, not impossible."},
            {"title": "Arithmetic constraints are built into the expectation", "body": "A serious expectation about twin primes does not pretend numbers are random in a naive way. It takes divisibility constraints seriously. For example, primes greater than 3 must avoid many residue classes, and good heuristic models correct for those restrictions rather than ignoring them. That is one reason mathematicians trust the expectation more than a simple coin-flip picture."},
            {"title": "A concrete way to think about it", "body": "Compare two claims. One claim says, 'I can point to many finite examples such as (11, 13), (17, 19), and (29, 31).' The stronger claim says, 'I expect this pattern never runs out.' The first is visible evidence. The second comes from combining that evidence with long-run heuristic models about prime density and local divisibility. The page exists to keep those two kinds of support separate."},
            {"title": "Why this still stops short of theorem status", "body": "Expectation is not enough in number theory. A proof has to show that exact gap 2 recurs infinitely often, not merely that the pattern seems persistent and mathematically plausible. This is why the site keeps expectation language and theorem language in different lanes. One can be strong without turning into the other."},
            {"title": "How this relates to Hardy-Littlewood", "body": "Hardy-Littlewood gives the more quantitative heuristic framework behind this expectation. This page is the shorter, more conversational version. It explains why mathematicians expect continuing twin primes without requiring you to absorb the full constant-and-logarithm machinery first."},
            {"title": "How this fits into the site's reading path", "body": "Use this page if you want the expectation side of the story before you move into the more formal conjecture and heuristic pages. Then go to Are There Infinitely Many Twin Primes?, Twin Prime Conjecture Explained, or Hardy-Littlewood For Twin Primes depending on whether you want the short answer, the formal statement, or the more detailed heuristic background."}
        ],
        "references": [
            {"label": "MathWorld: Twin Prime Conjecture", "href": "https://mathworld.wolfram.com/TwinPrimeConjecture.html", "note": "Compact reference for the open status of the conjecture and the strength of mathematical expectation around it."},
            {"label": "MathWorld: Twin Primes", "href": "https://mathworld.wolfram.com/TwinPrimes.html", "note": "Reference for the recurring finite pattern and the strong heuristic form of the conjecture."},
            {"label": "Hardy and Littlewood, Some Problems of Partitio Numerorum (V)", "href": "https://academic.oup.com/plms/article-pdf/s2-22/1/46/4372641/s2-22-1-46.pdf", "note": "Classic heuristic source behind the expectation that twin primes should continue."}
        ],
        "related_links": [
            {"title": "Read the search-style answer first", "body": "Use the direct infinite-question page when you want the shortest careful answer before the fuller heuristic explanation.", "href": "/are-there-infinitely-many-twin-primes", "label": "Read Are There Infinitely Many Twin Primes?"},
            {"title": "See the full heuristic framework", "body": "Hardy-Littlewood is the more detailed page for why mathematicians expect continuing twin-prime structure.", "href": "/hardy-littlewood-twin-primes", "label": "Read Hardy-Littlewood For Twin Primes"},
            {"title": "Return to the formal conjecture", "body": "Use the conjecture page when you want expectation separated from the exact statement that still needs proof.", "href": "/twin-prime-conjecture", "label": "Read Twin Prime Conjecture Explained"},
            {"title": "Return to the main pattern", "body": "The core twin-primes page stays the best place to see the pattern itself before you think about why it should continue.", "href": "/what-are-twin-primes", "label": "Read What Are Twin Primes?"}
        ]
    },
    {
        "route": "/arithmetic-progressions-primes",
        "nav_label": "Arithmetic Progressions Explained For Prime Patterns",
        "title": "TwinPrimeExplorer.com | Arithmetic Progressions Explained For Prime Patterns",
        "meta_description": "A plain-language explanation of arithmetic progressions in prime-number study, including why residue classes, Dirichlet's theorem, and Green-Tao matter for reading prime patterns.",
        "eyebrow": "Research Background",
        "hero_title": "Arithmetic progressions explained for prime patterns",
        "hero_text": "Arithmetic progressions sound like a simple school-math idea, but they play a serious role in prime-number research. They help explain why modular structure matters and why primes are studied inside patterned numerical lanes.",
        "intro_title": "Why this background helps on the site",
        "intro_text": "This page explains why arithmetic progressions matter for prime patterns on TwinPrimeExplorer.com. It connects the site's Mod 6 and residue-class language to deeper mathematical ideas about how primes distribute inside allowed progressions.",
        "reviewed": "Last reviewed: April 2026",
        "sections": [
            {"title": "What an arithmetic progression is", "body": "An arithmetic progression is a sequence that moves by a constant step size, such as 5, 11, 17, 23 or 1, 7, 13, 19. The pattern is simple: each term differs from the next by the same amount. That simplicity is exactly why arithmetic progressions are so useful in prime-number study. They let mathematicians ask whether primes keep showing up inside a structured lane instead of inside the integers all at once."},
            {"title": "Why primes in progressions matter", "body": "Once you think in terms of residue classes, prime patterns stop looking like isolated accidents. For example, primes greater than 3 must live in the 1 or 5 classes mod 6. That means much of the site's modular structure can be rephrased as a statement about which arithmetic progressions primes are allowed to occupy. The progression viewpoint turns a visual pattern into a research-level distribution question."},
            {"title": "Dirichlet's theorem is the first big result here", "body": "Dirichlet's theorem says that if the starting term and step size share no common factor, then the progression contains infinitely many primes. So sequences like 6n + 1 and 6n + 5 do not merely happen to contain primes early on. They contain infinitely many primes. This helps explain why modular filters on the site are more than visual tricks: they reflect serious mathematical structure."},
            {"title": "Green-Tao shows the pattern can be much richer", "body": "The Green-Tao theorem goes further by proving that the prime numbers contain arbitrarily long arithmetic progressions. In other words, primes do not merely appear infinitely often inside some allowed lanes. They can themselves line up in long evenly spaced strings. That result is not about twin primes directly, but it shows how structured prime patterns can be at theorem strength."},
            {"title": "A concrete way to connect this to mod 6", "body": "If you look at numbers of the form 6n + 1, you get 7, 13, 19, 25, 31, 37, and so on. Some entries are prime and some are composite, but the progression itself captures one of the allowed lanes where large primes can live. The same is true for 6n + 5. This is one reason the Lab's Mod 6 view and the theory of primes in arithmetic progressions fit together so naturally."},
            {"title": "Why this still does not solve twin primes", "body": "Knowing that primes distribute richly inside arithmetic progressions is not the same as proving that exact gap-2 pairs occur infinitely often. Arithmetic progressions control where primes may appear and how they can spread across residue classes. Twin primes ask for a much more specific local pairing condition. So this background is important, but it is only one part of the larger puzzle."},
            {"title": "How to use this page on the site", "body": "Use this page when Mod 6, residue classes, or primes in arithmetic progressions start appearing across the Theory, Glossary, and Analysis surfaces and you want them to feel like one idea instead of scattered vocabulary. It pairs especially well with the Mod 6 explainer, the methods overview, and the Theory approaches material."}
        ],
        "references": [
            {"label": "Britannica: Dirichlet's theorem", "href": "https://www.britannica.com/science/Dirichlets-theorem", "note": "Plain-language reference for infinitely many primes in coprime arithmetic progressions."},
            {"label": "MathWorld: Dirichlet's Theorem", "href": "https://mathworld.wolfram.com/DirichletsTheorem.html", "note": "Compact reference for the arithmetic-progression theorem behind many modular patterns."},
            {"label": "Annals of Mathematics: The primes contain arbitrarily long arithmetic progressions", "href": "https://annals.math.princeton.edu/2008/167-2/p03", "note": "Green-Tao theorem source for long arithmetic progressions of primes."}
        ],
        "related_links": [
            {"title": "Read the Mod 6 explainer", "body": "Use the short modular page first if you want the quickest route from residues to visible prime structure.", "href": "/why-mod-6-shows-up-so-often", "label": "Read Why Mod 6 Shows Up So Often"},
            {"title": "See the methods overview", "body": "The methods page shows how arithmetic progressions fit beside sieves, heuristics, and bounded-gap work.", "href": "/how-mathematicians-study-twin-primes", "label": "Read How Mathematicians Study Twin Primes"},
            {"title": "Open Theory: Approaches", "body": "Theory keeps the arithmetic-progression idea inside the broader research picture.", "href": "/theory#approaches", "label": "Open Theory: Approaches"},
            {"title": "Use the Glossary alongside it", "body": "Glossary is still the fastest route when you only need a term like residue class or arithmetic progression defined briefly.", "href": "/glossary", "label": "Open Glossary"}
        ]
    }
    ,
    {
        "route": "/how-to-read-analysis",
        "nav_label": "How To Read The Analysis Page",
        "title": "TwinPrimeExplorer.com | How To Read The Analysis Page",
        "meta_description": "A plain-language guide to reading the Analysis page on TwinPrimeExplorer.com, including which tab to open first and how to connect Modular, Gaps, Factors, Density, and Expected.",
        "eyebrow": "Analysis Companion",
        "hero_title": "How to read the Analysis page",
        "hero_text": "The Analysis page is easiest to use when you begin with one question and let that question choose the tab. This page gives the short, practical route before the fuller guide takes over.",
        "intro_title": "A practical way to enter Analysis",
        "intro_text": "This page is the shorter companion to the full Analysis Guide. It is meant for visitors who want a fast, plain-language answer to what each Analysis tab is for, which one to open first, and how to move from one tab to the next without treating every metric as equally important at once.",
        "reviewed": "Last reviewed: April 2026",
        "sections": [
            {"title": "Start with your question, not with all five tabs", "body": "The Analysis page becomes much easier once you decide what you are asking. If you want structural rules, start with Modular. If you want spacing behavior, start with Gaps. If you want center arithmetic, start with Factors. If you want local clustering, start with Density. If you only want a rough benchmark, open Expected last rather than first."},
            {"title": "Modular is the best first tab for visible structure", "body": "Use Modular when you want the quickest explanation of why the same residue-class patterns keep appearing. It is usually the cleanest first stop because it turns the range into a small number of structural buckets rather than a long list of counts. If the site keeps mentioning Mod 6 or residue classes, this is the fastest tab to make that language feel concrete."},
            {"title": "Gaps is the best first tab for spacing questions", "body": "Use Gaps when your question is about how twin-prime pairs are spread across the range. This tab helps separate close clustering from wider separation and works especially well after the prime-gaps pages. It is the right entry point when the question in your head sounds like, 'Are the pairs bunching up or spreading out here?'"},
            {"title": "Factors is really about centers, not about every number", "body": "Factors is most useful when you want to compare twin-prime centers with other nearby even numbers. It is less about generic factor tables and more about whether centers look structurally unusual. If twin centers are still a fuzzy idea, this tab makes more sense after Why Twin Centers Matter or after a quick pass through Explorer."},
            {"title": "Density and Expected should usually come later", "body": "Density and Expected are comparison tabs rather than entry tabs. Density asks whether twin-prime neighborhoods look locally richer than the surrounding range. Expected asks how the observed count compares with a rough benchmark. Both are more useful once you already know what the range looks like structurally, because otherwise the summaries can float free of the actual pattern."},
            {"title": "A concrete reading sequence that works well", "body": "A reliable sequence is: start with Modular for structure, move to Gaps for spacing, then use Factors if twin centers are part of the question. After that, open Density if you want neighborhood comparison and Expected if you want a rough benchmark. This order keeps the more interpretive tabs from arriving before the underlying pattern is clear."},
            {"title": "How this page fits with the rest of the site", "body": "Use this page as the quick companion when you land on Analysis and want orientation fast. Use the full Analysis Guide when you want the longer walkthrough. Move back to the live Analysis page when you are ready to test a real range, and use the Lab or Explorer if the numbers still need a more visual or row-by-row reading first."}
        ],
        "references": [
            {"label": "Britannica: modular arithmetic", "href": "https://www.britannica.com/science/modular-arithmetic", "note": "Background for the modular reading path used by the page."},
            {"label": "MathWorld: Prime Gaps", "href": "https://mathworld.wolfram.com/PrimeGaps.html", "note": "Reference for the spacing language behind the Gaps tab."},
            {"label": "Hardy and Littlewood, Some Problems of Partitio Numerorum (V)", "href": "https://academic.oup.com/plms/article-pdf/s2-22/1/46/4372641/s2-22-1-46.pdf", "note": "Background for the rough benchmark framing used in the Expected tab."}
        ],
        "related_links": [
            {"title": "Open the live Analysis page", "body": "Use the actual Analysis surface once you know which question you want the tabs to answer.", "href": "/analysis#analysis-views-title", "label": "Open Analysis"},
            {"title": "Read the full Analysis Guide", "body": "The longer guide explains each tab in more depth and works better when you want the fuller walkthrough.", "href": "/analysis-guide", "label": "Read the Analysis Guide"},
            {"title": "Step back to prime gaps", "body": "The prime-gaps page helps when your Analysis question is really about spacing language first.", "href": "/prime-gaps", "label": "Read What Are Prime Gaps?"},
            {"title": "Connect it to bounded-gap reading", "body": "The bounded-gaps explainer helps when the Gaps and Expected tabs raise theory questions about near misses versus exact twin primes.", "href": "/what-bounded-gaps-between-primes-actually-proved", "label": "Read What Bounded Gaps Between Primes Actually Proved"}
        ]
    }
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
                "article_link": {
                    "label": "Read more: Arithmetic Progressions Explained For Prime Patterns",
                    "href": "/arithmetic-progressions-primes",
                },
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
                    "label": "Read more: Hardy-Littlewood For Twin Primes",
                    "href": "/hardy-littlewood-twin-primes",
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

