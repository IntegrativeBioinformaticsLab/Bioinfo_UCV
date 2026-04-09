from Bio import SeqIO

#defining variable
count=0


#prints top of table
print(f"{'ID':<45} {'Len':<8} {'Info'}")
print("-"*100)



#Loop
for record in SeqIO.parse(filename, "fastq"):
    count += 1
    
    # Extract data from the current record
    sample_id = record.id
    read_length = len(record.seq)
    sample_info = record.description

#printing row of table
print(f"{record.id:<45} {len(record.seq):<8} {record.description}")
#summary

print("-"*100)
print(f"Total Reads: {count}")
