from Bio.Blast import NCBIXML

def parse(file, E_VALUE_THRESH):

    result_handle = open(file)
    blast_record = NCBIXML.read(result_handle)
    FILE = []
    if E_VALUE_THRESH == None:
        E_VALUE_THRESH = 0.05
    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:
            if hsp.expect < E_VALUE_THRESH:
                y = alignment.title + '|' + str(alignment.length) + '|' + str(hsp.expect)
                FILE.append(y)
    return FILE

def isol_Prot(parsed_list):

    DicAC = {}
    for hit in parsed_list:
        c = []
        for y in range(len(hit)):
            if hit[y] == '|':
                c.append(y)
        type = hit[0: c[0]]
        if type == "gb":
            k = hit[c[0]+1 : c[1]]
            if k not in DicAC:
                DicAC[k] = 1
    ListProt = list(DicAC.keys())
    return ListProt

x = parse('blastProtein(S)', E_VALUE_THRESH=None)
ListaProt = isol_Prot(x)
with open('id_list_prot(S).txt', 'w') as f:
        for item in ListaProt:
            f.write("%s\n" % item)