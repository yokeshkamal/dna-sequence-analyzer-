# DNA Sequence Analyzer
sequence = input("Enter DNA sequence: ").upper()

A = sequence.count("A")
T = sequence.count("T")
G = sequence.count("G")
C = sequence.count("C")

total = len(sequence)

gc_content = ((G + C) / total) * 100

# DNA → RNA
rna = sequence.replace("T", "U")

# Reverse DNA
reverse_dna = sequence[::-1]

print("\nNucleotide Count")
print("A:", A)
print("T:", T)
print("G:", G)
print("C:", C)

print("\nGC Content:", round(gc_content, 2), "%")

print("\nRNA Sequence:", rna)

print("\nReverse DNA Sequence:", reverse_dna)