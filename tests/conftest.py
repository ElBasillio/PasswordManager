import pytest
from app import create_app, db
from app.models import User, Vault, Password

@pytest.fixture
def app():
    """Create application for the tests."""
    app = create_app('testing')
    return app

@pytest.fixture
def client(app):
    """Create test client."""
    return app.test_client()

@pytest.fixture
def init_database():
    """Initialize test database."""
    db.create_all()
    
    # Create test user
    user = User(username='testuser', email='test@example.com')
    user.set_password('password123')
    db.session.add(user)
    
    # Create test vault
    vault = Vault(name='Test Vault', user=user)
    db.session.add(vault)
    
    db.session.commit()
    
    yield db  # this is where the testing happens
    
    db.session.remove()
    db.drop_all() 