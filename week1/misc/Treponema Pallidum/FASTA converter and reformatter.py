from Bio import SeqIO
import os

# 1. Setup paths
input_file = ".fastq"
# This trick automatically changes .fastq to .fasta
output_file = input_file.replace(".fastq", ".fasta")

print(f"Converting {input_file} to FASTA format...")

# 2. The Conversion Engine
# We use 'with' to make sure the file closes properly at the end
with open(output_file, "w") as out_handle:
    # Bio.SeqIO.convert is a high-speed "Power Tool" 
    # that does the loop for you!
    count = SeqIO.convert(input_file, "fastq", out_handle, "fasta")

print("-" * 30)
print(f"Conversion Complete!")
print(f"Total sequences written: {count}")
print(f"New file created: {os.getcwd()}\\{output_file}")