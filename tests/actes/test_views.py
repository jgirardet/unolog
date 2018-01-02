import pytest
from rest_framework.reverse import reverse, reverse_lazy
from rest_framework.test import APIRequestFactory


class TestObservationViewSet:
    def test_owner_readonly(self, apiclient):
        id = apiclient.handler._force_user.id
        data = {
            "patient": "http://localhost:8000/patients/1/",
            "owner": "http://localhost:8000/users/" + str(id + 1) + "/",
            "motif": "cccccccccc",
            "body": "cccccccc"
        }
        r = apiclient.post(
            reverse('observation-list'), data=data, format='json')

        assert r.data['owner'][-2] == str(id), "owner should be logged user"
