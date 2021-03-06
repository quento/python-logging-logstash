import logging
import logstash
import Logger as custom_logger
import Utility as util
import sys
import time


class MultipleChecker:
    """ A simple game that checks to interger values """

    def __init__(self): 
        # Show that game was initialized
        util.game_header()    
        util.game_instructions() 
        # Initialize logger class
        self.game_logger = custom_logger.Logger()
        # TODO - Log that game has started.  
        self.game_logger.doLog("info","python-logstash: new multiplier game initialized.")

    @property    
    def game_logger(self):
        return self._game_logger    

    @game_logger.setter
    def game_logger(self, value):
        self._game_logger = value
    

    def is_multiple(self, n, m):
        "Function takes 2 integers, checks if first is a multiple of second"
        
        # Use modulo to check if there is a remainder (i.e. if it's a multiple)    
        if n % m == 0:
            return True
        else:
            return False
        

    def play_game(self):
        """ Play the 'is multiple' game """
        status = "incomplete"
        game_status = None
        
        while status == "incomplete":
            try:
                # Get two integers from user
                first_num = int(input("Type in first integer value: "))
                str_first_num = str(first_num)
                second_num = int(input("Type in a possible multiple of '" + str(first_num) + "' : "))
                # WARNING  - Log that possible "vaue error may occurr?"
                self.game_logger.doLog("warn","python-logstash: Got user input, may be null values.")
                
                print("++++++++++++++++++++++++++ RESULT +++++++++++++++++++++++++++++++")            
                
                # Check if second number is multiple of first                       
                if self.is_multiple(first_num, second_num):
                    print("{0} is a multiple of {1}.".format(second_num, first_num))
                    game_status = True
                else:            
                    print("{0} is not a multiple of {1}.".format(second_num, first_num))
                    game_status = False
                
                print("*****************************************************************")

                # Add extra fields to logstash msg
                extra = self.game_stats(first_num, second_num, game_status)
                # Log msg plus exta fields.
                self.game_logger.doLog("info","python-logstash: game completed successfully.", extra)
                
                status = "complete"
            except ValueError:
                # If non-numeric value is typed, show error message
                util.error_display("ERROR: Please type in numeric input(s).")
                # TODO: ERROR Log Value Error
                self.game_logger.doLog("exception","python-logstash: ValueError occurred")                
            finally:
                try:
                    play_again = int(input("Play again? (type '1' for yes or '2' for No.): "))
                    if play_again == 1:
                        util.game_header()    
                        util.game_instructions() 
                        self.play_game()                                
                    else:
                        status = "complete"
                except NameError:
                    self.game_logger.doLog("error","python-logstash: NameError occurred in try again area.")  
                    status = "complete"                  

    def game_stats(self, num1, num2, game_status):
        """ Created json format to track game stats in logs """
        return {
            'game_num1': num1,
            'game_num2': num2,
            'game_status': game_status
        }                

def main():
    "Get two integers from user, check if 1st is multiple of 2nd"
    
    # Initialize the multiplier game class    
    multiplier_game = MultipleChecker()
    # play the game
    multiplier_game.play_game()
  
                
if __name__ == '__main__': main()            