<h1 align="center"> Code-Plagiarism-Detector</h1>

A hybrid plagiarism detection tool for Python code.
It combines Data Structures & Algorithms (DSA) (AST parsing, tree diff, structural hashing) with Machine Learning (ML) (TF-IDF + cosine similarity) to detect code similarity, even if variables are renamed or formatting is changed.

⸻

Features
**•	AST-based structural comparison (DSA)**

•	Parses Python code into Abstract Syntax Trees (AST).
•	Compares structure of functions/classes using tree edit distance and line diffs.
•	Detects disguised plagiarism (e.g., renaming variables, reordering).


**•	ML-based text similarity**

•	Uses TF-IDF vectorization + cosine similarity.
•	Captures token-level similarity between reference and candidate code. 
•	Robust against comments, spacing, and simple edits.


**•	Hybrid scoring**

•	Combines AST (60%) + TF-IDF (40%) into one unified plagiarism score. 
•	Gives a more balanced judgment (structural + textual).


**•	CLI Tool**

•	Run directly from the terminal.
•	Shows per-file plagiarism percent, TF-IDF score, and hybrid score.


**Project Structure**
```text
Code-Plagrism-Detector/
│
├── pycode_similar.py       # Main script (AST + ML hybrid comparison)
├── ml_scorer.py            # ML layer (TF-IDF, cosine similarity)
├── examples/
│   ├── ref.py              # Example reference code
│   └── cand.py             # Example candidate code
├── requirements.txt        # Python dependencies
└── README.md               # Documentation
```

**Installation**
	1.	Clone this repo:
```text
git clone https://github.com/Emma8762/Code-Plagrism-Detector.git
cd Code-Plagrism-Detector
```

2.	Create a virtual environment (recommended):
```text
python -m venv venv
source venv/bin/activate       # Mac/Linux
.\venv\Scripts\activate        # Windows
```
3.	Install dependencies:
```text
pip install -r requirements.txt
```

**Usage**

Run plagiarism detection between a reference file and one/more candidate files:
```text
python pycode_similar.py examples/ref.py examples/cand.py
```
Example Output:
```text
ref: examples/ref.py
candidate: examples/cand.py
100.00 % (26/26) of ref code structure is plagiarized by candidate.
TF-IDF cosine similarity: 0.6467
Combined hybrid similarity (AST 60% + TF-IDF 40%): 0.8587
```
**Testing with Examples**

Example 1 — Identical Code
	•	AST = 100% match
	•	TF-IDF = ~1.0
	•	Hybrid = ~1.0

Example 2 — Variable Renaming
```text
def add(a, b): return a + b
def add(x, y): return x + y
```
	
•	AST = High (structure same)
	•	TF-IDF = Medium (~0.6)
	•	Hybrid = ~0.85

Example 3 — Completely Different Code
	•	AST = Low (<20%)
	•	TF-IDF = Low (~0.1)
	•	Hybrid = Low



**Dependencies**
	•	scikit-learn → TF-IDF & cosine similarity
	•	zss → tree edit distance
	•	Python standard libraries: ast, difflib, argparse, etc.

**License**

MIT License. Free to use and modify.
