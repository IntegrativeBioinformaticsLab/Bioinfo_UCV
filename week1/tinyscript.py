from Bio import SeqIO

#defining variable
count=0


#prints top of table
print(f"{'ID':<45} {'Len':<8} {'Info'}")
print("-"*100)

#loop goes through file

for record in SeqIO.parse(".fastq", "fastq"):count=count+1

#getting ID
sample_id = record.id

#getting length
read_length=len(record.seq)

#getting info
sample_info=record.description

#printing row of table
print(f"{record.id:<45} {len(record.seq):<8} {record.description}")
#summary

print("-"*100)
print(f"Total Reads: {count}")
