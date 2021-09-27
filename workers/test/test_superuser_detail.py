import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_superuser_detail(client, admin_user):
   url = reverse(
       'superuser-detail-view', kwargs={'pk': admin_user.pk}
   )
   response = client.get(url)
   assert response.status_code == 200
   assert 'admin' in response.content