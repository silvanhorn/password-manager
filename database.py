import os.path
import sqlite3
from cryptography.fernet import Fernet
from datetime import datetime, date
import globals #because of the userinformation varibale that is stored there
import logic


def save_key():

    if not os.path.exists("secret.key"):
        key = Fernet.generate_key()
        with open("secret.key", "wb") as f:
            f.write(key)





def database_connection(userinformation):


    database = sqlite3.connect("password.db")

    cursor = database.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS userinformation(
        id integer PRIMARY KEY,
        hash text NOT NULL,
        service text,
        url text,
        username text,
        Datum DATE,
        note text
    );
    """)




def insert_into_db(password_secret, service_entry, url_entry, name_entry ):


    with open("secret.key", "rb") as f:
        secret_key = f.read()
        f = Fernet(secret_key)


    hashed_password = f.encrypt(password_secret.encode())
    datum = date.today()
    p1 = globals.userinformation(

    hash=hashed_password,
    service=service_entry,
    url = url_entry,
    username = name_entry,
    Datum = datum
    )


    conn = sqlite3.connect("password.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO userinformation (hash, service, url, username, Datum) VALUES (?, ?, ?, ?, ?)",
                   # the ?-signs are important to prevent sql-injection
                   (p1.hash, p1.service, p1.url, p1.username, p1.Datum))


    conn.commit()
    conn.close()





def select_from_database():

    connect = sqlite3.connect("password.db")
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM userinformation")

    globals.select_results_complete = cursor.fetchall()



    cursor.execute("select hash from userinformation")
    globals.rows = cursor.fetchall()



    #
    for row in globals.rows:

       # print(secret_key)

        encrypted_password = row[0]
        #print("encrypted_password", encrypted_password)


        decrypted_password =  logic.decrypt_data(encrypted_password)
        globals.decrypt_passwords.append(decrypted_password)




    for password, dataset in zip(globals.decrypt_passwords, globals.select_results_complete):
        temp = list(dataset)
        temp[1] = password
        globals.dataset_with_decrypted_password.append(temp)

           # print("FROM HERE",globals.dataset_with_decrypted_password)
#it is neccesarry to change it to a list, because a tuple is immmutable.




    connect.close()


