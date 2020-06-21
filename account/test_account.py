import pytest
import uuid
from django.contrib.auth.models import User
from django.urls import reverse


####### Fixtures ########

@pytest.fixture
def test_password():
    """ Fixture to act as password for user to be created """
    return 'some_strong_password'


@pytest.fixture
def create_user(db, django_user_model, test_password):
    """ Fixture to create User """
    def make_user(**kwargs):
        kwargs['password'] = test_password
        if 'username' not in kwargs:
            kwargs['username'] = str(uuid.uuid4())
        return django_user_model.objects.create_user(**kwargs)
    return make_user


@pytest.fixture
def auto_login_user(client, create_user, test_password):
    def make_auto_login(user=None):
        if user is None:
            user = create_user()
        client.login(username=user.username, password=test_password)
        return client, user
    return make_auto_login


############################

@pytest.mark.django_db
def test_user_create():
    """ Create Test User """
    User.objects.create_user('test', 'test@example.com', 'testpassword')
    assert User.objects.count() == 1


@pytest.mark.django_db
def test_login_view(client):
    """ Test for checking login url """
    url = reverse('account:login')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_login_view(auto_login_user):
    client, user = auto_login_user()
    url = reverse('account:login')
    response = client.get(url)
    assert response.status_code == 200
    assert 'My Dashboard' in response.content.decode('utf8')
