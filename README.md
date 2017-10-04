[![Build Status](https://travis-ci.org/jgirardet/unolog.svg?branch=master)](https://travis-ci.org/jgirardet/unolog)


# unolog
Un NOuveau LOgiciel de Gestion de patient



## TODO UnologBase
- patient
  - base method : ~~list~~, update, partial update, remove, create
  - add more base fields : ~~street~~, ~~city~~, ~~tel~~, ~~email~~
- model base act
  - champs de base
  - liaison en foreignKey
  - modification 
- extension de base act
  - observation
  - ordonnance
  - etc...
- class utilisateur




## bug divers
update(niveauqueryset) ne prend pas en charge le save (du model) donc auto
time et capwors des noms sans effet



## Grand principes pour la doc
- chaque élement fils de BaseAct n'appartient qu'à un seul uilisateur pour
  creation ou modification.
_ on ne sauve rien sans passer par objects create ou update

