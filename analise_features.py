from Bio import SeqIO

record = SeqIO.read('sequence.gb', 'genbank')
featcds = []
featgene= []
otherfeat = []
for i in range(len(record.features)):
    if record.features[i].type == 'CDS':
        featcds.append(i)
    elif record.features[i].type == 'gene':
        featgene.append(i)
    else:
        otherfeat.append(i)

f = open('sequence.txt', 'r')
table = []
for line in f.readlines():
    table.append(line.split('\t'))
    f.close()

CDS_protein = []
CDS_geneID = []
for i in record.features:
    if i.type == 'CDS':
        CDS_protein.append(i.qualifiers['protein_id'][0])
        CDS_geneID.append(i.qualifiers['db_xref'][1].strip('GeneID:'))
        
print(CDS_protein)
print(CDS_geneID)