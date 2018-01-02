from string import capwords

from django.contrib.auth import get_user_model

import pytest
from actes.models import Observation
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIRequestFactory

pytestmark = pytest.mark.django_db


class TestActesPermissions:
    """
    test permissions
    """

    def testOnlyOwnerCanEdit(self, observation, apiclient):
        r = apiclient.patch(
            reverse('observation-detail', kwargs={
                "pk": observation.pk
            }),
            data={
                'motif': 'test'
            })
        assert r.status_code == status.HTTP_403_FORBIDDEN

    def testOkForSageMethod(self, apiclient, observation):
        r = apiclient.get(reverse('observation-detail', kwargs={"pk": observation.pk}))
        assert r.status_code == status.HTTP_200_OK
