import sys

file = sys.argv[1]

reads = 0
lengths = []

with open(file) as f:
    for i, line in enumerate(f):
        if i % 4 == 1:  # sequence line in FASTQ
            seq = line.strip()
            reads += 1
            lengths.append(len(seq))

print("Sample:", file)
print("Reads:", reads)
print("Avg length:", sum(lengths)/len(lengths))