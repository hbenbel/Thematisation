import os.path
import sys.stdin
from glob import iglob as glob
from shlex import split as shplit

def parse(*paths):
  if not paths:
    return parse_file(sys.stdin)
  thematics = {}
  for path in paths:
    dirname = os.path.dirname(path)
    with open(path, 'r') as f:
      new_themas = parse_file(f, dirname)
      for th in new_themas:
        add_files_to_thematic(thematics, th, *new_themas[th])
  return thematics

def parse_file(f, dirname=''):
  thematics = {}
  for line in f:
    thema, *patts = shplit(line)
    files = [fi for pattern in patts for fi in find_files(pattern, dirname, thema)]
    add_files_to_thematic(thematics, thema, *files)
  return thematics

def add_files_to_thematic(all_ths, thema, *files):
  if thema not in all_ths:
    all_ths[thema] = set()
  all_ths[thema].update(files)

def find_files(pattern, dirname, thematic):
  files = [os.path.relpath(fi) for fi in glob(os.path.join(dirname, pattern)) if os.path.isfile(fi)]
  if not files:
    print("WARNING: This pattern did not match any file (Th: '{}'): {}".format(thematic, pattern));
  return files
