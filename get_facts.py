from pyswip import Prolog

prolog = Prolog()
prolog.consult("utf_facts.pl", catcherrors=True)
print(list(prolog.query("current_prolog_flag(encoding,X)")))
print(list(prolog.query("father(X)")))