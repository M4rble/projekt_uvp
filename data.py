import csv


def preberi():
    tabela = []
    fp = open("tabela_nakazil.csv", "rt")
    reader = csv.DictReader(fp)
    for row in reader:
        sub_tabela = []
        sub_tabela += [int(row["ID"])]
        sub_tabela += [row["datum"]]
        sub_tabela += [row["namen"]]
        sub_tabela += [float(row["nakazilo"])]
        sub_tabela += [row["opombe"]]
        tabela += [sub_tabela]
    return tabela


def vnos(podatki):
    f = open('tabela_nakazil.csv', 'a')
    writer = csv.writer(f)
    writer.writerow(podatki)
    f.close()

def ustvari_novo():
    f = open('tabela_nakazil.csv', 'w')
    writer = csv.writer(f)
    writer.writerow(header)
    f.close()

header =  ["ID", "datum", "namen", "nakazilo", "opombe"]