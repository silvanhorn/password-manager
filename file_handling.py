import user_interface
import password
import globals



def file_check(secret): # dont take password here, bc its already taken by the module name



    password_invalidy=0

    with (open("10-million-password-list-top-1000000.txt", "r") as file):
        try:
            for line in file:
                if  globals.count_regenerating  <= 20:
                    if secret == line.strip():
                        print("generating new")
                        globals.count_regenerating += 1
                        print("count", globals.count_regenerating)
                        password.is_valid_length(len(secret))
                        print(secret)
                        password_invalidy=1


                else:
                    print("to many errors")
                    return


        except:
            user_interface.catch_api_problem("root")

        print(password_invalidy)
        if password_invalidy == 0:
            user_interface.close_window(secret)
            print("after that")