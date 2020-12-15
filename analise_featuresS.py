from Bio import SeqIO

record = SeqIO.read('sequenceS.gb', 'genbank')
print(record.id)
print(record.seq)
print (record.description)     
print (record.name)    
print (len(record.seq))
print('-------------------------------------')
print (record.annotations)
print (record.letter_annotations) #não existem
print('-------------------------------------')
print (record.features)

featcds = []
featgene = []
featothers = []

for i in range(len(record.features)):
    if record.features[i].type == "CDS":
        featcds.append(i)
    elif record.features[i].type == 'gene':
        featgene.append(i)
    else:
        featothers.append(i)
        
for k in featcds:
    print (record.features[k].location)
    
for k in featcds:
    print(record.features[k].extract(record.seq))
    


