# password generator
# silvan horn
# silauho@gmail.com


import database
import user_interface
import atexit
from database import save_key

database.save_key()

database.select_from_database()
user_interface.interface()
