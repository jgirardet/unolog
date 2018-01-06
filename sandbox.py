import random
from operator import attrgetter, iadd

from tests.factories import *


def test():
    o = FacOrdonnance()
    l = random.choices((FacMedicament, FacConseil), k=10)
    e = [i(ordonnance=o) for i in l]
    random.shuffle(e)
    for i, x in zip(e, range(10)):
        i.position = x
    f = "id : {}  position : {}   "
    return e

    print('----------départ---------------')
    for i in e:
        print(f.format(i.id, i.position, i.__str__()))

    print('----------cherche index')
    index = 0
    rid = e[3].id  #id recherché
    for i, x in zip(e, range(len(e))):
        if i.id == rid:
            index = x
    print("id " + str(rid) + "à l'index : " + str(index))

    print('-------- +  1  après new pose prévu-----------------')
    np = 6
    for i in e[6:]:
        i.position += 1

    for i in e:
        print(f.format(i.id, i.position, i.__str__()))
    print('----------moins index 3---------------------')
    item = e.pop(index)
    item.position = np
    for i in e:
        print(f.format(i.id, i.position, i.__str__()))
    print("item : ", item.id, item.position, item.__str__())
    print('--------on ajoute  à np-----------')
    for i in e:
        print(f.format(i.id, i.position, i.__str__()))
    return e


"""
np en index
ap en index

si ap > np
    list[np].position +=1
si ap < np

"""


def change_pos(e, ap, np):
    import copy
    a = copy.deepcopy(e)
    """
    réaffectation des rangs selon la position dans la liste :
    2 cas particuliers :
     - ap et np se suivent donc simple interversion
     - np en dernière position
     """

    if abs(np - ap) == 1:
        #1 rang de diféreence donc on échange juste
        a[ap].position = np
        a[np].position = ap

    elif ap > np:
        if np == len(a) - 1:
            #dernière position donc met un pos max pour le classement
            a[ap].position = len(a)
        else:
            a[ap].position = np
        a[np].position += 1
    elif ap < np:
        a[ap].position = np

    else:
        return copy.deepcopy(a)
    a.sort(key=attrgetter('position'))
    for i, x in zip(a, range(10)):
        i.position = x
    return copy.deepcopy(a)
