from itertools import groupby


def compress_string(s):
    groups = []
    uniquekeys = []
    for k, g in groupby(s):
        groups.append(len(list(g)))
        uniquekeys.append(int(k))
    return list(zip(groups, uniquekeys))

