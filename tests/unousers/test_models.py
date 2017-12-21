from django.contrib.auth import get_user_model

import pytest

#pytestmark = pytest.mark.django_db


class TestUnoUser:
    """
    test model class
    """

    def test_fixt(self, testuser):
        mod = get_user_model()
        #testuser.save()
        assert isinstance(testuser, mod)
