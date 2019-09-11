import data
import matplotlib.pyplot as plt

def izrisi_graf():
    podatki = data.preberi()
    tabela = [0]
    for row in podatki:
        tabela += [row[3] + tabela[len(tabela)-1]]
    
    plt.figure()
    plt.xlabel("Potek Transakcij")
    plt.ylabel("Stanje v Evrih")
    plt.title("Graf stanja v transakcijah")

    plt.plot(tabela, label = "Stanje")
    plt.show()