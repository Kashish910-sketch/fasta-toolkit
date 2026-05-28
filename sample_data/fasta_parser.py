def read_fasta(file_path):
    sequences = {}

    with open(file_path, "r") as file:
        current_header = ""

        for line in file:
            line = line.strip()

            if line.startswith(">"):
                current_header = line[1:]
                sequences[current_header] = ""
            else:
                sequences[current_header] += line

    return sequences
