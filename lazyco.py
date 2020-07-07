""" lazyco.py copies files and ignores permission errors """


from pathlib import Path
from argparse import ArgumentParser
import sys
import glob
import os
import shutil
import pprint


def expand_pats(pats):
    res = []
    for p in pats:
        res.extend(glob.glob(p, recursive=True))
    return res


def safe_copy(src, tgt):
    print(f"cp {src} => {tgt}")
    try:
        shutil.copy(src, tgt)
    except PermissionError:
        print(f"EPERM copying '{src}', skipping")
        pass


def main():
    p = ArgumentParser()
    p.add_argument("--from", nargs="+", dest="src", required=True)
    p.add_argument("--to", nargs="+", required=True)
    args = p.parse_args(sys.argv[1:])
    sources = expand_pats(args.src)
    targets = expand_pats(args.to)
    if not targets:
        print("Targets expanded to nothing! Sources:")
        pprint.pprint(sources)
        pprint.pprint(args.src)
    pairs = [(s, t) for s in sources if os.path.isfile(s) for t in targets]
    for src, tgt in pairs:
        safe_copy(src, tgt)


if __name__ == "__main__":
    main()

