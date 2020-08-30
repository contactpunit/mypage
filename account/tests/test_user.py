import pytest
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_user_create():
    """ Test USer creation """
    User.objects.create_user(username='anki', email='an@example.com', password='anki', first_name='ankita',
                             last_name='jain')
    assert User.objects.count() == 1
    user = User.objects.get(pk=1)
    assert user.last_name == 'jain'
    assert user.email == 'an@example.com'
