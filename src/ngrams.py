from collections import Counter
from functools import reduce
import re
import math

# Generate k-grams from a string
def shingles(string, k=3):
  tokens = tokenize(string)
  for i in range(len(tokens) - k + 1):
    yield ' '.join(tokens[i:i+k])

# Cleanup and prepare the input for shingles
def tokenize(doc_str):
  clean_doc = re.sub(r'[^\w\s]',' ', doc_str).lower()
  return clean_doc.split()

# Counts each ngrams occurences in docs
def count_ngrams(docs, k_grams=3):
  if isinstance(docs, Counter): # Counters are pre-computed results, just return those
    return docs
  elif isinstance(docs, list):  # List should be counted recursively
    counters = map(lambda doc: count_ngrams(doc, k_grams), docs)
    return reduce(lambda acc, new: acc + new, counters, Counter())
  else:                         # In other cases (i.e strings), count the kgrams
    return Counter(shingles(docs, k_grams))

# From a counter of ngrams
# Outputs a dict wich associates each ngram with its frequency (like tf)
def counter_to_freqs(counter):
  counts = counter.values()
  total = sum(counts)
  freqs = map(lambda c: c / total, counts)
  return dict(zip(counter.keys(), freqs))

# From a map of theme to counter (a counter of ngrams per theme)
# Outputs an inverse frequency (like idf but across themes rather than documents)
def counters_to_inv_freqs(thm_counters):
  nbthms = len(thm_counters)
  thm_ngrams = {}
  for thm in thm_counters:
    thm_ngrams[thm] = set(thm_counters[thm])
  ngrams = set.union(*thm_ngrams.values())
  itf = {}
  for ng in ngrams:
    denom = sum(map(lambda x: 1 if ng in x else 0, thm_ngrams.values())) 
    itf[ng] = math.log(nbthms / denom) if denom > 0 else -1
  return itf

def scores(thm_docs, k_grams=3):
  thm_counters = {}
  for thm in thm_docs:
    thm_counters[thm] = count_ngrams(thm_docs[thm], k_grams)

  # initialize scores to frequency within the theme
  thm_scores = {}
  for thm in thm_counters:
    thm_scores[thm] = counter_to_freqs(thm_counters[thm])

  # if there is more than 1 theme, adjust scores with inverse frequency
  if len(thm_counters) > 1:
    itf = counters_to_inv_freqs(thm_counters)
    for freq_dict in thm_scores.values():
      for ng in freq_dict:
        freq_dict[ng] *= itf[ng]
  return thm_scores
