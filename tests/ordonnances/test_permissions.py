import random
from unittest.mock import MagicMock

from tests.factories import *

import pytest
from ordonnances.permissions import OnlyOwnerCanEditLigneOrdonnance
from rest_framework.permissions import SAFE_METHODS


def test_onlyownercaneditligneordonnancesafemethods():
    perm = OnlyOwnerCanEditLigneOrdonnance()
    r = MagicMock()
    r.method = random.choice(SAFE_METHODS)
    obj = MagicMock()
    obj.ordonnance.owner = ""
    assert perm.has_object_permission(r, "view", obj)


def test_onlyownercaneditligneordonnanceowner():
    perm = OnlyOwnerCanEditLigneOrdonnance()
    r = MagicMock()
    r.user = "Moi"
    obj = MagicMock()
    obj.ordonnance.owner = "Moi"
    assert perm.has_object_permission(r, "view", obj), 'user should be owner'
    r.user = "PasMoi"
    assert not perm.has_object_permission(r, "view",
                                          obj), 'user not owner shold be false'
