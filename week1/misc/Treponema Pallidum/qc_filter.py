from Bio import SeqIO

# Define your input and output
input_file = ".fastq"
output_file = "filtered_reads.fastq"

count_kept = 0
count_total = 0

# Open the output file for writing
with open(output_file, "w") as out_handle:
    for record in SeqIO.parse(input_file, "fastq"):
        count_total += 1
        
        # Calculate average quality score for the whole read
        qualities = record.letter_annotations["phred_quality"]
        avg_qual = sum(qualities) / len(qualities)
        
        # Keep the read if avg_qual is 20 or higher
        if avg_qual >= 9:
            SeqIO.write(record, out_handle, "fastq")
            count_kept += 1

print(f"Done! Processed {count_total} reads.")
print(f"Kept {count_kept} high-quality reads.")
print(f"Discarded {count_total - count_kept} low-quality reads.")