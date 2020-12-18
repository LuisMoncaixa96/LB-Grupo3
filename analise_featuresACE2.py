from Bio import SeqIO

record = SeqIO.read('sequenceACE2.gb', 'genbank')
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

from Bio import SeqIO
gb_file = "sequenceACE2.gb"
for gb_record in SeqIO.parse(open(gb_file,"r"), "genbank") :
    # now do something with the record
    print ("Name %s, %i features" % (gb_record.name, len(gb_record.features)))
    print (repr(gb_record.seq))


def index_genbank_features(gb_record, feature_type, qualifier) :
    answer = dict()
    for (index, feature) in enumerate(gb_record.features) :
        if feature.type==feature_type :
            if qualifier in feature.qualifiers :
                #There should only be one locus_tag per feature, but there
                #are usually several db_xref entries
                for value in feature.qualifiers[qualifier] :
                    if value in answer :
                        print ("WARNING - Duplicate key %s for %s features %i and %i" \
                           % (value, feature_type, answer[value], index))
                    else :
                        answer[value] = index
    return answer

locus_tag_cds_index = index_genbank_features(gb_record,"CDS","locus_tag")
print(locus_tag_cds_index)

db_xref_cds_index = index_genbank_features(gb_record,"CDS","db_xref")
print(db_xref_cds_index)

gb_feature = gb_record.features[21]
print(gb_feature)