import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_login_url(client):
    url = reverse('account:login')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_logout_redirect_without_login(client):
    url = reverse('account:logout')
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_password_change_redirect_without_login(client):
    url = reverse('account:password_change')
    response = client.get(url)
    assert response.status_code == 302


@pytest.mark.django_db
def test_edit_profile_redirect_without_login(client):
    url = reverse('account:profile')
    response = client.get(url)
    assert response.status_code == 302
