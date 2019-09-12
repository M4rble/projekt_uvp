import model
import data
import bottle


@bottle.get('/')
def pozdravna_stran():
    return bottle.template("pozdravna_stran.tpl")

@bottle.get('/glavni_meni/')
def glavni_meni():
    return bottle.template("glavni_meni.tpl")

@bottle.get('/pregled/')
def trenutno_stanje():
    return bottle.template("pregled_stanja.tpl", stanje = model.izpis_stanja())

@bottle.get('/tabela/')
def zadnje_transakcije():
    return bottle.template("zadnje_transakcije.tpl", podatki = model.vrni_podatke())

@bottle.get('/graf/')
def graf_transakcij():
    return bottle.template("graf_transakcij.tpl")

@bottle.post('/uredi/')
def dodaj_transakcijo():
    return bottle.template("dodaj_transakcijo.tpl")

bottle.run(reloader=True, debug=True)