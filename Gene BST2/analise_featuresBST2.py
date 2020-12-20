from Bio import SeqIO

record = SeqIO.read('sequenceBST2.gb', 'genbank')
#Informação sobre a seqência
print(record.id, '\n')
print(record.seq, '\n')
print (record.description, '\n')     
print (record.name, '\n')    
print (len(record.seq), '\n')
print(record.dbxrefs, '\n')
print(record.annotations["source"], '\n' )
#anotações, features e qualifiers
for k,v in record.annotations.items():
    print(k,v)
print('\n',len(record.features), '\n')
for i in record.features:
    print(i)
print('\n', record.features, '\n')