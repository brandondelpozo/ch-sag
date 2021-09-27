import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_unauthorized(client):
   url = reverse('superuser-url')
   response = client.get(url)
   assert response.status_code == 401


@pytest.mark.django_db
def test_superuser_view(admin_client):
   url = reverse('superuser-url')
   response = admin_client.get(url)
   assert response.status_code == 200