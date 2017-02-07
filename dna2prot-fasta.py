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
