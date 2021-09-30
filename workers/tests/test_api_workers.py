import re
import pytest 

from rest_framework.reverse import reverse
from rest_framework import status

from ..models import FieldWorker


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    
    return APIClient()



@pytest.fixture
def test_api_can_create_a_workers(db, api_client):
    url = reverse('workers:field_workers-list')
    data = {
        'first_name': 'some',
        'last_name': 'ramdom',
    }
    res = api_client.post(url, data=data)
    assert res.status_code == status.HTTP_201_CREATED
    assert FieldWorker.objects.count() == 1
    worker_from_db = FieldWorker.objects.get(first_name='some')
    assert worker_from_db.first_name == 'some'


@pytest.mark.django_db
def test_api_can_get_a_workers(api_client):
    url = reverse('workers:field_workers-list')
    res = api_client.get(url)
    assert res.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_api_cat_detail_a_workers(api_client, test_api_can_create_a_workers):
    worker = FieldWorker.objects.first()
    url = reverse('workers:field_workers-detail', kwargs={'pk': worker.id})
    res = api_client.get(url)
    assert res.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_api_cat_update_a_workers(api_client, test_api_can_create_a_workers):
    worker = FieldWorker.objects.first()
    url = reverse('workers:field_workers-detail', kwargs={'pk': worker.id})
    data = {
        'first_name': 'Some random first_name',
        'last_name': 'ramdom',
    }
    res = api_client.put(url, data=data)
    assert res.status_code == status.HTTP_200_OK
    worker_from_db = FieldWorker.objects.get(first_name='Some random first_name')
    assert worker_from_db.first_name == 'Some random first_name'


@pytest.mark.django_db
def test_api_cat_patch_a_workers(api_client, test_api_can_create_a_workers):
    worker = FieldWorker.objects.first()
    url = reverse('workers:field_workers-detail', kwargs={'pk': worker.id})
    data = {
        'function': 'Prunning'
    }
    res = api_client.patch(url, data=data)
    assert res.status_code == status.HTTP_200_OK
    worker_from_db = FieldWorker.objects.get(function='Prunning')
    assert worker_from_db.function == 'Prunning'
