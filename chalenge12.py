from itertools import permutations

def Permutation(n, k):
    nums = [str(i) for i in range(1, n + 1)]
    perms = list(permutations(nums))
    perms.sort()
    return "".join(perms[k - 1])
print(Permutation(4, 8))  

#the itertools.permutations function generates all possible arrangements of the input elements.