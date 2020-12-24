from Bio import SeqIO
from Bio.Blast import NCBIWWW

def get_prot(id):
    
    from Bio import ExPASy
    with ExPASy.get_sprot_raw(id) as handle:
        seq_record = SeqIO.read(handle, "swiss")
    tam= len(seq_record.seq)
    seq= seq_record.seq
    tax= seq_record.annotations["taxonomy"]
    org= seq_record.annotations["organism"]
    #host= seq_record.annotations["organism_host"]
    y = ('ID:' + id + '|' + 'SEQUENCE:' + seq + '|' + 'SEQUENCE LENGTH:' + str(tam) + 'bp' + '|' + 'TAXONOMY:' + str(tax) + '|' + 'ORGANISM:' + org )
    return y

def filtro(seq):
    
    seq = seq.split('|')
    return seq

idPRSS1 = 'P07477' #ID na swissprot do PRSS1
x = get_prot(idPRSS1)
seq = filtro(x)
result_handle = NCBIWWW.qblast('blastp', 'nr', seq)
with open('blastProtein(PRSS1)', "w") as out_handle:
    out_handle.write(result_handle.read())
result_handle.close()
