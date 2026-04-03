from Bio import SeqIO
import matplotlib.pyplot as plt

filename = "filtered_reads.fastq"
gc_values = []

print("Analyzing GC content... please wait.")

for record in SeqIO.parse(filename, "fastq"):
    sequence = record.seq
    
    # Count G and C (case-insensitive just in case)
    g_count = sequence.count("G") + sequence.count("g")
    c_count = sequence.count("C") + sequence.count("c")
    
    # Calculate percentage
    gc_percent = (g_count + c_count) / len(sequence) * 100
    gc_values.append(gc_percent)

plt.hist(gc_values, bins=100, color='orangered', edgecolor='black')
plt.title("GC Content Distribution (18S Control)")
plt.xlabel("GC Percentage (%)")
plt.ylabel("Number of Reads")

# Calculate the average from your list
avg_gc = sum(gc_values) / len(gc_values)

# Print it clearly
print(f"Done! Total Reads: {len(gc_values)}")
print(f"Average GC Content: {avg_gc:.2f}%")