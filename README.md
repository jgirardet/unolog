[![Build Status](https://travis-ci.org/jgirardet/unolog.svg?branch=master)](https://travis-ci.org/jgirardet/unolog)


# unolog
Un NOuveau LOgiciel de Gestion de patient



## TODO
- patient
  - base method : ~~list~~, ~~update, partial update, remove, create~~
  - add more base fields : ~~street~~, ~~city~~, ~~tel~~, ~~email~~
- model base act
  - ~~champs de base~~
  - ~~liaison en foreignKey~~
  - ~~ modification~~
- extension de base act
  - ~~observation~~
  - ordonnance
  - etc...
- class utilisateur



## Grand principes pour la doc
- chaque élement fils de BaseAct n'appartient qu'à un seul uilisateur pour
  creation ou modification.
_ on ne sauve rien sans passer par objects create ou update
_ chaque creation se fait via les serializers

## mise en place
python setup.py pipenv
./launch.py mm //mk migration + migrate
./launch.py createsuperuser
