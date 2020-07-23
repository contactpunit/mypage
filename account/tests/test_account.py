import pytest
import uuid
from django.test import Client
from django.contrib.auth.models import User
from django.urls import reverse


@pytest.fixture
def create_password():
    return 'testpassword'


@pytest.fixture
def create_user(db, django_user_model, create_password):
    def return_created_user(**kwargs):
        kwargs['password'] = create_password
        if 'username' not in kwargs:
            kwargs['username'] = str(uuid.uuid4())
        return django_user_model.objects.create_user(**kwargs)
    return return_created_user


@pytest.fixture
def auto_login_user(db, client, create_user, create_password):
    def auto_login(user=None):
        if user is None:
            user = create_user()
        client.login(username=user.username, password=create_password)
        return client, user
    return auto_login


@pytest.mark.django_db
def test_user_create(auto_login_user):
    client, user = auto_login_user()
    assert User.objects.count() == 1
    response = client.login(username=user.username, password='testpassword')
    assert response is True
