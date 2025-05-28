import pytest
from flask import url_for

def test_home_page(client):
    """Test home page."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Password Manager' in response.data

def test_login_page(client):
    """Test login page."""
    response = client.get('/auth/login')
    assert response.status_code == 200
    assert b'Login' in response.data

def test_register_page(client):
    """Test register page."""
    response = client.get('/auth/register')
    assert response.status_code == 200
    assert b'Register' in response.data

def test_login_process(client):
    """Test login process."""
    response = client.post('/auth/login', data={
        'username': 'testuser',
        'password': 'password123'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Welcome' in response.data

def test_register_process(client):
    """Test registration process."""
    response = client.post('/auth/register', data={
        'username': 'newuser',
        'email': 'new@example.com',
        'password': 'newpassword123',
        'password2': 'newpassword123'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Congratulations' in response.data

def test_protected_page(client):
    """Test access to protected page."""
    response = client.get('/vault', follow_redirects=True)
    assert response.status_code == 200
    assert b'Please log in' in response.data 