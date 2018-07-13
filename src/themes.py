#! /usr/bin/python

import ngrams
import os
import parser
import re
import sys

def parse_args():
  if len(sys.argv) < 2:
    print('USAGE: ./themes.py K CONFIG_FILES*')
    print('   - k is the size of k-grams')
    print('   - if no config file is provided, the program reads from stdin')
    print('   - see the README for more details on config files')
    sys.exit(1)
  k, cfs = int(sys.argv[1]), sys.argv[2:]
  if k < 1:
    print('ERROR: k must be > 0')
    sys.exit(1)
  # more invalid input checking can be done here but we
  # assume that the user feeds valid input to the program
  return k, cfs

def open_all_files(themes_files):
  themes = {}
  for th in themes_files:
    themes[th] = []
    for path in themes_files[th]:
      with open(path, 'r') as f:
        themes[th].append(f.read())
  return themes

def to_filename(string, ext):
  fname = re.sub(r'[^\w]', '_', string).lower()
  return '.'.join([fname, ext])

def write_outputs(scores):
  for th in scores:
    fname = to_filename(th, ext='thm')
    with open(fname, 'w') as f:
      f.write(th + os.linesep)
      for ngs in scores[th]:
        f.write(ngs[0] + '\t' + str(ngs[1]) + os.linesep)

if __name__ == "__main__":
  kgrams, confs = parse_args()
  input_files = parser.parse_confs(*confs);
  themes_strings = open_all_files(input_files)
  scores = ngrams.scores(themes_strings, kgrams)
  for th in scores:
    scores[th] = sorted(list(scores[th].items()), key=lambda x: x[1], reverse=True)
  write_outputs(scores)
