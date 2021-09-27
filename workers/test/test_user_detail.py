import pytest

from django.urls import reverse


@pytest.mark.django_db
def test_user_detail(client, django_user_model):
   user = django_user_model.objects.create(
       username='someone', password='password'
   )
   url = reverse('user-detail-view', kwargs={'pk': user.pk})
   response = client.get(url)
   assert response.status_code == 200
   assert 'someone' in response.content