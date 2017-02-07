RNA_codon_table = {
# 			Second Base
#    U 	         C           A           G
# U
'UUU': 'F', 'UCU': 'S', 'UAU': 'Y', 'UGU': 'C', # UxU
'UUC': 'F', 'UCC': 'S', 'UAC': 'Y', 'UGC': 'C', # UxC
'UUA': 'L', 'UCA': 'S', 'UAA': '*', 'UGA': '*', # UxA
'UUG': 'L', 'UCG': 'S', 'UAG': '*', 'UGG': 'W', # UxG
# C
'CUU': 'L', 'CCU': 'P', 'CAU': 'H', 'CGU': 'R', # CxU
'CUC': 'L', 'CCC': 'P', 'CAC': 'H', 'CGC': 'R', # CxC
'CUA': 'L', 'CCA': 'P', 'CAA': 'Q', 'CGA': 'R', # CxA
'CUG': 'L', 'CCG': 'P', 'CAG': 'Q', 'CGG': 'R', # CxG
# A
'AUU': 'I', 'ACU': 'T', 'AAU': 'N', 'AGU': 'S', # AxU
'AUC': 'I', 'ACC': 'T', 'AAC': 'N', 'AGC': 'S', # AxC
'AUA': 'I', 'ACA': 'T', 'AAA': 'K', 'AGA': 'R', # AxA
'AUG': 'M', 'ACG': 'T', 'AAG': 'K', 'AGG': 'R', # AxG
# G
'GUU': 'V', 'GCU': 'A', 'GAU': 'D', 'GGU': 'G', # GxU
'GUC': 'V', 'GCC': 'A', 'GAC': 'D', 'GGC': 'G', # GxC
'GUA': 'V', 'GCA': 'A', 'GAA': 'E', 'GGA': 'G', # GxA
'GUG': 'V', 'GCG': 'A', 'GAG': 'E', 'GGG': 'G'  # GxG
}

def rev_complement(seq):
    return seq[::-1]

file_location = raw_input("Where is your FASTA file? ")
stripped = []
metadata = []
sequence = []
N = 0
with open(file_location) as f: #opens file
    lines = f.readlines() #defines file under content
for i in lines:
    stripped.append(i.rstrip("\n"))
for i in stripped:
    if i.startswith(">"): #identifies metadata
        metadata.append(i) #stores metadata
        DNA = "" #resets DNA
    elif i == "": #identifies end of sequence
        sequence.append(DNA) #appends concatenated DNA to sequence[]
        N+=1 #iterates counter that may not really be needed
    else: 
        DNA = DNA + i #concatenates new DNA line with earlier lines
for i in range(0,N):
    #print metadata[i]
    print sequence[i]
