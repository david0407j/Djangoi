from django.test import  Client
from django.urls import reverse
import pytest

from projeto.django_assertions import assert_contains

@pytest.fixture
def resp(client,):
    resp = client.get(reverse('base:home'))
    return resp

def test_status_code(resp):
    assert resp.status_code == 200 

def test_title(resp):
   assert_contains(resp, '<title> Python Pro - home</title>' )

def test_home_link(resp):
    assert_contains(resp, f'href="{reverse("base:home")}">Python Pro</a>')