# ml_scorer.py
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def code_to_text(code_str):
    # remove Python comments
    code = re.sub(r'#.*', ' ', code_str)
    # remove multi-line string literals (docstrings)
    code = re.sub(r'("""|\'\'\')(.*?)(?:"""|\'\'\')', ' ', code, flags=re.S)
    # replace non-word chars with space
    code = re.sub(r'[^0-9A-Za-z_]+', ' ', code)
    return code

def tfidf_pair_score(ref_code, cand_code):
    a = code_to_text(ref_code)
    b = code_to_text(cand_code)
    vec = TfidfVectorizer(token_pattern=r'\w+').fit([a, b])
    tfidf = vec.transform([a, b])
    sim = cosine_similarity(tfidf[0], tfidf[1])[0, 0]
    return float(sim)

def batch_tfidf_scores(pycode_string_list):
    if len(pycode_string_list) < 2:
        return []
    texts = [code_to_text(s) for s in pycode_string_list]
    vec = TfidfVectorizer(token_pattern=r'\w+').fit(texts)
    tfidf = vec.transform(texts)
    ref = tfidf[0]
    results = []
    for i in range(1, len(texts)):
        sim = cosine_similarity(ref, tfidf[i])[0, 0]
        results.append((i, float(sim)))
    return results
  