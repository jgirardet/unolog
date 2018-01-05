from tests.factories import *


def test():
    o = FacOrdonnance()
    l = random.choices((FacMedicament, FacConseil), k=10)
    e = [i(ordonnance=o) for i in l]
    print([(i.id, i.position) for i in e])
    return e
