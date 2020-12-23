from Bio.Blast import NCBIXML

def isol_AC(lista, id):
    '''
    VARIAVEIS:
        id = id associado ao gene a ser tratado
        lista = Lista devolvida filtrada pela função obter_x
    RETURNS:
        Lista de Acession numbers filtrados pelo tipo gb e sem repetições.
    '''
    DicAC = {}
    DicAC[id] = 1
    for hit in lista:
        c = []
        for y in range(len(hit)):
            if hit[y] == '|':
                c.append(y)
        type = hit[c[1]+1 : c[2]]
        if type == "gb":
            y = hit[c[2]+1 : c[3]]
            if y not in DicAC:
                DicAC[y] = 1
    ListAC = list(DicAC.keys())
    return ListAC

def obter_lista(file, E_VALUE_THRESH):
    '''
    VARIAVEIS:
        file = Nome do ficheiro a dar com o resultado do Blast ( ex: "FGB_blast.xml")
        E_VALUE_THRESH = Recebe valor None ou qualquer numero inteiro, corresponde ao valor de e-value maximo
        aceitavel para tratamento do outpur do blast.
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
    result_handle.close()
    return FILE

def DNA(id, file, E_VALUE_THRESH = None):
    '''
    VARIAVEIS:
        id = id associado ao gene a ser tratado
        file = Nome do ficheiro derivado do Blast
        E_VALUE_THRESH = Recebe valor None ou qualquer numero inteiro, corresponde ao valor de e-value maximo
        aceitavel para tratamento do outpur do blast.
    RETURNS:
        Gera um ficheiro .txt contendo os Acession Number dos resultados do blast com filtração segundo o
        E_VALUE_THRESH e "gb".
    '''

    x = obter_lista(file, E_VALUE_THRESH)
    ListAC = isol_AC(x, id)
    with open('id_listDNA(ACE2).txt', 'w') as f:
        for item in ListAC:
            f.write("%s\n" % item)


DNA(59272, 'ACE2blast.xml')