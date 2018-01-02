from django.contrib.contenttypes.models import ContentType
from tests.factories import FacBaseActe

import factory
from ordonnances.models import Conseil, LigneOrdonnance, Medicament, Ordonnance

fk = factory.Faker


class FacOrdonnance(FacBaseActe):
    class Meta:
        model = 'ordonnances.Ordonnance'

    position = fk('text', max_nb_chars=50, locale="fr_FR")


class FacMedicament(factory.django.DjangoModelFactory):
    class Meta:
        model = Medicament

    cip = fk('ean13', locale="fr_fr")
    nom = fk('last_name', locale="fr_FR")
    posologie = fk('text', max_nb_chars=50, locale="fr_FR")
    duree = fk('pyint')
    # ligne = GenericRelation(LigneOrdonnance, related_query_name='medicament')


class FacLigneOrdonnance(factory.DjangoModelFactory):

    position = factory.Sequence(lambda n: n)
    ordonnance = factory.SubFactory(FacOrdonnance)
    ald = fk('boolean')

    object_id = factory.SelfAttribute('contenu.id')
    content_type = factory.LazyAttribute(
        lambda o: ContentType.objects.get_for_model(o.contenu))

    class Meta:
        exclude = ['contenu']
        abstract = True


class FacLigneMedicament(FacLigneOrdonnance):
    contenu = factory.SubFactory(FacMedicament)

    class Meta:
        model = LigneOrdonnance
