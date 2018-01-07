def create_ordre(ligne):
    ordo = ligne.ordonnance
    ordo.ordre = ";".join((ordo.ordre, ligne.nom_id))
    ordo.ordre = ordo.ordre.strip(';')
    ordo.save()
