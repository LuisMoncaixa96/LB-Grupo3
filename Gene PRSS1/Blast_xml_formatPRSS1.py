from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from Bio import SeqIO

record = SeqIO.read(open('sequencePRSS1.gb'), format='gb' )

result_handle = NCBIWWW.qblast('blastn', 'nt', record.seq)

with open("PRSS1blast.xml", "w") as out_handle:
    out_handle.write(result_handle.read())

result_handle.close()
