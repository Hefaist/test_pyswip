## My test library pyswip.

#### Python version
```
3.6.6 |Anaconda custom (64-bit)| (default, Jun 28 2018, 11:27:44) [MSC v.1900 64 bit (AMD64)]
Python Type "help", "copyright", "credits" or "license" for more information.

```

#### Library version
```
pyswip                             0.2.8
```

#### Test with UTF-8 facts - test_utf_facts.py
```python
from pyswip import Prolog

prolog = Prolog()
prolog.assertz(u"father('franišek')")
prolog.assertz(u"father('bonifác')")

print(list(prolog.query("father(X)")))
```
Output:
```
[{'X': 'franišek'}, {'X': 'bonifác'}]
```

#### utf_facts.pl

```python
:- set_prolog_flag(encoding,utf8).

father('franišek').
father('bonifác').

```

#### Test utf_facts.pl in SWI-Prolog
```
Welcome to SWI-Prolog (threaded, 64 bits, version 8.0.3)
SWI-Prolog comes with ABSOLUTELY NO WARRANTY. This is free software.
Please run ?- license. for legal details.

For online help and background, visit http://www.swi-prolog.org
For built-in help, use ?- help(Topic). or ?- apropos(Word).

?- consult('utf_facts').
true.

?- father(X).
X = franišek ;
X = bonifác.

?-
```
#### Fetching from utf_facts.pl in Python - get_facts.py

```python
from pyswip import Prolog

prolog = Prolog()
prolog.consult("utf_facts.pl", catcherrors=True)
print(list(prolog.query("current_prolog_flag(encoding,X)")))
print(list(prolog.query("father(X)")))
```

Output:
```python
[{'X': 'utf8'}]
```
with error:

```python
File "d:\xwrk\sandbox\prolog\test_pyswip\get_facts.py", line 6, in <module>
  print(list(prolog.query("father(X)")))
File "D:\xprg\python\Conda35\Lib\site-packages\pyswip\prolog.py", line 111, in __call__
  t = getTerm(swipl_list)
File "D:\xprg\python\Conda35\Lib\site-packages\pyswip\easy.py", line 404, in getTerm
  res = getList(t)
File "D:\xprg\python\Conda35\Lib\site-packages\pyswip\easy.py", line 420, in getList
  result.append(getTerm(head))
File "D:\xprg\python\Conda35\Lib\site-packages\pyswip\easy.py", line 406, in getTerm
  res = getFunctor(t)
File "D:\xprg\python\Conda35\Lib\site-packages\pyswip\easy.py", line 429, in getFunctor
  return Functor.fromTerm(t)
File "D:\xprg\python\Conda35\Lib\site-packages\pyswip\easy.py", line 254, in fromTerm
  return cls(f.value, args=args, a0=a0)
File "D:\xprg\python\Conda35\Lib\site-packages\pyswip\easy.py", line 231, in __init__
  self.__value = self.func[self.handle](self.arity, *self.args)
File "D:\xprg\python\Conda35\Lib\site-packages\pyswip\easy.py", line 295, in _unifier
  return {args[0].value:args[1].value}
File "D:\xprg\python\Conda35\Lib\site-packages\pyswip\easy.py", line 82, in get_value
  ret = ret.decode()

builtins.UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe1 in position 5: invalid continuation byte
```

