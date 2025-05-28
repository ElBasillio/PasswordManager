import pytest
from app.models import User, Vault, Password
from app import db

def test_new_user():
    """Test creating new user."""
    user = User(username='testuser', email='test@test.com')
    user.set_password('password123')
    assert user.username == 'testuser'
    assert user.email == 'test@test.com'
    assert user.check_password('password123')
    assert not user.check_password('wrongpassword')

def test_password_hashing():
    """Test password hashing."""
    user = User(username='testuser', email='test@test.com')
    user.set_password('password123')
    assert user.password_hash is not None
    assert user.password_hash != 'password123'
    assert user.check_password('password123')

def test_vault_creation(init_database):
    """Test vault creation."""
    user = User.query.filter_by(username='testuser').first()
    vault = Vault(name='New Vault', user=user)
    db.session.add(vault)
    db.session.commit()
    
    assert vault in db.session
    assert vault.name == 'New Vault'
    assert vault.user.username == 'testuser'

def test_password_entry(init_database):
    """Test password entry creation."""
    vault = Vault.query.first()
    password = Password(
        title='Test Password',
        encrypted_password='encrypted_test_password',
        url='https://example.com',
        notes='Test notes',
        vault=vault
    )
    db.session.add(password)
    db.session.commit()
    
    assert password in db.session
    assert password.title == 'Test Password'
    assert password.url == 'https://example.com'
    assert password.vault.name == 'Test Vault' 