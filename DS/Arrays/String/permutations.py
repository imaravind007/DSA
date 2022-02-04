from itertools import permutations
def find_permutation(self, S):
        # Code here
        # S=''.join(sorted(S))
        
        l=list(''.join(i) for i in permutations(S))
        return l