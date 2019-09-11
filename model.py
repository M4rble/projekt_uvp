import data
import graf

def dodaj_vnos(podatki):
    data.vnos(podatki)

def vrni_podatke():
    return data.preberi()

def izpis_stanja():
    podatki = vrni_podatke()
    stanje = 0
    for row in podatki:
        stanje += row[3]
    return stanje

def nov_vnos(datum, namen, nakazilo, opombe):
    try:
        x = int(nakazilo)
    except ValueError:
        return napaka_pri_vnosu()
    if len(datum) == 0 or len(namen) == 0 or len(nakazilo) == 0:
        return prazen_vnos() 
    id = len(vrni_podatke()) + 1
    dodaj_vnos([id, datum, namen, nakazilo, opombe])

def napaka_pri_vnosu():
    return 'Napaka pri vnosu! Prosimo ponovite vnos.'

def prazen_vnos():
    return 'Napaka pri vnosu! Prosimo izpolnite vsa polja.'

def izris_graf_stanja():
    graf.izrisi_graf()

def izprazni_tabelo():
    data.ustvari_novo()