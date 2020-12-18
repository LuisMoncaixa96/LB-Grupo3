from Bio.Blast import NCBIWWW
from Bio import SeqIO
record = SeqIO.read(open("sequenceS.gb"), format="genbank")
result_handle = NCBIWWW.qblast("blastp", "nt", record.format("genbank"))
print (result_handle)