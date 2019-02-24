# Utility Functions to help with the display in the game.

def game_header():
    """ Display game msg or error """
    print("*****************************************************************")
    print("********************** Is a Multiple Of *************************")
    print("*****************************************************************")

def game_instructions():
    """ Display the game instructions """
    print("INSTRUCTIONS")
    print("Get two integers from user, check if 1st is a multiple of the 2nd.")

def error_display(error_msg):
    """ Display error messages """
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("+            ", error_msg, "          +")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

