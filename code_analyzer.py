# write your code here
import sys
import os
import re


def s001(_res, _count, _line, _fpath):
    if len(_line) > 79:
        _res += f"{_fpath}: Line {_count}: S001 Too long",


def s002(_res, _count, _line, _fpath):
    ind = next(i for i, c in enumerate(_line) if c != " ")
    if ind % 4 != 0:
        _res += f"{_fpath}: Line {_count}: S002 Indentation is not a multiple of four",


def s003(_res, _count, _line, _fpath):
    _line = re.sub('#.*', "", _line).strip()
    if _line and _line[-1] == ";":
        _res += f"{_fpath}: Line {_count}: S003 Unnecessary semicolon after a statement",


def s004(_res, _count, _line, _fpath):
    match = re.search("#", _line.strip())
    if match:
        ind = match.span()[0]
        if ind and _line[ind-2:ind] != '  ':
            _res += f"{_fpath}: Line {_count}: S004 Less than two spaces before inline comments",


def s005(_res, _count, _line, _fpath):
    if re.search("#", _line):
        _line = re.sub('.*#', "", _line).strip().lower()
        if re.search("todo", _line):
            _res += f"{_fpath}: Line {_count}: S005 TODO found",


def s006(_res, _count, _fpath):
    _res += f"{_fpath}: Line {_count}: S006 More than two blank lines preceding a code line",


def analyzer(_res, _file):
    count = 0
    with open(_file, 'r') as f:
        empty = 0
        for line in f:
            count += 1
            if line == "\n":
                empty += 1
            else:
                s001(_res, count, line, _file)
                s002(_res, count, line, _file)
                s003(_res, count, line, _file)
                s004(_res, count, line, _file)
                s005(_res, count, line, _file)

                if empty > 2:
                    s006(_res, count, _file)

                empty = 0


arg = sys.argv[1]

res = []
if os.path.isdir(arg):
    for file in sorted(os.listdir(arg)):
        if re.match(r".+\.py", file):
            analyzer(res, arg + "/" + file)
elif os.path.isfile(arg):
    analyzer(res, arg)


for x in res:
    print(x)
