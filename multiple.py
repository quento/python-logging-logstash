def is_multiple(n, m):
    "Functions takes 2 integers, checks if first is a multiple of second"
    
    # Use modulo to check if there is a remainder (i.e. if it's a multiple)    
    if n % m == 0:
        return True
    else:
        return False

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
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("+            ", error_msg, "          +")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")    

def play_game():
    status = "incomplete"
    
    while status == "incomplete":
        try:
            # Get two integers from user
            first_num = int(input("Type in first integer value: "))
            second_num = int(input("Type in second integer value: "))
            
            print("++++++++++++++++++++++++++ RESULT +++++++++++++++++++++++++++++++")            
            
            # Check if second number is multiple of first            
            if is_multiple(first_num, second_num):
                print("{0} is a multiple of {1}.".format(second_num, first_num))
            else:            
                print("{0} is not a multiple of {1}.".format(second_num, first_num))
            
            print("*****************************************************************")
            status = "complete"
            
        except ValueError:
            # If non-numeric value is typed, show error message
            error_display("ERROR: Please type in numeric input(s).")

def main():
    "Get two integers from user, check if 1st is multiple of 2nd"
    
    #Show the game intro
    game_header()
    # Show the game instructions
    game_instructions()

    play_game()
            
    
if __name__ == '__main__': main()            