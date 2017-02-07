file_location = raw_input("Where is your FASTA file? ")
head = []
body = []
N = 0
with open(file_location) as f:
    content = f.readlines()
for i in content:
    if i.startswith(">"):
        head[N] = i
        N += 1
    elif i == "":
        break
