import database
import password
from cryptography.fernet import Fernet
import base64
import os

def entry_get(*args):
    # the first parameter that calls this function is supposed to pass information about which function is calling this function.
    # Based on that information the funtion works differently.



    if args[0] == "UI":
        length = args[1].get()
        password.is_valid_length(length)
    elif args[0] == "DB":

          url_entry_value = args[3].get()
          service_entry_value = args[2].get()
          name_entry_value = args[1].get()
          password_secret = args[4]
          database.insert_into_db(password_secret, service_entry_value, url_entry_value, name_entry_value)


def decrypt_data(encrypted_data):

    if isinstance(encrypted_data, str):
        encrypted_data = encrypted_data.encode('utf-8')



    with open("secret.key", "rb") as f:
        secret_key = f.read()
        print("from decryption", secret_key)
        s = Fernet(secret_key)

        decrypted_data = s.decrypt(encrypted_data)


        return decrypted_data