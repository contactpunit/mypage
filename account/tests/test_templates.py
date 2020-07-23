import pytest
from pytest_django.asserts import assertTemplateUsed
from django.urls import reverse


@pytest.mark.parametrize('test_url, result', [
    ('account:login', 'registration/login.html'),
    ('account:logout', 'registration/login.html'),
    ('account:password_change', 'registration/login.html'),
    ('account:register', 'registration/register.html'),
])
@pytest.mark.django_db
def test_login_url(client, test_url, result):
    url = reverse(test_url)
    response = client.get(url, follow=True)
    assert result in [template.name for template in response.templates]
