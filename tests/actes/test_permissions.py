from string import capwords

from django.contrib.auth import get_user_model

import pytest
from actes.models import Observation
from mixer.backend.django import mixer
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIRequestFactory

pytestmark = pytest.mark.django_db


class TestActesPermissions:
    """
    test permissions
    """

    def testOnlyOwnerCanEdit(self, apiclient, testuser):
        o = mixer.blend(Observation, owner=testuser)
        r = apiclient.patch(
            reverse('observation-detail', kwargs={
                "pk": o.pk
            }),
            data={
                'motif': 'test'
            })
        assert r.status_code == status.HTTP_403_FORBIDDEN

    def testOkForSageMethod(self, apiclient, testuser):
        o = mixer.blend(Observation, owner=testuser)
        r = apiclient.get(reverse('observation-detail', kwargs={"pk": o.pk}))
        assert r.status_code == status.HTTP_200_OK
