from itertools import permutations

words, length = input().split()

perm = list(permutations(words, int(length)))
perm.sort()

for letters in perm:
    print("".join(letters))
