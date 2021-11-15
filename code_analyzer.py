# write your code here
import re
count = 0


def s001(_res, _count, _line):
    if len(_line) > 79:
        _res += f"Line {_count}: S001 Too long",


def s002(_res, _count, _line):
    ind = next(i for i, x in enumerate(_line) if x != " ")
    if ind % 4 != 0:
        _res += f"Line {_count}: S002 Indentation is not a multiple of four",


def s003(_res, _count, _line):
    semicolon = False
    last = True
    found_last = False
    for i in reversed(_line):
        if not found_last and i not in [";", " ", "\n"]:
            last = False
            found_last = True
        if i == ";":
            semicolon = True
            if not found_last:
                found_last = True
                last = True
        if i == "#":
            semicolon = False
            found_last = False
            last = True

    if semicolon and last:
        _res += f"Line {_count}: S003 Unnecessary semicolon after a statement",


def s004(_res, _count, _line):
    try:
        ind = _line.index("#")
    except ValueError:
        ind = None

    if ind:
        if _line[ind-2:ind] != '  ':
            _res += f"Line {_count}: S004 Less than two spaces before inline comments",


def s005(_res, _count, _line):
    try:
        ind = _line.index("#")
    except ValueError:
        ind = -1

    if ind >= 0:
        if "todo" in line[ind:].lower():
            _res += f"Line {_count}: S005 TODO found",


def s006(_res, _count):
    _res += f"Line {_count}: S006 More than two blank lines preceding a code line",


with open(input(), 'r') as f:
    res = []
    empty = 0
    for line in f:
        count += 1
        if line == "\n":
            empty += 1
        else:
            s001(res, count, line)
            s002(res, count, line)
            s003(res, count, line)
            s004(res, count, line)
            s005(res, count, line)

            if empty > 2:
                s006(res, count)
                first = False
                empty = 0


for x in res:
    print(x)
