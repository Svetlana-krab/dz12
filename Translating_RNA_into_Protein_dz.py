#Translating RNA into Protein
def load_codon_table(filename: str)-> dict:
    table = {}
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split()
            if len(parts)>=2:
                table[parts[0]]=parts[1]
    return table
def translate_rna(rna, table):
    protein = ""
    for i in range(0,len(rna),3):
        codon = rna[i:i+3]
        amino = table[codon]
        if amino == 'Stop':
            break
        protein += amino
    return protein
rna = input().upper().strip()
table=load_codon_table("/home/user/Документы/dz12/amino_acids.txt")
print(translate_rna(rna,table))