import model
import data
import bottle


@bottle.get('/')
def pozdravna_stran():
    return bottle.template("pozdravna_stran.tpl")

@bottle.get('glavni_meni')
def glavni_meni():
    return bottle.template("glavni_meni.tpl")

@bottle.get('pregled')
def trenutno_stanje():
    return bottle.template("pregled_stanja.tpl")

bottle.run(reloader=True, debug=True)