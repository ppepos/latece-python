# Python
## Qu'est-ce que Python
Langage Dynamique
Oriente Objet
Philisophie de python: import this

## Version

2.7 pour Formation de vendredi
3.4 Actuelle

## Python et IPython

### Interpreteur python
$ python toto.py

ou 

$ python
>>> print 'trop difficile'

### IPython

Comme python mais avec auto-complétion et quelques outils de plus

## Syntaxe de base

### Print

print, print()
print format (%s, .format())
print -> , +
future print(end)

### Commentaires

\#
""" Docstring """

### Contrôle de flot

if, elif, else
for elem in population:
while:
try, except, with
indentation

### Built-in functions
* len
* map
* eval
* casts (chr, ord, byte, float, int)
* raw_input, input
* ...
* https://docs.python.org/2/library/functions.html

### Sucre syntaxique
* x, y = point




### Avoir de l'aide
``` python
>>> toto = []
>>> dir(toto)
>>> help(toto)
>>> toto.<tab><tab>
```

## Types

### Nombres
#### Operateurs
+,-,*,/,%
Division entiere //
Puissance \**
Division d'entier VS division de float

#### Particularite des entiers
Typage dynamique permet de gerer les Longs

### Chaines de caracteres
#### Chaines de caracteres python
lucas = "Mon allemand prefere"
lucas = 'Mon allemand prefere'

chaine_multi_ligne = """Salut,
Je suis definie sur plusieurs
lignes.

hihihi!"""

#### Adressage et fonctions

lucas[0] = 'M'
lucas[-1] = 'e'
lucas.find()
lucas.encode('hex')
lucas.decode('utf-8')
lucas.<tab><tab>

### Listes

#### Les listes en python
une_liste_vide = []
une_autre_liste = [1, 2, 3]
ma_liste = [1, 'wtf', 3]
une_liste_de_listes = [[], [], []]

#### Adressage
une_liste[idx_debut:idx_fin:saut]
liste = [1, 2, 3, 4, 5]
liste[1]   # 2
liste[-1]  # 5
liste[2:4] # [3, 4]
liste[:3:2] # [1, 3]

#### Comprehensions de listes
liste = [1, 2, 3, 4]
liste = [elem * 2 for elem in liste]

### Dictionnaires

#### Les dictionnaires python
mon_dict_vide = {}
mon_dict_non_vide = {'cle': 1337}

mon_dict_vide['cle'] = 1337 # Insertion

mon_dict_vide.pop('cle')
del mon_dict_non_vide['cle']

### Tuples
#### Tuples python
mon_tuple = (1, 2)
mon_autre_tuple = (b, liste)
mon_tuple[0] == 1
un, deux = mon_tuple

### Fonctions
#### Syntaxe de base
def nom_de_fonction(arg1, arg2):
    return arg1 + arg2

#### Sucre syntaxique
def fonction_avec_params_optionnels(arg1, arg2=0):
    ...

def fonction_avec_nombre_params_variable(\*args, \**kwargs)
    ...

def fonction_retourne_deux_params():
    return 3, 4

### Fichiers
#### Overture et fermeture
fd = open('/etc/passwd', 'r')
fd.read() # fd<tab><tab>
fd.close()

#### Utilisation
try:
    open, read, close
except:
    Raise IOError('brise')

with open(...) as fd:
    fd.read() # Close sera appelle en brisant l'indentation

## Objets

### Classes
``` python
class Humain(object):

    fun = True

    def __init__(self, arg1, arg2):
    	self.x = arg1
	self.y = arg2

    def to_tuple(self):
        return self.x, self.y

    def fun_function():
        return fun

pepos = Humain(23, 1991)
print pepos.to_tuple()

```




-----------


## Modules utiles
### sys
### os
### json
### ctypes
### PIL
### requests
### bs4
### csv
### string

## Preparation Big Data / Data Analysis
### Pandas
### mathplotlib
http://www.analyticsvidhya.com/blog/2014/08/baby-steps-python-performing-exploratory-analysis-python/

