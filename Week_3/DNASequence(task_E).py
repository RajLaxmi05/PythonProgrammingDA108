dna_sequence = "ATGTACTC ATTCGTTTCG GAAGAGACAG GTACGTTAAT AGTTAATAGC GTACTTCTTT TTCTTGCTTT CGTGGTATTC TTGCTAGTTA CACTAGCCAT CCTTACTGCG CTTCGATTGT GTGCGTACTG CTGCAATATT GTTAACGTGA GTCTTGTAAA ACCTTCTTTT TACGTTTACT CTCGTGTTAA AAATCTGAAT TCTTCTAGAG TTCCTGATCT TCTGGTCTAA"

reversed_sequence = ""
for sequence in dna_sequence.split():
    if len(sequence) == 8:
        reversed_sequence += sequence[::-1] + " "
    else:
        reversed_sequence += sequence + " "

print("Reversed sequence:", reversed_sequence)
print("Occurence of TTACT:", dna_sequence.count("TTACT"))
