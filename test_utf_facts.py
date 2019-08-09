from pyswip import Prolog

prolog = Prolog()
prolog.assertz(u"father('franišek')")
prolog.assertz(u"father('bonifác')")

print(list(prolog.query("father(X)")))