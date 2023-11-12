from utils import EncryptionUtility

def test_encryption_decryption():
    original_message = "Secret Message"
    key = EncryptionUtility.generate_key()
    encrypted_message = EncryptionUtility.encrypt_message(original_message, key)
    decrypted_message = EncryptionUtility.decrypt_message(encrypted_message, key)

    assert original_message == decrypted_message