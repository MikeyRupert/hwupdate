
from collections import Counter
dna = ('AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC')
print('\nthymine:(T)~(A):adenine|\t|guanine(G)~(C)cytosine\n',f'\n{list(Counter(dna).most_common())}\n')


