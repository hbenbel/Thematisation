from collections import Counter
from functools import reduce
import re

def shingles(words, k=3):
  for i in range(len(words) - k + 1):
    yield ' '.join(words[i:i+k])

def words(doc_str):
  return doc_str.split(" ") # maybe can be improved ?

def count_ngrams(docs, k_grams=3):
  if isinstance(docs, list):
    counters = map(lambda doc: count_ngrams(doc, k_grams), docs)
    return reduce(lambda acc, new: acc + new, counters, Counter())
  else:
    return Counter(shingles(words(docs), k_grams))

def freqs(doc, k_grams=3):
  docs = re.sub(r'[^\w\s]*','', doc).lower()
  counter = count_ngrams(docs, k_grams)
  counts = counter.values()
  ngrams = counter.keys()
  total = sum(counts)
  freqs = map(lambda c: c / total, counts)
  return list(zip(ngrams, freqs));
