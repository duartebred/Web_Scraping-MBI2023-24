import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import time
import sys
import pymysql


def save_genbank(text):

    """
    Função que recebe a informação de um gene do ncbi e guarda num ficheiro formato gb
    """

    match = re.search(r'LOCUS\s+(.*?)\s+\b', text)

    if match:
        nuccore_id = match.group(1)
        print(f'O ID na base de dados Nucleotide é {nuccore_id}.')

        filename = f'{nuccore_id}.gb'
        with open(filename,'w',encoding='utf-8') as gb_file:
            gb_file.write(text)
            print(f'Resultados gravados no ficheiro {filename}.')



def parse_genbank(locus):
    
    """
    Extração de alguns dados do registo Genbank e retorna um tuplo com os dados de interesse: 
    "id", "organismo" e "sequência"
    """
    i = re.match(r'LOCUS\s+(\w+)', locus)
    if i:
        id = i.group(1)
    organism = ""
    o = re.search(r'SOURCE\s+.+', locus)
    if o:
        s = re.match(r'SOURCE\s+(.+)', o[0] )
        if s:
            organism = s.group(1)
    sequencia = ""
    existe = re.findall(r'^\s+\d+ [actg ]+', locus, re.MULTILINE )
    if existe:
        for linha in existe:
            m = re.match( r'\s+\d+ (.+)', linha, re.DOTALL )
           
            sequencia = sequencia + re.sub(r'\s+', '', m.group(1) )
    return (id, organism, sequencia)


def get_genbank(gene):

    """
    Vai buscar o registo a partir do nome do gene
    """

    url = f'https://www.ncbi.nlm.nih.gov/nuccore/{gene}'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    id = soup.find_all('meta',{'name':'ncbi_uidlist'})[0].attrs['content']
    url = f"https://www.ncbi.nlm.nih.gov/sviewer/viewer.fcgi?id={id}&db=nuccore&report=genbank&conwithfeat=on&hide-cdd=on&retmode=text&maxdownloadsize=5000000"
    r2 = requests.get(url)
    return r2.text



DataBase = pymysql.connect(
host ="127.0.0.1",
user ="DuarteVelho1",
password ="123duarte",
    database ="duartetrabalhos"
)

# Criação de um cursor para executar comandos SQL
Cursor = DataBase.cursor()

# Parâmetros para a criação da tabela
TableName ="""CREATE TABLE IF NOT EXISTS genbank
    (
    locusid varchar(255) PRIMARY KEY, 
    dnasource text, 
    dnasequence LONGTEXT
    );
"""

# Executamos os comandos com recurso ao cursor
Cursor.execute(TableName)

sql = "INSERT IGNORE INTO genbank (locusid, dnasource, dnasequence) VALUES (%s, %s, %s)"

for arg in sys.argv[1:]:
    content = get_genbank(arg)
    save_genbank(content)
    val = parse_genbank(content)
    Cursor.execute(sql, val) 
    time.sleep(2)

DataBase.commit()



Cursor.close()
DataBase.close()

