from collections import defaultdict

def group_anagrams(a):
    dfdict = defaultdict(list)
    for i in a:
        sorted_i = " ".join(sorted(i))
        print(sorted_i)
        dfdict[sorted_i].append(i)
    return dfdict.values()
words = ["tea", "eat", "bat", "ate", "arc", "car"]
print(group_anagrams(words))