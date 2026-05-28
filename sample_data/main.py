from fasta_parser import read_fasta

fasta_file = "sample_data/test_sequences.fasta"

sequences = read_fasta(fasta_file)

for header, sequence in sequences.items():
    print(f">{header}")
    print(sequence)
    print()
