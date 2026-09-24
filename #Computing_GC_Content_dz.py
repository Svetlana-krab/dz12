#Computing GC Content
def gc_content(dna: str) -> float:
    g = dna.count('G')
    c = dna.count('C')
    return (g+c) / len(dna) * 100

file=open("Computing_GC_Content.txt", "r", encoding="utf-8")
data = file.read()
file.close()

blocks = data.split('>')[1:]

max_id = None
max_gc = 0

for block in blocks:
    lines = block.strip().split('\n')
    seq_id = lines[0]
    dna = ''.join(lines[1:])
    
    gc = gc_content(dna)
    
    if gc > max_gc:
        max_gc = gc
        max_id = seq_id

print(max_id)
print(f"{max_gc:.6f}")      #с 6 знаками после .