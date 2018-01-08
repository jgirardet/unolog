import factory
# from ordonnances.models import Conseil, LigneOrdonnance, Medicament, Ordonnance
from ordonnances.models import Conseil, LigneOrdonnance, Medicament, Ordonnance
from tests.factories import FacBaseActe

fk = factory.Faker


class FacOrdonnance(FacBaseActe):
    class Meta:
        model = 'ordonnances.Ordonnance'

    ordre = ""

    # ligne = GenericRelation(LigneOrdonnance, related_query_name='medicament')


class FacLigneOrdonnance(factory.DjangoModelFactory):

    ordonnance = factory.SubFactory(FacOrdonnance)
    ald = fk('boolean')

    class Meta:
        abstract = True

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        """Override the default ``_create`` with our custom call."""
        manager = cls._get_manager(model_class)
        # The default would use ``manager.create(*args, **kwargs)``

        return manager.new_ligne(**kwargs)


class FacMedicament(FacLigneOrdonnance):
    class Meta:
        model = Medicament

    cip = fk('ean13', locale="fr_fr")
    nom = fk('last_name', locale="fr_FR")
    posologie = fk('text', max_nb_chars=50, locale="fr_FR")
    duree = fk('pyint')


class FacConseil(FacLigneOrdonnance):
    class Meta:
        model = Conseil

    texte = fk('text', max_nb_chars=200, locale="fr_FR")
