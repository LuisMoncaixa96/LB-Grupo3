from Bio.Blast import NCBIXML

def parse(file, E_VALUE_THRESH):
    '''
    VARIAVEIS:
        file = Nome do ficheiro a dar com o resultado do Blast ( ex: "FGB_blast.xml")
        E_VALUE_THRESH = Recebe valor None ou qualquer numero inteiro, corresponde ao valor de e-value maximo
        aceitável para tratamento do output do blast.
    RETURNS:
        Devolve uma lista dos resultados do blast filtrados pelo e-value, com o nome do alinhamento, comprimento
        do alinhamento e e-value
    '''
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
    '''
    VARIAVEIS:
        parsed_list = Lista devolvida filtrada pela função parse
    RETURNS:
        Lista de Acession numbers filtrados pelo tipo gb e sem repetições.
    '''
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

x = parse('blastProtein(ACE2)', E_VALUE_THRESH=None)
ListaProt = isol_Prot(x)
with open('id_list_prot(ACE2).txt', 'w') as f:
        for item in ListaProt:
            f.write("%s\n" % item)
