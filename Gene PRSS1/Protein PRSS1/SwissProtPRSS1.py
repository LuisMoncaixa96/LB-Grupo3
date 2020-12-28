import Bio.SwissProt as sp
with open('P07477.txt') as handle:
    records = sp.parse(handle)
    for record in records:
        a1 = "Gen_Name:" +  str(record.gene_name)
        a2 = "\nEntry_name:" + str(record.entry_name)
        a3 = "\nSeq_length:" + str(record.sequence_length)
        a4 = "\nOrganismClass:" + str(record.organism_classification)
        a5 = "\nOrganism:" + str(repr(record.organism))
        a6 = "\nTaxonomy:" + str(record.taxonomy_id)
        #print(record.description)
        a8 = "\nFunction:" + str(record.comments[0])
        ficheiro = open("SwissProt_PRSS1.txt",'w')
        ficheiro.write(a1)
        ficheiro.write(a2)
        ficheiro.write(a3)
        ficheiro.write(a4)
        ficheiro.write(a5)
        ficheiro.write(a6)
        ficheiro.write(a8)
        ficheiro.close()
        

