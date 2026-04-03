


from Bio import SeqIO
import matplotlib.pyplot as plt


lengths = []

records = list(SeqIO.parse(".fastq", "fastq"))

for record in records:
    lengths.append(len(record.seq))





#vizualisation

plt.hist(lengths, bins=50, color='skyblue', edgecolor='black')
plt.yscale('log') # makes us see small baars
plt.title("Read Length Distribution")
plt.xlabel("Length (bp)")
plt.ylabel("Count (Log Scale)")
plt.savefig("read_length_histogram.png")

#identifying species using BLAST (using first long read)
SeqIO.write(records[0], "query_for_blast.fasta", "fasta")
print(f"Graph saved. Total reads analyzed: {len(lengths)}")
print("File 'query_for_blast.fasta' is ready for BLAST.")
