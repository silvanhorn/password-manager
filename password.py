# generate_password.py


import string
import random
import file_handling
import user_interface



def is_valid_length(length):

    if not isinstance(length, int):

        try:
            length = int(length)
            print("succes")
        except ValueError:
            user_interface.user_error()
            return

      #Abbruchkriterien#

    if length == "":
        user_interface.user_error()
        return

    elif length < 5 or length > 30:
        print("3")
        user_interface.user_error()
        return

    generate_password(length)

def generate_password(length):

    characters = string.ascii_letters + string.digits + string.punctuation + "ä" + "ö" + "ü" + "Ä" + "Ö" + "Ü" + "ß" + " "

    final_password = [None] * length

    for i in range(length):

        random_char = str(random.choice(characters))  # Klein- und Großbuchstaben
        str(random_char)
        #complete_string = random_char
        final_password[i] = random_char

    if None not in final_password:
        output = ''.join(final_password)
        # print(ausgabe)


    file_handling.file_check(output)
      # calls a function that set a flag to a certain, whenever that is true, it would close the windows one.

    # It is neccesary to pass the password variable to the closewindow function, because that funtion calls the build_finishwindows function, who calls the database function.
    # Before these changes, we workes more with global varibales. Like that its cleaner.

