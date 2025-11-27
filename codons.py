def create_codon_dict(file_path):
    path = file_path
    file = open(path)
    rows = file.readlines()
    file.close()
    dictionary = {}
    codon = []
    amino_acids = []
    for r in rows:
        row = r.strip().split('\t')
        codon = row[0]
        amino_acids =row[2]
        dictionary[codon] = amino_acids

    return dictionary


