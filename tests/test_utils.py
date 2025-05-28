import pytest
from app.utils.crypto import generate_key, encrypt_password, decrypt_password

def test_key_generation():
    """Test encryption key generation."""
    key = generate_key()
    assert key is not None
    assert isinstance(key, bytes)
    assert len(key) == 32  # 256 bits

def test_password_encryption():
    """Test password encryption."""
    key = generate_key()
    password = "mysecretpassword"
    encrypted = encrypt_password(password, key)
    
    assert encrypted is not None
    assert encrypted != password
    assert isinstance(encrypted, bytes)

def test_password_decryption():
    """Test password decryption."""
    key = generate_key()
    password = "mysecretpassword"
    encrypted = encrypt_password(password, key)
    decrypted = decrypt_password(encrypted, key)
    
    assert decrypted == password
    assert isinstance(decrypted, str)

def test_encryption_different_keys():
    """Test encryption with different keys."""
    key1 = generate_key()
    key2 = generate_key()
    password = "mysecretpassword"
    
    encrypted1 = encrypt_password(password, key1)
    encrypted2 = encrypt_password(password, key2)
    
    assert encrypted1 != encrypted2
    
    with pytest.raises(Exception):
        decrypt_password(encrypted1, key2)

def test_password_roundtrip():
    """Test complete encryption/decryption cycle."""
    key = generate_key()
    original_password = "mysecretpassword123!@#"
    
    encrypted = encrypt_password(original_password, key)
    decrypted = decrypt_password(encrypted, key)
    
    assert decrypted == original_password
    assert encrypted != original_password
    assert isinstance(encrypted, bytes)
    assert isinstance(decrypted, str) 