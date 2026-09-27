import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home_redirects(client):
    response = client.get('/')
    assert response.status_code in [200, 302]


def test_login_page_loads(client):
    response = client.get('/login')
    assert response.status_code == 200


def test_signup_page_loads(client):
    response = client.get('/signup')
    assert response.status_code == 200


def test_dashboard_requires_login(client):
    response = client.get('/dashboard')
    # Should redirect to login since not logged in
    assert response.status_code == 302


def test_history_requires_login(client):
    response = client.get('/history')
    assert response.status_code == 302