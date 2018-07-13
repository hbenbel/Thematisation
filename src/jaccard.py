#! /usr/bin/python

from ngrams import shingles
import parser
import sys

def parse_args():
  if len(sys.argv) < 3:
    print('USAGE: ./jaccard.py K FILE THEME_FILES*')
    print('   - k is the size of k-grams')
    print('   - file is the file to classify')
    print('   - theme files contain ngrams information about themes (cf README)')
    sys.exit(1)
  k, f, thms = int(sys.argv[1]), sys.argv[2], sys.argv[3:]
  if k < 1:
    print('ERROR: k must be > 0')
    sys.exit(1)
  # more invalid input checking can be done here but we
  # assume that the user feeds valid input to the program
  return k, f, thms

def jaccard_index(s1, s2):
  return len(s1 & s2) / len(s1 | s2)

if __name__ == "__main__":
  kgrams, file_to_classify, theme_files = parse_args()
  with open(file_to_classify, 'r') as f:
    ngrams = set(shingles(f.read(), kgrams))
  themes = parser.parse_themes(*theme_files)
  jacidx = sorted(map(lambda t: (t, jaccard_index(themes[t], ngrams)), themes), key=lambda x: x[1], reverse=True)
  for th, dist in jacidx:
    print(th,"==>", str(dist))
