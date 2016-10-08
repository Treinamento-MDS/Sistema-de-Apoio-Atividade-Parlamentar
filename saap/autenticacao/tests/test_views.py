# coding=utf-8
from autenticacao.views import *
import pytest
from django.test import Client
from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory

@pytest.fixture
def logar_usuario(client):
	user = User(username="asdf",password="1234")
	user.set_password('123456')
	user.save()
	client.login(username=user.username, password="123456")
	return user,client

@pytest.mark.django_db
def teste_usuario_logado(client):
	user,client = logar_usuario(client)

	assert user is not None

@pytest.mark.django_db
def test_login_view_get(client):
	response = client.get('/login/')
	assert 300 >= response.status_code < 400
