from Bio import Entrez
from Bio import Medline
Entrez.email = "pg42874@alunos.uminho.pt"
handle = Entrez.egquery(term = "PRSS1")
record = Entrez.read(handle)
for row in record["eGQueryResult"]:
    if row["DbName"]=="pubmed":
        total = row["Count"]

handle = Entrez.esearch(db = "pubmed", term = "PRSS1", retmax=total)
record = Entrez.read(handle)
idlist = record["IdList"]
handle = Entrez.efetch(db="pubmed", id=idlist, rettype="medline", retmode="text")
records = list(Medline.parse(handle))
record_results = open("artigos_PubMedPRSS1.txt", 'w')
for record in records: 
    a1 = "Title: " + str(record.get("TI", "?"))
    a2 = "\nAuthors: " + str(record.get("AU", "?"))
    a3 = "\nSource: " + str(record.get("SO", "?"))
    record_results.write(a1)
    record_results.write(a2)
    record_results.write(a3)
    record_results.write("\n\n")
record_results.close()
